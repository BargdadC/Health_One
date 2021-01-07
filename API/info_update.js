var client = require("./mysql").mysql_pool;

exports.info_update = function(req,res,next){
  var email = req.body.email;
  var nic = req.body.nic;
  var name = req.body.name;
  var tel = req.body.tel;
  console.log(email);
  client.query('update p_s_mbrdata set nic = ?, name = ?, tel1 = ?, tel2 = ? where email = ?',[nic, name, tel, tel, email],function(err, result){
    if(err){    //db연결오류
      res.json({code:500})
      console.log(err)
    }else{      //게시판 부르기성공
      res.json({code:210});
      console.log('update success')
    }
  })
}
