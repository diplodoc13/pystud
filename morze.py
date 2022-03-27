def eng_to_morze(txt: str) -> object:
    res = ""
    for char in txt:
        for key, value in d.items():
            if char.upper() == key:
                res += value + " "
    return res


letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
         '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
         '...--', '....-', '.....', '-....', '--...', '---..', '----.']
d = dict(zip(letters, morse))

text = "Interstellar"
print(eng_to_morze(text))
