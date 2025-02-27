def palindromes_between_indices(s):
    range_s = s[3:10]
    range_s = range_s.lower()
    range_set = set(range_s)
    range_length = len(range_set)
    if range_length < 7:
        return set()
    range_combinations = set()
    for i in range(range_length):
        for j in range(i, range_length):
            for k in range(j, range_length):
                for l in range(k, range_length):
                    for m in range(l, range_length):
                        for n in range(m, range_length):
                            for o in range(n, range_length):
                                combination = range_set[i] + range_set[j] + range_set[k] + range_set[l] + range_set[m] + range_set[n] + range_set[o]
                                if combination == combination[::-1]:
                                    range_combinations.add(combination)
    return range_combinations