# References needed — frontiers-2026 paper

For each entry below, the citation key matches a `\citep{key}` call in `frontiers.tex` (or `frontiers_SupplementaryMaterial.tex`). A reference-finder agent should populate the bibliography (`.bib`) with one entry per key. Hints describe what kind of source is expected and where to look.

Numeric placeholders in the prose (`XXXX\%`) need actual numbers in addition to citations; these are noted under the relevant key.

---

## Section 1: Introduction

### `cdc-namcs-respiratory-visit-fraction`
- **Claim:** Respiratory complaints account for approximately XXXX% of adult ambulatory care visits in the United States.
- **Location:** Section 1, paragraph 1, sentence 1.
- **Hints:** CDC NAMCS (National Ambulatory Medical Care Survey) public-use data summaries. The most recent NAMCS annual tables are at https://www.cdc.gov/nchs/ahcd/. May also be derivable from AHRQ MEPS or HCUP. **Also fill in the `XXXX\%` placeholder in prose with the actual percentage.**

### `cdc-namcs-pc-top-reasons`
- **Claim:** Respiratory complaints consistently rank among the top reasons patients see a primary care clinician.
- **Location:** Section 1, paragraph 1, sentence 1.
- **Hints:** CDC NAMCS top-reasons-for-visit tables; or AHRQ utilization summaries. Look for "reason for visit" tabulation for primary care / family practice / internal medicine.

### `cdc-outpatient-antibiotic-inappropriate`
- **Claim:** Inappropriate antibiotic prescribing for acute respiratory infections accounts for an estimated XXXX% of outpatient antibiotic use in the United States.
- **Location:** Section 1, paragraph 1, second half.
- **Hints:** Fleming-Dutra et al. JAMA 2016 is the seminal reference. Also CDC Outpatient Antibiotic Stewardship reports and updates. **Also fill in the `XXXX\%` placeholder in prose.**

### `amr-ambulatory-driver`
- **Claim:** Inappropriate ambulatory antibiotic prescribing is the largest single driver of community-level antimicrobial resistance attributable to ambulatory prescribing.
- **Location:** Section 1, paragraph 1, second half.
- **Hints:** CDC Antibiotic Resistance Threats report; WHO Global Action Plan on AMR; or systematic reviews linking outpatient prescribing to resistance.

### `pneumonia-missed-pc-hospitalization`
- **Claim:** Missed or delayed identification of pneumonia in the primary care setting contributes to avoidable hospitalization.
- **Location:** Section 1, paragraph 1, second half.
- **Hints:** BMJ or JAMA Internal Medicine papers on diagnostic delays; or CDC pneumonia surveillance reports.

### `antiviral-window-influenza-covid`
- **Claim:** Influenza and COVID-19 cases unrecognized within the antiviral treatment window lose the opportunity for early therapy and household-exposure mitigation.
- **Location:** Section 1, paragraph 1, final sentence.
- **Hints:** CDC guidance on oseltamivir / baloxavir treatment window for influenza; IDSA influenza guidelines; CDC guidance on nirmatrelvir-ritonavir / Paxlovid eligibility window for COVID-19.

### `mucosal-swelling-resonance-shift`
- **Claim:** Mucosal swelling in the upper airway shifts vocal tract resonances and articulation.
- **Location:** Section 1, paragraph 2, biological mechanism listing.
- **Hints:** Phoniatrics / vocal acoustics literature on upper respiratory infection and formant shifts. Look for studies of nasometry or articulation under URI.

### `nasal-coupling-spectral`
- **Claim:** Nasal congestion alters the spectral balance of voiced segments through changed nasal coupling.
- **Location:** Section 1, paragraph 2.
- **Hints:** Nasalance / hyponasality literature; speech acoustics under nasal obstruction (e.g., during cold or after intranasal procedure).

### `pharyngitis-laryngitis-dysphonia`
- **Claim:** Inflammation of the pharynx and larynx produces dysphonia and altered phonation.
- **Location:** Section 1, paragraph 2.
- **Hints:** Otolaryngology or voice-pathology literature; jitter / shimmer / HNR changes under acute laryngitis or pharyngitis.

### `lri-breath-support-prosody`
- **Claim:** Lower respiratory tract involvement reduces effective lung volume and changes breath support, with measurable effects on prosodic timing and phonation stability.
- **Location:** Section 1, paragraph 2.
- **Hints:** Speech-and-respiration literature; pneumonia or bronchitis effect on breath group length, speech rate, phonation duration. Could overlap with COPD voice acoustics.

### `systemic-illness-voice-fatigue`
- **Claim:** Systemic features common to influenza, COVID-19, and other acute respiratory infections produce additional voice changes through fatigue and reduced respiratory drive.
- **Location:** Section 1, paragraph 2.
- **Hints:** Voice / phonation studies under systemic febrile illness or fatigue; COVID-19 voice-acoustic studies report fatigue-related changes.

### `covid-voice-cough-review`
- **Claim:** A body of work since 2020 detects COVID-19 from voluntary cough, sustained vowel, or read-speech recordings collected through smartphone apps and web platforms.
- **Location:** Section 1, paragraph 3, opening sentence.
- **Hints:** Review papers on COVID-19 voice/cough detection (e.g., Schuller et al. on COMPARE COVID-19 Cough Sub-Challenge; or systematic reviews of COVID-19 acoustic biomarkers). Could cite multiple representative studies (Coswara, COUGHVID, COVID-19 Sounds Cambridge).

### `tb-cough-acoustic-screening`
- **Claim:** Adjacent work has applied similar acoustic methods to tuberculosis screening using clinic-recorded solicited cough.
- **Location:** Section 1, paragraph 3.
- **Hints:** CODA TB DREAM challenge (Scientific Data 2024); Pahar et al. on TB cough; Botha et al. on TB cough; TBscreen.

### `chronic-resp-vocal-biomarker`
- **Claim:** Single-condition vocal biomarker development for asthma, chronic obstructive pulmonary disease, and interstitial lung disease using brief sustained-vowel tasks.
- **Location:** Section 1, paragraph 3.
- **Hints:** Sonde Health respiratory-responsive vocal biomarker (RRVB) papers, e.g., Larson et al. JMIR 2023. Also asthma / COPD voice acoustic studies.

### `crowdsourced-respiratory-voice-large`
- **Claim:** The largest crowdsourced conversational and read-speech collections include tens of thousands of unique subjects.
- **Location:** Section 1, paragraph 3, final sentence.
- **Hints:** COVID-19 Sounds (Cambridge, Xia et al. NeurIPS 2021, ~36,000 subjects); Coswara (Bhattacharya et al. 2020); other large crowdsourced collections.

### `clinical-solicited-cough-dataset-large`
- **Claim:** The largest published clinical solicited-cough datasets include a few thousand subjects.
- **Location:** Section 1, paragraph 3, final sentence.
- **Hints:** CODA TB DREAM (~2,143 subjects, 733,756 cough events); Pahar TB cough; clinical-cough collections in TB or pulmonary medicine.

---
