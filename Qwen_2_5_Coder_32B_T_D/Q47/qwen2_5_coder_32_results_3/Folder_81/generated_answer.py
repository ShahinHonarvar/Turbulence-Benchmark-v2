def palindromes_of_specific_lengths(s):
    s = s[12:123].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 12, min(i + 221, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes