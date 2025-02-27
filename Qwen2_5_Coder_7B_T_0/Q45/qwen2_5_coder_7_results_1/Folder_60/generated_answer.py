def palindromes_between_indices(s):
    letters = s[3:7].lower()
    unique_letters = set(letters)
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
                                                for t in range(s, len(unique_letters)):
                                                    for u in range(t, len(unique_letters)):
                                                        for v in range(u, len(unique_letters)):
                                                            for w in range(v, len(unique_letters)):
                                                                for x in range(w, len(unique_letters)):
                                                                    for y in range(x, len(unique_letters)):
                                                                        for z in range(y, len(unique_letters)):
                                                                            candidate = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[n] + unique_letters[o] + unique_letters[p] + unique_letters[q] + unique_letters[r] + unique_letters[s] + unique_letters[t] + unique_letters[u] + unique_letters[v] + unique_letters[w] + unique_letters[x] + unique_letters[y] + unique_letters[z]
                                                                            if candidate == candidate[::-1] and len(candidate) >= 4:
                                                                                palindromes.add(candidate)
    return palindromes