# Citation decisions log — frontiers-2026

Tracks author decisions on each citation question surfaced by the 5 reference-finder agents.
Status: RESOLVED = decided; PENDING = awaiting author; APPLY = ready to write into bib/prose.

## Resolved

### Q1 — McIsaac 1998 (Supp B07) — RESOLVED
Use the **CMAJ 1998** paper (McIsaac, White, Tannenbaum, Low; 158(1):75-83; PMID 9475915 / PMC1228750).
It is the score-development/validation paper that introduced the age-adjusted ("age-appropriate") score.
NOT the Med Decis Making RCT (McIsaac & Goel, DOI 10.1177/0272989X9801800211). No bib change needed (agent chose correctly). Add PMC URL so it resolves (no journal DOI).

### Q2 — Sonde RRVB ~5,000 (Sec 2.1.3 + Table 1 line 416) — RESOLVED
Verified paper: Kaur S, Larsen E, Harper J, Purandare B, Uluer A, Hasdianda MA, Umale NA, Killeen J, Castillo E, Jariwala S. JMIR 2023;25:e44410. DOI 10.2196/44410. Task = 6-sec sustained vowel "ahh".
- Fix author: **Kaur et al.** (NOT Kaplan) in bib.
- "~5,000" is DEFENSIBLE = validation cohort total ~4,936 (asthma 1,694 + COPD 625 + persistent cough 814 + ILD 98 + healthy 1,705). KEEP ~5,000 in Table 1.
- COVID-19 is a SEPARATE case-control study (283 analyzed / 497 enrolled) — clarify prose so it doesn't imply COVID is in the 5,000.
- Proposed prose: "~5,000 subjects across respiratory-impairment validation cohorts (asthma, COPD, ILD, persistent cough), plus a separate 283-subject COVID-19 case-control study."

### Q3 — Coswara (Table 1) — RESOLVED
Cite the **2023 Scientific Data paper**: Bhattacharya et al., Sci Data 10:397 (2023), DOI 10.1038/s41597-023-02266-0 (2,635 subjects). NOT the 2020 arXiv preprint. Keep bib key `coswara-2020` (opaque label) but set year=2023; update Table 1 year cell 2020 -> 2023 if present.

### Q4 — Tobacco prevalence (Supp S1.3) — RESOLVED
Replace stale "~14%" with BOTH figures: ~9.9% cigarette use (2024 NHIS) AND ~19.5% (~20%) any tobacco product (2023). Cite CDC NHIS/FastStats + MMWR mm7407a3.

### Q6 — AMR "largest single driver" (Sec 1 ¶1) — RESOLVED
Soften to "a leading driver" (CDC AR Threats Report 2019 says "most important factor", DOI 10.15620/cdc:82532).

### Q7 — Respiratory visit fraction (Sec 1 ¶1) — RESOLVED
Accept "approximately 10–11%", framed as a DERIVED sum of NAMCS reason-for-visit categories (not a verbatim CDC figure).

## Pending author decision

### Q5 — Antibiotic figure (Sec 1 ¶1, line 80) — RESOLVED
Rewrite the sentence to: "...acute respiratory infections account for approximately 44% of outpatient antibiotic prescriptions, of which roughly half are unnecessary..." (Fleming-Dutra et al., JAMA 2016, PMID 27139059 / DOI 10.1001/jama.2016.4151). Replaces the single conflated XXXX% with two directly-stated figures.

### Q8 — Unverified subject counts — DEFERRED TO WORKFLOW
NoCoCoDa n=10, Virufy n=16, DiCOVA-1 n=1,040 could not be confirmed from abstracts. Author wants the adversarial Workflow to re-attempt with full-text access. Flag as high-priority verification targets.

## Bucket D — coding-validation (PENDING author decisions)

### Verified clean (no decision):
- `icd9-486-pneumococcal-sensitivity-14pct` → Guevara et al. 1999 AJE, DOI 10.1093/oxfordjournals.aje.a009801, "14.2%" exact. (NOT Skull.)
- `u071-positive-predictive-value` → Lynch et al. 2021 (VA), PMID 34737645, DOI 10.2147/CLEP.S335621, "77.7% outpatient / 93.8% inpatient" exact. (NOT Kadri/HCUP.)

### Q9 — flu coding "~26%" (Supp B02): RECOMMEND relabel as hospital-discharge data (Mira-Iglesias 2025, DOI 10.1111/irv.70069, ~25.3%); no primary-care source exists. Soften "in primary care" wording.
### Q10 — flu "61% under-coding + PPV 60%/68.5%" (Supp B08): RECOMMEND keep 61% but relabel hospital (same Mira-Iglesias study); DROP the PPV 60%/68.5% (no source found).
### Q11 — sinusitis "10-15% bacterial" (Supp B06): RECOMMEND reword to IDSA framing — Chow et al. 2012 (DOI 10.1093/cis370) says bacterial complicates 0.5-2.0% of viral URIs (different denominator). 10-15% not verbatim anywhere.
### Q12 — GAS AUROC (Supp B07): RESOLVED (author override) — USE EXACT NUMBERS + citation. Replace "0.65-0.70" with the exact reported values: Centor AUC 0.72, McIsaac AUC 0.71 (Fine et al. 2012, DOI 10.1001/2013.jamainternmed.1093). Verify exact AUCs in workflow.
### Q13 — long-COVID (Supp B09): (a) seroprevalence "60-80%" UNVERIFIED → RECOMMEND find a dated CDC seroprevalence figure or drop; (b) voice → cite Lin et al. 2023 meta (DOI 10.1016/j.amjoto.2023.103950, 17.1%/20.1%); DROP the ~5% lower bound (not found); restate as "~17-20%".
### Q14 — icd-coding-fidelity-variation (Sec 4.4): Khera 2021 is a medRxiv PREPRINT → RECOMMEND cite Waxse 2025 (published, DOI 10.1038/s41598-025-02183-9) as primary; find Khera published version or drop.
### Q15 — clinical-coding-practice-pneumonia-strep (Sec 4.4): RECOMMEND reframe as diagnostic-guideline recommendation (Shulman 2012 GAS DOI 10.1093/cid/cis629; Metlay 2019 CAP DOI 10.1164/rccm.201908-1581ST), not a coding-practice claim. Re-fetch DOIs in workflow.

## Bucket E — voice/acoustic mechanism (PENDING author decisions)

### Verified clean (no decision):
- `nasal-coupling-spectral` → Hernández-García 2020 (FESS), PMID 30853310. HIGH.
- `pharyngitis-laryngitis-dysphonia` → Pimenta et al. 2022, PMID 35078701. HIGH.
- `lri-breath-support-prosody` + `copd-asthma-voice-acoustics` (B01) → Węglarz 2025 (PMID 40010581) + Lyu 2025 (PMID 40770052). HIGH.
- `covid19-voice-acoustic-prior-work` (B09) → Brown 2020 (Cambridge), Bhattacharya 2023 (Coswara), Orlandic 2021 (COUGHVID), Shimon 2021. HIGH.
- `ics-dysphonia-laryngeal-deposition` (B01 confound, Sec 4.4) → Williamson 1995 (PMID 7664859), Naunheim 2023 (PMID 36939522), Krishnan 2021 (PMID 34311589). HIGH.
- `gas-pharyngitis-voice-articulation` (B07) → Finkelstein 1993 (PMID 8399275). HIGH, with caveat.

### Q16 — DEFERRED (author: "come back to this"). FOUR claims with NO supporting literature: `systemic-illness-voice-fatigue` (Sec 1 p2), `pneumonia-vs-bronchitis-acoustic` (B04), `influenza-systemic-voice-changes` (B08), `bacterial-vs-viral-voice-literature-absent` (B10).
### Q17 — DIGGING IN (author request). B00 umbrella review (`voice-acoustics-acute-resp-mechanisms`).
FINDING: A real umbrella review EXISTS — Sara JDS, Orbelo D, Maor E, Lerman LO, Lerman A. "Guess What We Can Hear—Novel Voice Biomarkers for the Remote Detection of Disease." Mayo Clin Proc 2023;98(9):1353-1375. PMID 37661144, DOI 10.1016/j.mayocp.2023.03.007. Peer-reviewed, discusses voice-biomarker disease mechanisms incl. infectious disease.
Secondary (weaker, 2-pg abstract): Rajasekar et al. 2025 audiomics review, Stud Health Technol Inform 327:884-885, DOI 10.3233/SHTI250491 — hold in reserve.
CONFIRMED: no review specific to the acute-respiratory mechanistic triad (mucosal swelling / nasal coupling / breath support).
RECOMMEND: cite Sara et al. 2023 as umbrella + bundle component refs (Hernández-García + Pimenta + Węglarz) for the specific triad. AWAITING author OK.
### Q18 — In-text caveats to ADD (no decision, just confirm): sinusitis B06 evidence is CHRONIC rhinosinusitis + prompted speech (not acute J01 spontaneous); "hot potato voice" B07 is the SEVERE peritonsillar-abscess end (cite Finkelstein for mass-effect mechanism only).
### Q19 — DOI spot-check: Williamson 1995 (ERS returned 403) and Brown 2020 KDD DOI not fetched from publisher landing — DEFER to workflow for belt-and-suspenders verification.
### Q-also — `infection-noninfection-voice-distinction` (B02) and `uri-lri-voice-contrast` (B03): SPARSE/speculative; Koç 2014 (PMID 25667789) covers non-infectious (allergic rhinitis) voice change only. RECOMMEND reword to avoid implying a head-to-head acoustic study exists; cite component refs.

## Adversarial Workflow verdicts (48 citations) + resolutions

OUTCOME: 40 CONFIRMED, 6 METADATA_FIX, 2 CLAIM_UNSUPPORTED, 0 WRONG_SOURCE, 0 UNVERIFIABLE. No hallucinations.

### Q7 — RESOLVED (author delegated; Claude confident call): respiratory visit fraction.
Workflow found ~10-11% does NOT reproduce; NAMCS 2019 Table 13 respiratory (J00-J99) primary dx = 5.1% (the 10.3% is CIRCULATORY — category mix-up). No NAMCS 2024 exists. DECISION: use "~5% by primary diagnosis", reword "complaints"->"respiratory conditions (by primary diagnosis)", cite NAMCS 2019 web tables PDF (https://www.cdc.gov/nchs/data/ahcd/namcs_summary/2019-namcs-web-tables-508.pdf), fix year to 2019.

### Antiviral window — RESOLVED (author OK): Uyeki 2019 (DOI 10.1093/cid/ciy866) supports flu <=48h ONLY (zero COVID content). ADD separate source for Paxlovid <=5d: NIH COVID-19 Treatment Guidelines (or FDA Paxlovid label). Split into two citations.

### METADATA FIXES (claims correct, fix identifiers):
- `cdc-namcs-sex-pc-utilization`: DOI -> 10.15585/mmwr.mm6639a6 (MMWR 2017;66(39):1060). Figures correct.
- `icd9-486-pneumococcal-sensitivity-14pct`: DOI -> 10.1093/oxfordjournals.aje.a009804 (PMID 9927225). 14.2% correct. (Finder's DOI was wrong.)
- `gas-clinical-criteria-ceiling`: DOI -> 10.1001/archinternmed.2012.950 (finder's was 404); venue "Arch Intern Med" 2012. AUCs 0.72/0.71 confirmed (Q12).
- `long-covid-voice-prevalence`: voice CONFIRMED (Lin 2023, 17.1%/20.1%, drop 5% floor). Seroprevalence 60-80% needs SEPARATE dated CDC source (e.g., CDC 2022 commercial-lab seroprev ~57.7% Feb 2022 -> ~77.5% Q3 2022) — do not let Lin cover it.

### Q-also — RESOLVED (author: yes reword + cite components):
- B02 `infection-noninfection-voice-distinction`: cite Koc 2014 (PMID 25667789) for non-infectious side only; reword to not imply head-to-head study.
- B03 `uri-lri-voice-contrast`: cite component refs (Hernandez-Garcia upper + Weglarz lower); reword.

### Q16 — RESOLVED (convention research + deep search):
Field convention (researched): ground mechanism PHYSICS in a textbook + the Sara 2023 review; frame disease-specific predictions as explicit hypotheses. No one cites a primary acoustic study for generic "illness->voice" mechanism.
- TEXTBOOK ANCHOR: Behrman A, Speech and Voice Science, 4th ed., Plural Publishing 2023, ISBN 9781635503227 (Ch.4 speech breathing / work of breathing). PRIMARY recommendation. Titze IR, Principles of Voice Production (Prentice Hall 1994, ISBN 9780137178933; or NCVS 2000 reissue ISBN 9780874141221) as alternative/additional for phonation physics.
- (a) systemic-illness-voice-fatigue (Sec 1 p2) + (b) influenza-systemic (B08): cite Behrman for the respiratory-drive/breath-support physiology; frame illness link as hypothesis.
- (c) B04 pneumonia-vs-bronchitis: SEE DEEP SEARCH BELOW (no longer pure-uncited).
- (d) B10 bacterial-vs-viral: SEE DEEP SEARCH BELOW (no longer bald-absent).

### B04 deep search — RESOLVED (claim was UNSAFE; now cited + narrowed):
Direct prior work EXISTS: Liao, Song, Wang, Wang 2022, PLoS ONE, DOI 10.1371/journal.pone.0275479 (PMC9612535) — cough-acoustic bronchitis-vs-pneumonia in 173 children, 86% acc. Plus Porter et al. 2019, Respir Res, DOI 10.1186/s12931-019-1046-6; Sharan et al. 2024, IEEE JBHI, DOI 10.1109/JBHI.2023.3327292. CITE these; narrow novelty to conversational-speech + adult + cascade. Recommended wording adopted (see chat).

### B10 deep search — RESOLVED (softened + acknowledge adjacent):
No direct etiology-validated bacterial-vs-viral acoustic work in adults, BUT adjacent wet/dry-cough proxy exists: Renjini et al. 2021, J Complex Networks, DOI 10.1093/comnet/cnab039 (wet->bacterial/dry->viral framing). Also imaging (not audio): Pneumonia-Plus 2023, Eur Radiol, DOI 10.1007/s00330-023-09833-4. CITE Renjini (+ optionally Pneumonia-Plus as imaging contrast); soften to "validated against clinical reference standard, in adults, remains unaddressed". Avoid "essentially absent". (Discarded a hallucinated "88% bacterial/viral/COVID classifier" — not real.)

### Q7 — UPDATED (author final): use REASON-FOR-VISIT framing (~10-11%), reword "complaints account for ~X% by reason for visit", cite NAMCS reason-for-visit data with explicit derivation. (NOT the ~5% primary-diagnosis option.) Need to source the NAMCS RVC respiratory figure during build.

### nasal-coupling / sinusitis — RESOLVED (author: option a, better targeted refs found):
- `nasal-coupling-spectral`: REPLACE Hernandez-Garcia with de Boer & Bressmann 2015, Cleft Palate Craniofac J 53(5):e163-71, DOI 10.1597/14-236 (PMID 26068387) — measures long-term averaged SPECTRA of hyponasal/oral-nasal balance. Direct fit.
- `sinusitis-hyponasality-acoustic`: REPLACE with Jiang & Huang 2006, Am J Rhinol 20(4):432-7, DOI 10.2500/ajr.2006.20.2882 (PMID 16955774) — measures NASALANCE in chronic rhinosinusitis (carries chronic caveat). Optional backup: Dalston 1991, DOI 10.1044/jshr.3401.11.

### CONFIRMED clean (no action): all bucket A; all bucket B datasets incl Q8 counts (NoCoCoDa/Virufy/DiCOVA-1 verified via full text); fleming-dutra, amr, singh pneumonia, tobacco, fluview; flu-26pct + flu-fidelity (hospital, relabel per Q9/Q10); u071; icd-coding-fidelity; clinical-coding-practice; Sara 2023 umbrella (Q17); pharyngitis-laryngitis (Pimenta), lri/copd (Weglarz/Lyu), gas-articulation (Finkelstein), covid-prior-work, ics-dysphonia.

## Notes
- Manuscript still uses `[CITE]` markers (not `\citep{}`) on the camille branch at lines 80, 131, 416, etc. (main converted some to `\citep`).
- Bib keys are kebab-case and match references_needed.md.
