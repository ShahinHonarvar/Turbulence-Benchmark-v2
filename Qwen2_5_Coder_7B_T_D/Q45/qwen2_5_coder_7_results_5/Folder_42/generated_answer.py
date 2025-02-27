def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:10]]
    unique_letters = set(letters)
    if len(unique_letters) < 3:
        return set()
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        for n in range(m, len(unique_letters)):
                            for o in range(n, len(unique_letters)):
                                for p in range(o, len(unique_letters)):
                                    for q in range(p, len(unique_letters)):
                                        for r in range(q, len(unique_letters)):
                                            for s in range(r, len(unique_letters)):
                                                word = ''.join([list(unique_letters)[i], list(unique_letters)[j], list(unique_letters)[k], list(unique_letters)[l], list(unique_letters)[m], list(unique_letters)[n], list(unique_letters)[o], list(unique_letters)[p], list(unique_letters)[q], list(unique_letters)[r], list(unique_letters)[s]])
                                                if word == word[::-1]:
                                                    palindromes.add(word)
    return palindromes