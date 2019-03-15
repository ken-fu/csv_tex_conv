# -*- coding: utf-8 -*-
'''メイン処理部分'''
import csv
import import_data

def csv_tex_convert(file_name):
	'''csvデータを取得、texのtebular形式に変換'''
	input_file = open('./input/'+file_name,'r')
	reader = csv.reader(input_file)
	list = []
	size_of_row = 0
	for el in reader:
		list.append(el)
		size_of_row+=1
	size_of_col = len(list[0])
	input_file.close()

	result_str = ''
	result_str += '\\begin{tabular}{|'
	for x in range(size_of_col):
		result_str += 'c|'
	result_str += '}\n'
	result_str += '\\hline\n'
	
	'''5.2E+3 -> 5.2x10^3のように変換'''
	for row in range(size_of_row):
		for col in range(size_of_col):
			if("E+" in list[row][col] or "E-" in list[row][col]):
				list[row][col] = list[row][col].replace("E+", "\(\\times 10^{").replace("E-", "\(\\times 10^{-") + "}\)"
	
	for row in range(size_of_row):
		for col in range(size_of_col-1):
			result_str += list[row][col]+'& '
		result_str += list[row][size_of_col-1]
		result_str += ' \\\ \hline\n'
	result_str += '\\end{tabular}\n'
	
	return result_str

def main():
	print('Convert CSV to TXT for latex style.')
	print('1. one file in ./input convert')
	print('2. all files in ./input convert')
	mode = input('Select : ')
	if (mode == '1'):
		file_list = import_data.import_one_file()
	else:
		file_list = import_data.import_all_file()
	
	for k in file_list:
		input_data = csv_tex_convert(k)
		output_file = open('./output/'+k.replace('csv','txt'), 'w')
		output_file.write(input_data)

if __name__ == '__main__':
    main()
