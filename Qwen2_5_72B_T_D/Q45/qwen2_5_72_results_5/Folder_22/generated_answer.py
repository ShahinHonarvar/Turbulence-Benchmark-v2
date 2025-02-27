def palindromes_between_indices(s):
    substring = s[5:7].lower()
    unique_chars = set(substring)
    possible_palindromes = set()
    if len(substring) < 2:
        return possible_palindromes
    for char in unique_chars:
        if substring.count(char) >= 2:
            possible_palindromes.add(char * 3)
    return possible_palindromes