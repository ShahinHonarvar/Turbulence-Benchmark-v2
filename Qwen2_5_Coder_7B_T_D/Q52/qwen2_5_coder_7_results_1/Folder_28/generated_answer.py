def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 42):
        substring = s[i:i + 43]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes