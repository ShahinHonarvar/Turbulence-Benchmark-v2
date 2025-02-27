def palindromes_of_specific_lengths(text):
    result = set()
    start, end = (75, 95)
    substr = text[start:end + 1]
    for length in range(7, 10):
        for i in range(0, end - length + 1):
            chunk = substr[i:i + length]
            if chunk.isalpha() and chunk.lower() == chunk[::-1].lower():
                result.add(chunk)
    return result