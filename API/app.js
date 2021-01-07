var express = require('express');;
var router = express.Router();
var login = require("./login");
var survey = require("./survey");
var list = require("./list");
var insert = require("./insert");
var register = require("./register");
var crawling = require("./crawling");
var weather = require("./weather");
var mlfood = require("./mlfood")
//var test = require("./test")
var deleteID = require("./deleteID")
var info_update = require("./info_update")
var pw_update = require("./pw_update")
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var youtube = require("./youtube");
var knowledge = require("./knowledge");
var multer = require('multer');

var storage = multer.diskStorage({
  destination: function (req, file, callback) {
    callback(null, '/project/ml/tmp')
  },
  filename: function (req, file, callback) {
    callback(null, file.fieldname)
  }
})

var upload = multer({storage: storage});
var type = upload.any()

var app = express();
app.use(cookieParser());
app.use(bodyParser.urlencoded({extended: false}));

app.listen(3000, function(){
  console.log('server is running');
})

app.post("/login", login.login)
app.post("/survey", survey.survey)
app.get("/list/:bbsid/:page", list.list)
app.delete("/deleteID/:email", deleteID.deleteID)
app.post("/insert", insert.insert)
app.post("/register", register.register)
app.get("/crawling/:email", crawling.crawling)
app.get("/weather/:lat/:long", weather.weather)
app.post("/mlfood",type,mlfood.mlfood)
//app.post("/test", test.test)
app.put("/info_update", info_update.info_update)
app.put("/pw_update", pw_update.pw_update)
app.get("/youtube/:email", youtube.youtube)
app.get("/knowledge/:email", knowledge.knowledge)
