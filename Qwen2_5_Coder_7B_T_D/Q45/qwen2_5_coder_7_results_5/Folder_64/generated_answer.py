def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = sorted(s)
    result = set()
    n = len(letters)
    for i in range(n):
        for j in range(i + 4, n + 1):
            candidate = ''.join(letters[i:j])
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result