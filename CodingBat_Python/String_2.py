# Given a string, return a string where for every char in the original, there are two chars.


def double_char(str):
    combined_word = ""
    for character in str:
        combined_word += character + character
    return combined_word


# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
    count = 0
    for i in range(0, len(str) - 1, 1):
        if str[i] == "h" and str[i + 1] == "i":
            count = count + 1
    return count


# Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    cat_count = 0
    dog_count = 0
    for i in range(0, len(str) - 1, 1):
        if str[i:i + 3] == "cat":
            cat_count = cat_count + 1
        elif str[i:i + 3] == "dog":
            dog_count = dog_count + 1
    if dog_count == cat_count:
        return True
    return False


# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
    count = 0
    for i in range(0, len(str) - 1, 1):
        if str[i:i + 2] == "co" and str[i + 3:i + 4] == "e":
            count = count + 1
    return count


# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
    # need to make the input as str() data type
    # to be able to use string builtin methods
    str(a)
    str(b)
    # need to convert to lower/upper case - string builtin methods
    if a.lower().endswith(b.lower()) or b.lower().endswith(a.lower()):
        return True
    else:
        return False


# Return True if the given string contains an appearance of "xyz"
# where the xyz is not directly preceded by a period (.).
# So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
    # solution : replace the condition which will return false (.xyz)
    # with "" , then use if-else so that it will fall on else condition
    str = str.replace(".xyz", "")
    if 'xyz' in str:
        return True
    else:
        return False
