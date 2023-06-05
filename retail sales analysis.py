item_dict={
    'name':['banana shake','orange juice','mango shake','coffee','tea'],
    'category':['shakes','juices','shakes','beverages','beverages'],
    'price':[50,40,60.50,25.25,10],
    'quantity':[5,4,5,10,25],
    'total_sales':[250,160,302.50,252.50,250]
}

#add
def add():
    while(True):
        name=input('enter the name of the item:')
        category=input('enter the item category:')
        price=float(input('enter the item price:'))
        quantity=int(input('enter the item quantity:'))
        item_dict['name'].append(name)
        item_dict['category'].append(category)
        item_dict['price'].append(price)
        item_dict['quantity'].append(quantity)
        t_sales=price*quantity
        item_dict['total_sales'].append(t_sales)
        print('item added to the menu:')
        print('Name:',name)
        print('category:',category)
        print('price:',price)
        print('quantity:',quantity)
        print()
        more=input('do you want to add more items?(y/n):').lower()
        if(more=='y'):
            continue
        elif(more=='n'):
            break
        else:
            print('invalid entry')
#add
#update
def update():
    view_items()
    while(True):
        name=input('enter the name of the item:')
        if(name in item_dict['name']):
            index=item_dict['name'].index(name)
            print(f'Existing Quantity of {name}:',item_dict['quantity'][index])
            new_quantity=int(input('enter the new Quantity:'))
            item_dict['quantity'].pop(index)
            item_dict['quantity'].insert(index,new_quantity)
            print(f'New updated Quantity of {name}:',item_dict['quantity'][index])
            print()
            break
        else:
            print('Item does not exist. Enter correct Item name')
            continue

#sale analysis
def sale_analysis():
    analysis_list=[]
    for data in zip(item_dict['total_sales'],item_dict['name']):
        analysis_list.append(list(data))
    analysis_list.sort(reverse=True)
    for sales,name in analysis_list:
        print(f'{name}:{sales}')
    print()

#sale analysis
#update
# view items
def view_items():
    import pandas as pd
    show=pd.DataFrame(item_dict)
    show.rename(columns={'name':'Item Name','category':'Item Category','price':'Item Price','quantity':'Item Quantity','total_sales':'Item Total Sales'},inplace=True)
    print(show)
#view items
#main

while(True):
    print('Welcome to the Cafe inventory and sales tracker!')
    print('What would you like to do?', end='')
    print('''
1.Add new items to the menu.
2.Update item quantities.
3.view sales summary.
4.view sales analysis.
5.Quits''')
    choice = int(input('enter your choice(1-5):'))

    if(choice==1):
        add()
        continue
    elif(choice==2):
        update()
        continue
    elif(choice==3):
        view_items()
        continue
    elif(choice==4):
        sale_analysis()
        continue
    elif(choice==5):
        break
    else:
        print('Invalid choice')


#main