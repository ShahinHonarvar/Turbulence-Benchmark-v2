def palindrome_of_length_n(s):
    palindromes = set()
    s_lower = s.lower()
    n = 29
    for i in range(len(s) - n + 1):
        substring = s_lower[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring.upper())
    return palindromes