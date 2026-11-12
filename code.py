url = "https://www.facebook.com/".strip().lower()

suspicious_words = [
    "micr0soft-security", "m1crosoft-verify", "rnicrosoft-auth", "msft-portal-signin", "office365-update",
    "g00gle-accounts", "goog1e-verify", "gogole-signin", "accounts-google-auth", "gmail-security-check",
    "app1e-id-verify", "appl3-security", "icloud-account-unlock", "apple-support-signin",
    "faceb00k", "fb-security-alert", "instagram-login-update",
    "amzn-prime-secure", "amazon-account-confirm",
    "netflix-billing-update", "netf1ix-verify-card",
    "paypal-secure-gateway", "paypa1-account-unlock",
    "binance-crypto-bonus", "coinbase-wallet-confirm",
    "linkedin-auth-proxy", "twitter-verify-badge",
    "dropbox-sync-login", "adobe-id-confirm", "github-ssh-verify", "yahoo-mail-security",
    "discord-nitro-claim", "steam-community-trade", "whatsapp-web-scan", "telegram-web-auth",
    "spotify-premium-free", "shopify-admin-login", "stripe-payment-verify",
    "citibank-secure-auth", "wellsfargo-signon", "hsbc-online-portal",
    "kraken-exchange-login", "metamask-wallet-sync", "ledger-live-update",
    "proton-mail-security", "zoom-meeting-auth", "slack-workspace-signin", "salesforce-login-portal"
]

if not url.startswith(("http://", "https://")):
    print("Invalid link format!")
elif any(word in url for word in suspicious_words):
    print("Warning! Suspicious link detected!")
else:
    print("No suspicious words found.")
