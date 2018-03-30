'''
Import Required Libraries
'''
import matplotlib.pyplot as plt
import glob
import numpy as np

'''
Get Data from File
'''

path = "/home/chris/Data_Analyst/Mobile_Data/*.csv"
data = glob.glob(path)
basedata = ''
for filename in data:
	f = open(filename, 'r')
	basedata += f.read()
	f.close()
datalist = basedata.split("\n")

'''
SMS List
'''
SMSlist = ''
for item in datalist:
	try:
		if item[23] == "S":
			SMSlist += item + ','
	except IndexError:
		continue
SMSitemised = SMSlist.split(',')

'''
Getting hour of text messages
'''
hour = []
for ind in range(4, len(SMSitemised), 16):
	if SMSitemised[ind][6:8] == 'pm':
		if int(SMSitemised[ind][0:2]) == 12:
			hour.append(12)
		else:
			hour.append(int(SMSitemised[ind][0:2]) + 12)
	else:
		if int(SMSitemised[ind][0:2]) == 12:
			hour.append(0)
		else:
			hour.append(int(SMSitemised[ind][0:2]))

'''
Plotting histogram 
'''
values, bins = np.histogram(hour, bins=range(0, 24))
plt.bar(bins[1:], values, align='center')
plt.xlim(xmin=1)
plt.xticks(range(0, 24))
plt.xlabel('Hour of Day')
plt.ylabel('SMS')
plt.title('Volume of SMS per hour')
plt.show()
