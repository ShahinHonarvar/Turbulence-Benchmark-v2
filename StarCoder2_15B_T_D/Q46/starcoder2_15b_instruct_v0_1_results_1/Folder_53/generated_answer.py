def gcf_three_nums(numbers):
    num_66 = numbers[66]
    num_56 = numbers[56]
    num_92 = numbers[92]

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    gcf_66_56 = gcf(num_66, num_56)
    return gcf(gcf_66_56, num_92)