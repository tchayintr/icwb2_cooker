############################################
# input

TRAIN_DATA=data/samples/sample_msr_training.utf8
TEST_DATA=data/samples/sample_msr_test_gold.utf8
OUTPUT_DATA=cooked/
OUTPUT_CHAR_TYPE=simplified

python3 src/icwb2_cooker.py \
    --dataset msr \
    --train_data $TRAIN_DATA \
    --test_data $TEST_DATA \
    --output_data_path $OUTPUT_DATA \
    --output_character_type $OUTPUT_CHAR_TYPE \
    --export_vocab \
