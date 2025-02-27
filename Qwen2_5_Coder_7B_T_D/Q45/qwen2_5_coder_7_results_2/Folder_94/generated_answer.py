def palindromes_between_indices(s: str) -> set:
    letters = s[3:5].lower()
    letters = ''.join(sorted(letters))
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            candidate = letters[i:j]
            if candidate == candidate[::-1] and len(candidate) >= 3:
                palindromes.add(candidate)
    return palindromes