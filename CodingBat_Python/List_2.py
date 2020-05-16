# Return the number of even ints in the given array.
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


def count_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count = count + 1
    return count


# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
# Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
    big = max(nums)
    small = min(nums)
    return big - small


# Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
# except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
# ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may
# assume that the array is length 3 or more.
def centered_average(nums):
    if len(nums) % 2 == 0:
        # need to store the len as int as len() returns float
        # print(nums[int((len(nums)/2)-1)])
        return int((nums[int((len(nums) / 2) - 1)] + nums[int((len(nums) / 2))]) / 2)
    else:
        return int(nums[int(len(nums) / 2)])


# print(centered_average([1, 2, 3, 4, 100]))
# print(centered_average([-10, -4, -2, -4, -2, 0]))
# print(centered_average([100, 0, 5, 3, 4]))


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
# and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum67(nums):
    record = True
    total = 0

    for n in nums:
        if n == 6:
            record = False

        if record:
            total += n
            continue

        if n == 7:
            record = True

    return total


print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 2, 2]))
print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) )


# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
    for i in range(0, len(nums) - 1, 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
