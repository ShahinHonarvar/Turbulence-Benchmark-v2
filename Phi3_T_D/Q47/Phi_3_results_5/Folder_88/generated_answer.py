def palindromes_of_specific_lengths(s):
    start, end = (11, 87)
    s = s.lower()
    palindromes = set()
    for i in range(start, end - 3):
        for length in range(4, 6):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes