def gcf_two_nums(numbers):
    gcf = numbers[28]
    for i in range(28, 20, -1):
        for j in range(i - 1, 19, -1):
            if numbers[i] % numbers[j] == 0:
                gcf = numbers[j]
                break
        if gcf != numbers[i]:
            break
    return gcf