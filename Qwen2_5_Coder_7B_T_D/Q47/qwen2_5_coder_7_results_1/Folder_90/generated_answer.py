def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[106:281].lower()
    for i in range(136, 152):
        for j in range(len(substring) - i + 1):
            substring_slice = substring[j:j + i]
            if substring_slice == substring_slice[::-1] and substring_slice.isalpha():
                result.add(substring_slice)
    return result