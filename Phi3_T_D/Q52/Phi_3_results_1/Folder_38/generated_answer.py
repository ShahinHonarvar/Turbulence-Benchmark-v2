def palindrome_of_length_n(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s) - 38 + 1):
        substring = s_lower[i:i + 38]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes