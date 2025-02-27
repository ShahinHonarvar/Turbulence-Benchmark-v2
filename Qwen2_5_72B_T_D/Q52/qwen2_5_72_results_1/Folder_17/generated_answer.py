def palindrome_of_length_n(s):
    s = s.lower()
    length = 289
    n = len(s)
    palindromes = set()
    for i in range(n - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes