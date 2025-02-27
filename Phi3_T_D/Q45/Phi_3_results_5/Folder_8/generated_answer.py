def palindromes_between_indices(s):
    english_letters = sorted(set((char.lower() for char in s.lower() if char.isalpha())))
    if len(english_letters) < 5:
        return set()
    half_palindromes = ['']
    for _ in english_letters[4:1:-1]:
        half_palindromes = [p[:i] + _ + p[i:] for p in half_palindromes for i in range(len(p) + 1)]
    palindromes = set((p + p[::-1] for p in half_palindromes))
    full_set = set((p for p in palindromes if len(p) >= 5))
    return full_set