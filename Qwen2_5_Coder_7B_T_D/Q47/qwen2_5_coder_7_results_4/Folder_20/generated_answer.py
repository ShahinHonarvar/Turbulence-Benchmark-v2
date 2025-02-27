def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[20:75].lower()
    for length in range(36, 43):
        for i in range(len(substring) - length + 1):
            substring_piece = substring[i:i + length]
            if substring_piece == substring_piece[::-1] and substring_piece.isalpha():
                result.add(substring_piece)
    return result