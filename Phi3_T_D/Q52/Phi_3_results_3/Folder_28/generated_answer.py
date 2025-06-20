def palindrome_of_length_n(s):
    palindromes = set()
    n = 43
    s = s.lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes