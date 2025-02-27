def all_ints_div_by_both_two_nums(ints):
    return [i for i in ints[10:77] if all((i % n == 0 for n in (-40, -12)))]