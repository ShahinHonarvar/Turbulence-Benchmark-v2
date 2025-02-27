def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[24:98].lower()
    for i in range(len(substring)):
        for j in range(i + 10, min(len(substring), j + 37)):
            substring_part = substring[i:j]
            if substring_part == substring_part[::-1] and substring_part.isalpha():
                result.add(substring_part)
    return result