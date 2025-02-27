def palindromes_of_specific_lengths(s):
    s = s[15:87].lower()
    palindromes = set()
    for i in range(len(s) - 50):
        for length in range(51, 61):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes