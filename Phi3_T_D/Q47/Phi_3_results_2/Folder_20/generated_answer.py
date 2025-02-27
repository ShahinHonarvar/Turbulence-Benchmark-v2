def palindromes_of_specific_lengths(text):
    start_index, end_index = (20, 74)
    length_lower_bound, length_upper_bound = (36, 42)
    palindromes = set()
    for length in range(length_lower_bound, length_upper_bound + 1):
        for i in range(start_index, end_index - length + 1):
            substring = text[i:i + length].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes