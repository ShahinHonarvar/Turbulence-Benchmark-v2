def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[11:98].lower()
    for length in range(29, 63):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i + length]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                result.add(substring_slice)
    return result