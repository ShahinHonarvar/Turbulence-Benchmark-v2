def palindromes_between_indices(s):
    letters = s[2:5]
    letters = letters.lower()
    unique_letters = set(letters)
    n = len(unique_letters)
    if n < 2:
        return set()
    palindromes = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(i + 1, n):
                for l in range(j + 1, n):
                    for m in range(j + 1, n):
                        for p in range(k + 1, n):
                            for q in range(l + 1, n):
                                for r in range(m + 1, n):
                                    for s in range(p + 1, n):
                                        for t in range(q + 1, n):
                                            palindrome = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[n] + unique_letters[o] + unique_letters[p] + unique_letters[q] + unique_letters[r]
                                            if palindrome == palindrome[::-1]:
                                                palindromes.add(palindrome)
    return palindromes