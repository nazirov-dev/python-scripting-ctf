#!/usr/bin/python3

def prinFlag():
    import base64

    decoded_data = base64.b64decode("UFlUSE9Oe1FhbmRheV9xaWxpYl91bmlfaWNoa2FyaWdhX29saXNofQ==")
    return (decoded_data.decode('utf-8'))
