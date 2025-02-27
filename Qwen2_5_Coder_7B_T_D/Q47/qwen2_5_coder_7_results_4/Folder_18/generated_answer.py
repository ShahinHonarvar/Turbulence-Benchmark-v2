import re

def palindromes_of_specific_lengths(s):
    start_index = 11
    end_index = 83
    min_length = 13
    max_length = 66
    palindrome_set = set()
    if start_index >= len(s) or end_index >= len(s):
        return palindrome_set
    substring = s[start_index:end_index + 1]
    cleaned_substring = re.sub('[^a-zA-Z]', '', substring).lower()
    for i in range(len(cleaned_substring)):
        for j in range(i + min_length, min(len(cleaned_substring), i + max_length) + 1):
            substring = cleaned_substring[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set