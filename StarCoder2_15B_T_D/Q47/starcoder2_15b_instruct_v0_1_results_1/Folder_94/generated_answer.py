import re

def palindromes_of_specific_lengths(string):
    """
    Returns a set of all palindromes in the substring from index 40 to index 94 (both inclusive)
    of the given string, with lengths between 45 to 51 (both inclusive). Only palindromes
    consisting of English letters are considered. The palindromes are found in a case-insensitive
    manner. If no such palindrome occurs in the specified index range, an empty set is returned.
    """
    index_range = re.search('index (\\\\d+) to index (\\\\d+)', string)
    if not index_range:
        return set()
    start_index = int(index_range.group(1))
    end_index = int(index_range.group(2))
    length_range = re.search('lengths? between (\\\\d+) to (\\\\d+)', string)
    if not length_range:
        return set()
    min_length = int(length_range.group(1))
    max_length = int(length_range.group(2))
    regex = re.compile('[a-zA-Z]{' + str(min_length) + ',' + str(max_length) + '}')
    return set((word for word in regex.findall(string[start_index:end_index + 1]) if word.lower() == word[::-1].lower()))