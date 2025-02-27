import re
import string

def palindromes_between_indices(text):
    text_specification = re.search('>.*<', text).group(0)[1:-1]
    text_specification = text_specification.replace('>', '').replace('<', '')
    substring = text[8:10]
    palindromes = set()
    for permutation in itertools.permutations(substring, len(substring)):
        permutation = ''.join(permutation)
        if permutation.lower() == permutation[::-1].lower() and len(permutation) >= 3:
            palindromes.add(permutation)
    return palindromes