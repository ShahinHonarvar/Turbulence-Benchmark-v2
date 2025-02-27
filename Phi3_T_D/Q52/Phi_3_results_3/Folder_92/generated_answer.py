def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 9):
        substring = s[i:i + 10]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes