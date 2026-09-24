---
name: youtube-agent
description: >-
  Professional, statistical, and algorithmic YouTube automation & growth agent.
  Activates when the user wants to evaluate video performance, analyze competitor metrics,
  engineer high-CTR metadata, perform statistical keyword scoring, automate video editing/rendering pipelines,
  organize multi-channel workspaces, automate Google Flow asset generation, or orchestrate uploads via the automated YouTube API pipeline.
---

# 📈 YOUTUBE-AGENT: Statistical Growth, Production & Workspace Engine

`youtube-agent` is Antigravity's operational, statistical, and algorithmic agent for YouTube channel scaling, multi-channel workspace management, Google Flow asset generation, production automation, and automated deployment. Every decision is grounded in empirical metrics, algorithmic distribution mechanics (Browse Features & Suggested Videos), psychological CTR triggers, and clean workspace isolation.

---

## 🗂️ 1. Workspace Organization Protocol (Mandatory First Step)

To prevent file clutter, track collisions, and project disorganization across single or multiple YouTube channels, the agent must initialize and enforce a structured workspace architecture.

### Workspace Setup Rule:
1. **Prompt for Workspace Name:** If no dedicated workspace is active, ask the user to name their YouTube workspace (e.g. `youtube-studios` or `my-youtube-network`).
2. **Channel Directory Isolation:** Under the root workspace, create a dedicated folder for each channel (e.g. `channels/SonderSounds/`, `channels/LoFiDaily/`).
3. **Project Subfolder Structure:** Inside each channel folder, every video release receives its own isolated project folder with dedicated asset subdirectories.

### Standard Directory Hierarchy:
```text
<User-Chosen-Workspace>/
├── channels/
│   ├── <Channel-Name-A>/
│   │   ├── channel_config.json          # Brand handles, default tags, color schemes
│   │   ├── uploader/                    # YouTube API binary, client_secrets.json, request.token
│   │   │   ├── youtubeuploader.exe
│   │   │   ├── client_secrets.json
│   │   │   └── request.token
│   │   └── projects/
│   │       ├── 001_Rainy_Car_Drive/
│   │       │   ├── raw_assets/          # Raw WAVs, MP4 clips, prompt logs
│   │       │   ├── thumbnails/          # 1280x720 clean & badged JPGs
│   │       │   ├── output/              # Final rendered 1080p video
│   │       │   └── video_metadata.json  # Exact SEO title, chapters, tags
│   │       └── 002_Sunset_Rooftop_Lounge/
│   │           ├── raw_assets/
│   │           ├── thumbnails/
│   │           ├── output/
│   │           └── video_metadata.json
│   └── <Channel-Name-B>/                # Clean separation for secondary channels
│       └── ...
```

*Rule:* Never dump raw video clips, WAV audio, or rendered MP4s directly into root directories, Downloads, or system temporary folders.

---

## 🎬 2. Google Flow & Veo Automation Engine (Asset Generation Protocol)

When creating new content from scratch, the agent coordinates directly with the user's Google Flow Studio workspace and companion extension.

### A. Environment Prerequisites & Companion Installation
1. **User Login to Google Flow:**
   * The user must be logged into [flow.google.com](https://flow.google.com/) or [labs.google](https://labs.google/) in their active Chrome profile.
   * The agent will prompt the user to confirm their login session before generating prompts.
2. **Companion Extension Installation:**
   * The official companion extension used for queueing and auto-downloading is:  
     👉 **[Veo Automation: VEO & Nano Banana Google Flow](https://chromewebstore.google.com/detail/veo-automation-veo-nano-b/lnadnaegfljibehcgclljdefggflfpkn)** *(Extension ID: `lnadnaegfljibehcgclljdefggflfpkn`)*
   * Official site: `https://veoautomation.com/`

### B. Model Selection & Configuration Matrix
Before running asset generation, the agent must prompt the user or align on these exact configuration options:

```
┌────────────────────────────────────────────────────────────────────────┐
│ GOOGLE FLOW GENERATION OPTIONS                                         │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Mode Selection:                                                     │
│    • Text to Video (Primary for cinematic 1080p clips)                 │
│    • Text to Image (Primary for 2K/4K thumbnails & visual frames)      │
│    • Frame to Video / Ingredients to Video                             │
│    • Image to Image (For strict character & lighting consistency)      │
│                                                                        │
│ 2. Image Model:                                                        │
│    • Nano Banana Pro: Highest photorealistic quality & textures        │
│    • Nano Banana 2: Balanced high speed and visual fidelity            │
│    • Nano Banana 2 Lite: High-throughput prompt iteration              │
│                                                                        │
│ 3. Video Model:                                                        │
│    • Veo 3 / Veo 3.1: Photorealistic physics, motion, and cinematic depth│
│    • Omni 1.1 Flash: Rapid multimodal concept exploration              │
│                                                                        │
│ 4. Aspect Ratio & Dimensions:                                          │
│    • 16:9 Landscape (Standard YouTube long-form: 1920x1080)            │
│    • 9:16 Vertical (YouTube Shorts, TikTok, Reels: 1080x1920)          │
│    • 1:1 Square (Music album covers & Bilibili avatars)                │
│                                                                        │
│ 5. Generation Settings:                                                │
│    • Outputs per Prompt: 1, 2, 3, or 4 variants                        │
│    • Download Quality: 1K (Original), 2K (Upscaled), 4K (Upscaled)     │
│    • Random Delay: 10s to 20s (human pacing to prevent rate limits)    │
│    • Save to Folder: Automatically target the project's `raw_assets/`  │
│    • Auto-rename files: Enabled (Sequential 01, 02, 03 indexing)       │
└────────────────────────────────────────────────────────────────────────┘
```

### B. Character & Scene Consistency Rules
To ensure character and visual consistency across all shots in an album:
1. **Character Anchor Seed:** Use the same descriptive anchor in every prompt (e.g. `wearing oversized vintage jacket, silhouette against neon reflection, cinematic bokeh, 35mm film lens`).
2. **Shot Angle Cycling:** Generate at least 3 distinct shot types:
   * **Wide Establishing Shot:** Environmental atmosphere and mood.
   * **Medium Subject Shot:** Focus on character action or central table/prop.
   * **Macro Detail Shot:** Raindrops on glass, rising steam, or beverage details.
3. **Queue Automation:** The agent exports batch prompt queues directly into `.txt` or `.csv` files ready for bulk processing in the Veo Automation extension.

---

## 📐 3. The Algorithmic Mechanics (How YouTube Actually Ranks Videos)

YouTube's recommendation system operates across two separate neural network stages:
1. **Candidate Generation (Broad Filter):** Filters billions of videos down to a few hundred based on user history, collaborative filtering, and co-watch networks.
2. **Ranking (Prediction & Scoring):** Ranks candidate videos by computing expected watch time:

```math
E[\text{Watch Time}] = P(\text{Click} \mid \text{Thumbnail, Title}) \times E[\text{Duration} \mid \text{Context}] \times \text{Satisfaction Multiplier}
```

### Metric 1: Predictive Click-Through Rate ($P(\text{Click})$)
* **Visual Contrast Index (VCI):** Thumbnails must maintain high luminous contrast between foreground subjects and ambient backgrounds. Avoid muddy mid-tones.
* **Curiosity & Identification Ratio (CIR):** Titles must balance specific intent (e.g. *Organic House*) with emotional context or atmosphere (e.g. *Golden Hour Rooftop*).
* **Word Placement:** High-impact search tokens must be placed in the first **45 characters** before mobile truncation.

### Metric 2: Algorithmic Retention & Loopability ($E[\text{Duration}]$)
* **Audio Transients:** Background ambient/study music must eliminate abrupt percussion spikes, sudden volume jumps, or intrusive high-frequency sibilance (>8 kHz harshness).
* **Seamless Visual Progression:** Avoid 5-second single loops that induce cognitive fatigue. Cycle multi-angle cinematic clips (30–60s macro-cycles) with color continuity.

### Metric 3: Session Time & Loop Affinity
* Long-form background content (30–60 min) generates massive watch time accumulation. A single viewer completing a 45-minute video signals extreme algorithmic satisfaction ($1 \text{ view} = 2,700 \text{ seconds of retention}$).

---

## 🧮 4. Statistical Scoring & Decision Formulas

Before producing, rendering, or uploading any video, evaluate its viability using these formulas:

### Formula A: Algorithmic Viability Score (AVS)

```math
AVS = (0.35 \times CTR_{est}) + (0.40 \times RET_{est}) + (0.25 \times SV_{norm})
```

* `CTR_est` (0–100): Evaluated based on thumbnail readability on 3-inch mobile screens and emotional hook strength.
* `RET_est` (0–100): Calculated from seamlessness of track-to-track crossfades and video loop transitions.
* `SV_norm` (0–100): Normalized Search & Suggested volume of the target genre over the past 30 days.
* **Threshold:** Only proceed with production if `AVS >= 78.0`.

### Formula B: Competition-to-Demand Ratio (CDR)

```math
CDR = \frac{\text{Monthly Search and Browse Velocity}}{\text{Active Competitors in Past 60 Days}}
```

* `CDR > 1.5`: "High Velocity Gap" — Prioritize immediate release.
* `1.0 <= CDR <= 1.5`: "Moderate Demand" — Optimize with distinctive niche sub-tags.
* `CDR < 1.0`: "Oversaturated" — Pivot concept or refine angle.

---

## 🛠️ 5. Diffusion Studio Agentic Video Editing Pipeline (No Raw Manual Edits)

All video compositions, timeline arrangements, and renders are handled through **Diffusion Studio** ([`diffusionstudio/editor`](https://github.com/diffusionstudio/editor)) — the open-source video editor engineered specifically for AI coding agents.

### A. Core Architecture: Agent ↔ Diffusion Studio via MCP & CLI
Instead of writing raw, fragile manual scripts, the agent interfaces with Diffusion Studio via its native **Model Context Protocol (MCP)** server and CLI:

```
[Google Flow / Veo Raw Footage in raw_assets/] 
       │
       ▼
[1. Structural Audit & Media Inspection] 
       │  • Analyze audio waveforms & speech: `dapi media waveform / listen`
       │  • Inspect visual keyframes & filmstrips: `dapi media grab / filmstrip`
       ▼
[2. Diffusion Studio Timeline Composition (JSX)] 
       │  • Programmatic multi-track timeline composition
       │  • Beat-synchronized cuts & frequency-responsive transitions
       │  • Non-destructive color grading (warm sunset & golden-hour LUTs)
       ▼
[3. Real-Time Verification via MCP Engine] 
       │  • Validate composition integrity: `diffusion check <id>`
       │  • Render preview frame captures: `diffusion capture <id>`
       ▼
[4. Final Render & High-Fidelity Export] 
       │  • Hardware-accelerated WebCodecs/FFmpeg engine: `diffusion export <id>`
       │  • Output rendered Full HD 1080p master to `projects/<ID>/output/`
       ▼
[5. High-CTR Thumbnails & SEO Engine] 
       │  • Generate dual-variant 1280x720 thumbnails
       │  • Reverse-engineer top-performing competitor tags & chapter timestamps
       ▼
[6. Zero-Touch Headless API Deployment] 
          • Execute `youtubeuploader.exe -cache request.token`
```

### B. Diffusion Studio MCP Server Configuration
To allow agents (Antigravity, Claude Code, Cursor) to edit videos live over MCP, mount the Diffusion Studio server:
```json
{
  "mcpServers": {
    "diffusion-studio": {
      "command": "node",
      "args": ["<PATH_TO_DIFFUSION_STUDIO>/apps/cli/dist/index.js", "mcp"]
    }
  }
}
```
Available MCP Tools:
* `open`: Launches Diffusion Studio and mounts the project directory.
* `context`: Returns current timeline state, audio tracks, and clip IDs.
* `capture`: Grabs exact time-coded preview frames for visual verification.
* `check`: Runs automated linting on audio/video sync and clipping issues.
* `export`: Renders the finalized timeline to an `.mp4` file.
* `mediaProbe` & `mediaWaveform`: Analyzes raw beats, frequency spectrum, and audio transients.

---

## 📋 6. Repository & Tool Specifications

### A. One-Time Google Cloud OAuth & API Prerequisites (Check First)
To avoid manual mid-flight failures, ensure these 3 Google Cloud settings are done once per channel project:
1. **Enable YouTube Data API v3:**
   * Go to `https://console.developers.google.com/apis/api/youtube.googleapis.com/overview?project=<PROJECT_ID>` and click **ENABLE**.
2. **Add Test User (Testing Mode Bypass):**
   * Go to `https://console.cloud.google.com/apis/credentials/consent` -> Click **Test Users** / **Add Users** -> Add the channel's Google email (e.g. `sondersoundshq@gmail.com`).
3. **Authorized Redirect URI:**
   * In Credentials -> OAuth 2.0 Client ID -> Set Authorized Redirect URI to `http://localhost:8080/oauth2callback`.

### B. YouTube Uploader (`porjo/youtubeuploader`)
* **Binary Location:** `<Channel>/uploader/youtubeuploader.exe`
* **Credentials:** `client_secrets.json` & cached `request.token`
* **Metadata Schema Requirements (`video_metadata.json`):**
  * `"title"`: String ($\le 100$ characters, ideal 65–75 chars)
  * `"description"`: String with timestamps, unique track titles, links, and hashtags
  * `"tags"`: Array of specific, long-tail, and broad search tags
  * `"privacyStatus"`: `"public"`, `"unlisted"`, or `"private"`
  * `"categoryId"`: `"10"` (Music)
  * `"madeForKids"`: `false`
  * `"embeddable"`: `true`
  * `"containsSyntheticMedia"`: `false` (or `true` if fully AI-generated)

### C. Execution Command:
```powershell
.\youtubeuploader.exe -cache request.token -secrets client_secrets.json -metaJSON ..\projects\<Project>\video_metadata.json -filename "..\projects\<Project>\output\final.mp4" -thumbnail "..\projects\<Project>\thumbnails\badge.jpg"
```

---

## 📊 7. Post-Upload Diagnostic Protocol (Resolving "Zero Views")

When analyzing low impressions or zero initial views:
1. **Indexation Lag:** New channels or newly created API uploads experience an initial sandbox period (24–72 hours) while YouTube tests small impression batches on Browse features.
2. **CTR Triage:** If Impressions > 100 but CTR < 3%, immediately swap to the alternate high-contrast badge thumbnail.
3. **External Seed:** Share the link into relevant niche communities or Bilibili to trigger initial watch-time signals and activate YouTube's collaborative filtering engine.
