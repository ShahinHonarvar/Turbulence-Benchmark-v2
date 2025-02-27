def palindromes_of_specific_lengths(s):
    s = s[155:284].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 103, min(i + 121, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes