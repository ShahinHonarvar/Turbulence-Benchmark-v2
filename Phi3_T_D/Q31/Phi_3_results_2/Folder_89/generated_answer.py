def if_perfect_num(lst):

    def is_perfect(num):
        sum, i = (1, 2)
        while i * i <= num:
            if num % i == 0:
                sum += i + num // i if i != num // i else i
            i += 1 if i != num // i else 2
        return sum == num
    return is_perfect(lst[18]) if 18 < len(lst) else False