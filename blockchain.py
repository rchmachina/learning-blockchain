import sys
import hashlib
import json 

from time import time
from uuid import UUID

from flask import Flask
from flask.globals import request
from flask.json import jsonify

import requests
from urllib.parse import urlparse

class Blockchain(object):
    difficultyTarget = "0000"
    def hash_block(self,block):
        block_encoded =json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()
    
    def __init__(self):
        self.chain=[]
        self.currentTransaction = []

        genesisHash = self.hash_block("genesisBlock")

        self.appendBlock(
            hashOfPreviousBlock = genesisHash,
            nonce = self.proofOfWork(0,genesisHash, [])
        )
    def ProofOfWork(self,index,hashOfPreviousBlock,transactions,nonce):
        nonce = 0
        
        while self.valid_proof(index,hashOfPreviousBlock,transactions,nonce) is False:
            nonce += 1
        return nonce
    
    def validProof(self,index,hashOfPreviousBlock,transactions,nonce):
        content = f'{index}{hashOfPreviousBlock}{transactions}{nonce}'.encode()

        contentHash = hashlib.sha256(content).hexdigest()

        return contentHash[:len(self.difficultyTarget)]== self.difficultyTarget 

        