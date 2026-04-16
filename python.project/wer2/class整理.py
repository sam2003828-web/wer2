"""Python class 基礎整理與範例。"""

# 1. 基本觀念
# class：類別，像是一張設計圖
# object / instance：物件 / 實例，根據類別建立出來的實際東西
# attribute：屬性，儲存在物件裡的資料
# method：方法，寫在類別裡的函式
# self：代表目前這個物件本身
# __init__：建立物件時會自動執行的初始化方法


class Dog:
    """用來說明 class 基本概念的簡單類別。"""

    def __init__(self, name, age):
        # 把資料存到這個物件自己的屬性中
        self.name = name
        self.age = age

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

    def bark(self):
        print(f"{self.name} says woof!")


class Student:
    """另一個 class 範例。"""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"My name is {self.name}. My score is {self.score}.")

    def update_score(self, new_score):
        self.score = new_score


print("=== Dog 範例 ===")
dog1 = Dog("Lucky", 3)
dog2 = Dog("Coco", 5)

print(dog1.name)   # 屬性
print(dog2.age)    # 屬性
dog1.describe()    # 方法
dog2.bark()        # 方法

print("\n=== 修改屬性 ===")
dog1.name = "Buddy"
dog1.age = 4
dog1.describe()

print("\n=== Student 範例 ===")
student1 = Student("Sam", 80)
student1.introduce()
student1.update_score(95)
student1.introduce()


# 快速整理：
# Dog / Student 是類別。
# dog1 / dog2 / student1 是物件。
# self 的意思是「這個物件自己」。
# self.name = name 是把資料存進物件屬性裡。
