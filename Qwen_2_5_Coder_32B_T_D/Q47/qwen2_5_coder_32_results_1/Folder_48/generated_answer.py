def palindromes_of_specific_lengths(s):
    s = s[155:284].lower()
    result = set()
    for start in range(len(s) - 103):
        for end in range(start + 103, min(start + 120, len(s)) + 1):
            sub = s[start:end]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result