def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[124:284].lower()
    for length in range(115, 135):
        for start in range(len(substring) - length + 1):
            substring_slice = substring[start:start + length]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                result.add(substring_slice)
    return result