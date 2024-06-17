from qreader import QReader
import cv2 as cv

# Database schema:
#  - id: int
#  - equipment name: str
#  - video file: str
#  - steps processes: pdf

reader = QReader()

img = cv.cvtColor(cv.imread('qrcode.png'), cv.COLOR_BGR2RGB)

decoded_text = reader.detect_and_decode(image=img)



# returns id of the item
# if the database doesn't have it, add
# if it does then retrieve the safety manual