def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[29:99].lower()
    for i in range(len(substring)):
        for j in range(i + 6, min(len(substring), i + 10)):
            substring_part = substring[i:j]
            if substring_part == substring_part[::-1] and substring_part.isalpha():
                result.add(substring_part)
    return result