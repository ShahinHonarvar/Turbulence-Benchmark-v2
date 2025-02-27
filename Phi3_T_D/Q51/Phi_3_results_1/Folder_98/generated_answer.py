def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    unique_words = {normalize(word) for word in words if len(word) >= 3}
    count = 0
    seen = set()
    for normalized in unique_words:
        if normalized in seen:
            count += 1
        seen.add(normalized)
    return count <= 46