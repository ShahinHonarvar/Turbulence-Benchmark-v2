def is_english_letter(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def palindromes_of_specific_lengths(s):
    substring = s[26:88]
    result_set = set()
    for length in range(52, 57):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((is_english_letter(char) for char in candidate)):
                cleaned = ''.join(filter(str.isalpha, candidate)).lower()
                if cleaned == cleaned[::-1]:
                    result_set.add(cleaned.upper())
    return result_set