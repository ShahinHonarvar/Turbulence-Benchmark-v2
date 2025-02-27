def palindromes_of_specific_lengths(s):
    s = s[36:93].lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(10, 36):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes