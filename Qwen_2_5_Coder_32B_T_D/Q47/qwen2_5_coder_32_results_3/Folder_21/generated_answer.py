def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 135, min(i + 161, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes