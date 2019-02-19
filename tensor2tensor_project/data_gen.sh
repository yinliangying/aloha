#!/usr/bin/env bash
__script_dir=$(cd `dirname $0`; pwd)
cd ${__script_dir}
USR_DIR=${__script_dir}/problem_model/
PROBLEM=my_reaction
DATA_DIR=${__script_dir}/t2t_data/
TMP_DIR=${__script_dir}/tmp/
TRAIN_DIR=${__script_dir}/train2/
MODEL=transformer
HPARAMS_SET=transformer_tiny  #transformer_base_single_gpu
mkdir -p $DATA_DIR $TMP_DIR $TRAIN_DIR

'
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
  --hparams_set=$HPARAMS_SET \
  --output_dir=$TRAIN_DIR

exit 9


t2t-decoder \
    --t2t_usr_dir=$USR_DIR  \
    --problem=$PROBLEM \
    --data_dir=$DATA_DIR \
    --model=${MODEL} \
    --hparams_set=${HPARAMS_SET} \
    --output_dir=$TRAIN_DIR \
    --decode_from_file=${__script_dir}/../data/test_sample \
    #--decode_to_file=$TRAIN_DIR/a.txt


