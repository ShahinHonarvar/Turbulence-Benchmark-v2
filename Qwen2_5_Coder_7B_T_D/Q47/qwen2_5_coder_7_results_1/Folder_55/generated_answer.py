def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:76].lower()
    for length in range(10, 21):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i + length]
            if substring_part == substring_part[::-1] and substring_part.isalpha():
                result.add(substring_part)
    return result