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
    print(a[len(b)-1:])
    print(b)
    print(b[len(a)-1:])
    print(a)


# print(end_other('Hiabc', 'abc'))
# print(end_other('AbC', 'HiaBc'))
# print(end_other('abc', 'abXabc'))


# Return True if the given string contains an appearance of "xyz"
# where the xyz is not directly preceeded by a period (.).
# So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
    for i in range(0, len(str) - 1, 1):
        if str[i:i+4] == ".xyz":
            return False
        elif str[i:i+3] == "xyz":
            return True



print(xyz_there('abcxyz'))




