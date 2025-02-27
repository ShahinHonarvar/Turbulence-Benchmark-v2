def palindromes_between_indices(s):
    s = s[4:8]
    s = s.lower()
    letters = set(s)
    n = len(letters)
    if n < 2:
        return set()
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(i, n):
                for l in range(k, n):
                    for m in range(l, n):
                        for o in range(m, n):
                            for p in range(o, n):
                                for q in range(p, n):
                                    word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[o] + letters[p] + letters[q]
                                    if word == word[::-1] and len(word) >= 4:
                                        palindromes.add(word)
    return palindromes