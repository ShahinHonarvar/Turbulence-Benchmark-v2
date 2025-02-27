def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[100:296]
    for length in range(136, 161):
        for i in range(len(substring) - length + 1):
            substring_piece = substring[i:i + length]
            if substring_piece.isalpha() and substring_piece.lower() == substring_piece[::-1].lower():
                result.add(substring_piece)
    return result