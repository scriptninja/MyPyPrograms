def border_sentence(sentence, border="#"):
    width = 4 + len(sentence)
    print(f"{border * width}")
    print(f"{border} {sentence} {border}")
    print(f"{border * width}")

border_sentence("Hello, World!")
