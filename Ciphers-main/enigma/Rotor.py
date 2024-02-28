from typing import List

from utils import \
    ENGLISH_ALPHABET_UPPERCASE, \
    HISTORICAL_ROTOR_1, \
    HISTORICAL_ROTOR_2, \
    HISTORICAL_ROTOR_3, \
    HISTORICAL_ROTOR_4, \
    HISTORICAL_ROTOR_5, \
    HISTORICAL_ROTOR_NOTCH_1, \
    HISTORICAL_ROTOR_NOTCH_2, \
    HISTORICAL_ROTOR_NOTCH_3, \
    HISTORICAL_ROTOR_NOTCH_4, \
    HISTORICAL_ROTOR_NOTCH_5


class Rotor:
    notch_index: int
    notch_letter: str
    alphabet_index: int
    right_alphabet: List[str]
    left_alphabet: List[str]

    def __init__(self, rotor_number: str, turn_number: int, target_letter: str):
        self.left_alphabet = ENGLISH_ALPHABET_UPPERCASE.copy()
        if rotor_number == 'I':
            self.right_alphabet = HISTORICAL_ROTOR_1.copy()
            self.notch_index = self.left_alphabet.index(HISTORICAL_ROTOR_NOTCH_1)
            self.notch_letter = HISTORICAL_ROTOR_NOTCH_1
        elif rotor_number == 'II':
            self.right_alphabet = HISTORICAL_ROTOR_2.copy()
            self.notch_index = self.left_alphabet.index(HISTORICAL_ROTOR_NOTCH_2)
            self.notch_letter = HISTORICAL_ROTOR_NOTCH_2
        elif rotor_number == 'III':
            self.right_alphabet = HISTORICAL_ROTOR_3.copy()
            self.notch_index = self.left_alphabet.index(HISTORICAL_ROTOR_NOTCH_3)
            self.notch_letter = HISTORICAL_ROTOR_NOTCH_3
        elif rotor_number == 'IV':
            self.right_alphabet = HISTORICAL_ROTOR_4.copy()
            self.notch_index = self.left_alphabet.index(HISTORICAL_ROTOR_NOTCH_4)
            self.notch_letter = HISTORICAL_ROTOR_NOTCH_4
        elif rotor_number == 'V':
            self.right_alphabet = HISTORICAL_ROTOR_5.copy()
            self.notch_index = self.left_alphabet.index(HISTORICAL_ROTOR_NOTCH_5)
            self.notch_letter = HISTORICAL_ROTOR_NOTCH_5
        else:
            print(f"Invalid rotor number: {rotor_number}")
            exit(1)
        self.__rotate_to_letter(target_letter)
        self.__rotate_for_ring_setting(turn_number)
        return

    def __rotate_to_letter(self, target_letter: str) -> bool:
        crossed_notch: bool = False
        while self.left_alphabet[0] != target_letter:
            if not crossed_notch:
                crossed_notch = self.rotate_ring_full()
            else:
                self.rotate_ring_full()
        return crossed_notch

    def rotate_ring_full(self) -> bool:
        self.__rotate_ring_right()
        return self.__rotate_ring_left()

    def __rotate_ring_right(self):
        first_element_right = self.right_alphabet.pop(0)
        self.right_alphabet.append(first_element_right)

    def __rotate_ring_left(self) -> bool:
        first_element_left = self.left_alphabet.pop(0)
        self.left_alphabet.append(first_element_left)
        self.notch_index = self.left_alphabet.index(self.notch_letter)
        return first_element_left == self.notch_letter

    def __rotate_for_ring_setting(self, turn_number: int):
        for i in range(1, turn_number, 1):
            letter = self.right_alphabet.pop()
            self.right_alphabet.insert(0, letter)
            letter = self.left_alphabet.pop()
            self.left_alphabet.insert(0, letter)
        self.notch_letter = self.left_alphabet[self.notch_index]

    def pass_left(self, signal_index: int) -> int:
        letter = self.right_alphabet[signal_index]
        return self.left_alphabet.index(letter)

    def pass_right(self, signal_index: int) -> int:
        letter = self.left_alphabet[signal_index]
        return self.right_alphabet.index(letter)

    def check_for_notch(self) -> bool:
        return self.notch_index == 0
