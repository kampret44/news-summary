"""make.fun bounty news-summary-01: summary of world news, Wednesday 11 November 2026.

Writes the (hardcoded, deterministic) summary to /output/entry.txt.
Python 3.13 stdlib only; no network.
"""

import os

SUMMARY = """Wednesday, 11 November 2026

America's government shutdown was hours from ending. The Senate passed a funding deal 60-40 on Monday after 41 days, the longest shutdown in US history, and the House was due to vote on Wednesday evening. It funds most of the government until 30 January, but health-insurance subsidies expiring at year-end remain unresolved. Federal workers went unpaid, food aid was delayed and flights were disrupted.

In Abu Dhabi, US-brokered talks between Russia and Ukraine entered a second day, the first trilateral meeting since February. President Volodymyr Zelenskiy called day one constructive, with prisoner exchanges and security guarantees on the agenda. Meanwhile, Russia struck Ukraine's power grid, hitting five substations in 10 regions and killing two people.

In the Gulf, tankers were still burning in the Strait of Hormuz despite hopes of US-Iran de-escalation. Three tankers were hit on Sunday, Iran's Revolutionary Guard said, and 37 ships were attacked in October, the most in a month since the conflict began in February.

In business, Anthropic priced its Nasdaq listing at $70-$78 a share, valuing it at up to about $1.4 trillion, with trading expected around 19 November. Nvidia and Google are each investing $10 billion alongside it. Nvidia was under pressure after President Donald Trump confirmed the FBI is examining CEO Jensen Huang's relationship with a woman suspected of being a Chinese agent. Its shares fell 4% on Monday.

Elsewhere, world leaders gathered in Antalya for the COP31 leaders' summit. Israel's new Knesset was sworn in with no government in sight: Benjamin Netanyahu's bloc holds 53 of 120 seats, Gadi Eisenkot's 48. US prosecutors charged three men over an alleged Iran-backed plot against RAF Fairford in Britain. And in South Korea, a bus ploughed into 32 vehicles in Seongnam, injuring 57 people, nine seriously."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(SUMMARY)


if __name__ == "__main__":
    main()
