# -*- coding: utf-8 -*-
import pandas as pd
import sys

if __name__ == '__main__':
    f_read = open('data/test.csv', 'rb')
    f_w = open('data/test-new.csv', 'w')
    for line in f_read:
        f_w.write(line.decode(encoding='gbk').encode(encoding='utf-8'))
    f_read.close()
    f_w.close()
    all_data = pd.read_csv('data/test-new.csv', index_col=False, delimiter=',')
    DataTextWriter = open('data/DataText.txt', 'w')
    DataFlag2Writer = open('data/DataFlag2.txt', 'w')
    for line in all_data['text']:
        line = str(line).replace('\r\n', '')
        DataTextWriter.write(line+'\n')
    for flag in all_data['flag2']:
        DataFlag2Writer.write(str(flag)+'\n')
    DataTextWriter.close()
    DataFlag2Writer.close()
