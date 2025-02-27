def palindrome_of_length_n(s):
    length = 56
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring)
    return palindromes