def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[75:96].lower()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i + length]
            if substring_part == substring_part[::-1] and substring_part.isalpha():
                result.add(substring_part)
    return result