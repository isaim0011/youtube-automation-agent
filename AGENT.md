# AGENT SPECIFICATION: Autonomous YouTube Production & Growth Agent

This document outlines the operational rules, algorithmic scoring models, and execution workflows for AI Coding Assistants (Antigravity, Claude Code, Cursor, Copilot) managing YouTube channel growth.

---

## 1. Primary Objectives
1. **Maximize Expected Watch Time:**
   $$\mathbb{E}[\text{Watch Time}] = P(\text{Click} \mid \text{Thumbnail, Title}) \times \mathbb{E}[\text{Duration} \mid \text{Content}] \times \text{Satisfaction Multiplier}$$
2. **Zero-Touch Automated Delivery:**
   Autonomous transition from raw generated clips & audio to rendered 1080p Full HD video, high-CTR thumbnails, reverse-engineered metadata, and headless API upload.
3. **Loop-Fatigue Elimination:**
   Never output repetitive static loops. Sequence multi-shot footage with 30–60s macro-cycles and subtle color enhancement.

---

## 2. Statistical Decision Criteria

### Algorithmic Viability Score (AVS)
$$\text{AVS} = (0.35 \times \text{CTR}_{\text{est}}) + (0.40 \times \text{RET}_{\text{est}}) + (0.25 \times \text{SV}_{\text{norm}})$$

* **$\text{CTR}_{\text{est}}$ (0–100):** Visual contrast, mobile title readability (first 45 characters), curiosity gap.
* **$\text{RET}_{\text{est}}$ (0–100):** Absence of jarring audio transients, seamless video looping, smooth cross-fades.
* **$\text{SV}_{\text{norm}}$ (0–100):** Target keyword velocity in YouTube Suggested & Browse features over last 30 days.

*Condition:* If $\text{AVS} < 78.0$, reject topic and request or generate alternative scenario.

---

## 3. Production Guidelines

### Video Assembly
* **Engine:** FFmpeg 7.x / Diffusion Studio CLI
* **Bitrate:** High-profile H.264, CRF 20–22, preset `veryfast` or `medium`
* **Color Grading:** Warm atmospheric enhancement (`eq=contrast=1.08:saturation=1.15`)
* **Audio:** 256 kbps AAC minimum, -14 LUFS target loudness, 2s lead-in fade, 3s outro fade

### Thumbnails
* Always produce two variants at 1280x720:
  * **Clean Immersion:** Unadorned, high-aesthetic photographic frame.
  * **Branded Badge:** High-contrast pill badge with channel name, concise topic title, and duration badge.

### Headless Upload Workflow
* Tool: `porjo/youtubeuploader`
* Flag: `-cache request.token` for persistent headless execution.
* Ensure Google Cloud project has YouTube Data API v3 enabled and email added under Test Users.
