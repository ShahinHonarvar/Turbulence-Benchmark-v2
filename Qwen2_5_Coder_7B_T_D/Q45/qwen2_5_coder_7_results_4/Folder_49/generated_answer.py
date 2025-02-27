def palindromes_between_indices(s):
    letters = sorted(s[5:8].lower())
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    for m in range(l, n):
                        for o in range(m, n):
                            candidate = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[o]
                            if candidate == candidate[::-1] and len(candidate) >= 3:
                                palindromes.add(candidate)
    return palindromes