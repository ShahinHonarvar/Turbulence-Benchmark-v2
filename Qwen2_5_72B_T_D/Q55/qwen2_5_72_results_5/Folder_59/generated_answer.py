from itertools import islice

def lists_with_product_equal_n(lst):

    def circular_sublists(lst, n):
        for i in range(len(lst)):
            yield list(islice(lst, i, i + n))
            if n > 1:
                for j in range(1, n):
                    yield list(islice(lst, i, i + n, j + 1))
    result = []
    for n in range(1, len(lst) + 1):
        for sub in circular_sublists(lst, n):
            if all((isinstance(x, int) for x in sub)) and sub and (sub[0] * sub[-1] == -3):
                if all((abs(sub[i] * sub[i + 1]) != 3 for i in range(len(sub) - 1))):
                    if all((sub[i] * sub[i + 1] != -3 for i in range(len(sub) - 1))):
                        result.append(sub)
    return result