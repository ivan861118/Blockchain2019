from block import Block, NewBlock, NewGnesisBlock
import hashlib

def main():
    #=== Hash 
    string = "hello".encode()
    x = hashlib.sha256(string).hexdigest()
    # print(x)
    #=== Block 
    # block = Block([],x)
    # print(block)

    #=== NewBlock 
    gBlock = NewGnesisBlock()
    new_block = NewBlock("fuck you",x,5)
    print(gBlock)
    print(new_block)

if __name__ == "__main__":
    main()
