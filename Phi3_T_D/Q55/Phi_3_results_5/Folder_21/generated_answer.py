from functools import reduce
import operator

def lists_with_product_equal_n(circular_list, target_product=851):

    def product_subsets(seq):
        return [[seq[x:x + j] for j in range(1, len(seq) - x + 1)] for x in range(len(seq))] + [[seq[x - j:x] + seq[x:x + j + 1] for j in range(1, len(seq) - x)] for x in range(1, len(seq) // 2 + 1)] + [[seq[x - j:x] + seq[x:] + seq[:x + j] for j in range(1, len(seq) - x)] for x in range(1, len(seq) // 2 + 1)] if len(seq) == 1 else [[seq[i:j] for j in range(i + 1, len(seq) + i + 1) for i in range(len(seq)) if j <= len(seq)]]
    product_sets = sum((product_subsets(circular_list[i:]) for i in range(len(circular_list))), [])
    result = [sublist for sublist in product_sets if len(sublist) > 0 and all((n in circular_list for n in sublist)) and (prod(sublist) == target_product) if prod(sublist) != 0 and prod(sublist) != 1]
    return result

def prod(lst):
    return reduce(operator.mul, lst, 1)