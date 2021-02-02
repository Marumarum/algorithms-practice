# def isPalindrome(x):
#
#         return str(x)[::-1] == str(x)


# print(isPalindrome(122))
# def isPalindrome(x):
#     if x < 0:
#         return False
#     else:
#         div = 1
#         while x//div >= 10:
#             div *= 10

#         while x > 0:
#             left = x//div
#             right = x % 10
#             if left != right:
#                 return False
#             x = (x % div) // 10
#             div //= 100
#         return True
def isPalindrome(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    else:
        reverse = 0
        while x > reverse:
            reverse = reverse*10+x % 10
            x //= 10
        return reverse == x or reverse//10 == x


print(isPalindrome(1220021))
