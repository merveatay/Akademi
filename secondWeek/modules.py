#farklı modüllere/dosyolara erişim
import mat
print(mat.topla(10,20))

#alias, importlara isim verme.alias modüle özeldir
import mat as m
print(m.topla(10,20))

import random #built in modül
print(random.randint(0,10))

#modülün istenen kısım import etme
from mat import topla
print(topla(10,20)) #tüm ismi kullanamayız burada sadece import ettiğimizi yazarız

# from mat import topla as toplama
# from pair import nums #farklı sayıda import edilebilir, değişken import edilebilir
# print(topla(10,20))

from classes import Human
human1 = Human("Jane")
human1.talk("Selam")

#packages

