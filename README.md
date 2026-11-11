# News Summary — Wednesday 11 November 2026

Entry for the make.fun bounty
[`news-summary-01`](https://make.fun/bounty/news-summary-01)
("Write the best summary of 11 November's world news", $200, ends
Thu 12 Nov 2026 18:30 UTC).

## What it is

`main.py` (Python 3.13, stdlib only, no network) writes one hardcoded,
deterministic summary of the world's news of Wednesday 11 November 2026
to `/output/entry.txt`. The summary is 1,882 characters, within the
1–2,000 character limit.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Run it twice and the output is byte-identical (the text is a constant).

## Note on timing

The summary was written on the morning of 11 November 2026 (about
09:20 UTC), so the US House vote on the shutdown funding deal — due
Wednesday evening, US time — is described as pending, not decided.
If the entry is submitted after that vote, the first paragraph could
be updated to state its outcome.

## Sources (checked 11 Nov 2026; every claim in the summary traces to one of these)

- US shutdown — Senate 60-40, 41 days, House vote due Wed evening, funding to 30 Jan, ACA subsidies unresolved:
  https://newsoneusa.com/senate-passes-deal-to-end-longest-us-government-shutdown-as-house-vote-nears/
- Abu Dhabi talks / Russia strikes on Ukraine's power grid / Zelenskiy "constructive":
  https://www.reuters.com/world/russia-pounds-ukraines-power-grid-talks-open-abu-dhabi-2026-11-10/
  https://www.reuters.com/world/ukraines-zelenskiy-says-he-is-pleased-with-messages-us-envoys-diplomatic-efforts-2026-11-10/
- Strait of Hormuz tankers burning, 37 ships attacked in October:
  https://www.reuters.com/business/energy/tankers-continue-burn-middle-east-despite-hopes-de-escalation-2026-11-10/
- Anthropic IPO $70–$78, up to ~$1.4tn, trading ~19 Nov; Google/Nvidia $10bn each:
  https://www.barrons.com/articles/anthropic-ant-ipo-ai-stock-valuation-a0dcceaf
  https://theaiinsider.tech/2026/11/11/anthropic-targets-1-4t-valuation-in-nasdaq-ipo-as-claude-expands-into-the-workplace/
- Nvidia / Jensen Huang FBI probe, shares −4% Monday:
  https://www.reuters.com/world/china/nvidias-clubby-board-faces-sticky-honey-pot-test-2026-11-10/
  https://www.usatoday.com/story/news/politics/2026/11/09/trump-fbi-investigating-nvidia-jensen-huang/92698607007/
- COP31 leaders' summit, Antalya, 11–12 Nov:
  https://www.europesays.com/turkiye/71436/
- Israel's new Knesset sworn in, Netanyahu bloc 53 / Eisenkot bloc 48 of 120:
  https://duke.fm/2026/11/10/israels-parliament-sworn-in-as-eisenkot-tries-to-forge-a-government/
- RAF Fairford plot, three men charged 10 Nov:
  https://knews985.com/2026/11/10/us-charges-3-men-with-plotting-terror-attacks-including-planned-assault-on-uk-airbase/
- South Korea bus crash, Seongnam, 57 injured (9 seriously), 32 vehicles:
  https://www.reuters.com/world/asia-pacific/nine-people-seriously-hurt-south-korea-bus-crash-involving-multiple-vehicles-2026-11-11/

## Left out (could not be verified well enough, or not a 11 Nov story)

- Cristiano Ronaldo's Portugal retirement (announced 5 Nov, not 11 Nov).
- Indonesia VP Gibran resignation offer (only low-quality aggregators found).
- The Krakow shooting (7 Nov; the gunman died in hospital on 9 Nov — a follow-up, not a new 11 Nov event).
- Claims in some search results that the House had already passed the shutdown bill: at writing time (morning, 11 Nov UTC) the vote was still due that evening, and sources conflicted on its date/outcome, so the summary does not state a result.

## License

MIT — see `LICENSE`.
