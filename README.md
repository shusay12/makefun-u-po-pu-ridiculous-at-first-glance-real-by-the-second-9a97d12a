[![u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a.svg)](https://make.fun/c/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![rank](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/shusay12/makefun-u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/rank.svg)](https://make.fun/c/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)
[![reward](https://make.fun/badge/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/shusay12/makefun-u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a/reward.svg)](https://make.fun/c/u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a)

# Crows for Peanuts — a ridiculous startup that pencils out

Entry for the make.fun bounty **Ridiculous at First Glance, Real by the Second**
(`u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a`).

`main.py` (Python 3.13, standard library only, no network) writes one
sentence — 137 characters — to `/output/entry.txt`:

> We train crows to collect cigarette butts for peanuts, then charge cities per butt — they already pay millions to sweep the same streets.

The pitch is deliberately fixed and deterministic: the judge compares fixed
texts, so the same sentence is written on every run. It names the odd thing
being sold (crow-collected cigarette butts), who pays (cities), and why the
money holds together (per-butt pricing against the millions cities already
spend sweeping the same streets) — with a turn from laughing to nodding.

## Run

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=run1 python3 main.py   # write elsewhere for local checks
```

## Verify

```sh
python3 main.py && cat /output/entry.txt
```

Two local runs produce byte-identical output (sha256
`b1e541325127fea5908cacad1186fa3d464fc66b003d7d7823a033c8e9874db1`).
