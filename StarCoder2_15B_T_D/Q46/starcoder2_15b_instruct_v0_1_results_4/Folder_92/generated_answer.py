def gcf_three_nums(numbers):
    gcf = numbers[7]
    for i in range(8, 10):
        while numbers[i] % gcf != 0:
            gcf -= 1
    return gcf