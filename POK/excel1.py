import xlsxwriter

workbook  = xlsxwriter.Workbook('filename1.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 5, 'nejde to')

workbook.close()