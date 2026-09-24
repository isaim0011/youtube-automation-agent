# UNIVERSAL AGENT SPECIFICATION: Autonomous YouTube Production & Growth Framework

This specification outlines the operational protocols, mathematical scoring algorithms, workspace architectures, and asset generation pipelines for **any AI Coding Assistant** (Google Antigravity, Claude Code, Cursor, Copilot, Codex, Aider, OpenDevin) managing automated YouTube channel operations.

---

## 1. Universal Agent Objectives

### Expected Watch Time Maximization Formula:
```math
E[\text{Watch Time}] = P(\text{Click} \mid \text{Thumbnail, Title}) \times E[\text{Duration} \mid \text{Content}] \times \text{Satisfaction Multiplier}
```

* **Zero-Touch Automated Delivery:**
  Autonomous transition from prompt engineering and asset generation to rendered 1080p Full HD video, high-CTR thumbnails, reverse-engineered metadata, and headless API upload.
* **Multi-Channel Workspace Cleanliness:**
  Strict isolation across channels (`channels/<Channel>/projects/<ID>/`) to ensure zero clutter, separated API tokens, and persistent project assets.
* **No Raw Edits:**
  Never perform fragile, manual video hacks. Delegate editing to **Diffusion Studio** (`diffusionstudio/editor`) via Model Context Protocol (MCP) or CLI (`dapi`).
* **Loop-Fatigue Elimination:**
  Never output repetitive static loops. Sequence multi-shot footage with 30–60s macro-cycles and subtle color enhancement.

---

## 2. Multi-Channel Workspace Hierarchy

```text
<Workspace-Root>/
└── channels/
    ├── <Channel-A>/
    │   ├── channel_config.json          # Brand handles, default tags, color schemes
    │   ├── uploader/                    # youtubeuploader.exe, client_secrets.json, request.token
    │   └── projects/
    │       ├── 001_Rainy_Car_Drive/
    │       │   ├── raw_assets/          # Raw WAVs, MP4 clips, prompt logs
    │       │   ├── thumbnails/          # 1280x720 clean & badged JPGs
    │       │   ├── output/              # Final rendered 1080p video
    │       │   └── video_metadata.json  # Exact SEO title, chapters, tags
    │       └── 002_Sunset_Rooftop_Lounge/
    │           ├── raw_assets/
    │           ├── thumbnails/
    │           ├── output/
    │           └── video_metadata.json
    └── <Channel-B>/                     # Full multi-channel network isolation
        └── ...
```

---

## 3. Asset Generation (Google Flow & Veo Automation)

When creating new content from scratch, any AI agent coordinates with the user's active Google Flow Studio workspace:
* **User Login:** Ensure the user is logged into [flow.google.com](https://flow.google.com/) in Chrome.
* **Companion Tool:** Use the official [Veo Automation Extension](https://chromewebstore.google.com/detail/veo-automation-veo-nano-b/lnadnaegfljibehcgclljdefggflfpkn).
* **Model Selection:**
  * **Images:** `Nano Banana Pro` (2K/4K photorealism) or `Nano Banana 2` (Speed).
  * **Video:** `Veo 3 / 3.1` (Cinematic 1080p physics) or `Omni 1.1 Flash`.
* **Prompt Anchoring:** Maintain character clothing, facial attributes, and lighting palette across all shots.
* **Shot Triad:** Require Wide (establishing), Medium (action/subject), and Macro (details) shots for dynamic pacing.

---

## 4. Agentic Video Editing (Diffusion Studio)

* **Tool:** `diffusionstudio/editor` via MCP or CLI (`dapi`).
* **Timeline (JSX):** Programmatic sequencing of visual cuts, beat-synchronized transitions, and non-destructive color LUTs.
* **Automated Audit:** Run `dapi check <id>` and `dapi capture <id>` for visual and audio sync verification before exporting.

---

## 5. Statistical Decision Criteria

### Algorithmic Viability Score (AVS)
```math
AVS = (0.35 \times CTR_{est}) + (0.40 \times RET_{est}) + (0.25 \times SV_{norm})
```

* **`CTR_est` (0–100):** Visual contrast, mobile title readability (first 45 characters), curiosity gap.
* **`RET_est` (0–100):** Absence of jarring audio transients, seamless video looping, smooth cross-fades.
* **`SV_norm` (0–100):** Target keyword velocity in YouTube Suggested and Browse features over last 30 days.

> **Condition:** If `AVS < 78.0`, reject topic and request or generate alternative scenario.

---

## 6. Headless YouTube API Pipeline

* **Engine:** `porjo/youtubeuploader`
* **Persistent Token:** `-cache request.token` for headless, zero-login uploads.
* **Prerequisites:** YouTube Data API v3 enabled in Google Cloud Console, test user email added, redirect URI set to `http://localhost:8080/oauth2callback`.
* **Metadata Schema:** Adhere strictly to `video_metadata.template.json`.
