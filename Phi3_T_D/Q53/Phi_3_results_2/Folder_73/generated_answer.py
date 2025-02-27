def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length):
            substring = s[i:j]
            if len(substring) >= 94 and substring == substring[::-1]:
                if all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes