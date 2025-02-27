def palindromes_of_specific_lengths(s):
    s = s[:51].lower()
    result = set()
    for start in range(len(s) - 49):
        for end in range(start + 49, min(start + 100, len(s))):
            substr = s[start:end + 1]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result