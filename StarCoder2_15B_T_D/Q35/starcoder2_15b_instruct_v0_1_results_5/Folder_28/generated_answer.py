import re

def remove_repeat_chars(string):
    chars = [c for c in string[86:99]]
    counts = {}
    for c in chars:
        counts[c] = counts.get(c, 0) + 1
    repeated_chars = [c for c, count in counts.items() if count > 1]
    pattern = re.compile(f'[{''.join(repeated_chars)}]')
    return pattern.sub('', string)