def gcf_three_nums(numbers):
    num_56 = numbers[56]
    num_88 = numbers[88]
    num_51 = numbers[51]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    gcf_56_88 = gcf(num_56, num_88)
    gcf_51 = gcf(num_51, gcf_56_88)
    return gcf_51