class Library:
    def __init__(self):        #listelerde yazmama gerek yok
        self.users=[]
        self.books=[]
        self.writers=set()
    def writers_appends(self):
        self.writers.clear()
        for i in self.books:
            self.writers.add(i.writer)    #burda hata olabilir
    def writers_knowledge(self):
        return self.writers
    def books_append(self,book):
        if book not in self.books:
            self.books.append(book)
            self.writers_appends() 
        else:print("burda var kör")
    def books_remove(self,book):
        if book in self.books:
            self.books.remove(book)
            self.writers_appends()
        else:print("burda bi yarrram yok")
    def user_appends(self,user):
        if user not in self.users:
            self.users.append(user)
        else:print("burda amk")
    def user_remove(self,user):
        if user in self.users:
            self.users.remove(user)
        else:print("zaten yohk allam")
class Book:
    def __init__(self,name,writer,pagenumber,year,writinghouse,id_no):
        self.name=name
        self.writer=writer
        self.pagenumber=pagenumber
        self.year=year
        self.writinghouse=writinghouse
        self.id_no=id_no
    def __str__(self):
        return f"{self.name}-{self.writer}-{self.pagenumber}-{self.year}-{ self.writinghouse}-{self.id_no}"       
class User:
    def __init__(self,name,surname,born,):
        self.name=name
        self.surname=surname
        self.born=born
        self.take=[]
        self.lastbook= None
        self.favourite=[]
        self.waiting=0
        self.waitingbookname=[]
    def favourite_appends(self,book):
        if book not in self.favourite:
            self.favourite.append(book)
        else:print("zaten favorilerde ag")
    def favourite_remove(self,book):
        if book in self.favourite:
            self.favourite.remove(book)
        else: print("ekli değil mk")
    def book_take(self,book):
        if self.waitingbookname<3:
            if book not in self.waitingbookname:
                self.waiting+=1
                self.waitingbookname.append(book)
                self.take.append(book)
                self.lastbook=book
            else:print("zaten sende")
        else:print("yeter la bu kadar diğer kitapları geri getir")
    def book_remove(self,book):
        if book in self.waitingbookname:
            self.waitingbookname.remove(book)
            self.waiting-=1
        else:print("yok işte mk sende")
    def __str__(self):  #yeni ekledim
        return f"{self.name} {self.surname}, doğum yılı: {self.born}"
isdfl_library=Library()
user1=User("arda","kaklkanlı","2006")
user2=User("şako","sjsjsjjss","2000")
user3=User("sefo","bilmemmi","2017")
user4=User("yarrra","beni","2014")
book1=Book("kısa yoldan bölme","ahmet kaya",120,1923,"epsilon",1)
book2=Book("kuklacı","abasıyanık",45,2014,"beyazıt",2)
book3=Book("selamlar","meralle",10,2017,"fsm",3)
book4=Book("kalkan","anan",77,1923,"düden",4)
isdfl_library.user_appends(user1)
isdfl_library.user_appends(user2)
isdfl_library.user_appends(user3)
isdfl_library.user_appends(user4)
isdfl_library.books_append(book1)
isdfl_library.books_append(book2)
isdfl_library.books_append(book3)
isdfl_library.books_append(book4)
for user in isdfl_library.users:
    print(user)
