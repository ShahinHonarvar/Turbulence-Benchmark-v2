def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 42):
        substr = s[i:i + 43]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes