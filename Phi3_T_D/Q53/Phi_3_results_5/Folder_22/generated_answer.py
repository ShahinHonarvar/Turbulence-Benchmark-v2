def palindrome_of_length_at_least_n(s):
    s = s.lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    alen = len(s)
    for i in range(alen - 96):
        for j in range(i + 97, min(i + 103, alen + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes