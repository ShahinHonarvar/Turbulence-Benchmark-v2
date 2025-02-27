def palindromes_of_specific_lengths(str):
    palindromes = set()
    str_lower = str.lower()
    start_index = 10
    end_index = 70
    min_length = 24
    max_length = 52
    for length in range(min_length, max_length + 1):
        for i in range(start_index, end_index - length + 1):
            substring = str_lower[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes