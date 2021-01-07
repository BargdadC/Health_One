# -*- coding: utf8 -*-
# https://www.youtube.com/watch?v=_eIGBgJkr0M
# 모듈 사용
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.callbacks import EarlyStopping
import pandas as pd, numpy as np


# 데이터 가공 - 0.0~1.0
csv = pd.read_csv("bmi.csv")
csv["weight"] /= 100
csv["height"] /= 200 

bmi_class = {
	"thin" : [1, 0, 0],
	"normal" : [0 ,1, 0],
	"fat" : [0, 0, 1]
}

y = np.empty((1000, 3))

for i, v in enumerate(csv["label"]):
	y[i] = bmi_class[v]

x = csv[["weight", "height"]].as_matrix()

x_train, y_train = x[1:801], y[1:801]
x_test, y_test = x[801:1001], y[801:999]

# 모델 생성
model = Sequential()
model.add(Dense(512, input_shape=(2,)))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(Dense(3))
model.add(Activation('softmax'))


# 레이어 형성
model.compile("rmsprop", "categorical_crossentropy", metrics=['accuracy'])


# 데이터 학습
model.fit(
	x_train,
	y_train,
	batch_size = 100,
	epochs = 20, #nb_epoch
	validation_split = 0.1,
	callbacks = [EarlyStopping(monitor='val_loss', patience=2)],
	verbose=1
)

# 예측
print(x[-3:])
score = model.predict(x[-3:])


# 정답률
#score = model.evaluate(x_test, y_test)
print("\n************************************************\n")
print(score)