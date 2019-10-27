from block import Block, NewBlock, NewGnesisBlock
# from blockchain import Blockchain
import hashlib

def main():
    #=== Hash 
    string = "hello".encode()
    msg = hashlib.sha256(string).hexdigest()
    # print(x)
    #=== Block 
    # block = Block([],x)
    # print(block)

    #=== NewBlock 
    gBlock = NewGnesisBlock()
    new_block = NewBlock("fuck you", msg, 5)
    print(gBlock)
    print(new_block)

if __name__ == "__main__":
    main()
