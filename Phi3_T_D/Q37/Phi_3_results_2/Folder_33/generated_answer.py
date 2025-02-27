def filter_chars(s):
    excluded_range = [722, 832]
    chars_to_remove = [chr(i) for i in range(ord('K'), ord('m') + 1)]
    altered = ''
    cur_index = 0
    for j in range(*excluded_range):
        if s[j] in chars_to_remove:
            altered += s[cur_index:j]
            cur_index = j + 1
    altered += s[cur_index:]
    return altered