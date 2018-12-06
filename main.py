import base64
import binascii
import codecs


if __name__ == "__main__":
    words = input()
    if not words:
        print("you should input something....")
        exit(1)

    matched = []
    print("=================  Base64  =================")
    try:
        print(f"| Base64(Byte): {base64.b64decode(words)}")
        print(f"| Base64(UTF-8): {base64.b64decode(words).decode(encoding='utf-8')}")
    except binascii.Error as e:
        print("| Base64: ERROR..")

    print("\n=================  ROT  =================")
    try:
        print(f"| ROT13: {codecs.decode(words, 'rot13')}")
    except TypeError as e:
        print("| ROT13: ERROR...")
    try:
        print(f"| Base64(UTF-8) -> ROT13: {codecs.decode(base64.b64decode(words))}")
    except:
        print("| Base64(UTF-8) -> ROT13: ERROR...")

    print("\n=================  Base58  =================")
    try:
        print(f"| Base58(Byte): {base64.b85decode(words)}")
        print(f"| Base58(UTF-8): {base64.b58decode(words).decode(encoding='utf-8')}")
    except:
        print("| Base58: ERROR..")
