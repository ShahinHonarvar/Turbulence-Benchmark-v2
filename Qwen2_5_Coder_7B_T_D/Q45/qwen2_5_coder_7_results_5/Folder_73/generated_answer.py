def palindromes_between_indices(s):
    range_str = s[3:7].lower()
    chars = sorted(range_str)
    n = len(chars)
    result = set()
    for i in range(n):
        for j in range(i + 2, n + 1):
            sub = ''.join(chars[i:j])
            if sub == sub[::-1]:
                result.add(sub)
    return result