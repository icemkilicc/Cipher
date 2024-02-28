from typing import List

from utils import \
    HISTORICAL_REFLECTOR_A, \
    HISTORICAL_REFLECTOR_B, \
    HISTORICAL_REFLECTOR_C, \
    ENGLISH_ALPHABET_UPPERCASE


class Reflector:
    left_alphabet: List[str]
    right_alphabet: List[str]

    def __init__(self, reflector_type: str):
        self.left_alphabet = ENGLISH_ALPHABET_UPPERCASE.copy()
        if reflector_type == 'A':
            self.right_alphabet = HISTORICAL_REFLECTOR_A.copy()
        elif reflector_type == 'B':
            self.right_alphabet = HISTORICAL_REFLECTOR_B.copy()
        elif reflector_type == 'C':
            self.right_alphabet = HISTORICAL_REFLECTOR_C.copy()
        else:
            print(f"Invalid reflector type: {reflector_type}")
            exit(1)

    def reflect(self, signal: int) -> int:
        right_letter = self.right_alphabet[signal]
        return self.left_alphabet.index(right_letter)

    def rotate_full(self):
        self.__rotate_ring_right()
        self.__rotate_ring_left()

    def __rotate_ring_right(self):
        first_element_right = self.right_alphabet.pop(0)
        self.right_alphabet.append(first_element_right)

    def __rotate_ring_left(self):
        first_element_left = self.left_alphabet.pop(0)
        self.left_alphabet.append(first_element_left)
