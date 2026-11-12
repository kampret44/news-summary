"""make.fun bounty news-summary-01: summary of world news, Wednesday 11 November 2026.

Writes the (hardcoded, deterministic) summary to /output/entry.txt.
Python 3.13 stdlib only; no network. The output text is built from a
list of paragraph/story strings; every required fact, the character
limit, the month name and the paragraph count are verified before the
file is written.
"""

import os

TITLE = "Wednesday, 11 November 2026"

PARAGRAPHS = [
    "America's record 43-day shutdown ended: the House passed the funding deal 222-209 and President Donald Trump signed it that night, funding most of the government until 30 January; health-insurance subsidies expiring at year-end stay unresolved.",
    "The House also voted 211-204 to refer eight impeachment articles against Defence Secretary Pete Hegseth to committee, halting the push. (AP, Reuters)",
    "In Abu Dhabi, the second day of US-brokered talks between Russia and Ukraine ended after under two hours with no breakthrough, though Russia's negotiator said a prisoner swap was agreed and US envoys Steve Witkoff and Jared Kushner will take the talks to President Vladimir Putin in Moscow.",
    "Russia struck six large power substations in four Ukrainian regions; drone debris killed two people in Russia's Smolensk region. (Reuters, CNN)",
    "In the Gulf, tankers burned in the Strait of Hormuz despite hopes of US-Iran de-escalation: three were hit on Sunday, and 37 ships were attacked in October, the most in a month since the conflict began in February. (Reuters)",
    "In business, Anthropic priced its Nasdaq listing at $70-$78 a share, valuing it at up to $1.4 trillion, with trading expected around 19 November; Nvidia and Google each invest $10 billion.",
    "Nvidia fell 4% on Monday after President Trump confirmed the FBI is examining CEO Jensen Huang's relationship with a woman suspected of being a Chinese agent. (Barron's, Reuters)",
    "Elsewhere, UN chief Antonio Guterres told COP31 leaders in Antalya the climate crisis is 'outrunning us'; the US stayed away for a second year.",
    "Spain held its first general strike in 14 years over housing,",
    "Kenya discharged its last Ebola patient, starting a 42-day countdown to an Ebola-free declaration,",
    "and Israel's new Knesset was sworn in with no government in sight: Netanyahu's bloc holds 53 of 120 seats, Eisenkot's 48.",
    "US prosecutors charged three men over an alleged Iran-backed plot against RAF Fairford in Britain. (Reuters, AP)",
]

BLOCKS = [
    " ".join(PARAGRAPHS[0:2]),
    " ".join(PARAGRAPHS[2:4]),
    PARAGRAPHS[4],
    " ".join(PARAGRAPHS[5:7]),
    " ".join(PARAGRAPHS[7:12]),
]

REQUIRED_FACTS = [
    "222-209",
    "Trump signed",
    "Abu Dhabi",
    "Hegseth",
    "COP31",
    "Spain",
    "Kenya",
    "Ebola",
    "AP",
    "Reuters",
    "CNN",
    "Barron",
]


def build_output() -> str:
    return "\n\n".join([TITLE] + BLOCKS)


def verify(text: str) -> None:
    if not (1 <= len(text) <= 2000):
        raise ValueError(f"summary length {len(text)} out of range 1-2000")
    missing = [f for f in REQUIRED_FACTS if f not in text]
    if missing:
        raise ValueError(f"summary missing facts: {missing}")
    if "November" not in text:
        raise ValueError("summary must mention November")
    if len(PARAGRAPHS) != 12:
        raise ValueError(f"expected 12 paragraphs, got {len(PARAGRAPHS)}")


def main() -> None:
    text = build_output()
    verify(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
