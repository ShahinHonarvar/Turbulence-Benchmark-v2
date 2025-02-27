def palindromes_between_indices(s):
    indices = s[3:9]
    letters = set(indices.lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            for o in range(n, len(letters)):
                                for p in range(o, len(letters)):
                                    word = ''.join(sorted(letters[i:j] + letters[k:l] + letters[m:n] + letters[o:p]))
                                    if len(word) >= 4 and word == word[::-1]:
                                        palindromes.add(word)
    return palindromes