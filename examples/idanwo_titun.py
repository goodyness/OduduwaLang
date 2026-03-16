#!/usr/bin/env python3
# Built with OduduwaLang

import oduduwa.stdlib.isiro as isiro
nomba1 = 10
nomba2 = 20
nomba3 = 30
apapo = isiro.apapo([nomba1, nomba2, nomba3])
iwon = isiro.iwon([nomba1, nomba2, nomba3])
print(f'Nọ́mbà wa ni: {nomba1}, {nomba2}, {nomba3}')
print(f'Àpapọ̀ wọn jẹ́: {apapo}')
print(f'Ìwọ̀n wọn jẹ́: {iwon}')
print(f'2 ni agbára 3 jẹ: {isiro.agbara(2, 3)}')
print(f'Gbere square 16 jẹ: {isiro.gbere_square(16)}')