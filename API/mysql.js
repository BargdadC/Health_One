var mysql      = require('mysql');
var MongoClient = require('mongodb').MongoClient;
var mysqldb;
mysqldb = {
    mysql_pool : mysql.createPool({
        host     : 'localhost',
        user     : 'root',
        password : 'kku2017',
        database : 'afewgoodman',
	port : 3306
    })
};
module.exports = mysqldb;

