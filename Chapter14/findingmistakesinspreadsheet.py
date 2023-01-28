import ezsheets
ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

sheet=ss[0]

for rowNum in range(2,15002):
    if int(ss[0].getRow(rowNum)[0]) * int(ss[0].getRow(rowNum)[1]) != int(ss[0].getRow(rowNum)[2]):
        print(rowNum,'is not correct')


