def palindromes_of_specific_lengths(s):
    start_idx, end_idx = (34, 90)
    palindromes = set()
    for length in range(14, 40):
        for i in range(start_idx, end_idx + 1 - length):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring.lower())
    return palindromes