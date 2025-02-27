def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    s_len = len(s)
    for i in range(s_len):
        for j in range(i + 57, s_len + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes