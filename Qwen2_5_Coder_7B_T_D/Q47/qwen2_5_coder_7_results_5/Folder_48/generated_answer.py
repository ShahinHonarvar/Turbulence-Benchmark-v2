def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[155:284].lower()
    for length in range(104, 121):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result