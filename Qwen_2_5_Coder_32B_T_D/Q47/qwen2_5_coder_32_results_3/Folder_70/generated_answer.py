def palindromes_of_specific_lengths(s):
    s = s[10:71].lower()
    result = set()
    for i in range(len(s) - 23):
        for j in range(i + 24, min(i + 53, len(s)) + 1):
            substr = s[i:j]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result