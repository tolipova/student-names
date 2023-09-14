# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

#     def move(self):
#         print("drive")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("uchdi")

# car = Car("Ford","Mustang") 
# boat = Boat("Qayiqmodel","Qayiq nomi")   

# for x in (car,boat):
#     x.move()

class Students:
    def __init__(self,student_number,uzlashtirishi,heigh_uzlashtirishi):
        self.student_number = student_number
        self.uzlashtirishi = uzlashtirishi
        self.heigh_uzlashtirishi = heigh_uzlashtirishi
class Sinf:
    def __init__(self) :
        self.list_name = []

    def add_name(self,student_number):
        self.list_name.append(student_number)


    def find_name(self,student_number):
        for name in self.list_name :
            if name.student_number == student_number :
                return name
        return None   

    def darsga_kelmadi(self,student_number):
        name = self.find_name(student_number)
        if name is not None:
            name.uzlashtirishi = "darsga kelmagan"
            print(f"{name.student_number} bugun darsga kelmagan")
        else:
            print("Xato ism")    
 
    def  darsga_keldi(self,student_number):
        name = self.find_name(student_number)
        if name is not None:
            name.uzlashtirishi = "darsda bor"
            print(f"{name.student_number} bugun darsga kelgan")
        else:
            print("Xatolik")    


    def  yaxshi_baho(self,student_number):
        name = self.find_name(student_number)
        if name is not None:
            name.heigh_uzlashtirishi = "yaxshi uzlashtirdi"
            print(f"{name.student_number} darsni yaxshi uzlashtirdi va a'lo baho oldi")
        else:
            print("yaxshi_baho da xato")    

    def  yomon_baho(self,student_number):
        name = self.find_name(student_number)
        if name is not None:
            name.heigh_uzlashtirishi = "yaxshi uzlashtirmadi"
            print(f"{name.student_number} darsga yaxshi tayyorlanmagan va past baho oldi")
        else:
            print("yomon_baho da xato")      

    def display_name(self):
        print("Hamma o'quvhcilar: ") 
        for name in self.list_name:
            print(f"{name.student_number} {name.uzlashtirishi} {name.heigh_uzlashtirishi}")

sinf = Sinf()
student=Students("Tolipova Shahina","darsda bor","yaxshi uzlashtirdi")
sinf.add_name(student)
student=Students("Abdullayeva Sabina","darsda bor","yaxshi uzlashtirdi")
sinf.add_name(student)
student=Students("Bozorov SHohruh","darsga kelmagan","yaxshi uzlashtirmadi")
sinf.add_name(student)
student=Students("Djalilova Jasmina","darsda bor","yaxshi uzlashtirmadi")
sinf.add_name(student)
student=Students("Ergashev Davron","darsda bor","yaxshi uzlashtirdi")
sinf.add_name(student)
student=Students("Ochilova Dilshoda","darsda bor","yaxshi uzlashtirdi")
sinf.add_name(student)
student=Students("Shamsiyev Otabek","darsga kelmagan","yaxshi uzlashtirmadi")
sinf.add_name(student)
student=Students("Raximov Said","darsda bor","yaxshi uzlashtirmadi")
sinf.add_name(student)
student=Students("Burxonova Amina","darsda bor","yaxshi uzlashtirmadi")
sinf.add_name(student)
student=Students("Tilavova Shahrizoda","darsda bor","yaxshi uzlashtirmadi")
sinf.add_name(student)
student=Students("Jurayev SHohruh","darsga kelmagan","yaxshi uzlashtirmadi")
sinf.add_name(student)
sinf.display_name()


while True:
    choice = input("Onlayn sinf ruyxati bilan tanishishingiz mumkin.Agar siz tanlasangiz (1)darsga_keldi, (2)darsga_kelmadi,(3)yaxshi baho olgan  bahosi,(4)yomon baho olgan (5)Umumiy ruyxat ,(6)dasturdan chiqasiz.")
    if choice == '6':
        print("Xayr , salomat bo'ling")
        break
   
    if choice not in ['1','2','3','4','5']:
        print("Xato raqam tanladiz")
        continue
    number = input("O'quvchining ism/familiyasini kiriting: ")

    if choice == '1':
        sinf.darsga_keldi(student_number)
    elif choice == '2' :
        sinf.darsga_kelmadi(student_number)
    elif choice == '3':
        sinf.yaxshi_baho(student_number)
    elif choice == '4':
        sinf.yomon_baho(student_number)
    elif choice == '5':   
        sinf.display_name()


