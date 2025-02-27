def palindromes_between_indices(s):
    subset = s[3:10]
    unique_chars = set(subset.lower())
    if len(unique_chars) < 5:
        return set()
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            for k in range(j, len(unique_chars)):
                for l in range(k, len(unique_chars)):
                    for m in range(l, len(unique_chars)):
                        for n in range(m, len(unique_chars)):
                            for o in range(n, len(unique_chars)):
                                for p in range(o, len(unique_chars)):
                                    for q in range(p, len(unique_chars)):
                                        for r in range(q, len(unique_chars)):
                                            for s in range(r, len(unique_chars)):
                                                candidate = ''.join(sorted([list(unique_chars)[i], list(unique_chars)[j], list(unique_chars)[k], list(unique_chars)[l], list(unique_chars)[m], list(unique_chars)[n], list(unique_chars)[o], list(unique_chars)[p], list(unique_chars)[q], list(unique_chars)[r], list(unique_chars)[s]]))
                                                if candidate == candidate[::-1]:
                                                    palindromes.add(candidate)
    return palindromes