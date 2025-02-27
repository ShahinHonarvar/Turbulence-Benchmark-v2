def palindromes_of_specific_lengths(text):
    substring = text[12:93]
    results = set()
    for length in range(42, 78):
        for start in range(len(substring) - length + 1):
            substring_to_check = substring[start:start + length]
            if substring_to_check.lower() == substring_to_check[::-1].lower():
                results.add(substring_to_check)
    return results