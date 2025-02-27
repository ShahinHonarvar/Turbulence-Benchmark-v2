def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('K'), ord('m') + 1)}
    return ''.join((char for char in s if char not in chars_to_remove or s.index(char) < 722 or s.index(char) > 832))