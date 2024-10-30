# Liquidity-Pool-Management
# Project: DeFi Liquidity API with FastAPI and Hardhat

## Project Overview
This project aims to create a backend API for interacting with a decentralized finance (DeFi) liquidity pool. Using FastAPI and Web3.py, we connect to a local Ethereum-compatible blockchain (using Hardhat), allowing users to perform and test liquidity-related actions like adding funds to a liquidity pool. The setup is designed to enable testing and integration with blockchain-based applications in a controlled local environment.

## Objective
The primary goal of this project is to create a set of backend endpoints to:

1- Connect to a test blockchain (local Hardhat network).
2- Add liquidity to a simulated liquidity pool.
3- Retrieve transaction details and ensure blockchain interactions are successful.

## Libraries and Dependencies
The project requires Python 3.9 or 3.10 and these Python libraries:

FastAPI: pip install fastapi
Uvicorn (ASGI server for FastAPI): pip install uvicorn
Web3.py (Python library for blockchain interactions): pip install web3
