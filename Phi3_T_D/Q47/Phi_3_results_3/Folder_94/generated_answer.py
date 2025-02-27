def palindromes_of_specific_lengths(string):
    substring = string[39:95].lower()
    valid_palindromes = set()
    for length in range(45, 52):
        for i in range(len(substring) - length + 1):
            substring_chunk = substring[i:i + length]
            if substring_chunk.isalpha():
                if substring_chunk == substring_chunk[::-1]:
                    valid_palindromes.add(substring_chunk)
    return valid_palindromes