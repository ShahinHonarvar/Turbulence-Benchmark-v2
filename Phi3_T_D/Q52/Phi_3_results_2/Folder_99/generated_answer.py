def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    n = len(s)
    for i in range(n - 419):
        substring = s[i:i + 420]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes