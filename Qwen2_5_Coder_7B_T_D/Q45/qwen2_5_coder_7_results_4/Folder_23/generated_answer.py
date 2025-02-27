def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = set(s)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            for o in range(n, len(letters)):
                                word = ''.join(sorted([letters[x] for x in [i, j, k, l, m, n, o]]))
                                if word == word[::-1] and len(word) >= 4:
                                    palindromes.add(word)
    return palindromes