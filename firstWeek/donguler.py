krediler = ["Hızlı Kredi", "Maaşını Halkban'tan alanlara özel", "Mutlu Emekli İhtiyaç Kredisi"]
for kredi in krediler:
  print(kredi)
#for döngüsü krediler dizisindeki elemanları sırası ile gezdi. bu gezilen değere kredi ismi verip o değeri print ettik, bu değere alias denilebilir.
for i in range(10):
  print(i)
#verilen range değeri kadar çalışır. 0'dan başlayarak range değerine kadar(10 dahil değil) print ile yazdırdık
for i in range(len(krediler)):
  print(krediler[i])
#i alias'ını krediler dizisinin elemanlarını gezecek şekilde yazdık, bunu krediler dizisinin uzunluğunu range olacak şekilde vererek yaptık
for i in range(3,10):
  print(i)
#3 dahil 10 dahil değil(sınır dahil olmaz)
for i in range(0,11,2):
  print(i)
#0'dan başlayarak 11'e kadar 2'şer 2'şer yazdırdık
for kredi in krediler:
  print("<option>"+kredi+"<option>")