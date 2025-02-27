def palindromes_between_indices(s):
    s = s[3:5].lower()
    letters = sorted(set(s))
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    for m in range(l, n):
                        palindrome = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if palindrome == palindrome[::-1]:
                            palindromes.add(palindrome)
    return palindromes if palindromes else set()