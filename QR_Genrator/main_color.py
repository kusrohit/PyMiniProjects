# QR Generator
# requires : qrcode library
#
# To generate colored qr
# pip install qrcode

from qrcode import *

qr = main.QRCode(version=1,
                 error_correction=constants.ERROR_CORRECT_H,
                 box_size=10,
                 border=4)

qr.add_data('https://www.twitter.com/kushtwts')
qr.make(fit=True)

img = qr.make_image(fill_color='blue', back_color='white')
img.save('TwitterProfile.png')
