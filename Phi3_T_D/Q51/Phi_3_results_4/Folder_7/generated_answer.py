import collections

def if_contains_anagrams(lst):
    count = 0
    checked = set()
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in checked:
            count += 1
            if count > 445:
                return False
        else:
            checked.add(sorted_word)
    return True