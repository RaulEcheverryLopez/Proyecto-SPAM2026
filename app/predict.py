"""Text preprocessing helpers for SMS spam prediction.

The baseline notebook tokenizes with a regex that keeps alphabetical words,
lowercases text, and often ignores very short tokens. These utilities mirror
that behavior so inference preprocessing is explicit and reusable.
"""

from __future__ import annotations

import re
from typing import List

_TOKEN_PATTERN = re.compile(r"\b[a-zA-Z]+\b")


def coerce_text(text: object) -> str:
    """Return a safe string representation for model preprocessing."""
    if text is None:
        return ""
    return str(text)


def tokenize_alpha_words(text: object) -> List[str]:
    """Tokenize using the notebook-style alpha regex and lowercase text."""
    raw = coerce_text(text).lower()
    return _TOKEN_PATTERN.findall(raw)


def simple_preprocess(text: object, min_token_len: int = 3) -> str:
    """Normalize text for inference.

    Steps:
    1. Convert input to string safely.
    2. Lowercase.
    3. Keep only alphabetical tokens via regex.
    4. Remove short tokens (default keeps len >= 3).
    5. Rejoin with single spaces.
    """
    tokens = tokenize_alpha_words(text)
    filtered = [tok for tok in tokens if len(tok) >= min_token_len]
    return " ".join(filtered).strip()
