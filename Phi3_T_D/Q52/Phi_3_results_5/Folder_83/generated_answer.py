def palindrome_of_length_n(s):
    length = 24
    s = s.lower()
    palindromes = set()
    if len(s) < length:
        return palindromes
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1]:
            palindromes.add(s[i:i + length])
    return palindromes