from Huffman import (
    read_input_file,
    save_compressed_file,
    read_compressed_file,
    save_decompressed_file,
    # حطوا الباقي بقي 
)
#decompress input
# codes={
#     'a':'00',
#     'b':'011',
#     'c':'010',
#     'd':'11',
#     'others':'10'
# }

# orignal_code={
#     'a': '0000',
#     'b': '0001',
#     'c' :'0010',
#     'd': '0011',
#     'f' :'0100',
#     'p' :'0101',
#     'q' :'0110',
#     'u' :'0111',
#     'z' :'1000'
# }

# compressed_code='000110100010100011001001000101001101100110101001110001100100101100011'





def main():
    min_limit = float(input() or 0.05)
    input_txt = "input.txt"
    compressed_bin = "compressed.bin"
    decompressed_txt = "decompressed.txt"

    while True:
        print("\n===== Modified Huffman =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = read_input_file(input_txt)
             #😼passحطي يا رنا الكلاس بتاعك و شيلي
            
            # save_compressed_file(
            #     bitstring,
            #     huffman_codes,
            #     others_map,
            #     compressed_bin,
            # )
            print("Compressed and saved to binary file successfully!")
            
            pass

        elif choice == "2":
             bitstring, header = read_compressed_file(compressed_bin)
            # x=HuffmanDecompression()
            # result=x.decompress(compressed_code,codes,orignal_code)
            # print(result)
             decoded_text = "abc"  # نص مؤقت للتجربة
             save_decompressed_file(decoded_text, decompressed_txt)
             print("Decompressed and saved to text file successfully!")
             pass

        elif choice == "3":
            print("Goodbye!💗")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()