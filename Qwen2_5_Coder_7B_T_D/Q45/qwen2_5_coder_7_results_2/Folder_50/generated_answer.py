def palindromes_between_indices(s):
    s = s[4:9].lower()
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
                                    for q in range(p, len(letters)):
                                        for r in range(q, len(letters)):
                                            word = ''.join(sorted(letters[i] * 2 + letters[j] * 2 + letters[k] * 2 + letters[l] * 2 + letters[m] * 2 + letters[n] * 2 + letters[o] * 2 + letters[p] * 2 + letters[q] * 2 + letters[r] * 2))
                                            if word == word[::-1] and len(word) >= 5:
                                                palindromes.add(word)
    return palindromes