def palindrome_of_length_at_least_n(s):
    s = s.lower()
    long_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substr = s[i:j + 1]
            if len(substr) >= 141 and substr == substr[::-1]:
                long_palindromes.add(substr)
    return long_palindromes