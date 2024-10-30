# Liquidity-Pool-Management
# Project: DeFi Liquidity API with FastAPI and Hardhat

## Project Overview
This project aims to create a backend API for interacting with a decentralized finance (DeFi) liquidity pool. Using FastAPI and Web3.py, we connect to a local Ethereum-compatible blockchain (using Hardhat), allowing users to perform and test liquidity-related actions like adding funds to a liquidity pool. The setup is designed to enable testing and integration with blockchain-based applications in a controlled local environment.

## Objective
The primary goal of this project is to create a set of backend endpoints to:

1- Connect to a test blockchain (local Hardhat network).<br>
2- Add liquidity to a simulated liquidity pool.<br>
3- Retrieve transaction details and ensure blockchain interactions are successful.<br>

## Libraries and Dependencies
The project requires Python 3.9 or 3.10 and these Python libraries:

***FastAPI***  pip install fastapi<br>
***Uvicorn*** (ASGI server for FastAPI): pip install uvicorn<br>
***Web3.py*** (Python library for blockchain interactions): pip install web3<br>

For the blockchain environment:

***Hardhat*** npm install --save-dev hardhat<br>

## Hardhat for a Local Blockchain

1- Initialize Hardhat: npx hardhat<br>
Choose “Create a JavaScript project” and follow the prompts to set up a basic Hardhat environment.<br>

2- Start the Hardhat Node: npx hardhat node<br>

## Configure FastAPI and Web3.py
I created main.py file in a local folder using VS Code and I already created an environment (in my case a conda environment) with Python 3.12.2.

## Run the FastAPI Server
In terminal, run: uvicorn main:app --reload<br>
It should show the following address: http://127.0.0.1:8000

## Test the API
1- Access the API Documentation: http://127.0.0.1:8000/docs<br>

2- Test the /add_liquidity Endpoint, by Try Out, for example using:<br>
user_id: A user identifier (e.g., "user1234")<br>
token_a_amount: Amount of token A to add to liquidity<br>
token_b_amount: Amount of token B to add to liquidity<br>

3- Expected response: A successful response should return a JSON object with the transaction details, including transaction_id and status.



