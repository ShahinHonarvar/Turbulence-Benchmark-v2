def count_distinct_characters(s):
    seen = set()
    for char in s.lower():
        seen.add(char)
    return len(seen)

def if_contains_anagrams(words):
    anagrams = {}
    for word in words:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        if key in anagrams:
            anagrams[key].append(word)
            if len(anagrams[key]) > 2:
                return False
        else:
            anagrams[key] = [word]
    count = sum((1 for word_list in anagrams.values() if len(word_list) > 1))
    return count <= 26