def palindromes_of_specific_lengths(s):
    substring = s[29:97]
    palindromes = set()
    for length in range(12, 19):
        for i in range(len(substring) - length + 1):
            piece = substring[i:i + length]
            if piece.isalpha() and piece.lower() == piece[::-1].lower():
                palindromes.add(piece)
    return palindromes