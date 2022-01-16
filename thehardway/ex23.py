import sys
script,input_encoding,error = sys.argv

def main (languages,encoding,errors):
    line = languages.read()
    if line:
        print_line(line,encoding,errors)
        return main(languages,encoding,errors)

def print_line(line,encoding,errors):
    next_lang=line.script()
    raw_bytes=next_lang.encode(encoding,errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes,"<===>",cooked_string)
languages = open("languages.txt", encoding="utf-8")


main(languages,input_encoding,error)


