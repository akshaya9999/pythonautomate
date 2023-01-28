import ezsheets

ss=ezsheets.Spreadsheet('1YmBZQuzN7IXbLnrxy6MET10DBMpjqMntHQPSF8cUGz4')
sheet=ss[0]

column3=sheet.getColumn(3)
for i in column3:
    print(i)