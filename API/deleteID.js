var client = require("./mysql").mysql_pool;

exports.deleteID = function(req,res,next){
  var email = req.params.email;
  console.log(email);
  client.query('delete from p_s_mbrdata where email = ?',[email],function(err, result){
    if(err){    //db연결오류
      res.json({code:500})
      console.log(err)
    }else{      //게시판 부르기성공
      res.json({code:210});
      console.log('delete success')
    }
  })
}
