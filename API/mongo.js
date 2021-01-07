var MongoClient = require('mongodb')
var url = "mongodb://localhost:27017/Health_One";
var db;

module.exports.connect = function connect(callback) {
    MongoClient.connect(url, function(err, conn){
        /* exports the connection */
        module.exports.db = conn.db('Health_One'); //database명을 명시했다.;
        callback(err);
    });
};
