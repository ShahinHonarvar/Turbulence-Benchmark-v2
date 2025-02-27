def palindromes_of_specific_lengths(s):
    s = s[18:99].lower()
    palindromes = set()
    for i in range(51 - 17):
        for length in range(17 + i, 31 + i + 1):
            for start_pos in range(92 - length + 1):
                yield s[start_pos:start_pos + length]