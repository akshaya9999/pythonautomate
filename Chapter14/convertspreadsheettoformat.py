import ezsheets

ss = ezsheets.upload('invertedspreadsheet.xlsx')

ss.downloadAsCSV()
ss.downloadAsExcel()
ss.downloadAsHTML()
ss.downloadAsODS()
ss.downloadAsPDF()
ss.downloadAsTSV()