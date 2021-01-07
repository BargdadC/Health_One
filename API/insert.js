var client = require("./mysql").mysql_pool;

exports.insert = function(req,res,next){
  var bbsid = req.body.bbsid;
  var multi_category = req.body.multi_category;
  var title = req.body.title;
  var contents = req.body.contents;
  console.log(bbsid, multi_category);
    if(!title){      //제목오류
      res.json({code:410})
      console.log('write failed.(Empty title)')
    }else{      //내용오류
      if(!contents){
        res.json({code:411});
        console.log('write failed.(Empty contents)')
      }else{
        client.query('insert into p_s_board (bbsid, multi_category, title, contents, hit, d_regis, d_modify) values (?, ?, ?, ?, 0, now(), now())',[bbsid, multi_category, title, contents],function(err, result){
          if(err){
            res.json({code:500});
            console.log(err);
          }else{
            console.log('write success')    //쓰기성공
            res.json({code:210})
          }
        })
      }
    }
}

