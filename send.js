const driver = require('bigchaindb-driver')
const uuidv4 = require('uuid/v4');


// BigchainDB server instance (e.g. https://test.bigchaindb.com/api/v1/)
const API_PATH = 'http://BIGCHAINDBROOTURL:9984/api/v1/'
var number = process.argv[2]
var list = [];
// Create a new keypair.
var total= 0
var start
var end

const alice = new driver.Ed25519Keypair()




    for (var i=0; i <= number; i++) { 
// Construct a transaction payload
const tx = driver.Transaction.makeCreateTransaction(
    // Define the asset to store, in this example it is the current temperature
    // (in Celsius) for the city of Berlin.
    { field: uuidv4()  },

    // Metadata contains information about the transaction itself
    // (can be `null` if not needed)
    {'start':'' },

    // A transaction needs an output
    [ driver.Transaction.makeOutput(
            driver.Transaction.makeEd25519Condition(alice.publicKey))
    ],
    alice.publicKey
)

// Sign the transaction with private keys
const txSigned = driver.Transaction.signTransaction(tx, alice.privateKey)
list.push(txSigned)
}




// Send the transaction off to BigchainDB
const conn = new driver.Connection(API_PATH)
for (var i=0; i <= number; i++) { 
conn.postTransactionAsync(list[i])
    if (i === 1) { start = new Date(); console.log(start) }
total++
if (total == number){
    end = new Date()
console.log("End time: d.",end);
    console.log("Sent all transactions in:  %ds seconds",(end - start)/1000);
    console.log("Transactions per second throughput is: c. %dtxs",number/((end - start)/1000));
}
    
}

