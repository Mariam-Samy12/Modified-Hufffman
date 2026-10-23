from Files_handling import (
    read_input_file,
    save_compressed_file,
    read_compressed_file,
    save_decompressed_file,
    save_compressed_text
)
from Compression import compression
from Decompression import decompress


def main():
    
    while True:
        
        print("\n===== Modified Huffman =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ")
        try:
           if choice == "1":
                min_limit = float(input("Enter Minimum Probability Limit (default 0.05): ") or 0.05)
                input_txt=input("Enter the name of the text file to compress (e.g. input.txt): ")
                text = "".join(read_input_file(input_txt).split())
                bitstring, huffman_codes, others_code_map = (
                    compression(text, min_limit)
                )
                text_file = input("Enter a name for the compressed file (e.g. compressed.bin): ")
                save_compressed_file(
                    bitstring,
                    huffman_codes,
                    others_code_map,
                    text_file,
                )
                showtext=input("Enter a name for the text file (e.g. compressed.txt):")
                save_compressed_text(bitstring, showtext)
                print("Compressed and saved to binary file successfully!")
           elif choice == "2":
                compressed_bin = input("Enter the name of the compressed file (e.g. compressed.bin): ")
                bitstring, header = read_compressed_file(compressed_bin)

                decoded_text = decompress(
                    bitstring,
                    header["huffman_codes"],
                    header["others_code_map"],
                )
                decompressed_txt = input("Enter a name for the output text file (e.g. decompressed.txt): ")
                save_decompressed_file(decoded_text, decompressed_txt)
                print("Decompressed and saved to text file successfully!")

           elif choice == "3":
                print("Goodbye!💗")
                break
           else:
               print("Invalid choice!")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    main()