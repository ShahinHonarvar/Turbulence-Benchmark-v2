def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[75:96].lower()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word == word[::-1]:
                result.add(word)
    return result