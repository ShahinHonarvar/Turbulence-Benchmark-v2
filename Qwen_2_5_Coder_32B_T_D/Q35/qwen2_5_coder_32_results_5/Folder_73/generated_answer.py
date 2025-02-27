def remove_repeat_chars(s):
    if len(s) <= 76:
        return s
    analysis_segment = s[11:76]
    repeat_chars = set([char for char in analysis_segment if analysis_segment.count(char) > 1])
    return ''.join([char for char in s if char not in repeat_chars])