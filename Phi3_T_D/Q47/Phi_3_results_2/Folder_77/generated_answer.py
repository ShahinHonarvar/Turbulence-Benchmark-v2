import re
from itertools import combinations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(input_string):
    start_index = 103
    end_index = 276
    min_length = 100
    max_length = 169
    substring = input_string[start_index:end_index].lower()
    letter_sub = re.findall('[a-z]', substring)
    possible_palindromes = set()
    for length in range(min_length, max_length + 1):
        for start_pos in range(len(letter_sub) - length + 1):
            candidate = ''.join(combinations(letter_sub[start_pos:start_pos + length], length))
            if is_palindrome(candidate):
                possible_palindromes.add(candidate)
    return possible_palindromes