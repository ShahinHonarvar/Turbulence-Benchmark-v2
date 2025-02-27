def palindromes_of_specific_lengths(string):
    start_index = 31
    end_index = 74
    min_length = 23
    max_length = 39
    palindromes = set()
    for i in range(start_index, end_index - min_length + 1):
        for j in range(i + min_length, end_index - max_length + 1, -1):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes