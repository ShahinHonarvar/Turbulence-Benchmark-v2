def gcf_two_nums(numbers):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(numbers[360], numbers[722])