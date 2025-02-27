def palindromes_of_specific_lengths(s):
    length_range = range(119, 142)
    relevant_slice = s[127:289]
    palindromes = set()
    for length in length_range:
        for i in range(len(relevant_slice) - length + 1):
            substring = relevant_slice[i:i + length]
            stripped = ''.join(filter(str.isalpha, substring)).lower()
            if len(stripped) == length and stripped == stripped[::-1]:
                palindromes.add(stripped)
    return palindromes