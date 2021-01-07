var client = require("./mysql").mysql_pool;

exports.list = function(req,res,next){
  var bbsid = req.params.bbsid;
  var page = (parseInt(req.params.page) - 1)*20;
  console.log(bbsid);
  client.query('select * from p_s_board where bbsid = ? order by seq limit ?, 20',[bbsid,page],function(err, result){
    if(err){    //db연결오류
      res.json({code:500})
      console.log(err)
    }else{      //게시판 부르기성공
      res.set({'content-type': 'application/json; charset=utf-8'});
      res.json({page:req.body.page,
                result: result?result:{}});
      console.log('load success')
    }
  })
}
