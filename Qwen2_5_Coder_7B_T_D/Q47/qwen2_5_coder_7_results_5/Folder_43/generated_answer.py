def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[41:90].lower()
    for length in range(23, 39):
        for i in range(len(substring) - length + 1):
            substring_chunk = substring[i:i + length]
            if substring_chunk == substring_chunk[::-1] and substring_chunk.isalpha():
                palindromes.add(substring_chunk)
    return palindromes