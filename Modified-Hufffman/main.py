from Huffman import (
    read_input_file,
    save_compressed_file,
    read_compressed_file,
    save_decompressed_file,
)

import Compression
import Decompression


def main():
    min_limit = float(input("Enter Minimum Probability Limit (default 0.05): ") or 0.05)
    input_txt = "files/input.txt"
    compressed_bin = "compressed.bin"
    decompressed_txt = "decompressed.txt"

    while True:
        print("\n===== Modified Huffman =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = "".join(read_input_file(input_txt).split())
            bitstring, huffman_codes, others_code_map = (
                Compression.compression(text, min_limit)
            )
            save_compressed_file(
                bitstring,
                huffman_codes,
                others_code_map,
                compressed_bin,
            )
            print("Compressed and saved to binary file successfully!")
        elif choice == "2":
            bitstring, header = read_compressed_file(compressed_bin)

            decoded_text = Decompression.decompress(
                bitstring,
                header["huffman_codes"],
                header["others_code_map"],
            )

            save_decompressed_file(decoded_text, decompressed_txt)

            print("Decompressed and saved to text file successfully!")

        elif choice == "3":
            print("Goodbye!💗")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()