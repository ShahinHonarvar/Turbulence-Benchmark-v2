def palindromes_between_indices(s):
    letters = set(s[:4].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            candidate = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]
                            if candidate == candidate[::-1] and len(candidate) >= 3:
                                palindromes.add(candidate)
    return palindromes