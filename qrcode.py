import qreader
import gspread
import pandas as pd

# QR code contains the data of the item

df = pd.read_csv('Gas_Inventory.csv')

for i in range(0, len(df)):
    qr = qreader.QRCodeWriter()
    qr.encode(df.iloc[i]['QR Code'])
    qr.save(f'qr_code{i}.png')


qr = qreader.QRCodeWriter()
qr.encode('https://docs.google.com/spreadsheets/d/18WtEVH14YbyUWgkUwkjoFihb9zREhAnDKUEWWyV3zrM/edit')
qr.save('qr_code.png')

def read_qr_code():
    qr = qreader.QRCodeReader()
    qr.decode('qr_code.png')
    return qr.data

def get_google_sheet():
    gc = gspread.service_account(filename='service_account.json')
    sheet = gc.open('Inventory')
    return sheet

def update_sheet(data):
    sheet = get_google_sheet()
    # if the sheet does not contain the entry already
    
    if not sheet.find(data):
        sheet.values_append('Sheet1', {'values': [data]})
    else:
        sheet.values_update('Sheet1', sheet.find(data), {'values': [data]})

if __name__ == '__main__':
    get_google_sheet()
    data = read_qr_code()
    update_sheet(data)