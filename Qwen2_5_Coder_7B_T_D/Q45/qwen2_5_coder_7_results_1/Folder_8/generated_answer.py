def palindromes_between_indices(s):
    result = set()
    subset = s[1:6]
    subset = subset.lower()
    chars = list(subset)
    for i in range(len(chars)):
        for j in range(i + 5, len(chars) + 1):
            sub = ''.join(sorted(chars[i:j]))
            if sub == sub[::-1]:
                result.add(sub)
    return result