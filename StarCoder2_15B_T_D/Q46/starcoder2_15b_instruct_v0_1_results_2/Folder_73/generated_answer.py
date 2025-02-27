def gcf_three_nums(numbers):
    gcf = numbers[90]
    for i in range(90, 84, -1):
        for j in range(i - 1, 84, -1):
            if numbers[j] % gcf == 0:
                gcf = numbers[j]
                break
    for k in range(84, 47, -1):
        for l in range(k - 1, 47, -1):
            if numbers[l] % gcf == 0:
                gcf = numbers[l]
                break
    return gcf