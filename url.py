# URL-



2 Attachments

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import xlrd
from xlrd import open_workbook
import xlsxwriter
workbook=xlsxwriter.Workbook("pro.xlsx")
worksheet=workbook.add_worksheet()
proj=(['oracle',"https://www.oracle.com","0.11764705882352941"],['user',"https://www.facebook.com","0"])
row=0
col=0
for key, urln, density in (proj):
    worksheet.write(row,col,key)
    worksheet.write(row,col+1,urln)
    worksheet.write(row,col+2,density)
    row+=1
chart = workbook.add_chart({'type': 'bar'})
chart.add_series({'values': '=Sheet1!$C$1:$C$2'})
worksheet.insert_chart('F1', chart)
workbook.close()
wb = open_workbook('pro.xlsx')
for s in wb.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)

url=values[0][1]
file_handle=urlopen(url)
str=file_handle.read()
Soup=BeautifulSoup(str,"html5lib")
for script in Soup(["body","title","head"]):
    script.extract()
    c=script.get_text()


#mylist=c.split(" ")
mylist=list(c);
for x in mylist:
    if "\t" in x:
        mylist.remove("\t")
    if "\n" in x:
        mylist.remove("\n")
    b="".join(mylist)
print(b)
co=0
w=0
for x in mylist:
    d=mylist.count(x)
    
print(d)
q=b.split(" ")
print(q)
s=b.count("Oracle")
print("count of word oracle",s)
density=s/d
print("density:",density
