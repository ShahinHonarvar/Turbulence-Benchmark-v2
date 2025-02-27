def palindromes_of_specific_lengths(s):
    start, end = (75, 95)
    substring = s[start:end + 1].lower()
    palindromes = set()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes