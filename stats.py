def count_words(content):
    return len(content.split())


def count_characters(content):
    character_dict = {}

    for char in content:
        char = char.lower()
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1

    return character_dict


def sort_on(dict):
    return dict["num"]


def sort_character_counts(char_dict):
    separated_dicts = []

    for key in char_dict:
        separated_dicts.append({
            "char": key,
            "num": char_dict[key]
        })

    separated_dicts.sort(reverse=True, key=sort_on)

    return separated_dicts