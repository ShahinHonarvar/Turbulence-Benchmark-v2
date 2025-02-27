def palindromes_of_specific_lengths(s):
    s = s[30:74 + 1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 23, min(i + 39, len(s)) + 1):
            substr = s[i:j].lower()
            if len(substr) >= 23 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes