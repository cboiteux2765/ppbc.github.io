from qreader import QReader
import cv2 as cv
import gspread

service_account = gspread.service_account(filename='service_account.json')
sheet = service_account.open('Sample_H2O_O2 Counts_032423').sheet1

wks = sheet.worksheet('H2O/O2 Counts')

wks.update('A1', 'Hello World')

def open_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)

current_row = open_row(wks)
wks.update(f'A{current_row}', 'JSON values from HTML')

# Database schema:
#  - id: int
#  - equipment name: str
#  - video file: str
#  - steps processes: pdf

# add all values to db

reader = QReader()

img = cv.cvtColor(cv.imread('qrcode.png'), cv.COLOR_BGR2RGB)

decoded_text = reader.detect_and_decode(image=img)



# returns id of the item
# if the database doesn't have it, add
# if it does then retrieve the safety manual