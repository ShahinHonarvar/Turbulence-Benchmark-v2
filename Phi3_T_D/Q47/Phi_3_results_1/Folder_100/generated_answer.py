def palindromes_of_specific_lengths(string):
    result_set = set()
    for length in range(12, 19):
        for i in range(29, 97 - length + 1):
            substring = string[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                result_set.add(substring.lower())
    return result_set