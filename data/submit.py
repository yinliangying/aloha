

import sys
import json
fp_test_id=open("test_id")
fp_test_predict=open("test_sample.transformer.transformer_tiny.my_reaction.beam4.alpha0.6.decodes")
fp_result=open("result.json","w")

out_dict={}
i=0
for line_id in fp_test_id:
    i+=1
    id=line_id.strip()
    line_predict=fp_test_predict.readline().strip()
    out_dict[id]=line_predict
for line in fp_test_predict:
    raise Exception
print(i)
print(json.dumps(out_dict),file=fp_result)