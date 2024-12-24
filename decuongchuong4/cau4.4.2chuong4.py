class Book:
    page = 0
    name = 0
    cost = 0
    def __init__(self):
        self.name=''
        self.page=0
        self.cost=0
        self.average=0
    def nhap(self):
        self.name=input()
        self.page=int(input())
        self.cost=int(input())
        self.average=round(self.page / self.cost,2)
    def xuat(self):
        print(self.name,self.page,self.cost,self.average)
n = int(input())
books=[]
for i in range (n):
    print("nhap quyen sach thu"i+1)
    book=Book()
    book.nhap()
    books.append(book)
books.sort(key=lambda X:X.average)
for b in book:
    b.xuat()