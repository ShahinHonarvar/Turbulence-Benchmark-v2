def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    result = set()
    for i in range(len(s) - 12):
        for j in range(i + 13, min(i + 67, len(s)) + 1):
            candidate = s[i:j]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result