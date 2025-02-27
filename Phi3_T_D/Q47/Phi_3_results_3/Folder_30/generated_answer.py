def palindromes_of_specific_lengths(s: str):
    substring = s[14:91]
    palindromes = set()
    for start in range(14, 72):
        for end in range(start + 54, min(start + 72, 91) + 1):
            substring_slice = substring[start:end + 1]
            if substring_slice.isalpha() and substring_slice.lower() == substring_slice[::-1].lower():
                palindromes.add(substring_slice.lower())
    return palindromes