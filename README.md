# 🛡️ CodeVeritas - AI-Powered Blockchain Code Attestation

**Zero-Trust Code Signing Pipeline with AI Security Analysis + Blockchain Proof**

[![CI/CD](https://github.com/yourusername/codeveritas/workflows/CI/badge.svg)](https://github.com/yourusername/codeveritas/actions)
[![Security](https://img.shields.io/badge/security-blockchain%20verified-green)](https://etherscan.io/address/your-contract)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🚀 What It Does

CodeVeritas creates **cryptographic proof** that your code is secure before deployment:

1. **AI Analysis** - Scans commits for malicious patterns, vulnerabilities, policy violations
2. **Risk Scoring** - Assigns confidence scores based on multiple security factors  
3. **Blockchain Attestation** - Records immutable proof of analysis on Ethereum
4. **Deployment Gates** - Blocks risky code from reaching production

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/codeveritas.git
cd codeveritas

# Install dependencies
pip install -r requirements.txt
npm install

# Setup environment
cp .env.example .env
# Edit .env with your credentials

# Deploy smart contract (testnet)
npm run deploy-testnet

# Run analysis on current repo
python scripts/ai_security_analyzer.py --repo-path .
