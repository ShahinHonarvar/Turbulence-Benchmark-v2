def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 12):
        substring = s[i:i + 13]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes