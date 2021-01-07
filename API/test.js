var client = require("./mysql").mysql_pool;
var mongo = require('./mongo.js');
var fs = require('fs');


exports.test = function(req,res,next){
  var filename = req.body.filename
  var base64Data = req.body.image
  console.log(base64Data);
  
  /*var spawn = require("child_process").spawn;
  var process = spawn('python',["/project/weather/weather.py",lat, long] );
  process.stdout.on('data', function(data){
    var test = JSON.parse(data.toString());
    test.status_en = new Buffer(test.status_en, 'base64').toString();
    test.address_en = new Buffer(test.address_en, 'base64').toString();
    test.find_dust_status_en = new Buffer(test.find_dust_status_en, 'base64').toString();
    if(!test){
      res.json({code:500})
    }else{
      console.log(test)
      res.json(test);
    }*/
}
