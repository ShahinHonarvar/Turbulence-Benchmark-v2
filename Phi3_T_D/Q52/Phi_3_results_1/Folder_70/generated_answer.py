def palindrome_of_length_n(s):
    s = s.lower()
    length = 401
    palindromes = set()
    s_len = len(s)
    for i in range(s_len - length + 1):
        substring = s[i:i + length]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes