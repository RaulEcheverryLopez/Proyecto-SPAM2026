import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'SMSSpamCollection'
DST_DIR = ROOT / 'data'
DST = DST_DIR / 'SMSSpamCollection'

def main():
    DST_DIR.mkdir(exist_ok=True)
    if not SRC.exists():
        print(f"Source dataset not found at {SRC}")
        return
    with open(SRC, 'rb') as fr, open(DST, 'wb') as fw:
        fw.write(fr.read())
    print(f"Copied dataset to {DST}")

if __name__ == '__main__':
    main()
