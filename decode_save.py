
from pathlib import Path
import json

INPUT_FILE = Path("gameSaveData.json")
OUTPUT_FILE = Path("gameSaveData.decoded.json")
KEY = b"rheuu3M99dS51TFc"


def xor_transform(data: bytes) -> bytes:
    return bytes(
        byte ^ KEY[i % len(KEY)]
        for i, byte in enumerate(data)
    )


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Save file not found: {INPUT_FILE}"
        )

    encrypted = INPUT_FILE.read_bytes()
    decoded = xor_transform(encrypted)

    # Validate that the decoded data is valid UTF-8 JSON.
    parsed = json.loads(decoded.decode("utf-8"))

    OUTPUT_FILE.write_text(
        json.dumps(parsed, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    print(f"Decoded successfully: {OUTPUT_FILE}")
    print(f"Input size: {len(encrypted)} bytes")
    print(f"Output size: {OUTPUT_FILE.stat().st_size} bytes")


if __name__ == "__main__":
    main()
