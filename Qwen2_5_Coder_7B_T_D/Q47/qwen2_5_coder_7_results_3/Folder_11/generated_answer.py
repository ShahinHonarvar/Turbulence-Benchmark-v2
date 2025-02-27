def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(24, 98):
        for j in range(i + 10, min(i + 37, len(s) + 1)):
            substr = s[i:j]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result