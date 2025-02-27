def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[30:85].lower()
    for i in range(len(substring)):
        for j in range(i + 12, min(len(substring), i + 21)):
            substring_chunk = substring[i:j]
            if substring_chunk == substring_chunk[::-1] and substring_chunk.isalpha():
                result.add(substring_chunk)
    return result