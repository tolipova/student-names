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
    def __init__(self,student,baho):
        self.student = student
        self.baho = baho


class Sinf:
    def __init__(self) :
        self.list_name = []

    def add_name(self,name):
        self.list_name.append(name)


    def find_name(self,student):
        for name in self.list_name :
            if name.student == student :
                return name
        return None   

    def darsga_kelmadi(self,student):
        name = self.find_name(student)
        if name is not None:
            name.baho = 'darsga kelmagan'
            print(f"{name.student} bugun darsga kelmagan")
        else:
            print("Xato ism")    
 
    def  darsga_keldi(self,student):
        name = self.find_name(student)
        if name is not None:
            name.baho = 'darsda bor'
            print(f"{name.student} bugun darsga kelgan")
        else:
            print("Xatolik")    


    def  yaxshi_baho(self,student):
        name = self.find_name(student)
        if name is not None:
            name.baho = 'yaxshi uzlashtiradi'
            print(f"{name.student} darsni yaxshi uzlashtirdi va 5baho oldi")
        else:
            print("yaxshi_baho da xato")    

    def  yomon_baho(self,student):
        name = self.find_name(student)
        if name is not None:
            name.baho = 'yaxshi uzlashtirmadi'
            print(f"{name.student} darsga yaxshi tayyorlanmagan va pas baho oldi")
        else:
            print("yomon_baho da xato")      

    def display_name(self):
        print("Hamma o'quvhcilar: ") 
        for name in self.list_name:
            print(f"{name.student}:{name.baho}")             


student = Students()
student.add_name(Sinf("Tolipova Shahina","darsda bor"))

