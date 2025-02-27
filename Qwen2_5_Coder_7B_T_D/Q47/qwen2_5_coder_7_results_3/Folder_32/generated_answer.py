def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[16:78].lower()
    for i in range(len(substring)):
        for j in range(i + 43, min(len(substring), i + 48) + 1):
            substring_part = substring[i:j]
            if substring_part == substring_part[::-1] and substring_part.isalpha():
                result.add(substring_part)
    return result