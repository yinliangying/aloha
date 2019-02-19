

import re
import json
from tensor2tensor.data_generators import problem
from tensor2tensor.data_generators import text_problems

from tensor2tensor.utils import registry

import os,sys
@registry.register_problem
class MyReaction(text_problems.Text2TextProblem):
  #Predict next line of poetry from the last line. From Gutenberg texts.


  @property
  def vocab_type(self):
      return text_problems.VocabType.CHARACTER

  @property
  def approx_vocab_size(self):
    return 2**8  # ~256

  @property
  def is_generate_per_split(self):
    # generate_data will shard the data into TRAIN and EVAL for us.
    return False

  @property
  def dataset_splits(self):
    #Splits of data to produce and number of output shards for each.
    # 10% evaluation data
    return [{
        "split": problem.DatasetSplit.TRAIN,
        "shards": 9,
    }, {
        "split": problem.DatasetSplit.EVAL,
        "shards": 1,
    }]

  def generate_samples(self, data_dir, tmp_dir, dataset_split):
    del data_dir
    del tmp_dir
    del dataset_split

    script_dir=os.path.split(os.path.realpath(__file__))[0]
    data_dir=script_dir+"/../../data/"
    fp_train_sample=open(data_dir+"/train_sample")

    for line in fp_train_sample:
        sample_dict=json.loads(line)
        yield {
          "inputs": sample_dict["inputs"],
          "targets": sample_dict["targets"],
        }
