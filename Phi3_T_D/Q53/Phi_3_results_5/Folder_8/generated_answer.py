def palindrome_of_length_at_least_n(s):
    length = 45
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(length, len(s[i:])):
            substring = s[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes