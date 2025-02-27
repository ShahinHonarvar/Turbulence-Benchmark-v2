def palindromes_between_indices(s):
    t = s[3:7]
    letters = set(t.lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            word = ''.join(sorted(letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n]))
                            if len(word) >= 4 and word == word[::-1]:
                                palindromes.add(word)
    return palindromes