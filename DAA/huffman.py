import heapq

# Create a Node class
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None

    # Compare nodes by frequency
    def __lt__(self, other):
        return self.freq < other.freq

# Generate Huffman codes
def generate_codes(root, code=""):
    if root is None:
        return

    if root.char is not None:
        print(root.char, ":", code if code else "0")
        return

    generate_codes(root.left, code + "0")
    generate_codes(root.right, code + "1")

# Accept user input
n = int(input("Enter no. of Characters:"))
heap = []

for i in range(n):
    char = input("Enter Character:")
    freq = int(input("Enter Frequency:"))
    heapq.heappush(heap, Node(char, freq))

# Build Huffman Tree
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    new_node = Node(None, left.freq + right.freq)
    new_node.left = left
    new_node.right = right

    heapq.heappush(heap, new_node)

# Display Huffman codes
print("\nHuffman Codes:")
generate_codes(heap[0])