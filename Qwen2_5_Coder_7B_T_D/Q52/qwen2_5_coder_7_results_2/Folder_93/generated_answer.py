def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 45 + 1):
        substring = s[i:i + 45]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes