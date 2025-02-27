def palindromes_of_specific_lengths(s):
    s = s[40:95].lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for start in range(len(s) - 44):
        for length in range(45, 52):
            if start + length <= len(s):
                sub = s[start:start + length]
                if all((c in valid_chars for c in sub)) and sub == sub[::-1]:
                    palindromes.add(sub)
    return palindromes