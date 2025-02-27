from itertools import tee

def lists_with_product_equal_n(circular_list):

    def get_pairs(iterable):
        a, b = tee(iterable)
        next(b, None)
        return zip(a, b)

    def find_sublists(seq, n):
        for length in range(1, len(seq) + 1):
            for start_idx in range(len(seq)):
                if seq[start_idx] % n == 0:
                    product_tmp = seq[start_idx]
                    for index, (prev, current) in enumerate(get_pairs(seq[start_idx:]), start=start_idx):
                        if product_tmp == n:
                            yield seq[start_idx:index + 1]
                            break
                        elif current % (n // product_tmp) == 0:
                            product_tmp *= current
                        else:
                            product_tmp = seq[start_idx]
                            continue
    found_sublists = list(find_sublists(circular_list, 96))
    return found_sublists