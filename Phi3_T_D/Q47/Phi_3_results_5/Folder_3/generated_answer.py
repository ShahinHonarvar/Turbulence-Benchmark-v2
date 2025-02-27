def palindromes_of_specific_lengths(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    result = set()
    for start_idx in range(27, 96 - 49 + 1):
        for length in range(2, 3):
            for end_idx in range(start_idx + length, 96 - length + 1):
                substr = s[start_idx:end_idx + 1]
                if all((c in alphabet for c in substr)) and substr.lower() == substr[::-1].lower():
                    result.add(substr)
    return result