def palindromes_between_indices(s):
    result = set()
    substring = s[4:6]
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1] and len(sub) >= 3:
                result.add(sub.lower())
    return result