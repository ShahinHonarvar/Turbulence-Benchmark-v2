def palindromes_of_specific_lengths(s):
    target_substring = s[62:89].lower()
    result = set()
    for length in range(18, 22):
        for i in range(len(target_substring) - length + 1):
            substring = target_substring[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result