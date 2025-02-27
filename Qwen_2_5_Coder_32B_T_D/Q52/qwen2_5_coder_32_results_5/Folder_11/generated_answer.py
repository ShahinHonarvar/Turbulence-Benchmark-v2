def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 76):
        substring = s[i:i + 77]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes