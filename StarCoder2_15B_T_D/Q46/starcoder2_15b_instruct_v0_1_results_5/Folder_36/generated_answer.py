def gcf_three_nums(numbers):
    num_427 = numbers[427]
    num_761 = numbers[761]
    num_148 = numbers[148]
    gcf = num_427
    while gcf != num_761 and gcf != num_148:
        if num_761 % gcf == 0 and num_148 % gcf == 0:
            break
        gcf -= 1
    return gcf