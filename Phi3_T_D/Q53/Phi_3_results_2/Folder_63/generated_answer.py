def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for length in range(37, len(s) - i + 1):
            substring = s[i:i + length]
            if substring[::-1] == substring and substring.isalpha():
                palindromes.add(substring)
    return palindromes