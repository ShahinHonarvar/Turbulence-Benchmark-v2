def palindromes_between_indices(s):
    letters = s[7:9].lower()
    if len(letters) < 2:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        for n in range(m, len(letters)):
                            for o in range(n, len(letters)):
                                for p in range(o, len(letters)):
                                    for q in range(p, len(letters)):
                                        for r in range(q, len(letters)):
                                            for s in range(r, len(letters)):
                                                for t in range(s, len(letters)):
                                                    for u in range(t, len(letters)):
                                                        for v in range(u, len(letters)):
                                                            for w in range(v, len(letters)):
                                                                for x in range(w, len(letters)):
                                                                    for y in range(x, len(letters)):
                                                                        for z in range(y, len(letters)):
                                                                            candidate = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n] + letters[o] + letters[p] + letters[q] + letters[r] + letters[s] + letters[t] + letters[u] + letters[v] + letters[w] + letters[x] + letters[y] + letters[z]
                                                                            if candidate == candidate[::-1] and len(candidate) >= 3:
                                                                                palindromes.add(candidate)
    return palindromes