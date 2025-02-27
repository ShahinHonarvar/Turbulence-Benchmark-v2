def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n - 56):
        substring = s[i:i + 57]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes