import sys

from Enigma import Enigma


def main():
    settings_file_name = sys.argv[1]
    inputs_file_name = sys.argv[2]

    settings_list = []

    with open(settings_file_name, 'r') as file:
        for line in file:
            settings_list.append(line.rstrip())
        file.close()

    rotors_order = settings_list[0].split("-")
    reflector = settings_list[1]
    key_settings = [*settings_list[2]]
    ring_setting = [int(val) for val in settings_list[3].split(",")]
    letter_pairs = settings_list[4].split(" ")

    enigma = Enigma(letter_pairs, rotors_order, reflector, key_settings, ring_setting)

    with open(inputs_file_name, "r", encoding="utf-8", newline='') as inputs_file:
        input_content = inputs_file.read()
        results: str = ""
        for char in input_content:
            if char.isalpha():
                encrypted_char = enigma.encrypt(char.upper())
                results += encrypted_char
            else:
                results += char
        print(results)
        inputs_file.close()


if __name__ == '__main__':
    main()
    exit(0)
