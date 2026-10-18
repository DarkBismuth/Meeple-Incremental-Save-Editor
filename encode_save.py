
from pathlib import Path
import json

INPUT_FILE = Path("gameSaveData.decoded.json")
OUTPUT_FILE = Path("gameSaveData.edited")
KEY = b"rheuu3M99dS51TFc"


def xor_transform(data: bytes) -> bytes:
    return bytes(
        byte ^ KEY[i % len(KEY)]
        for i, byte in enumerate(data)
    )


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"JSON file not found: {INPUT_FILE}"
        )

    # Validate JSON before encoding.
    text = INPUT_FILE.read_text(encoding="utf-8")
    parsed = json.loads(text)

    # Produce compact JSON without indentation.
    payload = json.dumps(
        parsed,
        separators=(",", ":"),
        ensure_ascii=False
    ).encode("utf-8")

    encoded = xor_transform(payload)
    OUTPUT_FILE.write_bytes(encoded)

    print(f"Encoded successfully: {OUTPUT_FILE}")
    print(f"JSON size: {len(payload)} bytes")
    print(f"Encoded size: {len(encoded)} bytes")


if __name__ == "__main__":
    main()
