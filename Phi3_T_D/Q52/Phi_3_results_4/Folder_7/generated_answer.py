def palindrome_of_length_n(s):
    if len(s) < 416:
        return set()
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s) - 416 + 1):
        substring = s_lower[i:i + 416]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes