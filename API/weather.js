var client = require("./mysql").mysql_pool;
var mongo = require('./mongo.js');

exports.weather = function(req,res,next){
  if((req.params.lat == 100) && (req.params.long == 100)){
    var lat = 36.9494546;
    var long = 127.9061259;
    var spawn = require("child_process").spawn;
    var process = spawn('python',["/project/weather/weather.py",lat, long] );
    process.stdout.on('data', function(data){
      var test=JSON.parse(data.toString());
      test.status_en = new Buffer(test.status_en, 'base64').toString();
      test.address_en = new Buffer(test.address_en, 'base64').toString();
      test.find_dust_status_en = new Buffer(test.find_dust_status_en, 'base64').toString();
      res.json(test);
    })
  }else{
    var lat = req.params.lat
    var long = req.params.long
    var spawn = require("child_process").spawn;
    var process = spawn('python',["/project/weather/weather.py",lat, long] );
    process.stdout.on('data', function(data){
      var test = JSON.parse(data.toString());
      test.status_en = new Buffer(test.status_en, 'base64').toString();
      test.address_en = new Buffer(test.address_en, 'base64').toString();
      test.find_dust_status_en = new Buffer(test.find_dust_status_en, 'base64').toString();
	console.log(test.status)
      if(!test){
        res.json({code:500})
      }else{
        client.query("select * from p_s_board where multi_category Like ?",['%'+test.status+'%'],function(err, result){
          if(err){
            res.json({code:500})
            console.log(err)
          }else{
            test.info = result;
            if(!err)
		{res.json(test)}
          }
        })
      }
    })
  }
}