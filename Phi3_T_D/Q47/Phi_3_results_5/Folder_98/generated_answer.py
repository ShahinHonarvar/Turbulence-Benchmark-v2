import re

def palindromes_of_specific_lengths(input_string):
    input_string = input_string[:21].lower()
    result_set = set()
    for length in range(5, 81):
        for start_index in range(len(input_string) - length + 1):
            substring = input_string[start_index:start_index + length]
            if re.fullmatch('[a-z]*', substring):
                if substring == substring[::-1]:
                    result_set.add(substring)
    return result_set