# Stress test

Enter after each file the number of transactions you are testing

e.g.
```node send.js 1000```

send.js generates a transaction payload and sends them to the bdb endpoint using the bdb js driver

listen.js is a simple counter for the time delta between the first and the last transaction using the bdb websocket

mongo.js is an experimental test for measuring the time delta using the bgb transaction collection. It uses the change streams api which has been implemented on MongoDB 3.6. It does not run on a standalone databse, so you need to convert to a replica set. Short version:

```
sudo stop mongodb service
start mongod --replSet rs0
```

mongo into your mongodb and run rs.initiate()

Now you can run the mongo.js alternative listener.

Long version:

```https://docs.mongodb.com/manual/tutorial/convert-standalone-to-replica-set/```

Example usage:

Modify the hardcoded BIGCHAINDBROOTURL in send.js and listen.js to your ip address. You can also change localhost in the mongo.js to your remote insecure mongodb instance :)

```
node listen.js 100 
and/or
node mongo.js 100
```
Now you are ready to receive the tx payload
```
node send.js 100
```


Known issues:
send.js reports abnormal txs
