def palindromes_between_indices(s):
    result = set()
    substr = s[4:7].lower()
    if len(substr) < 3:
        return result
    for i in range(len(substr)):
        for j in range(i + 3, len(substr) + 1):
            sub = substr[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result