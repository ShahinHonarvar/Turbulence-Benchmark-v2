def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 16):
        substr = s[i:i + 17]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes