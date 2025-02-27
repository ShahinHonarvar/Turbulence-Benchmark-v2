def palindromes_between_indices(s):
    indices = s[2:6].lower()
    unique_chars = set(indices)
    palindromes = set()
    for i in range(3, len(indices) + 1):
        for j in range(len(indices) - i + 1):
            substring = indices[j:j + i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes