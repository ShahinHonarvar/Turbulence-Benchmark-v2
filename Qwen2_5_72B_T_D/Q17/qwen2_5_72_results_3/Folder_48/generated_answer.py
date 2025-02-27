def all_ints_div_by_both_two_nums(lst):
    divisors = [982, 319]
    result = []
    for num in lst[306:958]:
        if all((num % d == 0 for d in divisors)):
            result.append(num)
    return result