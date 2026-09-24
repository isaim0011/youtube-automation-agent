# YouTube Automation & Autonomous Media Production Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Windows / macOS / Linux](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-brightgreen.svg)]()
[![Engine: FFmpeg / DiffusionStudio / Go](https://img.shields.io/badge/Stack-FFmpeg%20%7C%20DiffusionStudio%20%7C%20Go-orange.svg)]()

> A professional, algorithmic, and statistical YouTube channel automation agent and autonomous media pipeline. Engineered for 24/7 background audio-visual generation with Google Flow, color grading, high-CTR metadata optimization, and zero-touch API deployment.

---

## 🚀 Key Features

* **🧠 Autonomous `youtube-agent` Skill:** A plug-and-play AI agent specification (`AGENT.md` and `SKILL.md`) that executes empirical CTR scoring (`P(Click)`), retention optimization, and chapter generation.
* **✨ Google Flow & Veo Automation Suite:** Direct instructions and templates for batch generating photorealistic 1080p video (Veo 3/3.1) and 2K/4K thumbnails (Nano Banana Pro) with automated character/scene consistency.
* **🎥 Multi-Angle Video Sequencing Engine:** Intelligent video stitching eliminating repetitive 5-second loop fatigue. Cycles multi-shot cinematic footage with progressive color enhancement (`contrast=1.08:saturation=1.15`) and studio fades.
* **🎵 Broadcast-Grade Audio Concat:** Lossless WAV-to-256kbps AAC audio mastering, loudness normalization, and micro-crossfade transitions.
* **🖼️ Dual-Variant High-CTR Thumbnails:** Automated generation of both clean photographic immersion (Bilibili/organic) and contrast-badged text graphics (YouTube mobile feed).
* **⚡ Headless YouTube API Pipeline:** Integration with `porjo/youtubeuploader` utilizing persistent OAuth tokens and structured JSON schema for zero-touch uploads.
* **🎨 Diffusion Studio Integration:** Ready-to-use agentic editing hooks with [`diffusionstudio/editor`](https://github.com/diffusionstudio/editor) for JSX compositions and timeline automation.

---

## 📂 Repository Architecture

```text
├── AGENT.md                       # Comprehensive autonomous agent operational manual
├── skills/
│   └── youtube-agent/
│       └── SKILL.md               # Antigravity & Agent skill definition
├── scripts/
│   ├── assemble_album_video.py    # Multi-clip sequencing & color-grading engine
│   ├── generate_thumbnails.py     # Dual-variant 1280x720 thumbnail generator
│   └── build_metadata.py          # Reverse-engineered SEO & chapter JSON generator
├── templates/
│   ├── video_metadata.template.json # Strict API schema for porjo/youtubeuploader
│   └── client_secrets.example.json  # OAuth 2.0 configuration blueprint
├── uploader/
│   └── README.md                  # YouTube Data API v3 setup & headless workflow
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Prerequisites & One-Time Setup

### 1. Google Flow Studio & Veo Automation Extension
To generate video clips and images with consistent characters and prompts:
1. **Login to Google Flow Studio:**
   * Open your browser and navigate to [flow.google.com](https://flow.google.com/) (or [labs.google](https://labs.google/)).
   * Sign in with your Google account. Ensure you are active in the workspace where you want media created.
2. **Install the Veo Automation Extension:**
   * Install the official companion extension:  
     👉 **[Veo Automation: VEO & Nano Banana Google Flow](https://chromewebstore.google.com/detail/veo-automation-veo-nano-b/lnadnaegfljibehcgclljdefggflfpkn)** *(Chrome Web Store extension ID: `lnadnaegfljibehcgclljdefggflfpkn`)*  
     *(Official Site: [veoautomation.com](https://veoautomation.com/))*
3. **Agent Protocol:**
   * The AI agent will prompt the user to ensure Google Flow is open and logged in.
   * The agent exports formatted prompt batches and instructs the extension to auto-save directly to `channels/<Channel>/projects/<ID>/raw_assets/`.

---

### 2. Google Cloud Console (YouTube Data API v3)
To enable automated headless uploads, configure these three settings once in your Google Cloud Project:
1. **Enable YouTube Data API v3:**
   * Go to [Google Cloud Console API Library](https://console.cloud.google.com/apis/library/youtube.googleapis.com) and click **ENABLE**.
2. **Add Test User (Testing Mode Bypass):**
   * Go to [OAuth Consent Screen](https://console.cloud.google.com/apis/credentials/consent) ➔ **Test Users** ➔ **Add Users** ➔ Enter your YouTube account email.
3. **Authorized Redirect URI:**
   * In [Credentials](https://console.cloud.google.com/apis/credentials) ➔ Click your OAuth 2.0 Client ID ➔ Add `http://localhost:8080/oauth2callback`.
   * Download the JSON file and save it as `client_secrets.json`.

---

## 🚀 Quick Start Guide

### Step 1: Clone Repository
```bash
git clone https://github.com/isaim0011/youtube-automation-agent.git
cd youtube-automation-agent
```

### Step 2: Build Album Video
Place your raw video loops in `inputs/videos/` and audio WAVs in `inputs/audio/`:
```bash
python scripts/assemble_album_video.py
```

### Step 3: Generate High-CTR Thumbnails
```bash
python scripts/generate_thumbnails.py --input raw_photo.jpg --title "SUNSET LOUNGE" --sub "DEEP ORGANIC HOUSE"
```

### Step 4: Automated Upload to YouTube
```bash
# First run prompts a one-time browser login, creating request.token.
# All subsequent uploads run completely headless!
.\uploader\youtubeuploader.exe -cache uploader/request.token -secrets uploader/client_secrets.json -metaJSON metadata.json -filename "output_video.mp4" -thumbnail "thumbnail.jpg"
```

---

## 📊 Algorithmic Viability Formulas

The agent enforces mathematical criteria before approving concepts for render:

### 1. Algorithmic Viability Score (AVS)

```math
AVS = (0.35 \times CTR_{est}) + (0.40 \times RET_{est}) + (0.25 \times SV_{norm})
```

> **Threshold:** Only concepts with `AVS >= 78.0` proceed to production.

### 2. Competition-to-Demand Ratio (CDR)

```math
CDR = \frac{\text{Monthly Search and Browse Velocity}}{\text{Active Competitors in Past 60 Days}}
```

> **Target:** `CDR > 1.5` indicates a high-probability search cluster.

---

## ⚖️ License & Attribution

* Licensed under the [MIT License](LICENSE).
* Core uploader engine based on [`porjo/youtubeuploader`](https://github.com/porjo/youtubeuploader).
* Compositions compatible with [`diffusionstudio/editor`](https://github.com/diffusionstudio/editor).
