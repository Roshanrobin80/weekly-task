# S P O R T S   S H O P   M A N A G E M E N T   S Y S T E M
shop=[]
id=1000
while True:
    print('''
1.Add products
2.View products
3.Update products
4.Delete products
5.Search products
6.Exit 
''')
    ch=int(input('Enter your choice: '))
    if ch==1:
        pname=str(input('Enter the name of product: '))
        pirce=int(input('Enter the price of product: '))
        stock=int(input('Enter the stock of product'))

    elif ch==2:
        for i in shop:
            print(i)

    elif ch==3:
        pname=str(input('Enter the name of product: '))
        f=0
        for i in shop:
            if i['pname']==pname:
                nstock=int(input('enter new stocks of product: '))
                nprice=int(input('enter new price: '))
                i['stock']=nstock
                i['price']=nprice
                f=1
        if f==0:
            print('invalid name')

    elif ch==4:
        pname=str(input('enter product name: '))
        f=0
        for i in shop:
            if i['pname']==pname:
                shop.remove(i)
                f=1
        if f==0:
            print('invalid name')
    elif ch==5:
        break
    else:
        print('invalid choice')

