def filter_chars(s):

    def should_remove(char):
        return 'T' <= char <= 'h'
    filtered_chars = [char for i, char in enumerate(s) if i < 373 or i > 901 or (not should_remove(char))]
    return ''.join(filtered_chars)