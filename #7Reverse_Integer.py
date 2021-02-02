def reverse(x):
    if x >= 2**31-1 or x <= -2**31:
        return 0
    else:
        if x > 0:
            rever = int(str(x)[::-1])
        else:
            rever = -int(str(-x)[::-1])
    if rever >= 2**31-1 or rever <= -2**31:
        return 0
    return rever


print(reverse(120000000000))
