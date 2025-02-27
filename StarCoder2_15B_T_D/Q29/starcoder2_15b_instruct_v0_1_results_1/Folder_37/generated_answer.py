def gcf_two_nums(numbers):
    gcf = numbers[29]
    for i in range(29, 74):
        while numbers[i] % gcf != 0:
            gcf -= 1
    return gcf