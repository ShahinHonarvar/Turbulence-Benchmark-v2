def palindromes_between_indices(s: str) -> set:
    s = s[1:5].lower()
    chars = set(s)
    result = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = ''.join(sorted(s[i:j]))
            if sub == sub[::-1]:
                result.add(sub)
    return result