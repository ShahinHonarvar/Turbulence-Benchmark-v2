def gcf_three_nums(lst):
    num1 = lst[33]
    num2 = lst[78]
    num3 = lst[93]

    def gcf_two_nums(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_1_2 = gcf_two_nums(num1, num2)
    return gcf_two_nums(gcf_1_2, num3)