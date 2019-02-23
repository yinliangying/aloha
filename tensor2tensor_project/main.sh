#!/usr/bin/env bash
__script_dir=$(cd `dirname $0`; pwd)
cd ${__script_dir}
USR_DIR=${__script_dir}/problem_model/
PROBLEM=my_reaction
DATA_DIR=${__script_dir}/t2t_data/
TMP_DIR=${__script_dir}/tmp/



MODEL=transformer
TRAIN_DIR=${__script_dir}/train_tiny/  #transformer_tiny
HPARAMS_SET=transformer_tiny

#TRAIN_DIR=${__script_dir}/train_tiny_dingzhi/
#HPARAMS_SET=transformer_tiny

#MODEL=lstm_seq2seq_attention_bidirectional_encoder
#TRAIN_DIR=${__script_dir}/train_lstm_attention/
#HPARAMS_SET=lstm_attention

#transformer_base_single_gpu


mkdir -p $DATA_DIR $TMP_DIR $TRAIN_DIR


#1. remove atom mapping number and create train and test file
#python 1_remove_mapping.py ../data   #don't change the arg ../data because of  the need of  the arg --problem below

'
#2. create t2t  data form
t2t-datagen \
  --t2t_usr_dir=$USR_DIR \
  --data_dir=$DATA_DIR \
  --tmp_dir=$TMP_DIR \
  --problem=$PROBLEM

exit 0
'

t2t-trainer \
  --t2t_usr_dir=$USR_DIR \
  --data_dir=$DATA_DIR \
  --problem=$PROBLEM \
  --model=$MODEL \
  --output_dir=$TRAIN_DIR\
  --train_steps 3000000\
  --hparams_set=$HPARAMS_SET  \
  #--hparams='batch_size=4000,num_hidden_layers=4,hidden_size=16,filter_size=16,num_heads=4'

exit 0

DECODE_TO_FILE=$TRAIN_DIR/a.txt
DECODE_FROM_FILE=../data/test_sample

t2t-decoder \
    --t2t_usr_dir=$USR_DIR  \
    --problem=$PROBLEM \
    --data_dir=$DATA_DIR \
    --model=${MODEL} \
    --output_dir=$TRAIN_DIR \
    --decode_from_file=${DECODE_FROM_FILE} \
    --decode_to_file=$DECODE_TO_FILE \
    --hparams_set=$HPARAMS_SET \
    --decode_hparams='return_beams=True,beam_size=10' # return topN(N=beam_size) result split by \t for each sample


RESULT_FILE=../data/result.json
TEST_ID_FILE=../data/test_id
#create submission data
python submit.py $DECODE_TO_FILE  ${TEST_ID_FILE}  ${RESULT_FILE}