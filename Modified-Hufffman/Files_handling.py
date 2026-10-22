import json

def read_input_file(filepath="input.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def save_compressed_file(bitstring, huffman_codes, others_code_map, output_bin_path="compressed.bin"):
    extra_padding = (8 - len(bitstring) % 8) % 8
    bitstring += "0" * extra_padding

    byte_array = bytearray()
    for i in range(0, len(bitstring), 8):
        byte_array.append(int(bitstring[i : i + 8], 2))

    header = {
        "huffman_codes": huffman_codes,
        "others_code_map": others_code_map,
        "padding": extra_padding
    }
    header_bytes = json.dumps(header).encode("utf-8")

    with open(output_bin_path, "wb") as f:
        f.write(len(header_bytes).to_bytes(4, byteorder="big"))
        f.write(header_bytes)
        f.write(byte_array)


def save_compressed_text(bitstring, output_txt_path="compressed.txt"):
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(bitstring)

def read_compressed_file(input_bin_path="compressed.bin"):
    with open(input_bin_path, "rb") as f:
        header_length = int.from_bytes(f.read(4), byteorder="big")
        header = json.loads(f.read(header_length).decode("utf-8"))
        compressed_bytes = f.read()

    bitstring = "".join(f"{byte:08b}" for byte in compressed_bytes)
    
    if header["padding"] > 0:
        bitstring = bitstring[:-header["padding"]]

    return bitstring, header


def save_decompressed_file(decoded_text, output_txt_path="decompressed.txt"):
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(decoded_text)




                

        

            






