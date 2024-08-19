# deasciifier.py
import xml.etree.ElementTree as ET
import os

class Deasciifier:
    ASCII_TO_TURKISH = {
        'c': 'ç',
        'g': 'ğ',
        'i': 'ı',
        'o': 'ö',
        's': 'ş',
        'u': 'ü',
        'C': 'Ç',
        'G': 'Ğ',
        'I': 'İ',
        'O': 'Ö',
        'S': 'Ş',
        'U': 'Ü'
    }

    def __init__(self, asciistring):
        self.asciistring = asciistring
        self.turkishstring = None
        self.turkish_pattern_table = self.load_patterns()

    def load_patterns(self):
        turkish_pattern_table = {}
        pattern_path = os.path.join(os.path.dirname(__file__), 'patterns.xml')
        tree = ET.parse(pattern_path)
        root = tree.getroot()

        for character in root.findall('character'):
            char = character.get('tag')
            turkish_pattern_table[char] = {}
            for pattern in character.findall('pattern'):
                key = pattern.get('key')
                value = int(pattern.get('value'))
                turkish_pattern_table[char][key] = value

        return turkish_pattern_table

    def convert_to_turkish(self):
        if self.turkishstring:
            return self.turkishstring
        self.turkishstring = ""
        i = 0
        while i < len(self.asciistring):
            ch = self.asciistring[i]
            if self.is_ascii_char(ch):
                replacement = self.deasciify_char(i)
                self.turkishstring += replacement
            else:
                self.turkishstring += ch
            i += 1
        return self.turkishstring

    def is_ascii_char(self, char):
        return char.lower() in self.turkish_pattern_table or char in self.ASCII_TO_TURKISH

    def deasciify_char(self, index):
        char = self.asciistring[index]
        lowercase_char = char.lower()

        if lowercase_char in self.turkish_pattern_table:
            substring = self.get_substring(index, 10)
            patterns = self.turkish_pattern_table[lowercase_char]
            best_pattern = self.find_best_pattern(substring, patterns)
            if best_pattern:
                replacement_char = self.apply_case(self.ASCII_TO_TURKISH[lowercase_char], char)
                return replacement_char

        return self.ASCII_TO_TURKISH.get(char, char)

    def get_substring(self, start, size):
        start_idx = max(0, start - size)
        end_idx = min(len(self.asciistring), start + size + 1)
        return self.asciistring[start_idx:end_idx]

    def find_best_pattern(self, substring, patterns):
        best_pattern = None
        max_value = float('-inf')
        for pattern, value in patterns.items():
            if pattern in substring and value > max_value:
                best_pattern = pattern
                max_value = value
        return best_pattern

    def apply_case(self, turkish_char, original_char):
        if original_char.isupper():
            return turkish_char.upper()
        return turkish_char