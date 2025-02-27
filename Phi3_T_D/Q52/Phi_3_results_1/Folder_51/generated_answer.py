def palindrome_of_length_n(s):
    s = s.lower()
    s_len = len(s)
    palindromes = set()
    for i in range(s_len - 72):
        substring = s[i:i + 73]
        if substring == substring[::-1]:
            palindromes.add(substring.upper())
    return palindromes