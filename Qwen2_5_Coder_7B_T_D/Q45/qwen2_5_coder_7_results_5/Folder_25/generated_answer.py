def palindromes_between_indices(s):
    letters = s[1:5].lower()
    letters_set = set(letters)
    palindromes = set()
    for i in range(len(letters_set)):
        for j in range(i, len(letters_set)):
            for k in range(j, len(letters_set)):
                for l in range(k, len(letters_set)):
                    for m in range(l, len(letters_set)):
                        for n in range(m, len(letters_set)):
                            for o in range(n, len(letters_set)):
                                for p in range(o, len(letters_set)):
                                    for q in range(p, len(letters_set)):
                                        for r in range(q, len(letters_set)):
                                            for s in range(r, len(letters_set)):
                                                for t in range(s, len(letters_set)):
                                                    for u in range(t, len(letters_set)):
                                                        for v in range(u, len(letters_set)):
                                                            for w in range(v, len(letters_set)):
                                                                for x in range(w, len(letters_set)):
                                                                    for y in range(x, len(letters_set)):
                                                                        for z in range(y, len(letters_set)):
                                                                            word = ''.join([list(letters_set)[i], list(letters_set)[j], list(letters_set)[k], list(letters_set)[l], list(letters_set)[m], list(letters_set)[n], list(letters_set)[o], list(letters_set)[p], list(letters_set)[q], list(letters_set)[r], list(letters_set)[s], list(letters_set)[t], list(letters_set)[u], list(letters_set)[v], list(letters_set)[w], list(letters_set)[x], list(letters_set)[y], list(letters_set)[z]])
                                                                            if word == word[::-1] and len(word) >= 3:
                                                                                palindromes.add(word)
    return palindromes