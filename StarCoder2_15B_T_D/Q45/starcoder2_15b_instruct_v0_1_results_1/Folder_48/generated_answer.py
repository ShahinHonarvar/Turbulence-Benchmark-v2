def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for i in range(6, len(s) - 1):
        for j in range(i + 1, min(i + 4, len(s))):
            for k in range(j + 1, len(s)):
                palindrome = s[i:k + 1]
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes