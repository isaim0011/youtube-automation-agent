# AGENT SPECIFICATION: Autonomous YouTube Production & Growth Agent

This document outlines the operational rules, algorithmic scoring models, workspace management, and asset generation workflows for AI Coding Assistants (Antigravity, Claude Code, Cursor, Copilot) managing YouTube channel growth.

---

## 1. Primary Objectives

### Maximize Expected Watch Time:
```math
E[\text{Watch Time}] = P(\text{Click} \mid \text{Thumbnail, Title}) \times E[\text{Duration} \mid \text{Content}] \times \text{Satisfaction Multiplier}
```

* **Zero-Touch Automated Delivery:**
  Autonomous transition from prompt engineering and asset generation to rendered 1080p Full HD video, high-CTR thumbnails, reverse-engineered metadata, and headless API upload.
* **Multi-Channel Workspace Cleanliness:**
  Strict isolation across channels (`channels/<Channel>/projects/<ID>/`) to ensure zero clutter, separated API tokens, and persistent project assets.
* **Loop-Fatigue Elimination:**
  Never output repetitive static loops. Sequence multi-shot footage with 30–60s macro-cycles and subtle color enhancement.

---

## 2. Workspace & Asset Generation Protocol

### A. Directory Structure
```text
<Workspace>/
└── channels/
    └── <Channel-Name>/
        ├── channel_config.json
        ├── uploader/ (youtubeuploader.exe, client_secrets.json, request.token)
        └── projects/
            └── <Project-ID>/ (raw_assets/, thumbnails/, output/, video_metadata.json)
```

### B. Google Flow & Veo Automation Integration
Before initiating creative generation, align with the user on:
* **Mode:** Text to Video (Veo 3/3.1) vs. Text to Image (Nano Banana Pro / 2 / 2 Lite)
* **Image Model:** `Nano Banana Pro` (Photorealistic 2K/4K) or `Nano Banana 2` (Balanced speed)
* **Video Model:** `Veo 3 / 3.1` (Cinematic physics & motion) or `Omni 1.1 Flash`
* **Aspect Ratio:** `16:9` (Long-form YouTube) vs. `9:16` (Shorts/TikTok)
* **Consistency:** Anchor prompts with persistent character clothing, lighting palette, and 3-angle shot cycling (Wide, Medium, Macro).

---

## 3. Statistical Decision Criteria

### Algorithmic Viability Score (AVS)
```math
AVS = (0.35 \times CTR_{est}) + (0.40 \times RET_{est}) + (0.25 \times SV_{norm})
```

* **`CTR_est` (0–100):** Visual contrast, mobile title readability (first 45 characters), curiosity gap.
* **`RET_est` (0–100):** Absence of jarring audio transients, seamless video looping, smooth cross-fades.
* **`SV_norm` (0–100):** Target keyword velocity in YouTube Suggested and Browse features over last 30 days.

> **Condition:** If `AVS < 78.0`, reject topic and request or generate alternative scenario.

---

## 4. Production Guidelines

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
* Target: Automatic JSON metadata ingestion (`video_metadata.json`).
