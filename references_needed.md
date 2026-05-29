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

## Section 2: Materials and Methods

### Dataset comparison (Section 2.1.3)

### `sonde-rrvb-jmir-2023`
- **Claim:** Sonde Health respiratory-responsive vocal biomarker (RRVB) work covers asthma, COPD, ILD, and COVID-19 across ~5,000 subjects using a six-second sustained vowel.
- **Location:** Section 2.1.3 (Comparison with prior datasets) AND Table 1 row.
- **Hints:** Larson et al., JMIR Form Res / JMIR mHealth, 2023; or Kaplan et al. Sonde Health team. Search "Sonde Health respiratory responsive vocal biomarker".

### `covid-19-sounds-xia-2021`
- **Claim:** COVID-19 Sounds dataset (Cambridge), 36,116 participants, read sentence + cough + breath.
- **Location:** Section 2.1.3 AND Table 1 row.
- **Hints:** Xia et al., NeurIPS 2021. Title contains "COVID-19 Sounds" dataset paper or related Cambridge group publications by Cecilia Mascolo's group.

### `coda-tb-dream-2024`
- **Claim:** CODA TB DREAM Challenge dataset: 733,756 cough events from 2,143 subjects, with a 565-subject longitudinal sub-cohort.
- **Location:** Section 2.1.3 AND Table 1 row.
- **Hints:** Scientific Data 2024 paper describing the CODA TB DREAM dataset and challenge. Search "CODA TB DREAM Scientific Data 2024".

### Per-binary biological mechanism citations (Section 2.2.1, B00-B10)

Each B-binary's task description ends with a single citation that supports the biological/acoustic mechanism for that contrast. Some keys may resolve to the same paper or a small set of papers. The reference-finder agent should propose 1-3 citations per key.

### `voice-acoustics-acute-resp-mechanisms`
- **Claim:** Acute respiratory illness alters voice production through upper-airway mucosal swelling, changed nasal coupling, and altered breath support / prosodic timing.
- **Location:** Section 2.2.1, B00 (Acute respiratory vs acute non-respiratory illness).
- **Hints:** Review on voice acoustics in upper respiratory infection; could overlap with `mucosal-swelling-resonance-shift` and `nasal-coupling-spectral` from the Introduction.

### `copd-asthma-voice-acoustics`
- **Claim:** Chronic respiratory disease produces persistent voice changes tied to lower-airway acoustics, breath support, and subglottal pressure (COPD, asthma, bronchiectasis, ILD).
- **Location:** Section 2.2.1, B01.
- **Hints:** Acoustic phenotyping of COPD; jitter / shimmer / HNR shifts under chronic asthma; reduced subglottal pressure literature in COPD.

### `infection-noninfection-voice-distinction`
- **Claim:** Acute infection and non-infectious respiratory presentations diverge in acoustic signature despite similar surface symptoms.
- **Location:** Section 2.2.1, B02 (Acute resp infection vs sick-but-no-infection).
- **Hints:** Voice acoustics in allergic rhinitis vs URI; voice in dyspnea/wheeze without infection. Speculative; may not have one canonical reference.

### `uri-lri-voice-contrast`
- **Claim:** Upper-tract inflammation primarily affects resonance/articulation while lower-tract inflammation primarily affects breath support, cough character, and gas exchange.
- **Location:** Section 2.2.1, B03.
- **Hints:** Speech-and-breath literature; voice acoustics under URI vs pneumonia comparisons.

### `pneumonia-vs-bronchitis-acoustic`
- **Claim:** Pneumonia (alveolar consolidation) versus bronchitis (airway-only inflammation) produce different voice/breath acoustic signatures.
- **Location:** Section 2.2.1, B04.
- **Hints:** Speech acoustics under parenchymal lung disease; cough acoustics in bronchitis vs pneumonia. May be a sparse evidence base.

### `sinusitis-hyponasality-acoustic`
- **Claim:** Sinusitis produces measurable hyponasality through paranasal resonance changes; other URIs produce more diffuse mucosal inflammation.
- **Location:** Section 2.2.1, B06.
- **Hints:** Hyponasality / nasometry literature; chronic rhinosinusitis voice studies; note that most published evidence is on chronic rhinosinusitis (J32) or nasal polyps (J33) with prompted stimuli, not acute J01 with spontaneous speech.

### `gas-pharyngitis-voice-articulation`
- **Claim:** Group A streptococcal pharyngitis produces tonsillar/pharyngeal inflammation altering oropharyngeal resonance, posterior-consonant articulation, and odynophagia-driven prosody.
- **Location:** Section 2.2.1, B07.
- **Hints:** Voice and articulation under acute pharyngeal inflammation; oropharyngeal resonance studies. Note: "hot potato voice" applies only to severe end (peritonsillar abscess); cite the milder mass-effect signature.

### `influenza-systemic-voice-changes`
- **Claim:** Influenza's systemic prodrome (fever, myalgia, fatigue) plausibly produces voice changes via reduced respiratory drive and fatigue, distinct from generic URI changes.
- **Location:** Section 2.2.1, B08.
- **Hints:** Voice / phonation studies under acute febrile illness; influenza-specific voice work if available.

### `covid19-voice-acoustic-prior-work`
- **Claim:** COVID-19 acoustic signature has been characterized in prior work, primarily on scripted speech and during pre-Omicron-dominant eras.
- **Location:** Section 2.2.1, B09.
- **Hints:** Anchor COVID-19 voice / cough detection papers (Cambridge COVID-19 Sounds, Coswara, COUGHVID studies). Overlaps with `covid-voice-cough-review` and `covid-19-sounds-xia-2021`.

### `bacterial-vs-viral-voice-literature-absent`
- **Claim:** The published literature on voice-based bacterial-versus-viral discrimination in adult primary care is essentially absent.
- **Location:** Section 2.2.1, B10.
- **Hints:** This citation should confirm a negative-result / literature-gap claim. The reference-finder should propose either (a) a systematic review establishing the gap, or (b) note that no such reference exists and the claim should stand without citation. Flag if the latter.

### Feature extraction (Section 2.3.1)

### `eyben-egemaps-2016`
- **Claim:** eGeMAPS acoustic feature set (Geneva Minimalistic Acoustic Parameter Set).
- **Location:** Section 2.3.1 (Audio Processing and Feature Extraction).
- **Hints:** Eyben et al., IEEE Transactions on Affective Computing, 2016. The seminal eGeMAPS paper.

### `eyben-opensmile-2010`
- **Claim:** openSMILE feature extraction toolkit.
- **Location:** Section 2.3.1.
- **Hints:** Eyben et al., openSMILE: The Munich Versatile and Fast Open-Source Audio Feature Extractor, ACM Multimedia 2010. The software paper.

### `librosa-mcfee-2015`
- **Claim:** librosa Python audio analysis library.
- **Location:** Section 2.3.1.
- **Hints:** McFee et al., librosa: Audio and music signal analysis in Python, SciPy 2015 conference paper. Version 0.11.0 is used.

### `wavlm-vad-odyssey-2024`
- **Claim:** WavLM-VAD-Odyssey2024 valence-arousal-dominance predictor.
- **Location:** Section 2.3.1.
- **Hints:** Speaker Odyssey 2024 workshop paper on a WavLM-based valence-arousal-dominance predictor. Search "WavLM VAD Odyssey 2024" or "speech emotion VAD WavLM".

### Table 1 additional dataset citations (Section 2.1.3, Table 1 rows)

### `botha-tb-cough-2018`
- **Claim:** Botha TB cough dataset, 38 subjects, voluntary cough in clinic, 2018.
- **Location:** Table 1 row.
- **Hints:** Botha et al. 2018, tuberculosis cough acoustic detection paper.

### `coswara-2020`
- **Claim:** Coswara dataset, 2,635 subjects, vowel + cough + breath + count, crowdsourced, COVID-19, 2020.
- **Location:** Table 1 row.
- **Hints:** Bhattacharya et al. 2020 (Indian Institute of Science), "Coswara — A Database of Breathing, Cough, and Voice Sounds for COVID-19 Diagnosis".

### `coughvid-2020`
- **Claim:** COUGHVID dataset, ~30,000 voluntary cough recordings, crowdsourced, COVID-19, 2020.
- **Location:** Table 1 row.
- **Hints:** Orlandic et al. 2020/2021 Scientific Data, COUGHVID dataset paper from EPFL.

### `nococoda-2020`
- **Claim:** NoCoCoDa dataset, 10 subjects / 73 cough events extracted from media interviews, COVID-19, 2020.
- **Location:** Table 1 row.
- **Hints:** Cohen-McFarlane et al. 2020 IEEE Access NoCoCoDa paper.

### `virufy-open-cough-2020`
- **Claim:** Virufy open cough dataset, 16 subjects / 121 voluntary cough recordings, COVID-19, 2020.
- **Location:** Table 1 row.
- **Hints:** Virufy / Stanford initiative; open cough dataset paper or technical report 2020.

### `dicova-1-2021`
- **Claim:** DiCOVA-1 dataset, 1,040 subjects, cough + breath + vowel + count, crowdsourced, COVID-19, 2021.
- **Location:** Table 1 row.
- **Hints:** Sharma et al. 2021 Interspeech / arXiv DiCOVA-1 challenge paper.

### `pahar-tb-cough-2021`
- **Claim:** Pahar TB cough dataset, 51 subjects / 1,358 cough events, voluntary cough + count + breath, clinic, 2021.
- **Location:** Table 1 row.
- **Hints:** Pahar et al. 2021 Computers in Biology and Medicine TB cough paper.

### `dicova-2-2022`
- **Claim:** DiCOVA-2 dataset, 1,436 subjects, cough + count + breath, crowdsourced, COVID-19, 2022.
- **Location:** Table 1 row.
- **Hints:** Sharma et al. 2022 Interspeech / IEEE DiCOVA-2 follow-up challenge paper.

### `tbscreen-2024`
- **Claim:** TBscreen dataset, 195 subjects / 34,600 cough events, passive + forced cough, clinic, TB + other respiratory, 2024.
- **Location:** Table 1 row.
- **Hints:** 2024 TB / respiratory cough screening paper, possibly in clinical or computational health journal.

---

## Section 4: Discussion

### `ics-dysphonia-laryngeal-deposition`
- **Claim:** Inhaled corticosteroid (ICS) therapy is known to produce dysphonia and voice quality changes through laryngeal deposition.
- **Location:** Section 4.4 (Limitations), B01 confound paragraph.
- **Hints:** Otolaryngology / pulmonology literature on ICS-induced dysphonia. Anchor refs include Williamson et al. (Eur Respir J on ICS local side effects), Galvan et al. (laryngeal deposition mechanism), or systematic reviews of ICS adverse effects on voice (jitter / shimmer / HNR changes).

### Candidate additional Discussion citations (not yet inserted)

The following claims in Discussion are substantive enough that a reviewer may flag them. Listed here for Vijay's review before insertion:

- **Line 245 (Summary):** "Prior voice-based respiratory work has predominantly used scripted speech ... or solicited cough produced on demand in controlled or semi-controlled settings." Already cited in Introduction (`covid-voice-cough-review`, `tb-cough-acoustic-screening`); may re-cite here for emphasis.
- **Line 256 (Confounder interpretation):** "Influenza is overwhelmingly concentrated in the winter months" — CDC FluView surveillance data.
- **Line 276 (Limitations):** "ICD coding fidelity varies by code and by setting" — ICD coding accuracy / validation literature.
- **Line 276 (Limitations):** "J18 pneumonia is typically coded after imaging confirmation; J02.0 streptococcal pharyngitis after rapid antigen or culture confirmation" — clinical practice; may be considered common knowledge.

---
