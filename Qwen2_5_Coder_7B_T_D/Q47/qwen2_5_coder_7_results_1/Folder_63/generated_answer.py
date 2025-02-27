def palindromes_of_specific_lengths(text):
    result = set()
    substring = text[33:86].lower()
    for length in range(26, 32):
        for start in range(len(substring) - length + 1):
            substring_part = substring[start:start + length]
            if substring_part == substring_part[::-1] and substring_part.isalpha():
                result.add(substring_part)
    return result