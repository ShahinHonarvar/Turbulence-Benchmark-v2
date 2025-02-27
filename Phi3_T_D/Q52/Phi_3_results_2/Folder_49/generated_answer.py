def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 46):
        substr = s[i:i + 47]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes