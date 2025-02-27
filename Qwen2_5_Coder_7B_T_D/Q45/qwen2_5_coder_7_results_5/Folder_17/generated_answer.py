def palindromes_between_indices(s):
    letters = set(s[2:7].lower())
    if len(letters) < 2:
        return set()
    even = {c * 2 for c in letters}
    odd = {c * 2 + c for c in letters}
    return even | odd