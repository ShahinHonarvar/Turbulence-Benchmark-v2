def if_contains_anagrams(words):

    def get_signature(word):
        counts = [0] * 26
        for letter in word.lower():
            if letter.isalpha():
                counts[ord(letter) - ord('a')] += 1
        return tuple(counts)
    anagram_groups = {}
    for word in words:
        signature = get_signature(word)
        if signature not in anagram_groups:
            anagram_groups[signature] = [word]
        else:
            anagram_groups[signature].append(word)
    return len(anagram_groups) <= 61