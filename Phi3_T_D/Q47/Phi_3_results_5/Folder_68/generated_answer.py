def palindromes_of_specific_lengths(s):
    start, end = (min(len(s), 50), min(len(s) + 1, 51))
    substring = s[:end]
    return {substring[i:j] for i in range(start) for j in range(i + 50, min(i + 101, len(substring) + 1)) if substring[i:j].isalpha() and substring[i:j].lower() == substring[i:j][::-1]}