def palindromes_between_indices(s: str) -> set:
    s = s.lower()
    palindromes = set()
    for i in range(5, len(s) - 1):
        for j in range(i + 1, min(i + 3, len(s))):
            if s[i] == s[j]:
                palindromes.add(s[i] + s[j])
    return palindromes