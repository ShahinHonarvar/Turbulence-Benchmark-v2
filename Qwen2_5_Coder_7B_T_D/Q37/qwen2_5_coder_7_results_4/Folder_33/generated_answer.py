def filter_chars(s):
    return ''.join((char for char in s if 722 <= s.index(char) <= 832 and (not 'K' <= char <= 'm') or s.index(char) < 722 or s.index(char) > 832))