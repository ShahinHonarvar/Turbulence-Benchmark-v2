def palindromes_between_indices(s):
    result = set()
    substring = s[5:7].lower()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result