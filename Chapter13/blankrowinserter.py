import openpyxl

wb=openpyxl.load_workbook('multiplicationtable.xlsx')
n=int(input("enter n"))
m=int(input("enter m"))
sheet=wb.active
sheet.insert_rows(n,m)
wb.save('multiplicationtabelwithspace.xlsx')