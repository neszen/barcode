import barcode
from barcode.writer import ImageWriter

product_number = '123456789011'
BarcodeClass = barcode.get_barcode_class('ean13')
ean = BarcodeClass(product_number , writer=ImageWriter())

filename = ean.save('barcode')








