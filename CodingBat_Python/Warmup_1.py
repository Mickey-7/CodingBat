# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile or not a_smile and not b_smile:
        return True
    else:
        return False


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


# Given an int n, return the absolute difference between n and 21,
# except return double the absolute difference if n is over 21.
def diff21(n):
    if 21 < n:
        return 2 * abs(21 - n)
    else:
        return abs(21 - n)


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20.
# Return True if we are in trouble.
def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
    if 110 >= n >= 90 or 210 >= n >= 190:
        return True
    else:
        return False


# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    if not negative and a > 0 > b or b > 0 > a:
        return True
    elif negative and a < 0 and b < 0:
        return True
    else:
        return False




































