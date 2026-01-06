import hashlib

SKIN_TYPES = ["Oily", "Dry", "Combination", "Normal"]
ISSUES = [
    "Acne",
    "Hyperpigmentation",
    "Dryness",
    "Redness",
    "Dark Circles",
    "Wrinkles",
]


def analyze_image(image_id: str) -> dict:
    digest = hashlib.sha256(image_id.encode("utf-8")).hexdigest()
    seed = int(digest[:8], 16)

    skin_type = SKIN_TYPES[seed % len(SKIN_TYPES)]

    issue_count = (seed % 3) + 1
    issues = []
    for idx in range(issue_count):
        issues.append(ISSUES[(seed + idx) % len(ISSUES)])

    confidence_seed = int(digest[8:12], 16)
    confidence = 0.60 + (confidence_seed % 36) / 100

    return {
        "skin_type": skin_type,
        "issues": issues,
        "confidence": round(confidence, 2),
    }
