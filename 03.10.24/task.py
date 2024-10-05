def register():
    print('Registration Portal')
    if len(user)==0:
        id=1000
    else:
        id=user[-1]['id']+1
    email=str(input('Enter your email :'))
    f=0
    for i in user:
        if i['email']==email:
            f=1
            print('Email already exists enter another one')
            register()
    if f==0:
        name=str(input('enter your name : '))
        phone=int(input('enter your number : '))
        password=input('enter the password : ')
        print('Registration Succesfull email id is your username')
        user.append({'id':id,'name':name,'email':email,'phone':phone,'password':password,'book':[]})

def login():
    usern=str(input('Enter Username : '))
    passw=input('Enter password : ')
    f=0
    u=''
    if usern=='admin' and passw=='admin':
        f=1
    for i in user:
        if usern==i['email'] and passw==i['password']:
            f=2
            u=i
    return f,u

def add_ph():
    print('ADD PHONE')
    if len(lib)==0:
        id=1
    else:
        id=lib[-1]['id']+1
    name=str(input('enter name : '))
    price=int(input('enter the price : '))
    stock=int(input('enter the stock availible : '))
    lib.append({'id':id,'name':name,'price':price,'stock':stock,})

def view_ph():
    print('PHONE DETAILS')
    print("{:<5}{:<15}{:<15}{:<15}".format('ID','MODEL NAME','PRICE','STOCK'))
    print('_'*40)
    for i in lib:
        print("{:<5}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['price'],i['stock']))

def update_ph():
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id:
            price=int(input('enter the price : '))
            stock=int(input('enter the stock : '))
            i['price']=price
            i['stock']=stock
            print('Details Updated')
            f=1
    if f==0:
        print('invalid id')

def delete_ph():
    id=int(input('enter the id : '))
    f=0
    for i in lib:
        if i['id']==id:
            lib.remove(i)
            print('data deleted')
            f=1
    if f==0:
        print('Invalid id')

def view_usr():
    print('USERS DETAILS')
    print("{:<10}{:<15}{:<15}{:<15}".format('ID','NAME','EMAIL','PHONE'))
    print('_'*55)
    for i in user:
        print("{:<10}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['email'],i['phone']))

def buy_ph(u):
    print('PHONE DETAILS')
    print("{:<5}{:<15}{:<15}{:<15}".format('ID','MODEL NAME','PRICE','STOCK'))
    print('_'*40)
    for i in lib:
        print("{:<5}{:<15}{:<15}{:<15}".format(i['id'],i['name'],i['price'],i['stock']))
    id=int(input('enter the id : '))
    f=0
    if i['id']==id:
        if i['stock']>0:
            i['stock']-=1
            # ---------------
        u['book'].append(id)
            # ---------------
        f=1
        amt=int(input('enter the amount needed : '))
        ttl=i['price']*amt
        print('Total Bill amount is : ',ttl)
    else:
        print('out of stock')   
    if f==0:
        print('no id availible')

def view_order():
     for i in user:
        print(f"Name : {i['name']} And Orders : {i['orders']}")   


user=[{'id': 1000, 'name': 'Roshan', 'email': 'r@','phone': 920712, 'password': 'qwer','book':[1,2]}]
lib=[{'id': 1, 'name': 'vivo t2', 'price': 20000, 'stock': 7},{'id': 2, 'name': 'redmi 7a', 'price': 140000, 'stock': 4}]
while True:
    print('''
    1.Register as User
    2.Login
    3.EXIT''')
    c=int(input('enter your choice : '))
    if c==1:
        register()
    elif c==2:
        f,u=login()
        if f==1:
            while True:
                print('''
                1.Add phone
                2.View phone
                3.Update phone 
                4.Delete phone
                5.View Users
                6.Logout''')


                c1=int(input('enter your choice : '))
                if c1==1:
                    add_ph()
                elif c1==2:
                    view_ph()
                elif c1==3:
                    update_ph()
                elif c1==4:
                    delete_ph()
                elif c1==5:
                    view_usr()
                elif c1==6:
                    break
                else:
                    print('invalid Choice')

        elif f==2:
            while True:
                print('''
                    1.view phone
                    2.buy phone
                    3.view order
                    4.logout''')
                c1=int(input('enter your choice : '))
                if c1==1:
                    view_ph()
                elif c1==2:
                    buy_ph()
                elif c1==3:
                    view_order()
                elif c1==4:
                    break
                else:
                    print('invalid choice')
                    
    elif c==3:
        break
    else:
        print('invalid choice')