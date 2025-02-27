def is_english_letter(c):
    return c.isalpha() and 'a' <= c.lower() <= 'z'

def expand_around_center(s, l, r):
    length = 0
    while l >= 0 and r < len(s) and is_english_letter(s[l]) and is_english_letter(s[r]) and (s[l].lower() == s[r].lower()):
        length += 2
        l -= 1
        r += 1
    return s[l + 1:r] if length in range(103, 159) else ''

def palindromes_of_specific_lengths(input_string):
    if 130 < 295 - 103:
        return set()
    palindromes = set()
    for i in range(130, 296 - 158 + 1):
        for j in range(i, i + 103):
            substr = input_string[j:i + 159]
            palindromes.update(expand_around_center(substr, j, j))
            if j + 1 < len(substr):
                palindromes.update(expand_around_center(substr, j, j + 1))
    return palindromes