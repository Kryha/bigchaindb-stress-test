const WebSocket = require('ws')

const ws = new WebSocket('ws://BIGCHAINDBROOTURL:9985/api/v1/streams/valid_transactions')

var param = process.argv[2]


var i = 0
var j = 0
var start
var end
// console.log("Test ready")
ws.on('message', (data) => {
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
        ws.terminate()
        process.exit();
    };

});
