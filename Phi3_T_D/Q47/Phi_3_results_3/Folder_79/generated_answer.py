def palindromes_of_specific_lengths(s):
    start, end = (1, 8)
    s = s.lower()[start:end]
    palindromes = set()
    for length in range(3, 5):
        for i in range(end - length + 1):
            substr = s[i:i + length]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes