var util = require("util");

exports.mlkonlpy = function (req, res, next) {
  var tel = req.body.tel;
  console.log(tel)
  var spawn = require("child_process").spawn;
  var process = spawn('python3',["/project/animal_welfare/result.py",tel]);
  process.stdout.on('data', function(data){
    var result2 = JSON.stringify(data.toString());
    var result = JSON.parse(result2);
    var test=JSON.parse(data.toString());
    res.json(test);
    console.log(test)
  })
}
