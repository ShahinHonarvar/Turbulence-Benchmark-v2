def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 6):
        substring = s[i:i + 7]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes