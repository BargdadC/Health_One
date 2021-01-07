var client = require("./mysql").mysql_pool;
var md5 = require("md5")

exports.register= function(req,res,next){
  var email = req.body.email;
  var nic = req.body.nic;
  var name = req.body.name;
  var tel = req.body.tel;
  var pwd = req.body.pwd;
  var pwdCheck = req.body.pwdCheck;
  var d = new Date();
  var date = d.getFullYear()+""+("0" + (d.getMonth() + 1)).slice(-2)+""+("0" + d.getDate()).slice(-2) +""+ ("0"+d.getHours()).slice(-2) +""+ ("0"+d.getMinutes()).slice(-2)+""+("0"+d.getSeconds()).slice(-2);
  console.log(email, pwd);
    if(!(email && nic && name && tel && pwd && pwdCheck)){      //제목오류
      res.json({code:410})
      console.log('register failed.(Something Empty)')
    }else{      //내용오류
      if(pwd != pwdCheck){
        res.json({code:411});
        console.log('register failed.(check your pwd)')
      }else{
        client.query('insert into p_s_mbrdata (auth, email, pw, tel1, tel2, name, nic, addfield ,d_modify, d_regis) values (1, ?, ?, ?, ?, ?, ?, ?, ?, ?)',[email, md5(pwd), tel, tel, name, nic, md5(pwd),date, date],function(err, result){
          if(err){
            client.query('select * from p_s_mbrdata where = ?',[email],function(error, row){
                if(row){
                  res.json({code:500});
                  console.log(err)
                }else{
                  res.json({code:501});
                  console.log('register faild.(dup email)')
                }
            })
          }else{
            console.log('register success')    //쓰기성공
            res.json({code:210})
          }
        })
      }
    }
}
