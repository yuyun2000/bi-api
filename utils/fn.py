def sum_of_negative_numbers(arr):
    sum_negative = sum(filter(lambda x: x < 0, arr))
    return sum_negative


def count_negative_numbers(arr):
    num = 0
    for x in arr:
        if x < 0:
            num += 1
    return num