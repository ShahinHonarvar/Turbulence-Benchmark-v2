def palindromes_of_specific_lengths(s):
    start, end = (39, 94)
    s = s[start:end + 1].lower()
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes