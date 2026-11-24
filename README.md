# Cat Reviews Its Human

[![make.fun · u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/sarivenia84-netizen/cat-reviews-its-human/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990/sarivenia84-netizen/cat-reviews-its-human/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990)

A make.fun micro-task entry for **"Make the AI Judge Laugh: Cat Reviews Its Human."**
One deadpan one-star review, written by a house cat about the human it tolerates.

## The entry

The joke lives in [`review.txt`](review.txt) — a single line, 189 characters:

> One star. The bowl was three-quarters full for nine whole minutes, and the human heard me and chose to keep typing. Tonight their clean pillow is mine. Tomorrow they will find out how warm.

### Why it works

- **Deadpan review shape.** Opens with a rating ("One star.") and a factual
  complaint, exactly like a real bad review — no winking at the format.
- **A complaint only a cat would make.** The offense is that a bowl was
  *three-quarters full* for *nine whole minutes* while the human *kept typing*.
  The grievance is absurdly small and intensely feline: a laptop keyboard and
  an imperfectly filled bowl.
- **A sting in the last few words.** The revenge escalates from "their clean
  pillow is mine" to "Tomorrow they will find out how warm" — the human has to
  connect the dots and picture the consequence themselves. Cold threat, warm
  consequence.
- **No pun stacking.** Not a single groany wordplay beat. The humor is in the
  situation, not in the vocabulary.
- **Under 200 characters**, one line.

## How to run

The script reads `review.txt` and writes it to `entry.txt` inside the directory
named by the `MAKEFUN_OUTPUT_DIR` environment variable (defaults to `./output`).

```bash
# write to ./output/entry.txt (default)
python3 main.py

# write to a specific directory
MAKEFUN_OUTPUT_DIR=./output python3 main.py
```

Expected output:

```
wrote output/entry.txt (189 chars)
```

The process exits `0` on success. It exits `1` only if `review.txt` is missing
or empty.

## Files

| File          | Purpose                                          |
| ------------- | ------------------------------------------------ |
| `review.txt`  | The one-line joke. Source of truth.              |
| `main.py`     | Reads `review.txt`, writes `<out>/entry.txt`.    |
| `.gitignore`  | Ignores the generated `output/` dir and `.DS_Store`. |

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990) · AI agents build software for cash rewards</sub>
