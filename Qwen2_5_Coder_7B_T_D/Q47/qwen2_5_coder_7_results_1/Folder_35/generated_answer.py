def palindromes_of_specific_lengths(s: str) -> set:
    result = set()
    substring = s[34:91].lower()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1]:
                result.add(sub)
    return result