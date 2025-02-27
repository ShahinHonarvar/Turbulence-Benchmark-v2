def palindromes_between_indices(s):
    s = s[1:9]
    s = s.lower()
    chars = set(s)
    max_length = min(len(s), 4)
    palindromes = set()
    for length in range(max_length, 3, -1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and len(set(substring)) >= 4:
                palindromes.add(substring)
    return palindromes