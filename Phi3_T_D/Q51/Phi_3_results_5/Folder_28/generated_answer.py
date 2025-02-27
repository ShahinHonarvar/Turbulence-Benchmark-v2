def if_contains_anagrams(word_list):

    def count_anagrams(word, rest):
        cnt = 0
        word_sorted = ''.join(sorted(word.lower()))
        anagrams = 0
        for w in rest:
            if len(word) >= 3 and len(w) >= 3:
                w_sorted = ''.join(sorted(w.lower()))
                if w_sorted == word_sorted:
                    anagrams += 1
            cnt += 1
        return anagrams if anagrams <= 78 else False
    for word in word_list:
        if isinstance(word, str):
            if count_anagrams(word, [w for w in word_list if w.lower() != word.lower()]):
                return True
    return False