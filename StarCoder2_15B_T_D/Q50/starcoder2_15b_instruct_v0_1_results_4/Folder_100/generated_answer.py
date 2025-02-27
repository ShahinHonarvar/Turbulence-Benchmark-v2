import re
import itertools

def if_contains_anagrams(lst):
    pattern = '\\[([^\\[\\]]+)\\]'
    text = re.search(pattern, instruction).group(1)
    return text