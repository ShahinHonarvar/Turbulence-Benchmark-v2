def palindromes_between_indices(s):
    s = s[2:9].lower()
    chars = list(s)
    n = len(chars)
    palindromes = set()
    for i in range(n):
        for j in range(i + 6, n + 1):
            substring = ''.join(chars[i:j])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes