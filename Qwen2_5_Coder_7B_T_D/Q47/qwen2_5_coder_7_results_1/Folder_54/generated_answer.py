def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i, min(i + 19, len(s))):
            substr = s[i:j + 1]
            if substr == substr[::-1] and substr.isalpha() and (18 <= len(substr) <= 19):
                result.add(substr)
    return result