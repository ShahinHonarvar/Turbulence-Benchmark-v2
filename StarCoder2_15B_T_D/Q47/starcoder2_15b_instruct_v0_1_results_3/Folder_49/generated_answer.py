def palindromes_of_specific_lengths(string):
    palindromes = set()
    start_index = 10
    end_index = 100
    for length in range(10, 51):
        for i in range(start_index, end_index - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes