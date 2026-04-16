"""常用流程控制（for loop / while / if）的自訂 function 範例。"""


def print_numbers_with_for(start, end):
    """用 for 迴圈印出 start 到 end（含 end）的整數。"""
    for number in range(start, end + 1):
        print(number)


def sum_until_with_while(limit):
    """用 while 迴圈把 1 累加到 limit，回傳總和。"""
    total = 0
    current = 1

    while current <= limit:
        total += current
        current += 1

    return total


def check_score_with_if(score):
    """用 if / elif / else 判斷分數等級。"""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def find_even_numbers(numbers):
    """搭配 for + if，找出所有偶數並回傳 list。"""
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


if __name__ == "__main__":
    print("for 迴圈範例：")
    print_numbers_with_for(1, 5)

    print("\nwhile 迴圈範例：")
    result = sum_until_with_while(5)
    print(f"1 加到 5 的總和是：{result}")

    print("\nif 判斷範例：")
    grade = check_score_with_if(86)
    print(f"86 分的等級是：{grade}")

    print("\nfor + if 範例：")
    evens = find_even_numbers([1, 2, 3, 4, 5, 6])
    print(f"偶數有：{evens}")
