def Button(text:str, css_strings: list[str])->str:
    css_string = ", ".join(css_strings)
    return f'<button style="{css_string}">{text}</button>'

if __name__ == "__main__":
    print(Button("Hello Samuel", ["color:red", "font-size:40px"]))
