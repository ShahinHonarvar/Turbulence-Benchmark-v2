from Q37.starcoder2_15B_results_2.Folder_46.generated_answer import filter_chars
import string
import random


def test_repeat_char():
    s = 'm' * (72 + 2)
    if 'i' <= 'm' <= 'v':
        assert filter_chars(s) == ''
    else:
        assert filter_chars(s) == s


def test_property_of_function():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(72 * 2))
    returned_s = filter_chars(s)
    sliced_s = s[11:72+1]
    for char in sliced_s:
        if 'i' <= char <= 'v':
            assert char not in returned_s


def test_compare_lengths_with_large_string():
    s = ''.join(random.choice(string.ascii_letters) for _ in range(72*100))
    assert len(filter_chars(s)) <= len(s)


def test_chars_not_in_range():
    s = ''
    given_range = list(range(ord('i'), ord('v') + 1))
    for _ in range(72 + 10):
        char = random.choice(string.ascii_letters + '$ % & * + < = > @ ')
        if ord(char) not in given_range:
            s += char
    
    assert filter_chars(s) == s


def test_chars_in_range():
    s = ''
    given_range = list(range(ord('i'), ord('v') + 1))
    for _ in range(11 + 1):
        s += 'i'
    for _ in range(72 - 11):
        s += chr(random.choice(given_range))
    
    assert filter_chars(s) == ''
