krediler = ["Hızlı Kredi", "Maaşını Halkban'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"]
#dizi tanımladık
print(krediler)
print(krediler[0])
print(len(krediler))
#len metodu ile dizinin uzunluğu yazdırıldı
krediler[0] = "Çabuk kredi"
#krediler dizisinin 0. elamanını yeniden tanımladık
print(krediler)
print(krediler[5])
#out of range hatası, 5.eleman krediler listesinde yoktur