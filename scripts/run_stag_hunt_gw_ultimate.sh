#!/bin/sh
python ma_main.py --config="./configs/stag-hunt-gw-ultimate.json" --seed=$1
# python ma_main.py --config="./configs/stag-hunt-gw-ultimate.json" --seed=$1 --num-steps=50 --save-dir="/tmp/123" --num-processes=2