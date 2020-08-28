import os
import csv
import qrcode
from qrcode.image.pure import PymagingImage

with open('qr_list.txt', newline='') as csvfile:
    qrReader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for line in qrReader:
        name = line[0]
        url = line[1]
        img = qrcode.make(url)
        nameString = os.path.join('qrCodes', name + '.png')
        img.save(nameString)
