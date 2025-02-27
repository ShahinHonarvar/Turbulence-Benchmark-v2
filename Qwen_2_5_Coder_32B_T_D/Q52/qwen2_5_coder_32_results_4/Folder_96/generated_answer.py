def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 82):
        substring = s[i:i + 83]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes