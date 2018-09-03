var MongoClient = require('mongodb').MongoClient;
var param = process.argv[2]
var j = 1


 JSONStream = require('JSONStream')
, es = require('event-stream')

MongoClient.connect("mongodb://localhost:27017/bigchain?readConcern=majority")
 .then(function(client){
   let db = client.db('bigchain')
   let change_streams = db.collection('transactions').watch()
      change_streams.on('change', function(change){

   console.log(change.length)
    

  
  
              
      
    }
  );
 })
