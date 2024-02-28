from typing import Dict, List

from utils import ENGLISH_ALPHABET_UPPERCASE


class Plugboard:
    dictionary: Dict[str, str]

    def __init__(self, pair_list: List[str]):
        self.dictionary = self.__get_initial_dictionary()
        self.__process_pairs(pair_list)

    def __get_initial_dictionary(self) -> Dict[str, str]:
        """ Create default dictionary from given characters.The resulting dictionary will be in the format like this: \n
        dict = {\n
        "A": "A",\n
        ... ,\n
        "Z": "Z"\n
        } """
        alphabet = {}
        for char in ENGLISH_ALPHABET_UPPERCASE:
            alphabet[char] = char
        return alphabet

    def __process_pairs(self, pairs: List[str]):
        """ Processes the given pair list and writes the changes to the main dictionary. """
        for pair in pairs:
            if len(pair) == 2:
                upper1 = str.upper(pair[0])
                upper2 = str.upper(pair[1])
                self.dictionary[upper1] = upper2
                self.dictionary[upper2] = upper1
            else:
                continue
        return

    def pass_left(self, signal: str) -> int:
        letter = self.dictionary.get(signal)
        return ENGLISH_ALPHABET_UPPERCASE.index(letter)

    def pass_right(self, signal: int) -> str:
        letter = ENGLISH_ALPHABET_UPPERCASE[signal]
        return self.dictionary.get(letter)
