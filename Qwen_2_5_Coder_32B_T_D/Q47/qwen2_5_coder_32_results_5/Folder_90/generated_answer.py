def palindromes_of_specific_lengths(s):
    s = s[106:281].lower()
    palindromes = set()
    for length in range(136, 152):
        for start in range(len(s) - length + 1):
            candidate = s[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes