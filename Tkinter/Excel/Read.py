import xlrd

path = 'book.xlsx'

input_workbook = xlrd.open_workbook(path)

input_worksheet = input_workbook.sheet_by_index(0)

# Prints number of rows and columns
print(input_worksheet.nrows)
print(input_worksheet.ncols)

print(input_worksheet.cell_value(1, 0))  # print cell, column 0, row 1

names = []
scores = []

'''
names.append(input_worksheet.cell_value(1, 0))
names.append(input_worksheet.cell_value(2, 0))
names.append(input_worksheet.cell_value(3, 0))

OR
'''

for y in range(1, input_worksheet.nrows):
    names.append(input_worksheet.cell_value(y, 0))
    scores.append(input_worksheet.cell_value(y, 1))

print(names)
print(scores)
