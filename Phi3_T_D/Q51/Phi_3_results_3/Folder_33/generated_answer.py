def if_contains_anagrams(words):

    def to_key(s):
        return ''.join(sorted(s.lower()))
    count = 0
    items = {}
    for word in words:
        key = to_key(word)
        if key in items and items[key][-1] != word.lower() or (len(word) >= 3 and key not in items):
            items[key] = [word.lower()]
            count += 1
        elif key in items:
            items[key].append(word.lower())
            if items[key][-1] != word.lower():
                count += 1
            if count > 85:
                return False
    return True