var client = require("./mysql").mysql_pool;
var mongo = require('./mongo.js');
var mongodb = require("mongodb")
var async = require('async');


exports.youtube = function(req,res,next){
    client.query('select * from p_s_mbrdata where email = ?',[req.params.email],function(err, result){
      if(err){    //db연결오류
         res.json({code:500})
         console.log(err)
      }else{      //게시판 부르기성공
        var survey_mbr = result[0].memberuid;
        if(!survey_mbr){
           res.json({code:411})
           console.log('crawling failed.(Plz Do Survey)')
        }else{      //내용오류
           mongo.connect(function(err){
             if(err) throw err;
             else{
               mongo.db.collection('survey').findOne({"survey_mbr":survey_mbr},function(err,doc){
                 if(err){
                   res.json({code:500});
                   console.log(err);
                 }else{
                   var spawn = require("child_process").spawn;
                   console.log(doc)
                   var process = spawn('python',["/project/src/contentss.py",doc._id] );
                   process.stdout.on('data', function(data){
                     var test=JSON.parse(data.toString());
                       var aJsonArray = new Array();
                       for (let i=0; i < test['result_video'].length; i++){
                         var p1 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].top1_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         var p2 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].top2_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         var p3 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].top3_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         var p4 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].top4_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         var p5 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].top5_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         var p6 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].new1_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         var p7 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].new2_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         var p8 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].ran1_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         var p9 = new Promise((resolve,reject)=>mongo.db.collection('video').find({_id: new mongodb.ObjectID(test['result_video'][i].ran2_id)}).toArray(function(err,doc){
                           resolve(doc[0]);
                         }))
                         Promise.all([p1,p2,p3,p4,p5,p6,p7,p8,p9]).then(values =>{aJsonArray.push(values)})
                       }
                       setTimeout(function() {
			  console.log(aJsonArray)
                          res.json({email:req.params.email,
                                    result:aJsonArray})
		       }, 500);
                   })
                 }
               })
             }
           })
         }
      }
  })
}
