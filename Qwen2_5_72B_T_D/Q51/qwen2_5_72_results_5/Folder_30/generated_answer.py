def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            norm_word = normalize(word)
            if norm_word in anagram_dict:
                anagram_dict[norm_word].append(word)
            else:
                anagram_dict[norm_word] = [word]
    for key in anagram_dict:
        n = len(anagram_dict[key])
        count += n * (n - 1) // 2
    return count <= 28