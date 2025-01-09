"""
Esta solución no es la mejor ya que no
retorna el output esperado (mencionado en la actividad),
pero es lo mejor que pude hacer en 40min :)
"""

import string


def wordIndex(raw_input: str) -> dict:
    res = {}

    translator = str.maketrans("", "", string.punctuation)
    clean_text = raw_input.translate(translator)

    current_position = 0

    for word in clean_text.split():
        start_index = raw_input.find(word, current_position)
        current_position = start_index + len(word)

        first_letter = word[0].lower()

        if first_letter not in res:
            res[first_letter] = []
        res[first_letter].append((word, start_index + 1))

    for letter in res:
        res[letter].sort(key=lambda x: x[1])

    return res


def run():
    raw_input = "Hello, this is my text"
    result = wordIndex(raw_input)
    print(result)


if __name__ == "__main__":
    run()
