def palindromes_between_indices(s):
    letters = set(s[1:10].lower())
    if len(letters) < 7:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            for o in range(n, len(letters)):
                                word = ''.join(sorted([list(letters)[i], list(letters)[j], list(letters)[k], list(letters)[l], list(letters)[m], list(letters)[n], list(letters)[o]]))
                                if word == word[::-1]:
                                    palindromes.add(word)
    return palindromes