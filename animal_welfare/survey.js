var mongo = require("./mongo.js")
var util = require("util")

exports.survey= function(req,res,next){
  var name = req.body.name;
  var tel = req.body.tel;
  var age = req.body.age;
  var category = req.body.category;
  var data = req.body.data;
  mongo.connect(function(err){
    if(err) throw err;
    var date = new Date();
    date.setHours(date.getHours()+9);
    mongo.db.collection('survey').insert({name:name, tel:tel, age:age, category:category, data:data, date:date},function(err,doc){
      if(err){
        res.json({code:500});
        console.log(err);
      }else{
        console.log('insert success')    //쓰기성공
        res.json({code:210})
      }
    })
  })
}
