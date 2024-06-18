import qreader
import gspread

# QR code contains the data of the item
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
    
    sheet.values_append('Sheet1', {'values': [data]})

    # else update the existing entry

    sheet.values_update('Sheet1', sheet.find(data), {'values': [data]})

if __name__ == '__main__':
    get_google_sheet()
    data = read_qr_code()
    update_sheet(data)