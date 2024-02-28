import sys


def main():
    if len(sys.argv) < 4:
        print("Insufficient number of arguments. Please use either \n -encrypt filename pairs\n or \n-decrypt "
              "filename pairs\n formats to run the code.\n")
    mode = sys.argv[1]
    filename = sys.argv[2]
    pairs = sys.argv[3]

    lines = readFile(filename)
    parsed_pairs = parse_pairs(pairs)

    if mode != "-encrypt" and mode != "-decrypt":
        print(f"Wrong flag name{mode}. Please use -encrypt or -decrypt.\n")
        exit(1)
    result_lines = handle_encrypt_decrypt(lines, parsed_pairs)
    write_results(result_lines, filename, mode)
    return


def parse_pairs(pairs: str) -> list[str]:
    return pairs.split("-")


def readFile(filename: str) -> list[str]:
    file = open(filename, "r", encoding="utf-8", newline='')
    lines = file.readlines()
    file.close()
    return lines


def write_results(result_lines: list[str], full_file_name: str, mode: str):
    """ Writes the results to the file named with one of the following format according to the command line mode flag:\n
    <original_file_name>-encrypted.<original_file_type>,\n
    <original_file_name>-decrypted.<original_file_type>. """
    file_name_parts = full_file_name.split(".")
    file_name = file_name_parts[0]
    file_type = file_name_parts[1]
    result_file_name = file_name + mode + "ed." + file_type
    result_file = open(result_file_name, "w", encoding="utf-8", newline='')
    result_file.write("".join(result_lines))
    result_file.close()
    print(f"Results are written into {result_file_name}.")


def handle_encrypt_decrypt(lines: list[str], pairs: list[str]) -> list[str]:
    """ With using SubstitutionCyper class encrypts or decrypts the given content. """
    cyper = SubstitutionCyper()
    cyper.process_pairs(pairs)
    transformed_lines = cyper.transform(lines)
    return transformed_lines


class SubstitutionCyper:
    ENGLISH_ALPHABET_UPPERCASE: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                                             "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    ENGLISH_ALPHABET_LOWERCASE: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                                             "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    accepted_chars: list[str] = []

    def __init__(self):
        self.dictionary = self.get_initial_dictionary()
        self.accepted_chars.extend(self.ENGLISH_ALPHABET_LOWERCASE)
        self.accepted_chars.extend(self.ENGLISH_ALPHABET_UPPERCASE)

    def get_initial_dictionary(self) -> dict[str, str]:
        """ Create default dictionary from given characters.The resulting dictionary will be in the format like this: \n
        dict = {\n
        "a": "a",\n
        ... ,\n
        "z": "z",\n
        "A": "A",\n
        ... ,\n
        "Z": "Z"\n
        } """
        alphabet = {}
        for char in self.ENGLISH_ALPHABET_UPPERCASE:
            alphabet[char] = char
        for char in self.ENGLISH_ALPHABET_LOWERCASE:
            alphabet[char] = char
        return alphabet

    def process_pairs(self, pairs: list[str]):
        """ Processes the given pair list and writes the changes to the main dictionary. """
        for pair in pairs:
            if len(pair) == 2:
                lower1 = str.lower(pair[0])
                lower2 = str.lower(pair[1])
                upper1 = str.upper(pair[0])
                upper2 = str.upper(pair[1])
                self.dictionary[lower1] = lower2
                self.dictionary[lower2] = lower1
                self.dictionary[upper1] = upper2
                self.dictionary[upper2] = upper1
            else:
                continue
        return

    def transform(self, lines: list[str]) -> list[str]:
        """ Transforms the given list of lines from original content to encrypted form.
        If the content is already encrypted then result is original content. """
        transformed_lines = []
        for line in lines:
            transformed_line = ""
            for char in line:
                if char in self.accepted_chars:
                    transformed_line += self.dictionary.get(char)
                else:
                    transformed_line += char
            transformed_lines.append(transformed_line)
        return transformed_lines


if __name__ == '__main__':
    main()
    exit(0)
