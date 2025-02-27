def palindromes_of_specific_lengths(string):
    string = string[127:289]
    string = ''.join((c for c in string if c.isalpha()))
    string = string.lower()
    result = set()
    for length in range(119, 142):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result