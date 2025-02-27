def palindromes_of_specific_lengths(data):
    unique_palindromes = set()
    for length_limit in range(104, 124):
        for start in range(119, min(257, len(data) - length_limit + 1)):
            substring = data[start:start + length_limit].lower()
            if substring.isalpha() and substring == substring[::-1]:
                unique_palindromes.add(substring)
    return unique_palindromes