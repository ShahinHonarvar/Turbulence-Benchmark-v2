def palindromes_of_specific_lengths(s):
    s = s[119:257].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 103, min(i + 123, len(s))):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes