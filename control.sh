#!/bin/bash
for i in `seq 1 $1`;
do
python3 test.py $(($i * 50 )) 150 | cut -d ":" -f 2  | sed ':a;N;$!ba;s/\n/,/g' |tee -a final.txt
sleep 10
done
