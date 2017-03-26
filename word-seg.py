# -*- coding:utf-8 -*-
import jieba
import sys

if __name__ == '__main__':
    f_reader = open('data/DataText.txt', 'r')
    f_writer = open('data/DataTextSeg.txt', 'w')
    max_len = 0
    sum = 0
    for line in f_reader.readlines():
        line = line.decode('utf-8')
        seg_list = jieba.lcut(line)
        if max_len < len(seg_list):
            max_len = len(seg_list)
        if len(seg_list) <= 50:
            sum += 1
        f_writer.write(' '.join(seg_list).encode('utf-8'))
    print max_len
    print sum
    f_reader.close()
    f_writer.close()
