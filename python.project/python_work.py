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
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
greet_user('jesse')
greet_user(input("what is your name? "))
def animal(type, name):#positional argument 位置參數
    """Display information about the animal."""
    print(f"i have a {type} and it's name is {name}") #type和name是參數 這裡的type和name只是暫時的變數 你可以換成其他的名字
animal('dog','wer2')
def animal(type, name):
    """Display information about the animal."""
    print(f"i have a {type} and it's name is {name}")
animal('dog','wer2')
animal('cat','mathew')
#keyword argument 關鍵字參數
def animal(type, name):
    """Display information about the animal."""
    print(f"i have a {type} and it's name is {name}")
animal(type='dog', name='wer2')
animal(name='mathew', type='cat')#keyword argument的順序可以隨便
#default value 預設值
def animal(type, name='unknown'):
    """Display information about the animal."""
    print(f"i have a {type} and it's name is {name}")
animal('dog')
animal('cat','mathew')#如果有預設值就可以不用輸入name的參數跟default value的參數如果有輸入就會覆蓋預設值
#avoiding argument error 避免參數錯誤
#return value 回傳值
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()#return會把full_name這個字串回傳給呼叫這個函式的程式碼
musician = get_formatted_name('jimi', 'hendrix')
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
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person# return會把person這個字典回傳給呼叫這個函式的程式碼
musicians = []
musicians.append(build_person('jimi', 'hendrix'))
musicians.append(build_person('john', 'lennon'))
print(musicians)
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name, 'age': age}
    if age:
        person['age'] = age #如果有輸入age的參數就會把age這個key的值改成輸入的age參數的值如果沒有輸入age的參數就會把age這個key的值改成None
    return person
musicians = build_person(first_name='jimi', last_name='hendrix',)
print(musicians)
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age is not None:
        person['age'] = age
    return person
musicians = build_person(first_name='jimi', last_name='hendrix')
print(musicians)
musician
