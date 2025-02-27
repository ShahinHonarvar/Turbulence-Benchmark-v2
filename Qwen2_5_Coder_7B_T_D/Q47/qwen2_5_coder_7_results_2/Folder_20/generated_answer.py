def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    substring = s[20:75]
    for i in range(36, 43):
        for j in range(len(substring) - i + 1):
            substring_slice = substring[j:j + i]
            if substring_slice == substring_slice[::-1]:
                result.add(substring_slice)
    return result