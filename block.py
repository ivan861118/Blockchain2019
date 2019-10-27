import time
import hashlib
import binascii
import pickle

import utils
from pow import Pow

def NewGnesisBlock():
    return NewBlock("創世區塊啦",'',0)


def NewBlock(transaction, prev_block_hash, prev_height):
    block = Block(transaction, prev_block_hash, prev_height)
    return block

class Block(object):
    """ Represents a new Block object.
    Args:
        transaction_lst (list): List of transaction.
        prev_block_hash (string): Hash of the previous Block. 
    Attributes:
        _timestamp (bytes): Creation timestamp of Block.
        _tx_lst (list): List of transaction.
        _prev_block_hash (bytes): Hash of the previous Block.
        _hash (bytes): Hash of the current Block.
        _nonce (int): A 32 bit arbitrary random number that is typically used once.
    """

    def __init__(self, transaction_lst=[], prev_block_hash='', prev_block_height=0):
        self._height = prev_block_height + 1
        self._prev_block_hash = utils.encode(prev_block_hash)
        self._timestamp = utils.encode(str(int(time.time())))
        self._bits = None
        self._nonce = None
        self._hash = None
        self._tx_lst = transaction_lst

        
        
    ## Define representation during "print()"
    def __repr__(self):
        return 'Block(timestamp={0!r}, tx_lst={1!r}, prev_block_hash={2!r}, height={3!r}, hash={4!r}, nonce={4!r})'.format(
            self._timestamp, self._tx_lst, self._prev_block_hash, self._height, self._hash, self._nonce)

    @property
    def height(self):
        return self._height

    @property
    def hash(self):
        return utils.decode(self._hash)
    
    @property
    def prev_block_hash(self):
        return utils.decode(self._prev_block_hash)

    @property
    def timestamp(self):
        return str(self._timestamp)

    @property
    def nonce(self):
        return str(self._nonce)

    @property
    def transactions(self):
        return self._tx_lst

    def pow_of_block(self):
        # Makes the proof of work of the current Block
        pow = Pow(self)
        nonce, hash = pow.run()
        self._nonce, self._hash = nonce, utils.encode(hash)
        return self

    def serialize(self):
        # serializes the block
        return pickle.dumps(self)

    def deserialize(self, data):
        """
        Deserializes the block.
        :param `bytes` data: The serialized data.
        :return: A Block object.
        :rtype: Block object.
        """
        return pickle.loads(data)


