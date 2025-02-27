def palindromes_between_indices(s):
    letters = s[4:9]
    lower_letters = letters.lower()
    unique_letters = set(lower_letters)
    n = len(unique_letters)
    if n < 3:
        return set()
    palindromes = set()
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
                                                                    palindrome = ''.join(unique_letters[i]) * 2 + ''.join(unique_letters[j]) * 2 + ''.join(unique_letters[k]) * 2 + ''.join(unique_letters[l]) * 2 + ''.join(unique_letters[m]) * 2 + ''.join(unique_letters[n]) * 2
                                                                    if palindrome == palindrome[::-1]:
                                                                        palindromes.add(palindrome)
    return palindromes