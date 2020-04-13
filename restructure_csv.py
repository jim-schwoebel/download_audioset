
# YouTube restructure 
import os, time
import xlsxwriter
from tqdm import tqdm

g=open('unbalanced_train_segments.csv').read()
h=g.split('\n')
ids=list()
starts=list()
ends=list()
classes=list()

for i in tqdm(range(len(h)), desc='reading data'):
	try:
		temp=h[i].split(', ')
		# print(temp)
		id_=temp[0]
		start=temp[1]
		end=temp[2]
		class_=temp[3].split(',')
		
		for j in range(len(class_)):
			ids.append(id_)
			starts.append(start)
			ends.append(end)
			classes.append(class_[j].replace('"',''))
		# print(len(ids))
		# print(len(starts))
		# print(len(ends))
		# print(len(classes))
		# time.sleep(1)
		
	except:
		pass

# now make a dataframe
workbook = xlsxwriter.Workbook('unbalanced_train_segments.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Ids')
worksheet.write('B1', 'Start')
worksheet.write('C1', 'End')
worksheet.write('D1', 'Class')

for i in tqdm(range(len(ids)), desc='writing excelsheet'):
	worksheet.write('A%s'%(str(i+2)), ids[i])
	worksheet.write('B%s'%(str(i+2)), starts[i])
	worksheet.write('C%s'%(str(i+2)), ends[i])
	worksheet.write('D%s'%(str(i+2)), classes[i])

workbook.close()