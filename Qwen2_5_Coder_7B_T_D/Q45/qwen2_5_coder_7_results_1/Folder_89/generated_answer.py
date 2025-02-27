def palindromes_between_indices(s):
    substring = s[5:10].lower()
    letters = sorted(substring)
    n = len(letters)
    palindromes = set()
    for i in range(n):
        for j in range(i + 5, n + 1):
            candidate = ''.join(letters[i:j])
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes