def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[14:91].lower()
    for length in range(55, 72):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result