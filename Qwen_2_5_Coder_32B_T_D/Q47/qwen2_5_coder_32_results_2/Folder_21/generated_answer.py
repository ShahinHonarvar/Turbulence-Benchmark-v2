def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    palindromes = set()
    for start in range(len(s) - 135):
        for length in range(136, 161):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes