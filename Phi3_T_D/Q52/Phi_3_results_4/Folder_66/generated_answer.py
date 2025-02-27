def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 24):
        substr = s[i:i + 25]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes