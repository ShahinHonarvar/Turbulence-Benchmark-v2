def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[63:71]
    for i in range(4, 6):
        for j in range(len(substring) - i + 1):
            if substring[j:j + i].isalpha():
                if substring[j:j + i].lower() == substring[j:j + i][::-1].lower():
                    result.add(substring[j:j + i].lower())
    return result