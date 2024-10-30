from fastapi import FastAPI
from pydantic import BaseModel
from web3 import Web3

app = FastAPI()

# Connect to the local Ganache blockchain
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

if w3.is_connected():
    print("Connected to the Hardhat blockchain!")
else:
    print("Failed to connect to the blockchain.")



# Define the request body structure for adding liquidity
class LiquidityRequest(BaseModel):
    user_id: str
    token_a_amount: float
    token_b_amount: float


@app.post("/add_liquidity")
async def add_liquidity(request: LiquidityRequest):
    # Use Account #0 from Hardhat accounts
    sender_address = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
    private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
    # Build a transaction: The transaction sends an amount equal to token_a_amount + token_b_amount (converted to wei).
    tx = {
        "from": sender_address,
        "to": "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",  # Example recipient from Hardhat accountss
        "value": w3.to_wei(request.token_a_amount + request.token_b_amount, "ether"),
        "gas": 21000,
        "gasPrice": w3.to_wei("50", "gwei"),
        "nonce": w3.eth.get_transaction_count(sender_address),
    }

    # Sign and send the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    response = {
        "message": f"Added liquidity for user {request.user_id}",
        "token_a_amount": request.token_a_amount,
        "token_b_amount": request.token_b_amount,
        "transaction_id": tx_hash.hex(),
        "status": tx_receipt.status,
    }
    return response
