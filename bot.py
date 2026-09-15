import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load token from environment variable (set on Railway)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


# ---------- Command Handlers ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Welcome to LearnCryptoNow_bot!\n\n"
        "I'm your crypto education assistant. Here's what I can do:\n\n"
        "/start - Show this welcome message\n"
        "/help - List all commands\n"
        "/about - About this bot\n"
        "/btc - What is Bitcoin?\n"
        "/eth - What is Ethereum?\n"
        "/blockchain - What is a blockchain?\n"
        "/wallet - What is a crypto wallet?\n"
        "/defi - What is DeFi?\n"
        "/nft - What is an NFT?\n"
        "/glossary - Common crypto terms\n"
        "/tips - Beginner safety tips"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Available commands:\n\n"
        "/start - Welcome message\n"
        "/help - This help menu\n"
        "/about - About this bot\n"
        "/btc - Bitcoin explained\n"
        "/eth - Ethereum explained\n"
        "/blockchain - Blockchain explained\n"
        "/wallet - Crypto wallets explained\n"
        "/defi - DeFi explained\n"
        "/nft - NFTs explained\n"
        "/glossary - Crypto glossary\n"
        "/tips - Safety tips"
    )


async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ About LearnCryptoNow_bot\n\n"
        "This bot provides free educational content about cryptocurrency "
        "and blockchain technology.\n\n"
        "⚠️ Disclaimer: This is NOT financial advice. "
        "Cryptocurrency is risky. Always do your own research (DYOR) "
        "and never invest more than you can afford to lose."
    )


async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "₿ What is Bitcoin?\n\n"
        "Bitcoin (BTC) is the first cryptocurrency, created in 2009 by "
        "the pseudonymous Satoshi Nakamoto.\n\n"
        "Key facts:\n"
        "• Decentralized — no bank or government controls it\n"
        "• Limited supply: only 21 million coins will ever exist\n"
        "• Uses Proof-of-Work mining to secure the network\n"
        "• Transactions are recorded on a public ledger (blockchain)\n\n"
        "Bitcoin is often called 'digital gold' because it is scarce "
        "and used as a store of value."
    )


async def eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Ξ What is Ethereum?\n\n"
        "Ethereum (ETH) is a decentralized blockchain launched in 2015 "
        "by Vitalik Buterin and others.\n\n"
        "Key facts:\n"
        "• Supports smart contracts — self-executing code\n"
        "• Native currency is Ether (ETH)\n"
        "• Powers DeFi, NFTs, DAOs, and dApps\n"
        "• Moved to Proof-of-Stake in 2022 (the 'Merge'), "
        "cutting energy use by ~99%\n\n"
        "Think of Ethereum as a 'world computer' anyone can build on."
    )


async def blockchain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 What is a Blockchain?\n\n"
        "A blockchain is a distributed, immutable digital ledger.\n\n"
        "How it works:\n"
        "• Transactions are grouped into 'blocks'\n"
        "• Each block links to the previous one via a hash\n"
        "• Thousands of computers (nodes) keep identical copies\n"
        "• Changing old data would require rewriting all later blocks\n\n"
        "This design makes blockchains transparent and extremely "
        "hard to tamper with."
    )


async def wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👛 What is a Crypto Wallet?\n\n"
        "A crypto wallet stores your private keys and lets you send "
        "and receive crypto.\n\n"
        "Types:\n"
        "• Hot wallets — connected to the internet (apps, browser)\n"
        "• Cold wallets — offline hardware devices (most secure)\n\n"
        "🔑 Golden rule: 'Not your keys, not your coins.'\n"
        "Whoever controls the private key controls the funds.\n\n"
        "Never share your seed phrase with anyone. Ever."
    )


async def defi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏦 What is DeFi?\n\n"
        "DeFi (Decentralized Finance) recreates financial services "
        "on blockchains without banks or middlemen.\n\n"
        "Common DeFi use cases:\n"
        "• Lending and borrowing\n"
        "• Decentralized exchanges (DEXs)\n"
        "• Stablecoins\n"
        "• Yield farming and staking\n\n"
        "⚠️ DeFi carries smart-contract risk, liquidation risk, "
        "and scam risk. Do your own research."
    )


async def nft(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🖼️ What is an NFT?\n\n"
        "NFT stands for Non-Fungible Token — a unique digital asset "
        "recorded on a blockchain.\n\n"
        "Key points:\n"
        "• Each NFT is one-of-a-kind (unlike Bitcoin, where each unit "
        "is identical)\n"
        "• Commonly used for digital art, collectibles, and game items\n"
        "• Ownership is verifiable on-chain\n\n"
        "Note: owning an NFT usually means owning a token that points "
        "to content — not always the copyright itself."
    )


async def glossary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 Crypto Glossary\n\n"
        "• DYOR — Do Your Own Research\n"
        "• HODL — Hold on for dear life\n"
        "• FOMO — Fear Of Missing Out\n"
        "• FUD — Fear, Uncertainty, Doubt\n"
        "• ATH — All-Time High\n"
        "• ATL — All-Time Low\n"
        "• Gas — Fee paid to process a transaction\n"
        "• Seed Phrase — 12/24 words that restore your wallet\n"
        "• Private Key — Secret code that controls your funds\n"
        "• Stablecoin — Crypto pegged to a stable asset (e.g., USD)\n"
        "• DEX — Decentralized Exchange\n"
        "• CEX — Centralized Exchange\n"
        "• Whitepaper — Technical document describing a project"
    )


async def tips(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ Beginner Safety Tips\n\n"
        "1. Never share your seed phrase or private key.\n"
        "2. Beware of 'guaranteed profit' offers — they are scams.\n"
        "3. Double-check wallet addresses before sending.\n"
        "4. Use hardware wallets for large amounts.\n"
        "5. Enable 2FA on exchanges (use an app, not SMS).\n"
        "6. Ignore unsolicited DMs offering 'support' or 'giveaways'.\n"
        "7. Start small. Only invest what you can afford to lose.\n"
        "8. Learn first, invest second."
    )


# ---------- Main ----------

def main():
    if not TOKEN:
        logger.error("TELEGRAM_BOT_TOKEN is not set. Exiting.")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("btc", btc))
    app.add_handler(CommandHandler("eth", eth))
    app.add_handler(CommandHandler("blockchain", blockchain))
    app.add_handler(CommandHandler("wallet", wallet))
    app.add_handler(CommandHandler("defi", defi))
    app.add_handler(CommandHandler("nft", nft))
    app.add_handler(CommandHandler("glossary", glossary))
    app.add_handler(CommandHandler("tips", tips))

    logger.info("LearnCryptoNow_bot is starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
