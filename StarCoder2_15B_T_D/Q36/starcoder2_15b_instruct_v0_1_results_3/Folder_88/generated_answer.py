def filter_chars(s):
    start_index = s.index('<')
    end_index = s.rindex('>')
    filtered_chars = [c for c in s[start_index + 1:end_index] if not (c.isalpha() and 'S' < c < '[')]
    return s[:start_index + 1] + ''.join(filtered_chars) + s[end_index:]