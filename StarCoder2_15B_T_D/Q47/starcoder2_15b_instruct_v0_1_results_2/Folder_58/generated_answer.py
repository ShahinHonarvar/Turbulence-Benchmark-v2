def palindromes_of_specific_lengths(string):
    result = set()
    substring = string[125:284]
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            if substring[i:j] == substring[i:j][::-1] and j - i in range(109, 127):
                result.add(substring[i:j])
    return result