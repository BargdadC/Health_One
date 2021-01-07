var secretObj = require("./jwt");
var md5 = require('md5');
var jwt = require("jsonwebtoken");
var client = require("./mysql").mysql_pool;

exports.login = function(req,res,next){
  var email = req.body.email;
  var pwd = req.body.pwd;
  console.log(email, pwd);
  var token = jwt.sign({
      email: email
  },
  secretObj.secret ,
  {
      expiresIn: '5m'   //토큰유지시간
  })
  client.query('select * from p_s_mbrdata where email = ?',[email],function(err, result){
    if(err){    //db연결오류
      res.json({code:500})
      console.log(err)
    }else if(result.length === 0){      //ID오류
      res.json({code:410})
      console.log('login failed.(ID)')
    }else{      //로그인성공
      if(result[0].pw === md5(pwd)){
        res.cookie("user", token);
        res.set({'content-type': 'application/json; charset=utf-8'});
        res.json({email:email,
                name:result[0].name,
                nic:result[0].nic,
		tel:result[0].tel1,
                code:210,
                token:token});
        console.log('login success')
      }else{    //pw오류
        console.log('login failed.(pw)')
        res.json({code:411})
      }
    }
  })
}

