def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            for o in range(n, len(letters)):
                                for p in range(o, len(letters)):
                                    candidate = letters[i] * 3 + letters[j] * 3 + letters[k]
                                    if candidate == candidate[::-1] and len(candidate) >= 6:
                                        palindromes.add(candidate)
    return palindromes