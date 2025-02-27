def palindromes_between_indices(s):
    result = set()
    substrings = s[3:10].lower()
    for i in range(len(substrings)):
        for j in range(i + 3, len(substrings) + 1):
            sub = substrings[i:j]
            if sub == sub[::-1]:
                result.add(sub)
    return result