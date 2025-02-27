def palindromes_of_specific_lengths(s):
    target_range = s[101:293]
    target_length_min = 154
    target_length_max = 182
    result = set()
    for i in range(len(target_range)):
        for j in range(i + target_length_min, min(i + target_length_max + 1, len(target_range) - i + 1)):
            substring = target_range[i:i + j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result.add(substring)
    return result