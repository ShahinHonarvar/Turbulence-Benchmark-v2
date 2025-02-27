def palindromes_between_indices(s):
    letters = s[4:10]
    letters = letters.lower()
    unique_letters = set(letters)
    unique_letters = sorted(unique_letters)
    n = len(unique_letters)
    result = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    for m in range(l + 1, n):
                        for p in range(m + 1, n):
                            for q in range(p + 1, n):
                                for r in range(q + 1, n):
                                    for s in range(r + 1, n):
                                        for t in range(s + 1, n):
                                            for u in range(t + 1, n):
                                                for v in range(u + 1, n):
                                                    for w in range(v + 1, n):
                                                        for x in range(w + 1, n):
                                                            for y in range(x + 1, n):
                                                                for z in range(y + 1, n):
                                                                    palindrome = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[n] + unique_letters[o] + unique_letters[p] + unique_letters[q] + unique_letters[r] + unique_letters[s] + unique_letters[t] + unique_letters[u] + unique_letters[v] + unique_letters[w] + unique_letters[x] + unique_letters[y] + unique_letters[z]
                                                                    if palindrome == palindrome[::-1]:
                                                                        result.add(palindrome)
    return result