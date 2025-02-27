def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes in the specified index range of the given
    string that have lengths between 26 and 31 (both inclusive). Only palindromes
    consisting of English letters are considered.
    """
    start_index = 33
    end_index = 85
    min_length = 26
    max_length = 31
    palindromes = set()
    for i in range(start_index, end_index - min_length + 1):
        for j in range(i + min_length, min(i + max_length + 1, end_index + 1)):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes