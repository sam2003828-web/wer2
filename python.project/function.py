"""常見 function 範例。"""


def greet():
    """不接參數，直接做固定的事情。"""
    print("Hello!")


def greet_user(name):
    """接收一個參數，使用傳進來的值。"""
    print(f"Hello, {name.title()}!")


def describe_pet(animal_type, pet_name):
    """接收多個參數。"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


def describe_pet_default(pet_name, animal_type="dog"):
    """使用預設值；如果沒有傳 animal_type，就會用 dog。"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


def get_full_name(first_name, last_name, middle_name=""):
    """用 return 把結果回傳出去。"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


def build_person(first_name, last_name, age=None):
    """回傳 dictionary；有 age 才加進去。"""
    person = {"first": first_name, "last": last_name}
    if age is not None:
        person["age"] = age
    return person


def greet_users(names):
    """把 list 傳進 function，逐一處理每個元素。"""
    for name in names:
        print(f"Hello, {name.title()}!")


def make_pizza(*toppings):
    """*toppings 會把多個普通參數收成 tuple。"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def build_profile(first, last, **user_info):
    """**user_info 會把多個關鍵字參數收成 dictionary。"""
    profile = {"first_name": first, "last_name": last}
    for key, value in user_info.items():
        profile[key] = value
    return profile


if __name__ == "__main__":
    # 不接參數的 function
    greet()

    # 接收一個參數
    greet_user("sam")

    # 接收多個參數
    describe_pet("cat", "mimi")

    # 使用預設值
    describe_pet_default("buddy")

    # return 字串
    musician = get_full_name("jimi", "hendrix")
    print(musician)

    # return dictionary
    user = build_person("albert", "einstein", 27)
    print(user)

    # 傳 list 進 function
    usernames = ["sam", "oscar", "mathew"]
    greet_users(usernames)

    # *args
    make_pizza("mushrooms", "green peppers", "extra cheese")

    # **kwargs
    profile = build_profile(
        "albert",
        "einstein",
        location="princeton",
        field="physics",
    )
    print(profile)
