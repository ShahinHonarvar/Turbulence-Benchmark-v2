def palindromes_between_indices(s):
    s = s[:4].lower()
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
                                            for s in range(r, len(letters)):
                                                word = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:n] + letters[o:p] + letters[q:r] + letters[s:]))
                                                if word == word[::-1] and len(word) >= 4:
                                                    palindromes.add(word)
    return palindromes