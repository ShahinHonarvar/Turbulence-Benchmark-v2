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
                            word = ''.join([list(letters)[i], list(letters)[j], list(letters)[k], list(letters)[l], list(letters)[m], list(letters)[n]])
                            if word == word[::-1] and len(word) >= 4:
                                palindromes.add(word)
    return palindromes