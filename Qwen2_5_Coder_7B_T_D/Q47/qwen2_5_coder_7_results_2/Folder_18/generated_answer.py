def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:84]
    for i in range(len(substring)):
        for j in range(i + 13, min(len(substring), i + 67)):
            substring_part = substring[i:j]
            if substring_part == substring_part[::-1] and substring_part.isalpha():
                result.add(substring_part.lower())
    return result