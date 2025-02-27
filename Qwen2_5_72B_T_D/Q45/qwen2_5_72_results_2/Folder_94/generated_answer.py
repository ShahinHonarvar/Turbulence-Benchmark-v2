def palindromes_between_indices(s):
    substring = s[3:5].lower()
    if len(set(substring)) == 1:
        return {substring[0] * 3}
    return set()