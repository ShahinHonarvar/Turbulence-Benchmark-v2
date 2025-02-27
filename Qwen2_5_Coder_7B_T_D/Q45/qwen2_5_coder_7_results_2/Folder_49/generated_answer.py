def palindromes_between_indices(s):
    letters = set(s[5:8].lower())
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
                                            word = ''.join(sorted(letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n] + letters[o] + letters[p] + letters[q] + letters[r]))
                                            if word == word[::-1] and len(word) >= 3:
                                                palindromes.add(word)
    return palindromes