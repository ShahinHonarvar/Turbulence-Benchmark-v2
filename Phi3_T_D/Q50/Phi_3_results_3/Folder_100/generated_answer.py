def if_contains_anagrams(words):
    count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    seen = set()
    for word in sorted_words:
        if word in seen:
            count += 1
        else:
            seen.add(word)
        if count >= 95:
            return True
    return False