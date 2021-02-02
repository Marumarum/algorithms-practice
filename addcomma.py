def add_comma(num):
    reversed_num = list(num[::-1])
    conat = ''
    for i in range(len(reversed_num)):
        if ((i+1) % 3) == 0 and i != len(reversed_num)-1:
            reversed_num[i] = ','+reversed_num[i]
    for i in range(len(reversed_num)):
        j = -i-1
        conat = conat+reversed_num[j]
    return conat


print(add_comma('123456'))
