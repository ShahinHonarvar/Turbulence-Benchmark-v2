import re
from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[1:8]
    letters = re.findall('[a-zA-Z]', sub_string)
    palindromes = set()
    for permutation in permutations(letters):
        joined_string = ''.join(permutation)
        for i in range(len(joined_string) - 2):
            if joined_string[i] == joined_string[i + 2]:
                palindromes.add(joined_string[i:i + 3])
    return palindromes