def palindromes_between_indices(s):
    subset = s[3:8].lower()
    letters = list(subset)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            candidates = [letters[i], letters[j], letters[k], letters[l], letters[m], letters[n]]
                            if candidates == candidates[::-1]:
                                palindromes.add(''.join(candidates))
    return palindromes