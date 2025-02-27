def palindromes_of_specific_lengths(s):
    s = s[101:293].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 153, min(i + 182, len(s)) + 1):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes