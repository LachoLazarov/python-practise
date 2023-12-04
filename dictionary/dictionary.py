#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things
# to save your village, and probably some good looking girl or boy you want to marry.
# All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed
# from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

#morning inventory
department_store = {}
for department in (freelancers, antiques, pet_shop):
    department_store.update(department)
    department_store.pop('name')
    print('Morning inventory of stores', sorted(department_store.items()))
    print('--------------------')
#create an dempty shopping cart
cart = {}
# purse
purse = 1000
buy_items1 = ''
#loop through stores/dicts
for shop in (freelancers,antiques,pet_shop) :
    #inputbox  to show what you can buy...capture textstring of what was bought...make lowercase
    buy_item = input(f'Welcome to {shop["name"]}! (type exit to exit store) What do you want to buy: {shop}').lower()
    # exit the store
    if buy_item == 'exit':
        continue
    if buy_item not in shop:
        continue
    #update the string
    buy_items1 = buy_items1 + f'{buy_item}:{shop[buy_item]} gold, '
    #update the cart
    cart.update({buy_item:shop.pop(buy_item)}) # use pop...
    items = ", ".join(list(cart.keys()))
    total_sum = sum(cart.values())
print(f'You Purchased {buy_items1}. Your total purse is {total_sum} gold. Your change is {purse - total_sum} gold. Have a nice day of mayhem!')

#ver 1.2 add ability to exit a store without buying and go to the next by typing 'exit',
# and to exit if a nonexistant item is bought.
# Add purse with 1000 gold pieces and payment for the items during or at the end of code and show a message
# about total cost and how much gold you have left

#ver 1.5 print inventory befire and after purchases as one department_store of stuff(combine inventories  from stores
# into one ...pretend Big Biz bought all the local stores, and want constant reporting from inventory)
department_store_after = {**freelancers, **antiques, **pet_shop}
department_store_after.pop('name')
print('--------------------')
print('Evening inventory of stores', sorted(department_store_after.items()))
