def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    palindromes = set()
    for start in range(len(s) - 56):
        for length in range(57, 61):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes