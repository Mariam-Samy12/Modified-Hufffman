import heapq
class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.probability < other.probability


def compression(text, Minimum_Probability_Limit):
    if not text:
        return "", {}, {}

    distinct_chars = sorted(set(text))
    bits = max(1, (len(distinct_chars) - 1).bit_length())

    original_codes = {
        char: format(index, f"0{bits}b")
        for index, char in enumerate(distinct_chars)
    }

    # Calculate probabilities
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    probabilities = {
        char: count / len(text)
        for char, count in freq.items()
    }

    others = {}
    normal_symbols = {}

    for char, probability in probabilities.items():
        if probability <= Minimum_Probability_Limit:
            others[char] = probability
        else:
            normal_symbols[char] = probability

    # Create Huffman nodes
    nodes = [
        Node(char, probability)
        for char, probability in normal_symbols.items()
    ]

    if others:
        nodes.append(Node("others", sum(others.values())))

    heapq.heapify(nodes)

    def create_parent(left, right):
        parent = Node(
            left.symbol + right.symbol,
            left.probability + right.probability
        )
        parent.left = left
        parent.right = right
        return parent

    # Keep two nodes
    while len(nodes) > 2:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        heapq.heappush(nodes, create_parent(left, right))

    huffman_codes = {}

    def generate_codes(node, current_code):
        if node.left is None and node.right is None:
            huffman_codes[node.symbol] = current_code or "0"
            return

        if node.left:
            generate_codes(node.left, current_code + "1")

        if node.right:
            generate_codes(node.right, current_code + "0")


    if len(nodes) == 2:
        generate_codes(nodes[0], "1")
        generate_codes(nodes[1], "0")


    others_code_map = {
        char: original_codes[char]
        for char in others
    }

    # Build the compressed bitstring
    compressed_text = ""

    for char in text:
        if char in others:
            compressed_text += (
                huffman_codes["others"] + original_codes[char]
            )
        else:
            compressed_text += huffman_codes[char]

    return compressed_text, huffman_codes, others_code_map
