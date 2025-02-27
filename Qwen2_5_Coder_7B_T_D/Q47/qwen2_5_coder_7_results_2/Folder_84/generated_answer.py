def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[23:78].lower()
    for i in range(len(substring)):
        for j in range(i + 13, min(i + 41, len(substring) + 1)):
            substring_part = substring[i:j]
            if substring_part == substring_part[::-1] and substring_part.isalpha():
                result.add(substring_part)
    return result