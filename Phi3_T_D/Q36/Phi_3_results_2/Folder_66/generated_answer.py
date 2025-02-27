def filter_chars(input_string):
    charset = set((chr(i) for i in range(ord('!'), ord('}') + 1))) - {'!'}
    filtered_string = ''.join((c for i, c in enumerate(input_string) if i < 39 or i >= 87 or c not in charset))
    return filtered_string