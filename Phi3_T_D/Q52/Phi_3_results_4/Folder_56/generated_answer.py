def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length_n = 95
    for i in range(len(s) - length_n + 1):
        substr = s[i:i + length_n]
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes