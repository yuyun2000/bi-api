def sum_of_negative_numbers_less_than(arr, threshold):
    sum_negative = sum(filter(lambda x: x < 0, arr))
    return sum_negative < threshold