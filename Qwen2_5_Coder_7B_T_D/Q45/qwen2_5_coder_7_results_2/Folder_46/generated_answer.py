def palindromes_between_indices(s):
    subset = s[4:10]
    subset = subset.lower()
    unique_chars = set(subset)
    if len(unique_chars) < 3:
        return set()
    chars = list(unique_chars)
    palindromes = set()
    for i in range(len(chars)):
        for j in range(i, len(chars)):
            for k in range(j, len(chars)):
                for l in range(k, len(chars)):
                    for m in range(l, len(chars)):
                        for n in range(m, len(chars)):
                            for o in range(n, len(chars)):
                                for p in range(o, len(chars)):
                                    for q in range(p, len(chars)):
                                        for r in range(q, len(chars)):
                                            for s in range(r, len(chars)):
                                                for t in range(s, len(chars)):
                                                    for u in range(t, len(chars)):
                                                        for v in range(u, len(chars)):
                                                            for w in range(v, len(chars)):
                                                                for x in range(w, len(chars)):
                                                                    for y in range(x, len(chars)):
                                                                        for z in range(y, len(chars)):
                                                                            candidate = chars[i] + chars[j] + chars[k] + chars[l] + chars[m] + chars[n] + chars[o] + chars[p] + chars[q] + chars[r] + chars[s] + chars[t] + chars[u] + chars[v] + chars[w] + chars[x] + chars[y] + chars[z]
                                                                            if candidate == candidate[::-1] and len(candidate) >= 6:
                                                                                palindromes.add(candidate)
    return palindromes