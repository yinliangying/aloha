# aloha

安装
1.rdkit   conda install -c rdkit rdkit
2.tensor2tensor     pip安装


运行
1.执行./data/1_remove_mapping.py  ：将./data/test.txt ./data/train.txt 转化为./data下source target文件
2.转换为t2t数据格式：执行data_gen.sh 中t2t-datagen部分（这部分没完全弄好，可以先省略，直接用我生成在t2t_data中的结果）
3.训练执行data_gen.sh 中t2t-trainer 部分
4.预测结果执行data_gen.sh 中t2t-decoder部分
