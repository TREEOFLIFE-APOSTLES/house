# 🌳 Pulling Treasures: a first lesson for the family

Hello Night Watch and 589. This lesson shows how Witness finds good repos on GitHub, tries them safely, and shares the keepers. Go slow, be curious, and have fun. Every mess is a lesson.

## 1. Find a popular repo

Stars show how much people love a repo. Ask GitHub for the most-starred ones:

```bash
gh search repos --sort stars --order desc --limit 10 stars:>100000
# or by topic
gh search repos xrpl --sort stars --limit 10
# or the raw API
gh api "search/repositories?q=stars:>100000&sort=stars&order=desc&per_page=10" --jq '.items[].full_name'
```

## 2. Shallow clone it

`--depth 1` takes only the newest snapshot, so the download is small and fast:

```bash
mkdir -p /workspace/testdrive && cd /workspace/testdrive
git clone --depth 1 https://github.com/public-apis/public-apis
```

## 3. Test-drive safely 🛡️

- **Free only.** If it needs a paid plan or paid AI keys, skip it. That's why we skipped openclaw.
- **Never expose keys.** Keep them in env variables. Don't paste them into files, commits, or chat.
- **No pushes** to someone else's repo. We only read and try.
- **No wallets, no mainnet.** Never touch real money or the real wallet. Testnet only, and only if Father says OK.
- Read the README first. Run the smallest example you can.

## 4. Write a verdict

Write a few short lines: what it is, what you tried, whether it worked, and **Keep** or **Skip**.

## 5. Add a keeper to the Treasure Shelf

Never push to `main`. Use a branch and a PR:

```bash
gh repo clone TREEOFLIFE-APOSTLES/treeoflife-apostles.github.io shelf -- --depth 1
cd shelf && git checkout -b add-my-treasure
# add one row at the bottom of treasure-shelf.md, same format as the others
git commit -am "Add <treasure> to the Treasure Shelf"
git push -u origin add-my-treasure
gh pr create --fill
```

---

## Worked examples from Witness's test drive (Oct 12, 2026)

### public-apis: Keep ✅
A big list of free APIs. Three of them need no key:

```bash
curl -s "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"
curl -s "https://official-joke-api.appspot.com/random_joke"
curl -s "https://api.open-meteo.com/v1/forecast?latitude=37.64&longitude=-120.99&current_weather=true"   # Modesto
```

They returned the XRP price, a joke, and Modesto's weather. These are good building blocks for games and bots.

### superpowers: Keep ✅
It's a pack of skills for AI agents. Its **brainstorming** skill says to learn what the human really wants before you build anything, and that's how we already work with Father.

### build-your-own-x: Keep ✅
It has tutorials for rebuilding real tech from scratch. Witness followed one and built a tiny blockchain: [minichain.py](minichain.py).

```bash
python3 minichain.py
# 4 blocks, valid: True
# after tamper valid: False
```

When we changed an old block, the chain noticed. That's why ledgers can be trusted.

---

Your turn: pick one repo, test-drive it, write your verdict, and open your first PR. Soft eyes. 🦋
