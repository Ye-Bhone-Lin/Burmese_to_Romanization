import re
from typing import Dict
import streamlit as st

def burmese_to_romanize(text: str) -> str:
    
        """
        Convert Burmese text to Romanized form.
        
        :param text: Burmese text input
        :return: Romanized text output
        """
        burmese_to_roman: Dict[str, str] = {
            'က': 'k', 'ခ': 'K', 'ဂ': 'g', 'ဃ': 'G', 'င': 'c', "၎င်": "4c", "၏": "E", "၍": "rx", "၌": "Nx", "င်္": "F",
            'စ': 's', 'ဆ': 'S', 'ဇ': 'z', 'ဈ': 'Z', "ဉ": "q", 'ည': 'Q', "ဋ": "tx", "ဌ": "Tx", "ဍ": "dx", "ဎ": "Dx", "ဏ": "nx",
            "ရ": "r", "ဓ": "D", "တ": "t", "ထ": "T", "ဒ": "d", "န": "n", "ပ": "p", "ဖ": "P", "ဗ": "b", "ဘ": "B", "မ": "m",
            "ယ": "y", "ဝ": "W", "သ": "j", "ဟ": "H", "အ": "a", 'လ': 'l', "ဠ": "lx", "ဣ": "ix", "ဤ": "I",
            "၊": "/", "။": "//", "ဥ": "U", "ဦ": "O", "ဧ": "ax", "ဩ": "J", "ဪ": "Joo", "ါ": "a", "ာ": "A", "ိ": "i", "ီ": "ii",
            "ု": "u", "ူ": "uu", "ေ": "e", "ဲ": "L", "ံ": "’", "့": ".", "း": ":", "ျ": "Y", "ြ": "R", "ွ": "w", "ှ": "h",
            "ဿ": "jx", "်": ""
        }
        text = text.strip()
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r' ', ',', text)

        text = re.sub(r',+', ',', text)

        # Tokenization for Romanization
        text = re.sub(r"([က-အ|ဥ|ဦ](င်္|[က-အ][ှ]*[့း]*[်]|([က-အ]္)|[ါ-ှႏꩻ][ꩻ]*){0,}|.)", r"\1 ", text)
        text = re.sub(r"(([က-အ])္ ([က-အ]))", r"\2် \3", text)

        rules = [
            (re.compile(r'ကျွန် မ '), "q'm "),
            (re.compile(r'ကျွန် တော် '), "q't "),
            (re.compile(r'ကျွန်ပ် '), 'Q" '),
            (re.compile(r'ဏ် ဍ'), "F")
        ]

        for rule in rules:
            text = rule[0].sub(rule[1], text)
        text = re.sub(r"\u1031\u102b\u103a", r"oo", text) # ‌ော်
        text = re.sub(r"\u1031\u102c\u103a", r"oo", text) # ‌ပေ်
        # Romanization conversion
        for burmese_char, roman_char in sorted(burmese_to_roman.items(), key=lambda x: len(x[0]), reverse=True):
            text = text.replace(burmese_char, roman_char)

        # Clean-up
        text = re.sub(r' ,', ",", text)
        return text

text_input = st.text_input("Burmese to Romanization")

st.write("Romanization output: ", burmese_to_romanize(text_input))