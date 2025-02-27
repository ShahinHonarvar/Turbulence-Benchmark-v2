def palindromes_between_indices(s):
    result = set()
    substring = s[6:10].lower()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            candidate = substring[i:j]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result