var MongoClient = require('mongodb').MongoClient;

var param = process.argv[2]


var i = 0
var j = 0
var start
var end

MongoClient.connect("mongodb://localhost:27017/bigchain?readConcern=majority")
 .then(function(client){
   let db = client.db('bigchain')
   let change_streams = db.collection('transactions').watch()
      change_streams.on('change', function(change){

    j++
    if (j==1) {
        start = new Date(); console.log("Start time: ",start)
    }
    else if (j==param) {
        end = new Date()
        console.log("End time: d.",end)
        console.log("Received all transactions in: e. %ds seconds",(end - start)/1000)
        console.log("Total number of transactions: f. ",j)
        console.log("Transactions per second throughput is: g. %dtxs",j/((end - start)/1000))
process.exit();    
};
                 
      
    }
  );
 })
