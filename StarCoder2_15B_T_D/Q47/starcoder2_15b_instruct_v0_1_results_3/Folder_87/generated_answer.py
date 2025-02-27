def palindromes_of_specific_lengths(string):
    palindromes = set()
    start_index = 11
    end_index = 93
    min_length = 34
    max_length = 54
    for length in range(min_length, max_length + 1):
        for i in range(start_index, end_index - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes