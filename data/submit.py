

import sys
import json
fp_test_id=open("test_id")
fp_test_predict=open()


out_dict={}
for line_id in fp_test_id:
    id=line_id.strip()
    line_predict=fp_test_predict.readline().strip()
    out_dict[id]=line_predict
print(json.dumps(out_dict))