username="John Doe"
userpassword="password123"
num=0
while num<3:
    input_username=input("请输入用户名：")
    input_password=input("请输入密码：")
    if input_username==username and input_password==userpassword:
        print("登录成功！")
        break
    else:
        print("用户名或密码错误，请重新输入。")
        num+=1
else:
    print("登录失败，账号已锁定。")
from decimal import Decimal, getcontext

getcontext().prec = 50

def arctan_inv(x):
    x = Decimal(x)
    total = Decimal(0)
    term = Decimal(1) / x
    n = 1
    sign = 1
    limit = Decimal("1e-45")

    while term > limit:
        total += sign * term / n
        term /= x * x
        n += 2
        sign *= -1

    return total

pi = 16 * arctan_inv(5) - 4 * arctan_inv(239)
pi_30 = pi.quantize(Decimal("1." + "0" * 30))

print(pi_30)

