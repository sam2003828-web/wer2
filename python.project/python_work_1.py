from tkinter.font import names

from numpy import empty


name="zixuan shih"
print(name.title())#.title 首字母大寫

first_name="sam"
last_name="shih"
full_name=f"{first_name}{last_name}"
print(full_name.title())

first_name="sam"
last_name="shih"
full_name=f"{first_name} {last_name}"
print(f"hello, {full_name.title()}!")

print("\tpython")#\t tab一下
print("python")
print("python\nC\nJava")#\n換行
favorite_language='python '
print(repr(favorite_language))
favorite_language='python '
favorite_language=favorite_language.rstrip()
print(repr(favorite_language))#repr顯示空格 strip左右空格都刪除 不然就r跟l
#數字不用引號但英文要
asd_ad='prepare'
asd_ad=asd_ad.removeprefix('pre')
print(asd_ad)
#decimal 小數 callecd float
#the zen of python
 #[] list
name=['sam','oscar','mathew']
print(name[0])
print(name[-3])
#list 可以跟其他txt format
name=['sam','oscar','mathew']
print(name[0])
print(name[-3])
name=['sam','oscar','mathew']
message=f"my best friend is {name[2].title()}"
print(message)
name=['sam','mathew','wer2']
print(name)
#設定誰是第一
name[0]='wer2'
name[1]='sam'
print(name)
name.append('nick')
print(name)
num=[]
num.append(1)
num.append(2)
print(num)
#insert可指定位置append加在最後
num.insert(1,1.5)
print(num)
num=(1,2,3)
print(num)
# tuple is immutable, so item assignment like num[0] = 1 would raise TypeError
#()裡面的東西不能動[]可動{}打在裡面的東西可以直接print出來表格類的用也有去重用
student={"name":"sam","age":20}
print(student["name"])
num={1,2,2,3,3,4}
print(num)
num.remove(4)
print(num)
#del 要在list才能用如果是{}用remove
#pop刪掉最後面且可以把刪掉的拿出來繼續使用 ()內的數字決定刪掉哪個
name=['sam','oscar','mathew','wer2'] 
last_name=name.pop(3)
print(f"{last_name.title()} is not my friend")
name=['sam','oscar','mathew','wer2']
del name[1]
print(name)
cars=['BMW','AUDI','toyota']
cars.sort()
print(cars)#照字母表
cars=['BMW','AUDI','toyota']
cars.sort(reverse=True)
print(cars)#reverse 永久的
#暫時list
cars=['BMW','AUDI','toyota']
print('here is orignal list:')
print(cars)
print('\nhere is the sorted list:')
print(sorted(cars))
print('\nhere is the orignal list again:')
print(cars)
cars=['BMW','AUDI','toyota']
cars.reverse()
print(cars)
cars=['BMW','AUDI','toyota']
print(len(cars))
#cars=['benz','audi','red bulll','ferrari']========================================================================
#FOR LOOP 迴圈
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician}, that's was a great trick")
    print(f"{magician.title()},i can't wait to see you next time")
#如果有tab代表還在loop內所以要出loop直接把空格去掉
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician}, that's was a great trick")
    print(f"{magician.title()},i can't wait to see you next time")
print(f"i can't wait to see you next time {magician.title()}")
#range()function
for value in range(1,5):#從1開始到4
    print(value)
number=list(range(1,5))
print(number)
number=list(range(1,5,2))
print(number)
squar=[]
for value in range(1,11):
    square=value**2
    squar.append(square)
print(squar)
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)
squares=[value**2 for value in range(1,11)]
print(squares)
digit=[]
for value in range(1,10):
    digit.append(value)
digit.append(0)
print(digit)
print(max(digit))
print(min(digit))
print(sum(digit))
#slice a list[star:end:step]
list=[value for value in range(1,11)]
print(list[0:3])
print(list[:4])
print(list[-3:])
name=['sam','oscar','mathew']
name.append('wer2')
print('here are the last three players on my team:')
for who in name[1:]:
    print(who.title())
#=============================================================
my_food=['pizza','burger','cake','fried_chicken']
friend_food=my_food[:]
print(my_food)
print('\nmy friend favorite food are:')
print(friend_food)
#(不可改)
#==================================================================
#if statement
cars=['benz','audi','red bulll','ferrari']
for car in cars:
    if car == 'ferrari':
        print(car.upper())
    else:
        print(car.title())
#======================================================================
# == equal mark != inequal mark
cars=['benz','audi','red bulll','ferrari']
for car in cars:
    if car != 'ferrari':
        print(car.upper())
    else:
        print(car)
age_0=22
age_1=19
if age_0 >=21 and age_1>=21:
    print('true')
else:
    print('false'.title())
age_0=22
age_1=19
if all(age >=21 for age in [age_0, age_1]):
    print('true')
else:
    print('false'.title())
cars=['benz','audi','red bulll','ferrari']
if 'bmw' in  cars:
    print('yes')
else:
    print('no')
cars=['benz','audi','red bulll','ferrari']
brand='bmw'
if brand not in cars:
    print(f'{brand.upper()} is not in f1')
#==========================
#只有兩個條件
#if conditional
#   do something
#else
#   do something
#============================
#超過兩個條件
# IF COMDITIONAL:
#   DO SOMETHING
#ELIFE :
#   DO SOMETHING
#ELSE:
#   DO SOMETHING
age=20
if age <4:
    price=0
elif age <18:
    price=25
else:
    price=40
print(f'your admission cost is ${price}.')
#也可以多個IF組一起
cars=['benz','audi','red bulll','ferrari']
if 'benz' in cars:
    print('yes')
if 'audi' in cars:
    print('good car')
if 'toyato' in cars:
    print('noob')
cars=['benz','audi','red bulll','ferrari']
cars.append('bmw')
for car in cars:
    if car == 'bmw':
        print(f'{car.capitalize()} is not in f1 ')
    else:
        print(f'{car.capitalize()} is in f1')
request_toppings=['mushroom','green peppers','extra cheese']
if request_toppings:
    for request_topping in request_toppings:
        print(f'adding {request_topping}')
else:
    print('are you share you want a plain pizza')
available_toppings=['mushroom','green peppers','extra cheese','oliver','pineapple','pepperoni']
request_toppings=['mushroom','green peppers','extra cheese','chicken']
for request_topping in request_toppings:
    if request_topping in available_toppings:
        print(f"adding {request_topping}")
    else:
        print(f"sorry, we don't have {request_topping}")
#=============================================================================================================     
alien_0={'color':'red','point':5}
print(alien_0['color'])
print(alien_0['point'])
new_point=alien_0['point']
print(f'you just earned {new_point} point !!!')
#{}是可以增加東西的直接打出來
alien_0={'color':'red','point':5}
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
alien_0={'color':'red','point':5}
new_point=alien_0['point']
print(f'you just earned {new_point} point !!!')
alien_0['point']=10
new_point=alien_0['point']
print(f'you just earned new {new_point} point !!!')
#=======================與if連動
alien_0={}
alien_0['x_position']=0
alien_0['y_position']=25
alien_0['speed']='medium'
print(f"original position :{alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    new_x_position=1
elif alien_0['speed'] == 'medium':
    new_x_position=2
else:
    new_x_position=3
alien_0['x_position'] = alien_0['x_position'] + new_x_position
print(f"New position : {alien_0['x_position']}")
#===========================================================================     
alien_0={'color':'red','point':5}
print(alien_0)
del alien_0['point']
print(alien_0)
#======================================================================
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print(favorite_languages)
print(favorite_languages['sarah'].title())
print(f"sarah's favorite language is {favorite_languages['sarah'].title()}.")
#========================================================using get() to access values
alien_0={'color':'red','speed':'slow'}
#print(alien_0['point'])#會報錯
#print(alien_0.get('points','No point value assigned.'))#用get就不會報錯還可以設定預設值
point_value=alien_0.get('points','No point value assigned.')
print(point_value)
alien_0={'color':'red','speed':'slow'}
#print(alien_0['point'])#會報錯
#print(alien_0.get('points','No point value assigned.'))#用get就不會報錯還可以設定預設值
point_value=alien_0.get('points','5 point')
print(point_value)
#==================================================================loops in dictionary
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
for key, value in user_0.items():#.items()會把key跟value都拿出來一次拿出一對
    print(f"{key}: {value}")
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name, languange in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {languange.title()}.")
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for language in favorite_languages.values():#.values()只會拿value
    print(language.title())
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
for name in favorite_languages.keys():
    print(name.title())
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python' 
}
friends=['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language=favorite_languages[name].title()
        print(f"\t{name.title()}, i see you love {language}!")
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python' 
}
if ' sam' not in favorite_languages.keys():
    print('sam, please take our poll!')
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby', 
    'phil': 'python'
}
for name in favorite_languages.keys():
    print(f'{name.title()} thank you for taking the poll.')
favorite_languages={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby', 
    'phil': 'python'
}
print('the following languages have been mentioned:')
for language in favorite_languages.values():#set()會把重複的刪掉
    print(language.title())
for language in set(favorite_languages.values()):
    print(language.title())
alien_0={'color':'red','point':5}
alien_1={'color':'yellow','point':10}
alien_2={'color':'green','point':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:#只印前五個
    print(alien)
print(aliens)
print(f"total number of aliens: {len(aliens)}") 
aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:#只改前面三個
    if alien['color']=='green':
        alien['color']='red'
        alien['speed']='fast'
        alien['point']=10
for alien in aliens[:5]:#只印前五個
    print(alien)
aliens=[]
for alien_number in range(10):
    new_alien={'color':'green','point':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:#只改前面三個
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['point']=10
for alien in aliens[:6]:#只印前五個
    if  alien['color']=='green':
        alien['color']='red'
        alien['speed']='fast'
        alien['point']=15
for alien in aliens:#只印前五個
    print(alien)
#======================================================LIST IN A DICTIONARY 
pizza={
    'crust':'thick',
    'toppings':['mushroom','extra cheese']
}
print(f"you ordered a {pizza['crust']}-crust pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")   
favorite_languages={
    'jen': ['python','rust'],
    'sarah': ['c'],
    'edward': ['rust','go'],
    'phil': ['python','haskell']
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for languange in language   :
        print(f'\t{languange.title()}')
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}
for username, user_info in users.items():#username是key user_info是value
    print(f"\nUsername: {username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location=user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
#======================================================================
#INPUT() FUNCTION
message=input("tell me something, and i will repeat it back to you: ")
print(message)
height=input("how tall are you? ")
height=int(height)
if height >= 36:
    print("you are tall enough to ride")
else:
    print("you need to grow taller to ride")
prompt="if you tell us who you are, we can personalize the messages you see."
prompt+="what's your first name? "#+=是把兩個字串合在一起
name=input(prompt)
print(f"hello, {name.title()}!")
#% operator  除完的餘數
number=input("enter a number, and i'll tell you if it's even or odd: ")
number=int(number)
if number % 2 == 0:
    print(f"{number} is even")
else:    
    print(f"{number} is odd")
#===========================================================while loop 條件成立就一直執行
current_number=1
while current_number <=5:#當current_number小於等於5就一直執行
    print(current_number)
    current_number +=1#current_number=current_number+1
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':#如果輸入的不是quit就印出來 
        print(message)
#===============using a flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
# true or false 直接用true或false當條件
prompt = "\nplease enter the name of a city you have visited:  " 
prompt += "\n(enter 'quit' when you are finished) "
while True:
    city = input(prompt)
    if city == 'quit':
        break# break會直接跳出迴圈
    else:
        print(f"I'd love to go to {city.title()}!")
current_number=0
while current_number <10:
    current_number +=1
    if current_number % 2 == 0:
        continue#continue會跳過這次迴圈剩下的程式碼直接進入下一次迴圈
    print(current_number)
#avoiding infinite loop 無限迴圈 crtl +c可以強制結束程式
prompt = "\n adding whether you want to add a new pizza topping or not? "
prompt += "\n(enter 'quit' when you are finished) "
toppings=[]
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(f"{message.title()} has been added to your pizza!")
        toppings.append(message)
print(f"your pizza toppings are: {toppings}")
uncofirmed_users=['alice','brian','candace']
confirmed_users=[]
while uncofirmed_users:
    current_user=uncofirmed_users.pop(0)#pop會把最後一個拿出來
    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
pet=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pet)
while 'cat' in pet:
    pet.remove('cat')#remove會把第一個找到的刪掉
print(pet)
'''
"""""
# 用字典儲存「姓名: 想爬的山」
responses={}
# 控制問卷是否繼續
responses = {}
polling_active=True
# 只要 polling_active 是 True，就持續收集回答
while polling_active:
    name=input("\nwhat is your name? ")
    mountain=input("which mountain would you like to climb someday? ")
    responses[name]=mountain
    # 只接受 yes / no，其他輸入要重新輸入
    while True:
        continue_poll=input("would you like to let another person respond? (yes/no) ").strip().lower()
        if continue_poll == 'yes':
            break
            # yes 代表繼續讓下一位作答
            break
        if continue_poll == 'no':
            # no 代表停止問卷
            polling_active=False
            break
        else:
            print("Please enter yes or no.")
# 顯示所有收集到的結果
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name} would like to climb {mountain.title()}.")
print(responses) 
"""

responses={}
# 控制問卷是否繼續
responses = {}
polling_active=True
# 只要 polling_active 是 True，就持續收集回答
while polling_active:
    name=input("\nwhat is your name? ")
    mountain=input("which mountain would you like to climb someday? ")
    responses[name]=mountain
    # 只接受 yes / no，其他輸入要重新輸入
    while True:
        continue_poll=input("would you like to let another person respond? (yes/no) ").strip().lower()
        if continue_poll == 'yes':
            break
            # yes 代表繼續讓下一位作答
            break
        if continue_poll == 'no':
            # no 代表停止問卷
            polling_active=False
            break
        else:
            print("Please enter yes or no.")
# 顯示所有收集到的結果
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name} would like to climb {mountain.title()}.")
print(responses)

'''

responses = {}
polling_active = True
while polling_active:
    name = input("\nwhat is your name? ")
    mountain = input("which mountain would you like to climb someday? ")
    responses[name] = mountain
    while True:
        continue_poll = input("would you like to let another person respond? (yes/no) ").strip().lower()
        if continue_poll == 'yes':
            break
        if continue_poll == 'no':
            polling_active = False
            break
        print("Please enter yes or no.")
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name} would like to climb {mountain.title()}.")
print(responses)

#========================================================functions
def greet_user_simple():
    """Display a simple greeting."""
    print("Hello!")
greet_user_simple()

def greet_user_named(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user_named('jesse')
greet_user_named(input("what is your name? "))
def animal(type, name):# type: ignore #positional argument 位置參數
    """Display information about the animal."""
    print(f"i have a {type} and it's name is {name}") #type和name是參數 這裡的type和name只是暫時的變數 你可以換成其他的名字
animal('dog','wer2')
animal('dog','wer2')
animal('cat','mathew')
#keyword argument 關鍵字參數
animal(type='dog', name='wer2')
animal(name='mathew', type='cat')#keyword argument的順序可以隨便
#default value 預設值
def animal_with_default(type, name='unknown'):
    """Display information about the animal."""
    print(f"i have a {type} and it's name is {name}")
animal_with_default('dog')
animal('cat','mathew')#如果有預設值就可以不用輸入name的參數跟default value的參數如果有輸入就會覆蓋預設值
#avoiding argument error 避免參數錯誤
#return value 回傳值
def get_formatted_name_basic(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()#return會把full_name這個字串回傳給呼叫這個函式的程式碼
musician = get_formatted_name_basic('jimi', 'hendrix')
print(musician)
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix','wer2')
print(musician)
def build_person_basic(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person# return會把person這個字典回傳給呼叫這個函式的程式碼
musicians = []
musicians.append(build_person_basic('jimi', 'hendrix'))
musicians.append(build_person_basic('john', 'lennon'))
print(musicians)
def build_person_with_age_initial(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name, 'age': age}
    if age:
        person['age'] = age #如果有輸入age的參數就會把age這個key的值改成輸入的age參數的值如果沒有輸入age的參數就會把age這個key的值改成None
    return person
musicians = build_person_with_age_initial(first_name='jimi', last_name='hendrix',)
print(musicians)
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age is not None:
        person['age'] = age
    return person
musicians = build_person(first_name='jimi', last_name='hendrix')
print(musicians)
#======================================================================
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
def greet_users(names):
    """Display a simple greeting."""
    for name in names:
        print(f"Hello, {name.title()}!")
names=[]
while True:
    name=input("please enter your name: ")
    print("enter 'q' to quit: ")
    if name == 'q':
        break
    names.append(name)
greet_users(names)
#======================================================================
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()#pop會把最後一個拿出來
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
#二合一
"""ef print_designs(unprinted_designs, completed_models):
    Simulate printing each design, until none are left.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    print("\nThe following models have been printed:")#跟while loop同一層所以不會被重複印出來
    for completed_model in completed_models:
        print(completed_model)
"""
'''
unprinted_designs = []
completed_models = []
while True:
    design = input("please enter the unprinted design(enter 'q' to quit ): ").strip()#strip()會把字串前後的空格刪掉
    if design == 'q':
        break
    if not design:#如果design是空的就跳過這次迴圈繼續下一次迴圈
        continue
    unprinted_designs.append(design)

def print_designs(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    if not completed_models:#如果completed_models是空的就印nothing
        print("nothing")
        return#return會直接跳出函式所以不會印出下面的models
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
print_designs(unprinted_designs, completed_models)
'''
#======================================================================
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left. move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    if not completed_models:
        print("nothing")
        return
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
"""print_models(unprinted_designs[:], completed_models) #如果不想改變原本的list就把unprinted_designs傳入函式的時候用切片的方式傳入unprinted_designs[:]
這樣就會傳入一個unprinted_designs的副本在函式裡面改變副本不會改變原本的list"""
show_completed_models(completed_models)
'''
#分兩個function比一個大function好
def make_pizza(*toppings):#*toppings會把所有的參數都放在一個tuple()裡面
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
def make_pizza(size, *toppings):#*toppings會把所有的參數都放在一個tuple()裡面
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''
def build_profile(first, last, **user_info):#**user_info會把所有的參數都放在一個dictionary裡面
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
'''

# 中文註釋版
def build_profile(first, last, **user_info):  # **user_info 會把多出的關鍵字參數收成 dictionary
    """Build a dictionary containing everything we know about a user."""
    profile = {}  # 先建立一個空的 dictionary
    profile['first_name'] = first  # 把 first 參數存進 profile
    profile['last_name'] = last  # 把 last 參數存進 profile
    for key, value in user_info.items():  # 把 user_info 裡的資料一組一組取出
        profile[key] = value  # 把額外的資料加入 profile
    return profile  # 回傳整理好的 dictionary

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')  # 後面的資料會進 user_info
print(user_profile)  # 印出最後建立好的使用者資料

import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
from pizza import make_pizza
make_pizza(16, 'pepperoni')
from pizza import make_pizza as mp# as mp 是給這個函式取一個別名叫mp
mp(16, 'pepperoni')#mp就是make_pizza的別名
toppings=[]
while True:
    topping=input("please enter a pizza topping(enter 'q' to quit): ").strip()
    if topping == 'q':
        break
    toppings.append(topping)
for topping in toppings:
    print(f"{topping} has been added to your pizza!")
print(toppings)#這裡的toppings是整個list的值
print(topping)#這裡的topping是最後一個topping的值因為for loop結束後topping會保留最後一個值
print(*toppings)#*toppings 叫做「解包」, 會把 toppings 這個 list 裡的元素一個一個傳入 make_pizza 函式
print([topping for topping in toppings])#這個迴圈會把 toppings 這個 list 裡的元素一個一個取出來放在 topping 這個變數裡面
mp(12, *toppings)
import pizza as p#給模組取別名
p.make_pizza(16, 'pepperoni')
from pizza import *#這樣就可以直接使用pizza模組裡的函式不用加上pizza.的前綴
make_pizza(16, 'pepperoni')
#======================================================================
list = [1, 0, 2, 0, 4, 0, 6, 0, 8, 0]
list = [num for num in list if num not in (0, 8)] + [0, 0, 0, 0]
#這個迴圈會把list裡的元素一個一個取出來放在num這個變數裡面
#如果num不在(0,8)這個tuple裡面就把num放在新的list裡面最後再把[0,0,0,0]這個list加在新的list的後面
print(list)
#======================================================================
#class class是用來定義一個物件的藍圖，裡面可以定義屬性和方法屬性是用來描述物件的特徵的方法是用來描述物件的行為
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):#__init__是特殊方法用來初始化物件的屬性 self是指這個物件本身
        """Initialize name and age attributes."""
        self.name = name#self 負責把東西存進去物件裡面 name和age是屬性
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
my_dog = Dog('willie', 6)#self=my_dog
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
#======================================================================
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Lucky", 3)
dog2 = Dog("Coco", 5)

print(dog1.name)
print(dog2.age)
dog1.bark()
dog1.__init__("Buddy", 4)  # 重新初始化 dog1 的屬性
print(dog1.name)  # 現在 dog1 的名字是 Buddy
#=====================================================================
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2020)
my_new_car = Car(input("enter the make of your car: "), input("enter the model of your car: "), int(input("enter the year of your car: ")))
print(my_new_car.get_descriptive_name())
#attributes 屬性
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #這裡定義了一個新的屬性odometer_reading並給它一個初始值0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")#這裡使用了odometer_reading這個屬性
my_new_car = Car('audi', 'a4', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

