__author__ = 'p369c258'
import qrcode
for line in open("p.txt"):
    img = qrcode.make('%s'% line.strip())
    img.save('%s.png'% line.strip())
