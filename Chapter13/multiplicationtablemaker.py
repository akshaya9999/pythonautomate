import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
n=int(input("enter no of rows"))
a=65
for i in range(1,n+1):   #for row heading
    sheet[f'A{i+1}']=i
    for i in range(1,n+1):   #for values
        for j in range(1,n+1):
            sheet[f'{chr(a+i)}{j+1}']=i*j

for i in range(1,n+1):   #for column heading
    a=a+1
    x=chr(a)
    sheet[f'{x}1']=i

wb.save('multiplicationtable.xlsx')