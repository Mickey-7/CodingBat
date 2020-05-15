# Given a string, return a string where for every char in the original, there are two chars.


def double_char(str):
    combined_word = ""
    for character in str:
        combined_word += character + character
    return combined_word


# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):





print(count_hi('abc hi ho'))
