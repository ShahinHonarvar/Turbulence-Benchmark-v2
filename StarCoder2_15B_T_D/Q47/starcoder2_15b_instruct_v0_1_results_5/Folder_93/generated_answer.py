def palindromes_of_specific_lengths(text):
    start_index = 17
    end_index = 95
    min_length = 13
    max_length = 49
    palindromes = set()
    for i in range(start_index, end_index - min_length + 1):
        for j in range(i + min_length, min(i + max_length + 1, end_index + 1)):
            substring = text[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes