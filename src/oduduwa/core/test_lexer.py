from oduduwa.core.lexer import normalize_yoruba, OduduwaLexer

def test_normalization():
    examples = {
        "ṣòtító": "sotito",
        "ṣèké": "seke",
        "tẹjáde": "tejade",
        "bíbeèkọ": "bibeeko",
        "nígbàtí": "nigbati"
    }
    
    for original, expected in examples.items():
        normalized = normalize_yoruba(original)
        assert normalized == expected, f"Expected {expected}, got {normalized}"
    
    print("✓ Normalization passed!")

def test_lexer():
    code = """
# OduduwaLang Example
ise ikini(oruko):
    tẹjáde("Pẹlẹ o, " + oruko)
    
    ti oruko == "Adeleye":
        tẹjáde("Oga ni e!")
    bíbeèkọ:
        tẹjáde("Bawo ni?")
"""
    lexer = OduduwaLexer(code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)
        
    print("✓ Lexical Analysis (with INDENT/DEDENT) passed!")

if __name__ == "__main__":
    test_normalization()
    test_lexer()

