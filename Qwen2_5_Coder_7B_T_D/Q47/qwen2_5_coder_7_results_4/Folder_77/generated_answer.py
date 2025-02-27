def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[103:277].lower()
    for i in range(len(substring)):
        for j in range(i + 100, min(len(substring), i + 170) + 1):
            substring_slice = substring[i:j]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                result.add(substring_slice)
    return result