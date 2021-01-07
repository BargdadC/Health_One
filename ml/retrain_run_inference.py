# -*- coding: utf-8 -*-

"""Inception v3 architecture 모델을 retraining한 모델을 이용해서 이미지에 대한 추론(inference)을 진행하는 예제"""

import sys
import numpy as np
import tensorflow as tf
import json
import pymongo
from bson import ObjectId
from bson import json_util
from bson import BSON

connection = pymongo.MongoClient('localhost', 27017)
db = connection.Health_One

var = sys.argv[1]
imagePath = '/project/ml/tmp/' + var                                      # 추론을 진행할 이미지 경로
modelFullPath = '/project/ml/tmp/output_graph.pb'                                      # 읽어들일 graph 파일 경로
labelsFullPath = '/project/ml/tmp/output_labels.txt'                                   # 읽어들일 labels 파일 경로


def create_graph():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')


def run_inference_on_image():
    answer = None
    result = {}

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)
        i=0
        result=[]

        top_k = predictions.argsort()[-5:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        for node_id in top_k:
            i=i+1
            human_string = labels[node_id]
            labels[node_id] = labels[node_id][2:-3]
            human_string = human_string[2:-3]
            score = predictions[node_id]
            food_data = db.food.find_one({"name_en":human_string},{'_id':0})
            result.append(({"food":food_data,"rank":i}))
            #print('%s (score = %.5f)' % (human_string, score))

        print(json.dumps({"code":200,"result": result},default=json_util.default,ensure_ascii=False))
        answer = labels[top_k[0]]
        #return answer


if __name__ == '__main__':
    run_inference_on_image()
