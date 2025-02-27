def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[1:300]
    for length in range(3, 11):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                result.add(candidate)
    return result