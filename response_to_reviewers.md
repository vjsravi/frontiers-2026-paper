Response to Reviewers

We thank both reviewers for their careful and constructive comments. They have helped us strengthen the manuscript. We have made a major revision and respond to each point below. For every accepted comment we point to the specific location in the revised manuscript or supplementary material. Where we could not make a change because the data or experiment was not available to us, we say so directly and record it as a limitation. Section, table, and figure numbers refer to the revised manuscript; items prefixed with S refer to the Supplementary Material.


REVIEWER 1

Summary

Reviewer: This manuscript presents a pilot study evaluating whether conversational ambient audio from routine adult primary care visits contains acoustic signal useful for respiratory triage. The study is ambitious and potentially important. Its main strengths are the unusually large dataset, the use of real-world conversational rather than scripted audio, the attempt to model clinically meaningful differential-diagnosis contrasts rather than simple sick-versus-healthy classification, and the inclusion of a panel-level confounder analysis. The manuscript is also clearly written and transparent in acknowledging several limitations. However, I recommend major revision before the manuscript can be considered suitable for publication. The central concern is that the current evidence supports the existence of weak-to-moderate acoustic signals, but does not yet support strong claims about clinical triage utility. Several methodological issues require clarification or additional analyses: the use of ICD-10 codes as labels without laboratory/radiographic confirmation, absence of external validation, potential site/clinic/coding artifacts, insufficient validation of the diarization and patient-speaker extraction pipeline, limited reproducibility due to unavailable data and unclear supplementary details, and incomplete evaluation of the composed hierarchical cascade.

Response: We thank the reviewer for the detailed comments. We have made a major revision and respond to each item below, pointing to where each change appears. Where a change could not be made because the data or experiment was not available to us, we say so directly and note it as a limitation.

Comment 1

Reviewer: The study relies on visit-level ICD-10 codes as the ground truth. This is understandable for a large retrospective dataset, but ICD-10 codes are not equivalent to confirmed diagnoses. The authors should provide stronger justification for each label group and discuss expected label noise by task. For example, pneumonia, streptococcal pharyngitis, COVID-19, and influenza may differ substantially in whether coding is supported by imaging, laboratory testing, rapid antigen testing, or clinical impression alone. The authors should specify, where possible, the proportion of cases supported by confirmatory tests or imaging, or explicitly state that such information was unavailable.

Response: We agree. ICD-10 codes are not equivalent to confirmed diagnoses, and the level of confirmation differs across conditions. For each visit we have only the audio and the ICD-10 codes; we do not have access to the underlying laboratory, antigen, or imaging results, so we cannot report the proportion of cases supported by confirmatory testing. We have stated this in the Limitations (Section 4.4) and noted that the level of confirmation is expected to differ by task, for example imaging for pneumonia, rapid antigen or culture for influenza and streptococcal pharyngitis, and clinical impression for acute sinusitis. The per-binary cohort definitions, including the coding-fidelity considerations for each contrast, are given in full in the Supplementary Material (Section 3).

Comment 2

Reviewer: The dataset is drawn from a single US primary care clinic network. Although geographically broad, this does not constitute external validation. The authors should either add an external validation cohort from another network/recording pipeline or substantially soften deployment-related language. At minimum, the manuscript should report site-level or state-level holdout experiments to estimate generalization across clinical settings.

Response: We agree that external validation is important. An external cohort at primary care scale is not available to us at this stage; we are collecting such data and will report it in future work. The dataset carries no clinic or site identifiers, only patient city and state, which we now state explicitly. We added two location analyses (Results Section 3.5). First, a city-grouped five-fold holdout in which whole cities are held out of training (Table 5): the gap between the random-split AUC and the mean held-out-city AUC is at most 0.020 on every binary, so discrimination on entirely unseen cities matches the random-split estimate. Second, a California-versus-rest experiment (Supplementary Section 8): performance is stable for the gate task (B00, 0.72 in both directions against a champion of 0.745) but falls close to chance for B05 and drops for the seasonal etiology binaries, consistent with the confounder findings. The absence of external validation is stated in the Limitations (Section 4.4). These results continue to support the main finding that conversational voice carries a discriminating signal for the respiratory contrasts tested.

Comment 3

Reviewer: The confounder analysis is a strength, but it also reveals important weaknesses. In particular, the pneumonia versus non-pneumonia lower respiratory infection task appears partly explained by patient-city or clinic-level coding patterns. The authors should provide additional analyses using clinic/site-level random effects, leave-one-city/site-out validation, or stratified performance by site. If clinic identifiers are unavailable, this limitation should be stated more explicitly.

Response: We do not have clinic or site identifiers; we have patient city and state, and we now state this explicitly (Results Section 3.5 and Discussion Section 4.2). The panel confounder analysis already reports B05 failing on patient city and on the state-by-city joint (Results Section 3.3), and the California-versus-rest experiment, in which B05 falls to near chance, corroborates it. We interpret B05 in Discussion Section 4.2 as reflecting the J22 unspecified-code documentation habits that are shared within clinics rather than a clean acoustic signal, and we point to B04 (pneumonia versus acute bronchitis, the same positive cohort against a cleaner negative cohort) as the more reliable pneumonia contrast. We do not draw any stronger conclusion than the available data support.

Comment 4

Reviewer: The manuscript depends critically on accurate extraction of patient speech from doctor-patient conversations. However, the speaker identification pipeline is not independently validated on manually annotated audio. The authors should provide a validation subset with manual speaker labels and report diarization error rate, patient-speaker assignment accuracy, and the effect of extraction errors on downstream features. Without this, it is difficult to assess whether the models are learning patient acoustic signals, clinician artifacts, encounter structure, or transcription/diarization artifacts.

Response: A manually annotated validation subset was outside the scope of this secondary analysis: the data-use agreement restricts use of the recordings to the aims of the approved protocol and does not permit sharing the audio with annotators or granting listening access for manual labeling. The pipeline therefore runs without manual speaker labels, as any deployed system would. We also searched for a published diarization error rate for the speech recognition model used and could not locate a verified figure. We have added this to the Limitations (Section 4.4), together with three features of the design that limit the influence of extraction errors on the reported contrasts: the same diarization pipeline is applied to every visit identically, so it does not introduce systematic differences between the two arms of a binary; the models use only acoustic and affective features computed from the audio and do not use the transcript content, word identity, or text embeddings, so they cannot exploit what was said; and every binary contrasts one symptomatic group against another, so structural differences between healthy and ill speech do not apply.

Comment 5

Reviewer: The manuscript states that balancing, patient-level splitting, five-fold cross-validation, hyperparameter selection, and final test evaluation were used. The authors should provide a clearer step-by-step diagram or pseudocode showing exactly when balancing occurs relative to splitting, how repeated visits from the same patient are handled across all 11 tasks, and whether any patient can appear in training for one binary and testing for another when cascade examples are generated. The current description is mostly plausible, but not sufficiently audit-ready.

Response: We have added two algorithms to the Methods. Algorithm 1 (Section 2.3.2) sets out the per-binary procedure: class balancing at the patient level before any split, a 30 percent patient-level test set frozen until final evaluation, five-fold cross-validation on the remaining patients, threshold selection by Youden's J on the development partition, model selection on development loss, and a single evaluation on the frozen test set. Algorithm 2 (Section 2.3.4) sets out the leak-safe cascade cohort, which excludes at the patient level any patient who contributed a visit to the training or development partition of any of the 11 binaries. We also state that a patient held out in one binary's test set may appear in another binary's training set, which is not leakage because each model excludes its own test patients from its own training set and no reported per-task metric combines models. We describe the procedure as leakage-safe but not a fully nested cross-validation, because hyperparameters were selected on a single development split and the selected configuration was then retrained under five-fold cross-validation.

Comment 6

Reviewer: AUC values between 0.602 and 0.745 indicate modest discrimination. For triage applications, sensitivity, specificity, PPV, NPV, likelihood ratios, decision curves, and calibration across clinically realistic prevalence settings are more informative than AUC alone. The authors should add clinically meaningful threshold analyses, especially for high-risk conditions such as pneumonia, COVID-19, influenza, and bacterial versus viral infection.

Response: We have added these. Results Section 3.2 and Table 3 report sensitivity, specificity, positive and negative likelihood ratios, and PPV and NPV at the operating point; 95% bootstrap confidence intervals (1000 resamples) for all of these metrics are reported in the Supplementary Material. The Supplementary Material projects PPV and NPV across a prevalence grid and each contrast's natural prevalence (Section 5, Table S3). Calibration is reported by expected calibration error and Brier score (Table 2). Decision-curve analysis for all 11 binaries is reported in the Supplementary Material (Section 6, Figure S5). We note in Results Section 3.2 that the likelihood ratios are modest across the panel, that none reaches the conventional threshold for a clinically decisive test, and that at the natural prevalence of the low-prevalence contrasts (influenza and COVID-19) the plausible use is rule-out rather than rule-in.

Comment 7

Reviewer: The cascade is presented as proof-of-concept, but the aggregate performance is weak: only a small proportion of cases are fully correct. The authors should avoid language suggesting readiness for clinical reasoning or decision support. The cascade should be framed as an exploratory demonstration only. More detailed error analysis is needed, including which nodes contribute most to failure and whether joint training or probabilistic propagation would improve performance.

Response: We have toned down the cascade throughout. It is now described as an exploratory demonstration that the independently trained classifiers can be composed, not as a system ready for clinical use (Discussion Section 4.3 and the Conclusion). We rebuilt the cascade reproducibly and report the patient-level leak-safe results (n = 868; 20.6 percent reached the correct anatomical terminal, 42.1 percent the correct etiology call, and 8.6 percent were fully correct, above a random-gate baseline of 13.1, 23.5, and 3.3 percent). We report the per-gate accuracies and explain the compositional error propagation that makes the composed cascade underperform the per-binary models. A full node-level error analysis belongs with a dedicated study of the cascade, together with joint training and probabilistic propagation, which we identify as future work (Section 4.5). We did not include it here so that the cascade remains in its intended exploratory role.

Comment 8

Reviewer: The manuscript would be stronger if it showed which acoustic feature streams contribute to each binary task. Ablation by feature family e.g., pitch, spectral, voice quality, prosodic, temporal, affective/VAD features would help determine whether the models learn biologically plausible respiratory signals or dataset artifacts.

Response: We added a feature-family ablation (Results Section 3.4 and Table 4; full leave-one-family-out and single-family tables in Supplementary Section 7). The librosa stream carries most of the discrimination on every binary, and the speech-rate and pause family contributes negligibly, which argues against the concern that performance reflects a recording-length artifact rather than acoustic content. We note that the ablation uses a single cross-validation fold, so differences below approximately 0.01 are within run-to-run variation.

Comment 9

Reviewer: The raw audio cannot reasonably be shared due to privacy, but the derived datasets are also proprietary. This limits independent verification. The authors should provide as much reproducibility support as possible: complete ICD-10 cohort definitions, feature extraction scripts, model code, hyperparameter grids, preprocessing parameters, and synthetic or aggregate feature distributions. If the supplementary material contains these details, the main text should explicitly summarize what is available.

Response: We added a Reproducibility subsection (Section 2.4) that points to each specification item and states that the pipeline uses only publicly available components: openSMILE eGeMAPSv02, librosa, a publicly available valence-arousal-dominance predictor, praat-parselmouth, and a standard feed-forward network. The ICD-10 cohort definitions are in Section 2.2 and Supplementary Section 3; the diarization and preprocessing parameters in Section 2.3.1 and the Supplementary Material; the feature-extraction configuration in Section 2.3.1 and the Supplementary Material; the architecture in Section 2.3.2 and Figure 2; and the full hyperparameter grid and training settings in Supplementary Table S1. We added per-class aggregate distributions of all 412 features for every binary to the Supplementary Material (Section 9); these are summary statistics with no per-visit values or identifiers and can be released without disclosing protected health information. The only items that cannot be shared are the raw audio and the visit-level derived feature tables, both of which are protected health information.

Comment 10

Reviewer: Both authors are employees and equity holders of the company funding the study. This does not invalidate the work, but because the study concerns a potentially commercial clinical AI technology, the manuscript should strengthen transparency around governance, independent oversight, data access, and whether any analyses were independently audited.

Response: We expanded the governance disclosures. The Ethics Statement describes the independent IRB review and exempt determination, the HIPAA authorization waiver with its regulatory citations, the patient opt-out mechanism through the originating network's Notice of Privacy Practices, and the data-use agreement that prohibits re-identification, and now adds that all audio and derived data were stored and processed only within a controlled cloud environment, with no local downloads and no storage on personal devices. The Conflict of Interest Statement discloses the authors' employment and equity in the funding company, states that the cohort definitions for all 11 binaries were specified in advance and that codes were not added or removed to change class sizes or to improve discriminability, refers to the named Principal Investigator responsible for the IRB-approved protocol (Acknowledgments), and states plainly that the analyses were not independently audited by a party outside the author team and that there was no external oversight board beyond the IRB review.

Strengths

Reviewer: The study addresses an important and timely problem: whether passively recorded clinical speech can support respiratory triage in primary care. The dataset size is a major strength, far exceeding most prior voice/cough respiratory studies. The use of conversational ambient audio is also highly relevant to real clinical deployment, since most prior work uses scripted speech or solicited cough. The task design is clinically more realistic than simple disease-versus-healthy classification because it focuses on differential diagnoses among symptomatic patients. The authors also deserve credit for including calibration metrics, confidence intervals, patient-stratified evaluation, and explicit non-acoustic confounder baselines.

Response: We thank the reviewer for these comments.

Limitations

Reviewer: The main limitations are substantial. First, ICD-10 codes are imperfect labels and may encode clinician/site documentation habits rather than true disease states. Second, there is no external validation outside the source clinic network. Third, the diarization and patient-channel extraction pipeline is not manually validated. Fourth, some important confounders are not fully addressed, including clinic/site, recording device, microphone distance, language/accent, race/ethnicity, comorbidities, medication exposure, and symptom severity. Fifth, the absolute performance is moderate, with several AUCs close to 0.60, limiting immediate clinical usefulness. Sixth, the hierarchical cascade compounds errors and currently performs too weakly to support clinical deployment claims. Finally, the proprietary nature of the data and derived datasets limits reproducibility.

Response: We agree with these limitations and address each in the numbered responses above and in the Limitations (Section 4.4). We expanded the Limitations to name the further confounders the reviewer lists, which are recording device, microphone distance, language and accent, race and ethnicity, comorbidities, medication exposure, and symptom severity, and to state that we do not have the metadata to model most of them.

Evaluation of methods

Reviewer: The overall methodological framework is reasonable for a pilot signal-detection study. Patient-level splitting, cross-validation, bootstrapped confidence intervals, calibration assessment, and confounder baselines are appropriate. However, several aspects need strengthening. The authors should clarify whether hyperparameter selection is fully nested and leakage-safe, whether class balancing was performed only within training folds, and whether all test sets remain untouched until final evaluation. The statistical analysis would also benefit from more clinically grounded metrics and uncertainty estimates for threshold-dependent outcomes.

Response: We answer the three questions in Section 2.3.2 and Algorithm 1. Class balancing is performed before splitting, by patient-level downsampling; the 30 percent patient-level test set is held out before balancing, hyperparameter selection, and threshold selection, and is scored once at final evaluation; hyperparameter selection and the Youden threshold are computed on the development partition only. The procedure is leakage-safe but not a fully nested cross-validation, because hyperparameters were selected on a single development split and the selected configuration was then retrained under five-fold cross-validation. We added the clinically grounded metrics and threshold-dependent uncertainty: Section 3.2 and Table 3, with 95% bootstrap confidence intervals for all operating-point metrics reported in the Supplementary Material.

Evaluation of results and interpretation

Reviewer: The results show that conversational speech contains some discriminative signal for several respiratory contrasts. However, the magnitude of performance is modest. The strongest task reaches AUC 0.745, while several clinically important tasks are near AUC 0.60-0.63. Therefore, the data support the conclusion that acoustic signal exists, but not that the system is clinically actionable. The authors generally acknowledge this, but some parts of the manuscript should be toned down to avoid overstatement. The interpretation should emphasize "pilot acoustic signal detection" rather than "clinical respiratory triage."

Response: We agree that the data support the existence of an acoustic signal, not clinical actionability. We revised the manuscript to make this distinction clear and to emphasize pilot acoustic signal detection rather than clinical respiratory triage. The abstract, Discussion, and Conclusion frame the work as a pilot and proof-of-concept, and the Conclusion states that substantial further work, including external validation, prospective evaluation, label-quality strengthening, and joint training, is required before any operational claim can be supported.


REVIEWER 2

Summary

Reviewer: The manuscript presents a voice-based clinical AI framework for respiratory disease triage using conversational primary care audio. Eleven binary classification tasks are modeled using feed-forward neural networks, and the resulting classifiers are combined into a hierarchical cascade to distinguish clinically relevant respiratory conditions. Although the large-scale dataset collection is commendable, the manuscript has several methodological and presentation concerns that need to be addressed.

Response: We thank the reviewer. We have revised the manuscript for clarity, organization, and presentation, and respond to each point below.

Comment 1

Reviewer: The first paragraph of the Introduction lacks clarity and should be revised for better coherence.

Response: We revised the opening of the Introduction. It now leads with the epidemiology of respiratory complaints in primary care and then, in a separate paragraph, the consequences of mistriage, with the long sentences broken up.

Comment 2

Reviewer: Punctuation errors are present and should be corrected throughout the manuscript.

Response: We reviewed the manuscript and corrected punctuation where found.

Comment 3

Reviewer: Many sentences are too long and cumbersome and should be revised for improved clarity and readability.

Response: We shortened several long sentences across the Introduction and Methods, splitting them at natural boundaries without changing their content.

Comment 4

Reviewer: Avoid the use of bold text in the manuscript for consistency with the journal's formatting style.

Response: We removed the emphasis bold from the contribution list, the task descriptions, and the algorithm step labels. We retained only structural formatting (the structured-abstract labels and table and figure labels), which follows the journal template.

Comment 5

Reviewer: There is no clear description of the age distribution or inclusion criteria of the patients in the collected dataset.

Response: The adult inclusion criterion (patients at least 18 years of age) and the age distribution are now summarized in the main Dataset section (median age 38 years, interquartile range 28 to 55, range 18 to 106), with the full distribution in Supplementary Section 1.

Comment 6

Reviewer: The criteria used for speaker segmentation are not clearly specified and should be described in detail.

Response: We describe the speaker diarization in the main Methods (Section 2.3.1): one to two expected speakers, English recognition, word-level timestamps, merging of consecutive same-speaker words into segments, and identification of the patient as the primary subject of the visit rather than a caregiver, translator, or other participant. The full parameters are in Supplementary Section 2.

Comment 7

Reviewer: The dataset information provided only in the supplementary material should be briefly summarized in the manuscript for better clarity and completeness.

Response: We added a demographic, geographic, and audio-duration summary of the analytic sample to the main Dataset section, and a reproducibility summary (Section 2.4) that points to the supplementary items.

Comment 8

Reviewer: The manuscript does not clearly explain how the collected dataset facilitates disease identification and how the labels are associated with the corresponding acoustic features.

Response: We added a statement in the Methods (Section 2.3) that each visit contributes one labeled example per binary: the label is determined by the visit's primary ICD-10 code under the cohort rules of Section 2.2, and the input is the 412-dimensional acoustic feature vector computed from that visit's patient speech; the models are trained to map the feature vector to the binary label.

Comment 9

Reviewer: Representative samples illustrating the audio signals before and after preprocessing should be included.

Response: The recordings are protected health information and cannot be published, so representative waveforms or spectrograms are not shown; we state this in Section 2.4. We also note that no signal-level preprocessing (denoising or amplitude normalization) is applied beyond diarization, so there is no before-and-after transformation of the signal itself to display.

Comment 10

Reviewer: Representative samples of the extracted features provided as input to the FFN are missing and should be included.

Response: Per-visit feature vectors cannot be shared because they are protected health information. In their place we added per-class aggregate distributions of all 412 features for all 11 binaries to the Supplementary Material (Section 9), which contain no per-visit values or identifiers and can be released.

Comment 11

Reviewer: The FFN model description lacks clarity; a simple architectural diagram illustrating the layers and a table summarizing the hyperparameter settings should be included instead of presenting all details in text.

Response: We added an architecture diagram (Figure 2) showing the input feature vector, the hidden blocks (linear, batch normalization, GELU, dropout), and the output logit, and a hyperparameter settings table (Supplementary Table S1).

Comment 12

Reviewer: Overall, the manuscript requires significant improvements in clarity, organization, and presentation to enhance its readability and comprehensibility.

Response: We revised the manuscript for clarity and consistency throughout, including standardizing terminology (AUC used consistently across the main text and the supplementary material) and notation.


We thank the reviewers again for their time and for comments that have improved the manuscript.
