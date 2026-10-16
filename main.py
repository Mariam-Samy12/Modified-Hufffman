from Huffman import *
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
    while True:
        print("\n===== Modified Huffman =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
             #😼passحطي يا رنا الكلاس بتاعك و شيلي
            pass

        elif choice == "2":
            # x=HuffmanDecompression()
            # result=x.decompress(compressed_code,codes,orignal_code)
            # print(result)
             pass

        elif choice == "3":
            print("Goodbye!💗")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()