# OduduwaLang Grammar Reference

## Keywords (Kókó Ọ̀rọ̀)
- `ise`: Define a function (`def`)
- `pada`: Return from a function (`return`)
- `ti`: If statement (`if`)
- `si_ti`: Else If statement (`elif`)
- `bibeeko`: Else statement (`else`)
- `fun`: For loop (`for`)
- `nigbati`: While loop (`while`)
- `tejade`: Print to console (`print()`)
- `sotito`: Boolean `True`
- `seke`: Boolean `False`
- `ofo`: Null value `None`

## Variables & Assignments
Variables are declared similarly to Python, using `=`.
```oduduwa
oruko = "Ade"
odun = 20
```

## Conditionals (Tí)
```oduduwa
ti odun > 18:
    tejade("O to lati se idibo!")
bibeeko:
    tejade("O ti kere ju.")
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
OduduwaLang provides localized stdlib implementations.
Example Math (`iro`):
```oduduwa
abajade = iro.gbongbo(16)
tejade("Gbongbo 16 je: ", abajade)
```
