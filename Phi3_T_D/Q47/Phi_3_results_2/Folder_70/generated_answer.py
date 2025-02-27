def palindromes_of_specific_lengths(s):
    s = s[10:71].lower()
    palindromes = set()
    for length in range(24, 53):
        for i in range(len(s) - length + 1):
            candidate = s[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes