def filter_chars(s):
    extracted_substring = s[2:7]
    filtered_characters = [c for c in extracted_substring if c > 'h' and c < 'k']
    filtered_string = ''.join(filtered_characters)
    return filtered_string