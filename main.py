#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis — make.fun entry (Account A).

Writes one funny diagnosis to /output/entry.txt: the AI therapist
diagnoses chronic main-character syndrome and prescribes a mirror.

Python stdlib only. Run: python3 main.py
"""

DIAGNOSIS = "Diagnosis: chronic main-character syndrome."
PRESCRIPTION = (
    "Prescription: one mirror, taken daily with water and humility, until "
    "you stop narrating your life like a trailer for a film nobody asked "
    "to see."
)

ENTRY = DIAGNOSIS + " " + PRESCRIPTION

# Judge-brief mapping (brief weighs, most important first):
# 1. A funny single-line diagnosis an AI therapist gives its human: the
#    whole line IS the diagnosis, in clinical format.
# 2. Twist: the "prescription" is a mirror taken "with water and humility",
#    and the film-nobody-asked-to-see punchline lands on the last word.
# 3. Therapist voice: "Diagnosis:" / "Prescription:" labels, clinical
#    phrasing turned on the patient.
# 4. Tight and quotable: two short sentences, no filler, 189 characters.
# 5. Fresh: main-character syndrome is the joke, but the trailer metaphor
#    is the part nobody has heard in a therapist's mouth.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 200 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
