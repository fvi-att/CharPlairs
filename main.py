import base64


if __name__ == "__main__":
    words = input()
    if not words:
        print("you should input something....")
        exit(1)

    # Base64
    print(f"Base64(Byte): {base64.b64decode(words)}")
    print(f"Base64(UTF-8): {base64.b64decode(words).decode(encoding='utf-8')}")
