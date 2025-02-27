def palindromes_between_indices(s):
    subset = s[6:10]
    letters = [char.lower() for char in subset if char.isalpha()]
    unique_letters = set(letters)
    result = set()
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
                                                for t in range(s, len(unique_letters)):
                                                    for u in range(t, len(unique_letters)):
                                                        for v in range(u, len(unique_letters)):
                                                            for w in range(v, len(unique_letters)):
                                                                for x in range(w, len(unique_letters)):
                                                                    for y in range(x, len(unique_letters)):
                                                                        for z in range(y, len(unique_letters)):
                                                                            candidate = ''.join([list(unique_letters)[i], list(unique_letters)[j], list(unique_letters)[k], list(unique_letters)[l], list(unique_letters)[m], list(unique_letters)[n], list(unique_letters)[o], list(unique_letters)[p], list(unique_letters)[q], list(unique_letters)[r], list(unique_letters)[s], list(unique_letters)[t], list(unique_letters)[u], list(unique_letters)[v], list(unique_letters)[w], list(unique_letters)[x], list(unique_letters)[y], list(unique_letters)[z]])
                                                                            if candidate == candidate[::-1] and len(candidate) >= 5:
                                                                                result.add(candidate)
    return result