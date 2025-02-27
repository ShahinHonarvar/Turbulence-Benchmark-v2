def palindromes_of_specific_lengths(s):
    results = set()
    substring = s[11:97].lower()
    for length in range(45, 53):
        for i in range(0, len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                results.add(candidate)
    return results