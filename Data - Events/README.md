\# Particle Physics Event Classification Dataset



Accurately separating rare \*\*signal (s)\*\* events from abundant \*\*background (b)\*\* is central to particle physics.  

This dataset contains reconstructed kinematic features from collider-like events and a per-event \*\*Weight\*\* to reflect experimental importance. The task is \*\*binary classification\*\*: predict whether an event is \*\*signal (`s`)\*\* or \*\*background (`b`)\*\*.



---



\## 📦 Contents



\- \*\*Rows:\*\* 250,001  

\- \*\*Columns:\*\* 33 (including `EventId`, `Weight`, and `Target`)  

\- \*\*Target:\*\* `Target` ∈ {`s`, `b`}  

\- \*\*Weight:\*\* continuous, used as `sample\_weight` during training and for \*\*weighted\*\* evaluation



---



\## 🔬 Feature Dictionary (summary)



\*\*Identifiers \& label\*\*

\- `EventId`: unique event identifier  

\- `Target`: `s` (signal) or `b` (background)  

\- `Weight`: per-event importance (use in training \& metrics)



\*\*Derived physics features\*\*

\- `DER\_mass\_MMC`: Missing Mass Calculator mass  

\- `DER\_mass\_transverse\_met\_lep`: Transverse mass from MET and lepton  

\- `DER\_mass\_vis`: Visible system mass  

\- `DER\_pt\_h`: Higgs-candidate transverse momentum  

\- `DER\_deltaeta\_jet\_jet`: |Δη| between two leading jets  

\- `DER\_mass\_jet\_jet`: Dijet mass  

\- `DER\_lep\_eta\_centrality`: Lepton η centrality w.r.t. jets



\*\*Primary objects (τ and ℓ)\*\*

\- `PRI\_tau\_pt`, `PRI\_tau\_eta`, `PRI\_tau\_phi`: tau kinematics  

\- `PRI\_lep\_pt`, `PRI\_lep\_eta`, `PRI\_lep\_phi`: lepton (e/μ) kinematics



\*\*Missing transverse energy (MET)\*\*

\- `PRI\_met`: MET magnitude  

\- `PRI\_met\_phi`: MET azimuth  

\- `PRI\_met\_sumet`: sum of transverse energy of all objects



\*\*Jets\*\*

\- `PRI\_jet\_num`: number of jets (integer)  

\- `PRI\_jet\_leading\_pt`, `PRI\_jet\_leading\_eta`, `PRI\_jet\_leading\_phi`: leading jet  

\- `PRI\_jet\_subleading\_pt`, `PRI\_jet\_subleading\_eta`, `PRI\_jet\_subleading\_phi`: subleading jet  

\- `PRI\_jet\_all\_pt`: sum of pT of all jets



---



\## 🎯 Task \& Recommended Metrics



\- \*\*Task:\*\* Binary classification (`s` vs `b`)  

\- \*\*Primary metric:\*\* \*\*Weighted ROC-AUC\*\* (use `Weight` as `sample\_weight`)  

\- \*\*Additional:\*\* Weighted logloss, F1 (weighted), PR-AUC, and physics-aware \*\*AMS\*\* (Approximate Median Significance) computed from weighted TP/FP at a chosen threshold.

