from collections import defaultdict

def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))

    def has_pair(lst_current, sizes_counted):
        for i, str1 in enumerate(lst_current):
            str1_normalized = normalize(str1)
            for str2 in lst_current[i + 1:]:
                if len(str1) < 3 or len(str2) < 3 or str1 == str2:
                    continue
                if normalize(str2) == str1_normalized:
                    sizes_counted[len(str1)] += 1
                    if sizes_counted[len(str1)] >= 2:
                        return True
        return False
    sizes_counted = defaultdict(int)
    while has_pair(lst, sizes_counted):
        lst = [i for i in lst if sizes_counted[len(i)] == 1]
    sum_of_pairs = sum((val // 2 for val in sizes_counted.values()))
    total_pairs = sum_of_pairs * 2
    return total_pairs >= 106