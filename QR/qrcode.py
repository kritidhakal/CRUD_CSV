import csv
import pyqrcode
import png
with open('../CSV/register.csv', 'r') as inp:
    for row in csv.reader(inp):
        content = row[0]+','+row[1]+','+row[2]
        qr = pyqrcode.create(content)
        qr.png(f'code{row[0]}.png', scale = 8)
            