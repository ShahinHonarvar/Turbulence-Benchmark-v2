def palindromes_of_specific_lengths(s):
    s = s[16:78].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 42, min(i + 48, len(s))):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes