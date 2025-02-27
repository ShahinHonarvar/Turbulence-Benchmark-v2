def palindromes_between_indices(s):
    letters = s[:8].lower()
    unique_letters = set(letters)
    if len(unique_letters) < 4:
        return set()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 6, len(letters) + 1):
            word = letters[i:j]
            if word == word[::-1] and len(word) >= 7:
                palindromes.add(word)
    return palindromes