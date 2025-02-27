def palindromes_between_indices(s):
    letters = s[2:4]
    letters = letters.lower()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        for n in range(m + 1, len(letters)):
                            for o in range(n + 1, len(letters)):
                                for p in range(o + 1, len(letters)):
                                    for q in range(p + 1, len(letters)):
                                        for r in range(q + 1, len(letters)):
                                            for s in range(r + 1, len(letters)):
                                                for t in range(s + 1, len(letters)):
                                                    palindrome = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[n] + letters[o] + letters[p] + letters[q] + letters[r] + letters[s] + letters[t]
                                                    if palindrome == palindrome[::-1]:
                                                        result.add(palindrome)
    return result