def palindromes_of_specific_lengths(s):
    start, end = (18, min(65, len(s)))
    palindromes = set()
    for length in range(23, 37):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes