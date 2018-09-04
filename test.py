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


bdb_root_url = 'http://BIGCHAINDBROOTURL:9984'  # Use YOUR BigchainDB Root URL here
bdb = BigchainDB(bdb_root_url)


# tx_count = input("How many transactions are we testing? ")
# size = input("What size? (Multiples of 36 characters(UUIDv4)) ")

# read tx burst count from arguments

tx_count = int(sys.argv[1])
size = 100

#size = sys.argv[2]

# set time to 0

t0 = 0
t1 = 0

# define number of processes

NUM_PROCESSES = int(16)

# split transactions for each processes

txcore=int(tx_count / NUM_PROCESSES)

# define payload sending

def sendtx(i,s):
        sent_creation_tx = bdb.transactions.send_async(transaction_list[i][s])
children = []



alice = generate_keypair()

transaction_list = defaultdict(list)

# generate a large array of transactions for each process


for x in range(int(tx_count)):
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
            transaction_list[int(x % NUM_PROCESSES)].append(fulfilled_creation_tx)
            
# start counting time

t0 = time.time()

# start sending

for process in range(NUM_PROCESSES):
    pid = os.fork()
    if pid:
        children.append(pid)
    else:
        for transaction in range(txcore):
            sendtx(process,transaction)
        os._exit(0)
for i, child in enumerate(children):
    os.waitpid(child, 0)
    t1 = time.time()


print("Number of transactions: a.", tx_count)
print("and the size of transactions: b.", size)
print("Txs rate: c.", tx_count/(t1-t0))
