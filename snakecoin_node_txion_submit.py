from flask import Flask
from flask import request

node = Flask(__name__)

# Store the transactions that this node has in the list
thisNodeTransactions = []

@node.route('/txion', methods=['POST'])
def transactions():
  if request.method == 'POST':
    # On each new POST request we extract the transaction data
    newTxion = request.get_json()

    # Then we add transaction to our list
    thisNodeTransactions.append(newTxion)

    # Because the transaction was successfully added we log it on the console
    print "New Transaction"
    print "FROM: {}" . format(newTxion['from'])
    print "TO: {}" . format(newTxion['to'])
    print "AMOUNT: {}\n" . format(newTxion['amount'])

    # Then we let client know it worked out
    return "Transaction submission successful\n"

node.run()