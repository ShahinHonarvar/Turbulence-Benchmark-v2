def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[155:284].lower()
    for length in range(104, 121):
        for start in range(len(substring) - length + 1):
            substring_slice = substring[start:start + length]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                result.add(substring_slice)
    return result