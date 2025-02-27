def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    palindromes = set()
    for i in range(len(s) - 16):
        for j in range(i + 17, min(i + 67, len(s)) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes