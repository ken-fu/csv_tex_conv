# -*- coding: utf-8 -*-
'''入力データリスト取得処理部分'''

import csv
import glob
import os

def import_all_file():
    '''inputフォルダにあるファイルを無条件に全て取得する'''
    path = './input'
    file_list = os.listdir(path)
    if '.DS_Store' in file_list:
        file_list.remove('.DS_Store')
    if '.gitkeep' in file_list:
        file_list.remove('.gitkeep')
    return file_list

def import_one_file():
    '''単一ファイルの取得'''
    while True:
        try:
            print('Please input filename. (zzzz of zzzz.csv)')
            filename = input("filename is ")
            input_file = open('./input/' + filename + '.csv', 'r')
            break
        except FileNotFoundError:
            print("%s is not found. " % (filename,))
    input_file.close()
    # 上記にある他のimport_file系関数と異なりファイル名を配列等に格納する手順がない
    # そのため返り値に拡張子をくっつける
    return [filename + '.csv']
