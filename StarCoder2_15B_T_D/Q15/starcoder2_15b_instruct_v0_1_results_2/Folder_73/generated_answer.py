def sum_odd_ints_inclusive(intList):
    sum = 0
    for num in intList[19:93]:
        if num % 2 != 0:
            sum += num
    return sum