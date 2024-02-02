import pyperclip
change_list = {
    "a": "λ", 
    "b": "β", 
    "y": "γ",
    "n": "η",
    "u": "μ",
    "A": "Λ",
    "o": "θ",
    "e": "ε",
    "p": "ρ",
    "x": "χ",
    "t": "τ",
    "k": "κ",
    "O": "Θ",
    "E": "Σ",
    "l": "ι"
}
i = 0
assembled_string = ""
while True:
    inp = input("string: ")
    for _ in range(len(inp)):
        try: new_char = change_list[inp[i]]
        except KeyError: new_char = inp[i]
        assembled_string += new_char
        i += 1
    print(assembled_string)
    pyperclip.copy(assembled_string)
    assembled_string = ""
    i = 0