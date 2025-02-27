def palindromes_of_specific_lengths(s):
    valid_positions = range(21, 63)
    return {s[i:j].lower() for i in valid_positions for j in range(i, min(i + 34, len(s) + 1)) if s[i:j].isalpha() and len(s[i:j]) >= 22 and (len(s[i:j]) <= 33) and (s[i:j].lower() == s[i:j][::-1])}