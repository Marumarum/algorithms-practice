
def find_most_repeatable(text):
    text_list = list(text)
    unrepeat_text_list = list(set(text_list))
    letter_times = {}
    for item1 in unrepeat_text_list:
        i = 0
        for item2 in text_list:
            if item1 == item2:
                i += 1
                letter_times[item1] = i

    return sorted(letter_times.items(), key=lambda kv: kv[1], reverse=True)[0]


print(find_most_repeatable("This is a common interview question"))

# def char_most(text):
#     char_times = {}
#     for char in text:
#         if char in char_times:
#             char_times[char] += 1
#         else:
#             char_times[char] = 1

#     return sorted(char_times.items(), key=lambda kv: kv[1])


# print(char_most('hello mmmm'))
