def palindromes_between_indices(s):
    letters = s[5:9]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    n = len(unique_letters)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    for m in range(l, n):
                        for n in range(m, n):
                            for o in range(n, n):
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
                                                                            palindrome = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n] + letters[o] + letters[p] + letters[q] + letters[r] + letters[s] + letters[t] + letters[u] + letters[v] + letters[w] + letters[x] + letters[y] + letters[z]
                                                                            if palindrome == palindrome[::-1] and len(palindrome) >= 3:
                                                                                palindromes.add(palindrome)
    return palindromes