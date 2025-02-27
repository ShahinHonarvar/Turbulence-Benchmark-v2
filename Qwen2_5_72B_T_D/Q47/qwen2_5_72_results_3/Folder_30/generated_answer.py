def palindromes_of_specific_lengths(s):
    substring = s[14:91]
    palindromes = set()
    for length in range(55, 72):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.lower() == candidate[::-1].lower() and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes