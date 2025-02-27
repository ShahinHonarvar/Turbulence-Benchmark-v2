def palindromes_of_specific_lengths(text):
    start, end = (62, 88)
    substring = text[start:end + 1]
    palindromes = set()
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            if substring[i:i + length].isalpha():
                substr_case_insensitive = substring[i:i + length].lower()
                if substr_case_insensitive == substr_case_insensitive[::-1]:
                    palindromes.add(substr_case_insensitive)
    return palindromes