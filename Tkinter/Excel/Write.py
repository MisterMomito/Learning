import xlsxwriter

# Create file (workbook) and worksheet
out_workbook = xlsxwriter.Workbook('out.xlsx')
out_sheet = out_workbook.add_worksheet()

# Declare Data
names = ['Kyle', 'Bob', 'Mary']
values = [70, 82, 71]


# Write Headers
out_sheet.write('A1', 'Names')
out_sheet.write('B1', 'Scores')

# Write data to file
for item in range(len(names)):
   out_sheet.write(item+1, 0, names[item])
   out_sheet.write(item+1, 0, values[item])

out_sheet.write('D1', 'Total')

'''
OR

out_sheet.write('A2', names[0])
out_sheet.write('A3', names[1])
out_sheet.write('A4', names[2])

out_sheet.write('B2', values[0])
out_sheet.write('B3', values[1])
out_sheet.write('B4', values[2])
'''

out_sheet.write_formula('D2', '=SUM(B2:B4)')

out_workbook.close()  # Closes the workbook