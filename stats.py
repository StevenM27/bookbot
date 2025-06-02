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