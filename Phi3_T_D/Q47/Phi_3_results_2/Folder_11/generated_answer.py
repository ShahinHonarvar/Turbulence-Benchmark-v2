from itertools import combinations

def palindromes_of_specific_lengths(input_string):
    input_string = input_string[24:98].lower()
    start_indices, palindromes = ([], set())
    for i in range(10, 37):
        for j in range(len(input_string) - i + 1):
            substring = input_string[j:j + i]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes