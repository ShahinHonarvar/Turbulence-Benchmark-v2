import re
import itertools

def palindromes_between_indices(string):
    text_specification = re.search('\\s*(\\S+)\\s*', string).group(1)
    required_length = int(re.search('\\s*(\\d+)\\s*', text_specification).group(1))
    letters = list(set(re.findall('[a-z]', string.lower())))
    arrangements = itertools.permutations(letters, 4)
    palindromes = set((letter_arrangement for letter_arrangement in arrangements if len(letter_arrangement) >= required_length and letter_arrangement == ''.join(reversed(letter_arrangement))))
    return palindromes