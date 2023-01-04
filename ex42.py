products=[]
def read_file():
    f=open("read.txt","r")
    for line in f:
        result= line.split(",")
        my_dic={"id":result[0],"name":result[1],
         "price":result[2],"count":result[3]}
        products.append(my_dic)
        print(products)

def show_menu():
    print("1- Add")
    print("2- Remove")
    print("3- Search")
    print("4- edit")
    print("5- show list")
    print("6- Buy")
    print("7- Exit")

def add():
    id=input("id: ")
    name=input("name: ")
    price=input("price: ")
    count=input("count: ")

    new_dic={"id":id,"name":name,"price":price,"count":count}
    products.append(new_dic)
    print(products)

def remove():
    ...
def search():
    key= input("Enter your key: ")
    for product in products:
        if product["id"]==key or product["name"]==key:
            print(product)
            break
    else:
        print("not found")
def edit():
   print("which part oh your info must change : 1-Name  2-Price  3-Count")
   user_cho=int(input("Enter number :"))
   if user_cho==1:
        name=input("please enter your correct name: ")
        print("اطلاعات با موفقیت به ر,ز رسانی شد")
   elif user_cho==2:
        price=input("please enter correct price: ")
        print("اطلاعات با موفقیت به ر,ز رسانی شد")
   elif user_cho==3:
        count=input("please enter correct count: ")
        print("اطلاعات با موفقیت به ر,ز رسانی شد")


def show_list():
    print("id\tname\tprice\tcount")
    for product in products:
        print(product["id"], "\t" ,product["name"],"\t",product["price"],"\t",product["count"])
def buy():
    ...
def exit():
    ...
def save_to_database():
    ...
read_file()
while True:
    show_menu()
    print(products)
    user_choice= int(input("Enter your choice: "))
    if user_choice ==1:
        add()
    elif user_choice==2:
        remove()
    elif user_choice==3:
        search()
    if user_choice==4:
        edit()
    elif user_choice==5:
        show_list()
    elif user_choice==6:
        buy()
    elif user_choice==7:
        exit(0)
        save_to_database()
    else:
        print("Please select another")
