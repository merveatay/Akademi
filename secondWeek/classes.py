# class Human:
#     def talk(self):
#         print("Human talking")
#     def walk(self):
#         print("Human walking")
# human1 = Human() #instance from class
# human1.talk()

class Human:
    #built-in fonk. nesne ürettiğimizde çalışan alan. önce çalışır
    def __init__(self,name):
        self.name =name #aşağıdaki isimlerviçin kullandık 
        print("Human inst. üretildi")
    def __str__(self): #print nesne yapıldığında adres yerine ne yazılacağını conf.etmek içinkullanıldı
        return f"Str fonk. dönen değer: {self.name}"
    def talk(self, sentence): #self res. parametredir
        name = "Ayşe"
        print(f"{sentence} {self.name}") #fstring değişken yazdırabilmek için
        #self kullanmazsak def içindeki aynı isimli değişkeni alır. self kullanarak class içindeki değişkene erişiriz
    def walk(self):
        print("Human walking")
human1 = Human("Merve") #instance from class
human1.name = "Fatma" #bu tanımdan sonra merhaba fatma yazar
human1.talk("Merhaba")
print(human1)

