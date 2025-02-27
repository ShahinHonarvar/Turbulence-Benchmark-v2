def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = 464
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes