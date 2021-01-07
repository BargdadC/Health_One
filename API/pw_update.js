var client = require("./mysql").mysql_pool;
var md5 = require("md5");

exports.pw_update = function(req,res,next){
  var email = req.body.email;
  var pw = req.body.pw;
  console.log(email);
  client.query('update p_s_mbrdata set pw = ? where email = ?',[md5(pw), email],function(err, result){
    if(err){    //db연결오류
      res.json({code:500})
      console.log(err)
    }else{      //게시판 부르기성공
      res.json({code:210});
      console.log('pw update success')
    }
  })
}
