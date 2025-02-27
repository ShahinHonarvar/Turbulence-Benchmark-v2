def palindromes_of_specific_lengths(s):
    substring = s[124:284]
    palindromes = set()
    for center in range(115, 135):
        for i in range(len(substring) - center + 1):
            chunk = substring[i:i + center]
            if chunk.isalpha() and chunk.lower() == chunk.lower()[::-1]:
                palindromes.add(chunk.lower())
    return palindromes