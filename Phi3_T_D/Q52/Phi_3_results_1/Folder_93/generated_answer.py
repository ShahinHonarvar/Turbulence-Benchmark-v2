def palindrome_of_length_n(s):
    s = s.lower()
    s_len = len(s)
    palindromes = set()
    for i in range(s_len - 44):
        substring = s[i:i + 45]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes