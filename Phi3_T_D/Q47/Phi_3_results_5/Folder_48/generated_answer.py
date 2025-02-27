def is_english_letter(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def is_palindrome(s):
    return s == s[::-1]

def find_palindromes(string, start, end, min_len, max_len):
    result = set()
    for length in range(min_len, max_len + 1):
        substr = [string[i:i + length].lower() for i in range(start, min(end, len(string) - length + 1))]
        for sub in substr:
            if all((is_english_letter(ch) for ch in sub)) and is_palindrome(sub):
                result.add(sub)
    return result

def palindromes_of_specific_lengths(string):
    return find_palindromes(string, 155, 283, 104, 120)