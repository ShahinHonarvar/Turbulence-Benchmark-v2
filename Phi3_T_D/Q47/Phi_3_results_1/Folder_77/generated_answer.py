def palindromes_of_specific_lengths(s):
    palindromes = set()
    start, end = (103, 276)
    s = s[start:end + 1].lower()
    for length in range(100, 170):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes