# OduduwaLang Grammar Reference

## Keywords (Kókó Ọ̀rọ̀)
- `ise`: Define a function (`def`)
- `pada`: Return from a function (`return`)
- `ti`: If statement (`if`)
- `si_ti`: Else If statement (`elif`)
- `tabi`: Else If statement (`elif`) [Alias for `si_ti`]
- `bibeeko`: Else statement (`else`)
- `fun`: For loop (`for`)
- `nigbati`: While loop (`while`)
- `tejade`: Print to console (`print()`)
- `gba_wole`: Input from user (`input()`)
- `sotito`: Boolean `True`
- `seke`: Boolean `False`
- `ofo`: Null value `None`

## Variables & Assignments
Variables are declared similarly to Python, using `=`.
```oduduwa
oruko = "Ade"
odun = 20
```

### Formatted Strings (f-strings)
You can embed expressions inside string literals using curly braces:
```oduduwa
tejade(f"Oruko mi ni {oruko}")
```

## Conditionals (Tí)
```oduduwa
ti odun < 13:
    tejade("O je omode.")
tabi odun < 20:
    tejade("O je odo.")
bibeeko:
    tejade("O je agbalagba.")
```

## Loops (Yíká)

### For Loop (`fun`)
Iterate from a number to another using `lati` (from) and `de` (to).
```oduduwa
fun i lati 1 de 5:
    tejade("Nọmba: ", i)
```

### While Loop (`nigbati`)
```oduduwa
i = 0
nigbati i < 5:
    tejade("A si n ka:", i)
    i = i + 1
```

## Data Structures (Ètò Ẹ̀kọ́ Kòkárilẹ̀)

### Lists (Àwọn Àkójọ)
```oduduwa
akeko = ["Bolu", "Seyi", "Dayo"]
```

### Dictionaries (Iwe-itumọ)
```oduduwa
oluko = {
    "oruko": "Adejoke",
    "ipo": "Olori Edu"
}
```

## Standard Library (Àkójọ́pọ̀ Kíni)
OduduwaLang provides localized stdlib implementations that map tightly to Python's capabilities.
```oduduwa
mu_wole isiro
mu_wole akoko
mu_wole onka

tejade(isiro.apapo([1, 2, 3])) # 6
tejade(onka.yipada(100)) # "ọgọ́rùn-ún kan le"
```

## Object-Oriented Programming
```oduduwa
egbe Eniyan:
    ise __ibere__(ara, oruko):
        ara.oruko = oruko
```

## Error Handling
```oduduwa
gbiyanju:
    # eléwù (risky code)
mu_asise:
    # a mu asise na (error caught)
ni_ipari:
    # ohun to gbodo sele (always executes)
```
