def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 400):
        substr = s[i:i + 401]
        if substr == substr[::-1] and substr.isalpha():
            palindromes.add(substr)
    return palindromes