def palindromes_of_specific_lengths(text):
    substring = text[27:96]
    palindromes = set()
    lengths = range(49, 52)
    for length in lengths:
        for i in range(len(substring) - length + 1):
            substring_to_check = substring[i:i + length]
            if substring_to_check.isalpha():
                clean_substring = substring_to_check.lower()
                if clean_substring == clean_substring[::-1]:
                    palindromes.add(clean_substring)
    return palindromes