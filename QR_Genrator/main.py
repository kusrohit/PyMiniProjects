# QR Generator
# requires : qrcode library
#
# To generate black and white qr
# pip install qrcode

import qrcode as qr

img = qr.make('https://www.github.com/kusrohit')
img.save('GithubProfile.png')
