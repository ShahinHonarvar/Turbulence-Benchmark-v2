def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:56].lower()
    for length in range(3, 8):
        for i in range(len(substring) - length + 1):
            word = substring[i:i + length]
            if word == word[::-1] and word.isalpha():
                result.add(word)
    return result