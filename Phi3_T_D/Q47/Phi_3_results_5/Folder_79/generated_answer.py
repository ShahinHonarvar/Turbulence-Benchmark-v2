def palindromes_of_specific_lengths(s):
    s = s[1:9].lower()
    result = set()
    for i in range(6):
        substr = s[i:i + 3]
        if substr == substr[::-1]:
            result.add(substr.upper())
    return result