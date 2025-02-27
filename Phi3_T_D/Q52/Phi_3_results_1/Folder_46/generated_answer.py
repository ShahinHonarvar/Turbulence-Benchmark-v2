def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 464, len(s) + 1):
            substring = s[i:j]
            if len(substring) == 464 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes