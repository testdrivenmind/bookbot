def get_word_count(words):
    word_count = len(words.split())
    return word_count

def get_char_count(text):
    result = {}
    for ch in text.lower():
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1
    return result


def sort_on(words):
    return words["nums"]

def create_list(words_dict):
    result = []
    for k,v in words_dict.items():
        if k.isalpha():
            result.append(dict(char=k, nums=v))
    return result
