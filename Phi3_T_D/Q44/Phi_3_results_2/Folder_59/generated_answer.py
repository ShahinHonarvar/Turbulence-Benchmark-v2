def composite_nums_between_indices(lst):
    if len(lst) > 10:
        lst = lst[:10]
    composite_set = set()
    for i in lst[0:10]:
        if i > 1:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    composite_set.add(i)
                    break
    return composite_set