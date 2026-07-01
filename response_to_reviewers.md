# Response to Reviewers

We thank both reviewers for their careful and constructive comments. They have helped us strengthen the manuscript. We have made a major revision and respond to each point below. For every accepted comment we point to the specific location in the revised manuscript or supplementary material. Where we could not make a change because the data or experiment was not available to us, we say so directly and record it as a limitation. Section, table, and figure numbers refer to the revised manuscript; items prefixed with S refer to the Supplementary Material.


## Reviewer 1

**1. ICD-10 codes as labels without laboratory or radiographic confirmation; expected label noise by task.**

We agree. ICD-10 codes are not equivalent to confirmed diagnoses, and the level of confirmation differs across conditions. For each visit we have only the audio and the ICD-10 codes; we do not have access to the underlying laboratory, antigen, or imaging results, so we cannot report the proportion of cases supported by confirmatory testing. We have stated this in the Limitations (Section 4.4) and noted that the level of confirmation is expected to differ by task, for example imaging for pneumonia, rapid antigen or culture for influenza and streptococcal pharyngitis, and clinical impression for acute sinusitis. The per-binary cohort definitions, including the coding-fidelity considerations for each contrast, are given in full in the Supplementary Material (Section 3).

**2. Single network is not external validation; add an external cohort or site- or state-level holdout.**

We agree that external validation is important. An external cohort at primary care scale is not available to us at this stage; we are collecting such data and will report it in future work. The dataset carries no clinic or site identifiers, only patient city and state, which we now state explicitly. We added two location analyses (Results Section 3.5). First, a city-grouped five-fold holdout in which whole cities are held out of training (Table 5): the gap between the random-split AUC and the mean held-out-city AUC is at most 0.020 on every binary, so discrimination on entirely unseen cities matches the random-split estimate. Second, a California-versus-rest experiment (Supplementary Section 8): performance is stable for the gate task (B00, 0.72 in both directions against a champion of 0.745) but falls close to chance for B05 and drops for the seasonal etiology binaries, consistent with the confounder findings. The absence of external validation is stated in the Limitations (Section 4.4). These results continue to support the main finding that conversational voice carries a discriminating signal for the respiratory contrasts tested.

**3. Confounder analysis reveals a clinic- or city-level effect for pneumonia versus non-pneumonia lower respiratory infection (B05).**

We do not have clinic or site identifiers; we have patient city and state, and we now state this explicitly (Results Section 3.5 and Discussion Section 4.2). The panel confounder analysis already reports B05 failing on patient city and on the state-by-city joint (Results Section 3.3), and the California-versus-rest experiment, in which B05 falls to near chance, corroborates it. We interpret B05 in Discussion Section 4.2 as reflecting the J22 unspecified-code documentation habits that are shared within clinics rather than a clean acoustic signal, and we point to B04 (pneumonia versus acute bronchitis, the same positive cohort against a cleaner negative cohort) as the more reliable pneumonia contrast. We do not draw any stronger conclusion than the available data support.

**4. The diarization and patient-speaker extraction pipeline is not validated on manually annotated audio.**

Manual speaker labeling of this dataset, even on a small subset, was not possible for us because the recordings are protected health information. We searched for a published diarization error rate for the speech recognition model used and could not locate a verified figure. We have added this to the Limitations (Section 4.4), together with three features of the design that limit the influence of extraction errors on the reported contrasts: the same diarization pipeline is applied to every visit identically, so it does not introduce systematic differences between the two arms of a binary; the models use only acoustic and affective features computed from the audio and do not use the transcript content, word identity, or text embeddings, so they cannot exploit what was said; and every binary contrasts one symptomatic group against another, so structural differences between healthy and ill speech do not apply.

**5. Provide audit-ready pseudocode; when balancing occurs relative to splitting; cross-task patient overlap in the cascade.**

We have added two algorithms to the Methods. Algorithm 1 (Section 2.3.2) sets out the per-binary procedure: class balancing at the patient level before any split, a 30 percent patient-level test set frozen until final evaluation, five-fold cross-validation on the remaining patients, threshold selection by Youden's J on the development partition, model selection on development loss, and a single evaluation on the frozen test set. Algorithm 2 (Section 2.3.4) sets out the leak-safe cascade cohort, which excludes at the patient level any patient who contributed a visit to the training or development partition of any of the 11 binaries. We also state that a patient held out in one binary's test set may appear in another binary's training set, which is not leakage because each model excludes its own test patients from its own training set and no reported per-task metric combines models. We describe the procedure as leakage-safe but not a fully nested cross-validation, because hyperparameters were selected on a single development split and the selected configuration was then retrained under five-fold cross-validation.

**6. AUC alone is insufficient; add sensitivity, specificity, PPV, NPV, likelihood ratios, decision curves, and calibration across realistic prevalence.**

We have added these. Results Section 3.2 and Table 3 report sensitivity, specificity, positive and negative likelihood ratios, and PPV and NPV at the operating point, with bootstrap confidence intervals. The Supplementary Material projects PPV and NPV across a prevalence grid and each contrast's natural prevalence (Section 5, Table S3). Calibration is reported by expected calibration error and Brier score (Table 2). Decision-curve analysis for all 11 binaries is reported in the Supplementary Material (Section 6, Figure S5). We note in Results Section 3.2 that the likelihood ratios are modest across the panel, that none reaches the conventional threshold for a clinically decisive test, and that at the natural prevalence of the low-prevalence contrasts (influenza and COVID-19) the plausible use is rule-out rather than rule-in.

**7. The cascade is weak; frame it as exploratory; provide node-level error analysis.**

We have toned down the cascade throughout. It is now described as an exploratory demonstration that the independently trained classifiers can be composed, not as a system ready for clinical use (Discussion Section 4.3 and the Conclusion). We rebuilt the cascade reproducibly and report the patient-level leak-safe results (n = 868; 20.6 percent reached the correct anatomical terminal, 42.1 percent the correct etiology call, and 8.6 percent were fully correct, above a random-gate baseline of 13.1, 23.5, and 3.3 percent). We report the per-gate accuracies and explain the compositional error propagation that makes the composed cascade underperform the per-binary models. A full node-level error analysis belongs with a dedicated study of the cascade, together with joint training and probabilistic propagation, which we identify as future work (Section 4.5). We did not include it here so that the cascade remains in its intended exploratory role.

**8. Show which feature families contribute to each binary.**

We added a feature-family ablation (Results Section 3.4 and Table 4; full leave-one-family-out and single-family tables in Supplementary Section 7). The librosa stream carries most of the discrimination on every binary, and the speech-rate and pause family contributes negligibly, which argues against the concern that performance reflects a recording-length artifact rather than acoustic content. We note that the ablation uses a single cross-validation fold, so differences below approximately 0.01 are within run-to-run variation.

**9. Provide as much reproducibility support as possible; summarize what is available in the main text.**

We added a Reproducibility subsection (Section 2.4) that points to each specification item and states that the pipeline uses only publicly available components: openSMILE eGeMAPSv02, librosa, a publicly available valence-arousal-dominance predictor, praat-parselmouth, and a standard feed-forward network. The ICD-10 cohort definitions are in Section 2.2 and Supplementary Section 3; the diarization and preprocessing parameters in Section 2.3.1 and the Supplementary Material; the feature-extraction configuration in Section 2.3.1 and the Supplementary Material; the architecture in Section 2.3.2 and Figure 2; and the full hyperparameter grid and training settings in Supplementary Table S1. We added per-class aggregate distributions of all 412 features for every binary to the Supplementary Material (Section 9); these are summary statistics with no per-visit values or identifiers and can be released without disclosing protected health information. The only items that cannot be shared are the raw audio and the visit-level derived feature tables, both of which are protected health information.

**10. Strengthen transparency around governance, oversight, data access, and independent audit.**

We expanded the governance disclosures. The Ethics Statement describes the independent IRB review and exempt determination, the HIPAA authorization waiver with its regulatory citations, the patient opt-out mechanism through the originating network's Notice of Privacy Practices, and the data-use agreement that prohibits re-identification, and now adds that all audio and derived data were stored and processed only within a controlled cloud environment, with no local downloads and no storage on personal devices. The Conflict of Interest Statement discloses the authors' employment and equity in the funding company, states that the cohort definitions for all 11 binaries were specified in advance and that codes were not added or removed to change class sizes or to improve discriminability, refers to the named Principal Investigator responsible for the IRB-approved protocol (Acknowledgments), and states plainly that the analyses were not independently audited by a party outside the author team and that there was no external oversight board beyond the IRB review.

**Strengths.** We thank the reviewer for recognizing the dataset scale, the use of conversational ambient audio, the differential-diagnosis task design, and the inclusion of calibration, confidence intervals, patient-stratified evaluation, and confounder baselines.

**Limitations (reviewer summary).** We agree with the limitations listed and address each in the numbered responses above and in the Limitations (Section 4.4). We expanded the Limitations to name the further confounders the reviewer lists, which are recording device, microphone distance, language and accent, race and ethnicity, comorbidities, medication exposure, and symptom severity, and to state that we do not have the metadata to model most of them.

**Evaluation of methods.** We answer the three questions in Section 2.3.2 and Algorithm 1. Class balancing is performed before splitting, by patient-level downsampling; the 30 percent patient-level test set is held out before balancing, hyperparameter selection, and threshold selection, and is scored once at final evaluation; hyperparameter selection and the Youden threshold are computed on the development partition only. As stated above, the procedure is leakage-safe but not a fully nested cross-validation. We added the clinically grounded metrics and threshold-dependent uncertainty (Section 3.2, Table 3).

**Evaluation of results and interpretation.** We agree that the data support the existence of an acoustic signal, not clinical actionability. We revised the manuscript to make this distinction clear and to emphasize pilot acoustic signal detection rather than clinical respiratory triage. The abstract, Discussion, and Conclusion frame the work as a pilot and proof-of-concept, and the Conclusion states that substantial further work, including external validation, prospective evaluation, label-quality strengthening, and joint training, is required before any operational claim can be supported.


## Reviewer 2

**The first paragraph of the Introduction lacks clarity.**
We revised the opening of the Introduction. It now leads with the epidemiology of respiratory complaints in primary care and then, in a separate paragraph, the consequences of mistriage, with the long sentences broken up.

**Punctuation errors throughout.**
We reviewed the manuscript and corrected punctuation where found.

**Many sentences are too long and cumbersome.**
We shortened several long sentences across the Introduction and Methods, splitting them at natural boundaries without changing their content.

**Avoid the use of bold text.**
We removed the emphasis bold from the contribution list, the task descriptions, and the algorithm step labels. We retained only structural formatting (the structured-abstract labels and table and figure labels), which follows the journal template.

**No clear description of the age distribution or inclusion criteria.**
The adult inclusion criterion (patients at least 18 years of age) and the age distribution are now summarized in the main Dataset section (median age 38 years, interquartile range 28 to 55, range 18 to 106), with the full distribution in Supplementary Section 1.

**Criteria for speaker segmentation are not clearly specified.**
We describe the speaker diarization in the main Methods (Section 2.3.1): one to two expected speakers, English recognition, word-level timestamps, merging of consecutive same-speaker words into segments, and identification of the patient as the primary subject of the visit rather than a caregiver, translator, or other participant. The full parameters are in Supplementary Section 2.

**Dataset information given only in the supplementary should be summarized in the main text.**
We added a demographic, geographic, and audio-duration summary of the analytic sample to the main Dataset section, and a reproducibility summary (Section 2.4) that points to the supplementary items.

**Explain how the dataset facilitates disease identification and how labels relate to acoustic features.**
We added a statement in the Methods (Section 2.3) that each visit contributes one labeled example per binary: the label is determined by the visit's primary ICD-10 code under the cohort rules of Section 2.2, and the input is the 412-dimensional acoustic feature vector computed from that visit's patient speech; the models are trained to map the feature vector to the binary label.

**Representative audio samples before and after preprocessing.**
The recordings are protected health information and cannot be published, so representative waveforms or spectrograms are not shown; we state this in Section 2.4. We also note that no signal-level preprocessing (denoising or amplitude normalization) is applied beyond diarization, so there is no before-and-after transformation of the signal itself to display.

**Representative samples of the extracted features.**
Per-visit feature vectors cannot be shared because they are protected health information. In their place we added per-class aggregate distributions of all 412 features for all 11 binaries to the Supplementary Material (Section 9), which contain no per-visit values or identifiers and can be released.

**FFN model description; add an architectural diagram and a hyperparameter table.**
We added an architecture diagram (Figure 2) showing the input feature vector, the hidden blocks (linear, batch normalization, GELU, dropout), and the output logit, and a hyperparameter settings table (Supplementary Table S1).

**Overall clarity, organization, and presentation.**
We revised the manuscript for clarity and consistency throughout, including standardizing terminology (AUC used consistently across the main text and the supplementary material) and notation.


We thank the reviewers again for their time and for comments that have improved the manuscript.
