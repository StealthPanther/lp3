import heapq

# Create a node
class Node:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


# Print Huffman codes
def printCodes(root, code):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.ch, ":", code if code else "0")
        return

    printCodes(root.left, code + "0")
    printCodes(root.right, code + "1")


# Main program
n = int(input("Enter number of characters: "))

if n <= 0:
    print("Number of characters must be positive.")

else:
    minHeap = []

    print("Enter each character and its frequency:")

    for i in range(n):
        ch, freq = input().split()
        freq = int(freq)

        heapq.heappush(minHeap, Node(ch, freq))

    # Build Huffman Tree
    while len(minHeap) > 1:

        left = heapq.heappop(minHeap)
        right = heapq.heappop(minHeap)

        parent = Node('$', left.freq + right.freq)
        parent.left = left
        parent.right = right

        heapq.heappush(minHeap, parent)

    print("\nHuffman Codes:")
    printCodes(minHeap[0], "")