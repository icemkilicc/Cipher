from Keyboard import Keyboard
from Plugboard import Plugboard
from Reflector import Reflector
from Rotor import Rotor


class Enigma:

    def __init__(self, plugboard_pairs, rotors, reflector, key_settings, ring_settings):
        self.keyboard = Keyboard()
        self.plugboard = Plugboard(plugboard_pairs)
        self.fast_rotor = Rotor(rotors[2], ring_settings[2], key_settings[2])
        self.medium_rotor = Rotor(rotors[1], ring_settings[1], key_settings[1])
        self.slow_rotor = Rotor(rotors[0], ring_settings[0], key_settings[0])
        self.reflector = Reflector(reflector)

    def encrypt(self, input_char: str) -> str:
        self.calculate_notch()

        result = self.keyboard.pass_left(input_char)
        result = self.plugboard.pass_left(result)
        result = self.fast_rotor.pass_left(result)
        result = self.medium_rotor.pass_left(result)
        result = self.slow_rotor.pass_left(result)
        result = self.reflector.reflect(result)
        result = self.slow_rotor.pass_right(result)
        result = self.medium_rotor.pass_right(result)
        result = self.fast_rotor.pass_right(result)
        result = self.plugboard.pass_right(result)
        result = self.keyboard.pass_right(result)
        return result

    def calculate_notch(self):
        if self.medium_rotor.check_for_notch():
            self.fast_rotor.rotate_ring_full()
            self.medium_rotor.rotate_ring_full()
            self.slow_rotor.rotate_ring_full()
            return
        notch_passed = self.fast_rotor.rotate_ring_full()
        if notch_passed:
            notch_passed = self.medium_rotor.rotate_ring_full()
            if notch_passed:
                notch_passed = self.slow_rotor.rotate_ring_full()
                if notch_passed:
                    self.reflector.rotate_full()
