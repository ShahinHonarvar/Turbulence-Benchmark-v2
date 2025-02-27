def palindromes_of_specific_lengths(s):
    substring = s[125:284]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    found_palindromes = set()
    for length in range(109, 127):
        for i in range(284 - length + 1):
            substring_chunk = substring[i:i + length]
            formatted_chunk = ''.join([c for c in substring_chunk if c.lower() in english_letters])
            if formatted_chunk.lower() == formatted_chunk[::-1].lower() and len(formatted_chunk) == length:
                found_palindromes.add(formatted_chunk.lower())
    return found_palindromes