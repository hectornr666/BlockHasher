import hashlib
import json
import datetime
from datetime import datetime

reward = 10.0
genesis_block = {

   'previous_hash': '',
   'index': 0,
   'transaction': [],
   'nonce': 23

}

blockchain = [genesis_block]
open_transactions = []
owner = 'Blockgeeks'

def hash_block(block):
   return hashlib.sha256(json.dumps(block).encode()).hexdigest()

def valid_proof(transactions, last_hash, nonce):
   guess = (str(transactions) + str(last_hash) + str(nonce)).encode()
   guess_hash = hashlib.sha256(guess).hexdigest()
   print("LAST BLOCK:" + str(last_hash) + " GUESSED[" + str(nonce) + "] " + guess_hash)
   return guess_hash[0:6] == '0001'

def pow():
   last_block = blockchain[-1]
   last_hash = hash_block(last_block)
   nonce = 0
   #print("LAST BLOCK:" + str(last_block) + "\nHASHED:" + str(last_hash) + "\nNONCE:" + str(nonce))


   while not valid_proof(open_transactions, last_hash, nonce):
       nonce += 1
   print ("found nonce" + str(nonce))
   return nonce

def get_last_value():
   """ extracting the last element of the blockchain list """
   return(blockchain[-1])

def add_value(recipient, sender=owner, amount=1.0):
   transaction = {'sender': sender,
   'recipient': recipient,
   'amount': amount}
   open_transactions.append(transaction)

def mine_block():
   last_block = blockchain[-1]
   hashed_block = hash_block(last_block)
   tstart = datetime.now()
   nonce = pow()
   print("running time: " + str(datetime.now() - tstart) + " seconds")
   reward_transaction = {
           'sender': 'MINING',
           'recipient': owner,
           'amount': reward
       }

   open_transactions.append(reward_transaction)
   block = {
       'previous_hash': hashed_block,
       'index': len(blockchain),
       'transaction': open_transactions,
       'nonce': nonce
   }

   blockchain.append(block)
   open_transactions.clear()

def get_transaction_value():
      tx_recipient = input('Enter the recipient of the transaction: ')
      tx_amount = float(input('Enter your transaction amount '))
      return tx_recipient, tx_amount

def get_user_choice():
      user_input = input("Please give your choice here: ")
      return user_input

def print_block():
      for block in blockchain:
         print("Here is your block")
         print(block)

while True:
   print("Choose an option")
   print('Choose 1 for adding a new transaction')
   print('Choose 2 for mining a new block')
   print('Choose 3 for printing the blockchain')
   print('Choose 4 for printing open transitions')
   print('Choose anything else if you want to quit')

   user_choice = get_user_choice()

   if user_choice == "1":
      tx_data = get_transaction_value()
      recipient, amount = tx_data
      add_value(recipient, amount=amount)
      print(open_transactions)

   elif user_choice == "2":
      mine_block()

   elif user_choice == "3":
      print_block()

   elif user_choice == "4":
      print(open_transactions)

   else:
      break