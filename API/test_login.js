var client = require("./mysql").mysql_pool;

exports.login = function(req,res,next){
  var id = req.body.id;
  var pw = req.body.pw;
  console.log(id, pw);

  client.query('select * from sys_admin where id = ?',[id],function(err, result){
    if(err){    //db연결오류
      res.json({code:500})
      console.log(err)
    }else if(result.length === 0){      //ID오류
      res.json({code:401});
      console.log('login failed.(ID)')
    }else{      //로그인성공
      if(result[0].pw === pw){
        res.set({'content-type': 'application/json; charset=utf-8'});
        res.cookie("auth",true)
        res.json({code:201});
        console.log('login OK')
      }else{    //pw오류
        console.log('login failed.(pw)')
        res.json({code:401});
      }
    }
  })
}

