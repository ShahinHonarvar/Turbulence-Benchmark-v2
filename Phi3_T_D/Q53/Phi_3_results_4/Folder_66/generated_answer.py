def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 76, len(s) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes