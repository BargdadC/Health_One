var multer = require('multer'); 

exports.mlfood = function (req, res, next) {
  var filename = req.files[0].fieldname;
  var path = req.files[0].path;
  var spawn = require("child_process").spawn;
  var process = spawn('python',["/project/ml/retrain_run_inference.py",filename] );
  process.stdout.on('data', function(data){
    var result2 = JSON.stringify(data.toString());
    var result = JSON.parse(result2);
    var test=JSON.parse(data.toString());
    console.log(result);
    res.json(test);
  })
}
