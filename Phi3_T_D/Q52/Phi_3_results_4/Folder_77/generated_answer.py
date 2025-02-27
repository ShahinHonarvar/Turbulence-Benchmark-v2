def palindrome_of_length_n(s):
    length = len(s)
    palindromes = set()
    s_lower = s.lower()
    for i in range(length):
        substring = s_lower[max(i - 172, 0):i + 173]
        if len(substring) == 173 and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes