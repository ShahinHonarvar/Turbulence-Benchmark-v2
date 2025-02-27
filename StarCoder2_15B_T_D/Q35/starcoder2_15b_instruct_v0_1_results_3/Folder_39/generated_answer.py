def remove_repeat_chars(text):
    occurrence_map = {}
    for i, char in enumerate(text):
        if char not in occurrence_map:
            occurrence_map[char] = [i]
        else:
            occurrence_map[char].append(i)
    for char, indices in occurrence_map.items():
        if len(indices) > 1 and 44 < indices[0] < 91:
            text = text.replace(char, '')
    return text