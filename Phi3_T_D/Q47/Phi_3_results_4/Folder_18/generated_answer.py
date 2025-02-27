def palindromes_of_specific_lengths(text):
    lower_bound = 11
    upper_bound = 83
    min_length = 13
    max_length = 66
    result = set()
    substring = text[lower_bound:upper_bound + 1]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    for length in range(min_length, max_length + 1):
        for start in range(len(substring) - length + 1):
            if substring[start:start + length] == substring[start:start + length][::-1]:
                result.add(substring[start:start + length])
    return result