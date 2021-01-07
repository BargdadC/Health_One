var client = require("./mysql").mysql_pool;
var mongo = require('./mongo.js');
var mongodb = require("mongodb")
var async = require('async');

exports.crawling = function(req,res,next){
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
          if(err){
            res.json({code:500})
          }
          else{
            mongo.db.collection('survey').findOne({"survey_mbr":survey_mbr},{sort:{'survey_date' : -1}},function(err,doc){
              if(err){
                res.json({code:500});
                console.log(err);
              }else if(!doc){
		res.json({code:510});
		console.log('result is NULL')
              }else{
                var spawn = require("child_process").spawn;
                var process = spawn('python3',["/project/src/contentss.py",doc._id] );
                process.stdout.on('data', function(data){
		console.log(doc)
                console.log(data.toString())
                  var test=JSON.parse(data.toString());
                  var aJsonArray = new Array();
                  for (let i=0; i < test['result'].length; i++){
                    var p1 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].top1_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    var p2 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].top2_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    var p3 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].top3_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    var p4 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].top4_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    var p5 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].top5_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    var p6 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].new1_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    var p7 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].new2_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    var p8 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].ran1_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    var p9 = new Promise((resolve,reject)=>mongo.db.collection('link').find({_id: new mongodb.ObjectID(test['result'][i].ran2_id)}).toArray(function(err,doc){
                      resolve(doc[0]);
                    }))
                    Promise.all([p1,p2,p3,p4,p5,p6,p7,p8,p9]).then(values =>{aJsonArray.push(values)})
                  }
                  setTimeout(function(){
                    console.log(aJsonArray)
                    res.json({email:req.params.email,result:aJsonArray})
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
