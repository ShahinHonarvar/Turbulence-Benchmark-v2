def palindromes_between_indices(s):
    substring = s[2:4].lower()
    if len(substring) != 2:
        return set()
    char_frequency = {}
    for char in substring:
        if char.isalpha():
            char_frequency[char] = char_frequency.get(char, 0) + 1
    possible_palindromes = set()
    for char, count in char_frequency.items():
        if count >= 2:
            possible_palindromes.add(char * 3)
    return possible_palindromes