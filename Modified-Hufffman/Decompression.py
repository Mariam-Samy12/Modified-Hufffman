#Decompression Function
def decompress(compressed_code, codes, orignal_code):
    reverse_codes = {}
    for x in codes:
        reverse_codes[codes[x]] = x
    reverse_orignal_code = {}
    for y in orignal_code:
        reverse_orignal_code[orignal_code[y]] = y

    current = ""
    result = ""
    i = 0

    if orignal_code:
        width = len(list(orignal_code.values())[0])
    else:
        width = 0

    while (i < len(compressed_code)):

        current = current + compressed_code[i]
        i = i + 1
        if "others" in codes and current == codes["others"]:
            orignal_bits = compressed_code[i:i + width]
            result = result + reverse_orignal_code[orignal_bits]
            current = ""
            i = i + width

        elif current in reverse_codes:
            result = result + reverse_codes[current]
            current = ""

    return result