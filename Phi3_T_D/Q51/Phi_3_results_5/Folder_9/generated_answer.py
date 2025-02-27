def char_count(s):
    count = [0] * 26
    for char in s:
        count[ord(char.lower()) - ord('a')] += 1
    return tuple(count)

def if_contains_anagrams(words):
    anagrams_count = 0
    word_map = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word)).lower()
            if sorted_word in word_map:
                anagrams_count += word_map[sorted_word]
                word_map[sorted_word] += 1
            else:
                word_map[sorted_word] = 1
    return anagrams_count <= 475