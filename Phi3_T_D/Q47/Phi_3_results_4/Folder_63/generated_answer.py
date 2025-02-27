def palindromes_of_specific_lengths(s):
    start, end = (33, 85)
    candidate_s = s[start:end + 1].lower()
    valid_lengths = range(26, 32)
    palindromes = set()
    for length in valid_lengths:
        for i in range(0, end - length + 1):
            substring = candidate_s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes