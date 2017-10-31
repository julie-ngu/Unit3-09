# Created by: Julie Nguyen
# Created on: Oct 2017
# Created for: ICS3U
# This program prints out the alphabet and each letter of the alphabet beside it

import unicodedata

for capital_counter in range(65, 91):
    for lowercase_counter in range(97, 123):
        print unichr(capital_counter), unichr(lowercase_counter)
