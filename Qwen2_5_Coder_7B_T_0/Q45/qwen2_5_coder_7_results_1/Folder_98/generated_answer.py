def palindromes_between_indices(s):
    letters = s[3:6].lower()
    letters = ''.join(sorted(letters))
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    for m in range(l, n):
                        for o in range(m, n):
                            for p in range(o, n):
                                for q in range(p, n):
                                    for r in range(q, n):
                                        for s in range(r, n):
                                            for t in range(s, n):
                                                for u in range(t, n):
                                                    for v in range(u, n):
                                                        for w in range(v, n):
                                                            for x in range(w, n):
                                                                for y in range(x, n):
                                                                    for z in range(y, n):
                                                                        candidate = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n] + letters[o] + letters[p] + letters[q] + letters[r] + letters[s] + letters[t] + letters[u] + letters[v] + letters[w] + letters[x] + letters[y] + letters[z]
                                                                        if candidate == candidate[::-1] and len(candidate) >= 4:
                                                                            palindromes.add(candidate)
    return palindromes