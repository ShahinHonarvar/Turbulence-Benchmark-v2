def palindromes_between_indices(s):
    sub = s[5:8].lower()
    letters = set(sub)
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            word = ''.join([list(letters)[i], list(letters)[j], list(letters)[k], list(letters)[l], list(letters)[m], list(letters)[n]])
                            if word == word[::-1]:
                                palindromes.add(word)
    return palindromes