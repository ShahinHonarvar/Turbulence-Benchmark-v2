def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[39:95]
    for i in range(14, 53):
        for j in range(len(substring) - i + 1):
            chunk = substring[j:j + i]
            if chunk.isalpha() and chunk == chunk[::-1]:
                result.add(chunk.lower())
    return result