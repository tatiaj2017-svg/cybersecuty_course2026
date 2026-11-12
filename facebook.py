url = "https://www.facebook.com/".strip().lower()

suspicious_words = [
    "face-book",
    "fakebook",
    "ffaceb00ok",
    "faceb00k_sign_in",
    "feisbook"
]

if not url.startswith(("http://", "https://")):
    print("Invalid link format!")
elif any(word in url for word in suspicious_words):
    print("Warning! Suspicious link detected!")
else:
    print("No suspicious words found.")

