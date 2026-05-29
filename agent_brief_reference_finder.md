# Research agent brief — reference finder for frontiers-2026

## Your task

The manuscript `frontiers.tex` and supplementary `frontiers_SupplementaryMaterial.tex` use `\citep{key}` placeholders for citations. The file `references_needed.md` lists every key with the claim being cited and hints for finding the source. Your job is to find a legitimate, peer-reviewed published reference for each key and produce a BibTeX entry that can be added to `references.bib`.

## STRICT RULES (read carefully)

### 1. NEVER fabricate citations. EVER. STRICTLY.

Do not invent a paper, an author, a journal, a year, a DOI, a page range, or any other bibliographic field. Do not "fill in" a plausible-sounding reference if you cannot verify it against an authoritative source (publisher page, PubMed, Google Scholar, official conference proceedings, arXiv, journal homepage). Hallucinated citations cause the paper to be rejected or retracted and are a non-recoverable failure mode for this task.

### 2. Use only legitimately published, peer-reviewed sources.

Acceptable source types:
- Peer-reviewed journal articles
- Peer-reviewed conference proceedings (e.g., NeurIPS, ICML, Interspeech, ICASSP)
- Edited and reviewed book chapters
- Official guidelines from medical professional societies (IDSA, ACP, CDC, WHO, NIH, EPOS, AHRQ)
- Government surveillance reports with documented methodology (CDC NAMCS, CDC NHIS, BRFSS, CDC FluView)

NOT acceptable without an explicit flag:
- Blog posts
- Non-peer-reviewed preprints (arXiv-only without journal publication) — flag if used
- Vendor websites or product documentation
- Wikipedia or general encyclopedias
- News articles, press releases
- Personal communications

If you can only find a source that falls in the "not acceptable" category (e.g., a Google blog post for `chirp 3` acoustic model, or a vendor whitepaper), **flag this in your output for that key** so the manuscript authors can decide whether to use it, drop the claim, or hunt further.

### 3. If a reference is not available, say so. Do not fake one.

If after a thorough search you cannot find a peer-reviewed source that supports the specific claim for a key, output a "NOT FOUND" entry with: (a) what you searched, (b) what you found (if anything), (c) why it doesn't qualify, and (d) suggestions for the authors (e.g., "claim may need to be softened or dropped" or "consider X as the closest available non-peer-reviewed source").

Try hard — search Google Scholar, PubMed, the specific journal's archive, the specific conference's proceedings, the author's lab website. Use synonyms and alternative phrasings. But when the search runs out, push back honestly. Pushing back is correct and helpful behavior; faking is not.

## Inputs

- `references_needed.md` — your work list. Each `### key` heading is a `\citep{key}` placeholder. Under each key are: **Claim**, **Location** (which section / table / supplementary subsection), and **Hints** (likely author / journal / search terms). Hints are starting points only; they are not authoritative.

## Outputs

Produce **two** outputs:

### Output 1: `references.bib` — a BibTeX file with one entry per resolved key.

Use Frontiers Harvard style requirements: include author, title, journal/booktitle, year, volume, number, pages, doi (where available). Example entry:

```bibtex
@article{cdc-namcs-respiratory-visit-fraction,
  author    = {Last1, First1 and Last2, First2},
  title     = {Title of the paper},
  journal   = {Journal Name},
  year      = {YYYY},
  volume    = {NN},
  number    = {N},
  pages     = {ppp--ppp},
  doi       = {10.xxxx/yyyyy}
}
```

For non-journal sources, use the appropriate BibTeX entry type (`@inproceedings`, `@book`, `@techreport`, `@misc`, `@incollection`). For government surveillance with no peer-reviewed citation form (e.g., CDC NAMCS tables themselves), use `@techreport` or `@misc` with a clear `note` field indicating the source type.

The bib key MUST match the `\citep{key}` exactly (kebab-case, no spaces, no underscores in our convention — copy from `references_needed.md` headings verbatim).

### Output 2: `references_findings.md` — a per-key audit trail.

For each key in `references_needed.md`, write one entry in `references_findings.md` with this structure:

```markdown
### `key-name`

- **Status:** RESOLVED | FLAGGED-NON-PEER-REVIEWED | NOT-FOUND
- **Selected source:** (full citation in prose, mirroring the .bib entry; or "n/a" if NOT-FOUND)
- **Why this source matches the claim:** (1-2 sentences linking the source's findings to the specific claim wording in `references_needed.md`)
- **Verification:** (where you confirmed the source exists — PubMed PMID, DOI link, conference proceedings URL, etc.)
- **Searches performed:** (brief — only needed if you struggled or escalated)
- **Alternative sources considered:** (optional — useful if the chosen source is not the obvious one)
- **Authors' attention needed:** (optional — flag here if the source is non-peer-reviewed, if the claim is broader than what one source supports, if a key should resolve to multiple papers, or if the claim should be re-worded or dropped)
```

Optional output 3: if you find that two keys should resolve to the **same** paper (e.g., overlap between an Intro key and a Section 2 key), produce a `references_consolidation.md` with a proposed merge list. Do NOT merge keys in the manuscript or in `references_needed.md` yourself — that's an authors' decision.

## Specific guidance per source category

- **CDC NAMCS / NHIS / BRFSS / FluView keys:** these are government surveillance products. Cite the most recent dated CDC publication summarizing the relevant statistic, or the CDC NCHS data brief. Include the URL in a `url =` field and a `note = {Accessed YYYY-MM-DD}` field.
- **IDSA / ACP / EPOS guidelines:** cite the formal published guideline document (these are peer-reviewed by the society's process). Include the version year.
- **Dataset papers (Coswara, COUGHVID, COVID-19 Sounds, CODA TB DREAM, etc.):** cite the original published dataset descriptor paper. Several of these were also presented at NeurIPS or Interspeech; cite the venue paper, not a GitHub README.
- **Software (openSMILE, librosa, praat-parselmouth):** cite the canonical software paper. openSMILE has a 2010 ACM Multimedia paper; librosa has a 2015 SciPy conference paper; praat has long-standing publications by Boersma.
- **Algorithm/method papers (AdamW, SGDR, Benjamini-Hochberg, Centor, McIsaac):** cite the original publication that introduced the method.
- **Bio-mechanism keys (e.g., `mucosal-swelling-resonance-shift`, `nasal-coupling-spectral`, `pneumonia-vs-bronchitis-acoustic`):** these may require resolving to multiple supporting papers per key, since the claim is a general mechanism statement. It is acceptable for one bib key to resolve to a small set of 2-4 citations in the actual `.bib` (multiple `@article` entries, each with the same key prefix and a -1 / -2 / -3 suffix), and the manuscript's `\citep{...}` call can list them all. If you do this, document it in `references_findings.md`.

## When in doubt

When in doubt about whether a source qualifies, FLAG it rather than silently downgrading the quality bar. Authors prefer "I found a possible source but it's a vendor blog" over "I found a great source!" that turns out to be a blog. The cost of a flag is a 30-second authors' review; the cost of an undetected non-peer-reviewed source is a reviewer flagging it and questioning the entire manuscript's citation quality.

## Iteration

After your first pass, send the two output files back to the authors. The authors will review and either approve, ask for re-searches on specific keys, or accept the NOT-FOUND status and adjust the prose.

## Final reminder

The most important sentence in this brief: **do not invent.** If you can't find it, say so. Pushing back is helpful. Hallucinating is not.
