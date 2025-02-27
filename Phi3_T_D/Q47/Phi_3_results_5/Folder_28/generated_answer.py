def is_english_letter(char):
    return 'a' <= char <= 'z'

def palindromes_of_specific_lengths(s):
    result = set()
    start, end = (32, 72)
    for length in range(21, 33):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if all((is_english_letter(c) for c in substring)) and substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result