def palindromes_of_specific_lengths(s):
    start, end = (31, 74)
    palindromes = set()
    for length in range(23, 40):
        for i in range(start, end + 1 - length):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring.lower())
    return palindromes