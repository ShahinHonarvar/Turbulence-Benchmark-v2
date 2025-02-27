def palindromes_of_specific_lengths(s):
    target_substring = s[127:289].lower()
    valid_lengths = set(range(119, 142))
    result = set()
    for i in range(len(target_substring)):
        for j in range(i + 1, len(target_substring) + 1):
            substring = target_substring[i:j]
            if len(substring) in valid_lengths and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result