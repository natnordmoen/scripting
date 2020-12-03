#!/usr/bin/env python

import random

def spre_juleglede():
    avsendere = ['Natalia', 'Torstein', 'Thorstein', 'Munkvold', 'Mr T', 'Christian', 'Christine', 'Benedictus', 'Bente', 'Merete', 'Edward', 'Rolf']
    mottakere = ['Bobby', 'Rune', 'Ståle', 'Isaac', 'Simen', 'Hanna']

    random.shuffle(avsendere)
    random.shuffle(mottakere)

    print(list(zip(avsendere, mottakere)))


spre_juleglede()