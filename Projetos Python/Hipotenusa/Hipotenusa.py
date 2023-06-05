# import math
from math import hypot
from exceptions import exceptions_float
co = exceptions_float("Comprimento do cateto oposto: ")
ca = exceptions_float("Comprimento do cateto adjacente: ")
# hipo = math.sqrt((co**2) + (ca**2))
hipo = hypot(co,ca)
print("A hipotenusa vai medir {:.2f}".format(hipo))
