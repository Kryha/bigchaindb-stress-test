from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit
import time
import sys
import os
import queue
import json
from threading import Thread, Event
from uuid import uuid4
import json
from collections import defaultdict
import websocket
import subprocess


# tx_count = input("How many transactions are we testing? ")
# size = input("What size? (Multiples of 36 characters) ")

tx_count = sys.argv[1]
size = sys.argv[2]

NUM_PROCESSES = int(tx_count)

def sendtx(s):
        sent_creation_tx = bdb.transactions.send_async(transaction_list['one'][s])
children = []

z = int(tx_count) #this is the number of transactions you want to test

alice = generate_keypair()

transaction_list = defaultdict(list)

final_transaction = []


args = ['node', 'listen.js', tx_count, "&"]
subprocess.Popen(args)

test = False


if test == True:
    tokens = {}
    bdb_root_url = 'https://test.bigchaindb.com' 
    tokens = {'app_id': 'SOMETHING', 'app_key': 'SOMETHINGMORE'}
    bdb = BigchainDB(bdb_root_url, headers=tokens)
else:
    bdb_root_url = 'http://BIGCHAINDBROOTURL:9984'  # Use YOUR BigchainDB Root URL here
    bdb = BigchainDB(bdb_root_url)


for x in range(0, z):
            prepared_creation_tx = bdb.transactions.prepare(
                operation='CREATE',
                signers=alice.public_key,
                asset= {
                            'data': {
                                'test': {
                                        'field': str(uuid4()) * int(size)
                                    },
                                },
                        })

            fulfilled_creation_tx = bdb.transactions.fulfill(
                prepared_creation_tx,
                private_keys=alice.private_key

            )
            transaction_list['one'].append(fulfilled_creation_tx)
t0 = time.time()

for process in range(NUM_PROCESSES):
    pid = os.fork()
    if pid:
        children.append(pid)
    else:
        sendtx(process)
        os._exit(0)
for i, child in enumerate(children):
    os.waitpid(child, 0)
t1 = time.time()


print("Number of transactions: a.", tx_count)
print("and the size of transactions: b.", size)
print("Txs rate: c.", z/(t1-t0))
