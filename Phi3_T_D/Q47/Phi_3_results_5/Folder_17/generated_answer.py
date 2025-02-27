def palindromes_of_specific_lengths(s):

    def is_valid_char(c):
        return 'a' <= c <= 'z'
    result = set()
    s = s[22:96]
    for i in range(len(s)):
        for length in range(52, 56):
            if len(s) - i >= length:
                substr = s[i:i + length].lower()
                if all((is_valid_char(c) for c in substr)) and substr == substr[::-1]:
                    result.add(substr)
    return result