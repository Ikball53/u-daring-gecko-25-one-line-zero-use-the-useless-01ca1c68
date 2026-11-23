from pathlib import Path

# Final line: grand setup ("any wall") collapsing into one vivid,
# useless detail — the payoff word "soup" lands last for the laugh.
LINE = "I can hear through any wall, but only when someone is whispering about soup."

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
