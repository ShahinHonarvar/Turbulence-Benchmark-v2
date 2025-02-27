def palindrome_of_length_n(s):
    length = 45
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - length + 1):
        substr = s[i:i + length]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes