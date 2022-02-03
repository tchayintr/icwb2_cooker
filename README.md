# ICWB2 Cooker
#### _icwb2_cooker_

A tool for extracting segmented words from icwb2 collection (http://sighan.cs.uchicago.edu/bakeoff2005/). 


#### Data formats
- **sl**: sentence line
- **wl**: word line

#### Random SEED
- as: AS
- cityu: CITYU
- msr: MSR
- phu: PKU

#### Usage
```
usage: icwb2_cooker.py [-h] [--quiet] --dataset {as,cityu,msr,pku} --train_data TRAIN_DATA --test_data TEST_DATA [--output_data_path OUTPUT_DATA_PATH]
                       [--input_data_format {utf8,txt}] [--output_data_format {sl,wl}] [--unshuffle]

optional arguments:
  -h, --help            show this help message and exit
  --quiet, -q           Do not report on screen
  --dataset {as,cityu,msr,pku}
  --train_data TRAIN_DATA
                        File path to training data
  --test_data TEST_DATA
                        File path to test data
  --output_data_path OUTPUT_DATA_PATH, -o OUTPUT_DATA_PATH
                        File path to output data
  --input_data_format {utf8,txt}, -f {utf8,txt}
  --output_data_format {sl,wl}
  --unshuffle           Specify to not shuffle data before cooking

```

#### Example outputs
```
Start time: 20220202_1626

### arguments
# quiet=False
# dataset=msr
# train_data=data/samples/sample_msr_training.utf8
# test_data=data/samples/sample_msr_test_gold.utf8
# output_data_path=cooked
# input_data_format=utf8
# output_data_format=sl
# unshuffle=False

save cooked train data: cooked/msr.train.seg.sl
save cooked validdata: cooked/msr.valid.seg.sl
save cooked test data: cooked/msr.test.seg.sl
### report
# [TRAIN] sent: 90 ...
# [TRAIN] word: 1741 ...
# [TRAIN] char: 2533 ...
# [TRAIN] words/sent: min=8 max=65 avg=19.344444444444445
# [TRAIN] chars/sent: min=15 max=78 avg=28.144444444444446
# [TRAIN] chars/word: min=1 max=4 avg=1.4549109707064904
####
# [VALID] sent: 10 ...
# [VALID] word: 194 ...
# [VALID] char: 297 ...
# [VALID] words/sent: min=11 max=28 avg=19.4
# [VALID] chars/sent: min=16 max=46 avg=29.7
# [VALID] chars/word: min=1 max=4 avg=1.5309278350515463
####
# [TEST] sent: 10 ...
# [TEST] word: 128 ...
# [TEST] char: 211 ...
# [TEST] words/sent: min=6 max=21 avg=12.8
# [TEST] chars/sent: min=9 max=35 avg=21.1
# [TEST] chars/word: min=1 max=4 avg=1.6484375
```
