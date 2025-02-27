def palindrome_of_length_n(s):
    if len(s) < 181:
        return set()
    s = ''.join((c for c in s.lower() if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 180):
        substring = s[i:i + 181]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes