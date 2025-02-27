def palindromes_of_specific_lengths(s):
    s = s[33:86].lower()
    result = set()
    for i in range(len(s) - 25):
        for j in range(i + 26, min(i + 32, len(s)) + 1):
            candidate = s[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result