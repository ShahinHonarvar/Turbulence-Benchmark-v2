def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 86):
        substr = s[i:i + 94]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes