def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[34:91].lower()
    for i in range(len(substring)):
        for j in range(i + 14, min(len(substring), i + 40)):
            substring_slice = substring[i:j]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                result.add(substring_slice)
    return result