import xlsxwriter

workbook  = xlsxwriter.Workbook("typstoziara,druh,rozsah" + '.xlsx')
worksheet = workbook.add_worksheet()


worksheet = workbook.add_worksheet("novy")
worksheet.set_column(0, 4, 24.86)
worksheet.write(0, 0, "typstoziara")
worksheet.write(1, 0, "Vzdialenosť (m)")
worksheet.write(1, 1, "Nulová zložka Impenancie")
worksheet.write(1, 2, "Súsledná zložka Impenancie")
worksheet.write(1, 3, "Spätná zložka Impenancie")
   
for i in range(5):  
    worksheet.write(i+2, 0, i+2)
    worksheet.write(i+2, 1, i+3)
    worksheet.write(i+2, 2, i+4)
    worksheet.write(i+2, 3, i+5)
    
worksheet.write(2, 4, "=SUM(A3:D3")

workbook.close()