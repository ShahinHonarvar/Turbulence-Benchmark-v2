def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[130:296].lower()
    for length in range(103, 159):
        for start in range(len(substring) - length + 1):
            substring_slice = substring[start:start + length]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                result.add(substring_slice)
    return result