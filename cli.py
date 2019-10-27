import argparse

import base58

import utils
from pow import Pow
from blockchain import Blockchain



def new_parser():
    parser = argparse.ArgumentParser()
    sub_parser = parser.add_subparsers(help='commands')
    # A print command
    print_parser = sub_parser.add_parser(
        'print', help='Print all the blocks of the blockchain')
    print_parser.add_argument('--print', dest='print', action='store_true')
    # A getbalance command
    balance_parser = sub_parser.add_parser(
        'getbalance', help='Get balance of ADDRESS')
    balance_parser.add_argument(
        '--address', type=str, dest='balance_address', help='ADDRESS of balance')
    # A createblockchain command
    bc_parser = sub_parser.add_parser(
        'createblockchain', help='Create a blockchain and send genesis block reward to ADDRESS')
    bc_parser.add_argument(
        '--address', type=str, dest='blockchain_address', help='ADDRESS')

    return parser

def create_blockchain(address):
    bc = Blockchain(address)
    # utxo_set = UTXOSet(bc)
    # utxo_set.reindex()

    print('Done!')


def print_chain():
    print ('Print Chain Start!')
    bc = Blockchain()

    for block in bc.blocks:
        print("Prev. hash: {0}".format(block.prev_block_hash))
        print("Hash: {0}".format(block.hash))
        pow = Pow(block)
        print("PoW: {0}".format(pow.validate()))

    print (len(list(bc.blocks) ) )
    
    


# def send(from_addr, to_addr, amount):
#     bc = Blockchain()
#     utxo_set = UTXOSet(bc)

#     tx = UTXOTx(from_addr, to_addr, amount, utxo_set)
#     cb_tx = CoinbaseTx(from_addr)
#     new_block = bc.MineBlock([cb_tx, tx])
#     utxo_set.update(new_block)
#     print('Success!')


if __name__ == '__main__':
    parser = new_parser()
    args = parser.parse_args()

    # if hasattr(args, 'wallet'):
    #     create_wallet()

    if hasattr(args, 'print'):
        print_chain()

    # if hasattr(args, 'balance_address'):
    #     get_balance(args.balance_address)

    if hasattr(args, 'blockchain_address'):
        create_blockchain(args.blockchain_address)

    # if hasattr(args, 'send_from') and \
    #         hasattr(args, 'send_to') and \
    #         hasattr(args, 'send_amount'):
    #     send(args.send_from, args.send_to, args.send_amount)


# command
"""
python cli.py print
python cli.py createwallet
python cli.py getbalance --address 1M2ZZAUWTzG6ocih4N2Yzr6D9B8bFj1XMy
python cli.py createblockchain --address 1X82i8GAzpSREp1pNLb6KzM9qZq1pjfbD 
python cli.py send --from 1X82i8GAzpSREp1pNLb6KzM9qZq1pjfbD --to 1M2ZZAUWTzG6ocih4N2Yzr6D9B8bFj1XMy --amount 6
python cli.py send --from 1JPHXxrL5kr849MHxkkQoeQGZ2ednqoMFy --to 1LzyZCn7QNNnKuafrdd7AtZVjnHQKzCmc8 --amount 4
"""
