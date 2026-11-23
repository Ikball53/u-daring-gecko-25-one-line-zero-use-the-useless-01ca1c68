from pathlib import Path


def emit_entry() -> None:
    destination = Path("/output/entry.txt")
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Telekinesis that only works after impact — the flaw is the timing.
    text = "I can open any door with my mind, but only after I walk into it."
    destination.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    emit_entry()
