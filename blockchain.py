import sys
import pickle

from block import Block, NewGnesisBlock, NewBlock
from db import Bucket



class Blockchain(object):
    """ Blockchain keeps a sequence of Blocks
    Attributes:
        _tip (bytes): Point to the latest hash of block.
        _bucket (dict): bucket of DB 
    """
    latest = 'l'
    db_file = 'blockchain.db'
    block_bucket = 'blocks'
    genesis_coinbase_data = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks'

    def __init__(self, address=None):
        self._bucket = Bucket(Blockchain.db_file, Blockchain.block_bucket)
        try:
            self._tip = self._bucket.get('l')
        except KeyError:
            genesis = NewGnesisBlock().pow_of_block()
            self._block_put(genesis)
            # if not address:
            #     self._tip = None
            # else:
            #     genesis = NewGnesisBlock().pow_of_block()
            #     self._block_put(genesis)


    def _block_put(self, block):
        self._bucket.put(block.hash, block.serialize())
        self._bucket.put('l', block.hash)
        self._tip = block.hash
        self._bucket.commit()

    @property
    def blocks(self):
        current_tip = self._tip
        while True:
            if not current_tip:
                # Encounter genesis block
                raise StopIteration
            encoded_block = self._bucket.get(current_tip)
            block = pickle.loads(encoded_block)
            yield block
            current_tip = block.prev_block_hash
    
    @property
    def length(self):
        return len(list(self.blocks))
