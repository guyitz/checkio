def find_message(text):
    return filter(lambda x: x.isupper(), text)


assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
assert find_message("hello world!") == ""
