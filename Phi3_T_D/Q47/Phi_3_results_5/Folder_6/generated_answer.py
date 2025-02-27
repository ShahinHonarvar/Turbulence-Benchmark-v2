def palindromes_of_specific_lengths(string):
    if len(string) < 98:
        return set()
    result_set = set()
    for length in range(40, 48):
        for i in range(45, len(string) - length + 1):
            substring = string[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                result_set.add(substring)
    return result_set