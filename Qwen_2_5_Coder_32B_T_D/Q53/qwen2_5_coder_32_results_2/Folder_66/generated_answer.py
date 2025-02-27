def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for start in range(len(s) - 75):
        for end in range(start + 75, len(s) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes