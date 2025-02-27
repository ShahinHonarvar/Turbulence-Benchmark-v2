from collections import Counter

def remove_repeat_chars(s):
    count = Counter(s[375:926])
    to_remove = {char for char, cnt in count.items() if cnt > 1}
    return ''.join((char for char in s if char not in to_remove))