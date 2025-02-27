def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[35:89].lower()
    for length in range(24, 34):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result