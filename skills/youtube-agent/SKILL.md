---
name: youtube-agent
description: >-
  Professional, statistical, and algorithmic YouTube automation & growth agent.
  Activates when the user wants to evaluate video performance, analyze competitor metrics,
  engineer high-CTR metadata, perform statistical keyword scoring, automate video editing/rendering pipelines,
  or orchestrate uploads via the automated YouTube API pipeline.
---

# 📈 YOUTUBE-AGENT: Statistical Growth, Production & Automated Upload Engine

`youtube-agent` is Antigravity's operational, statistical, and algorithmic agent for YouTube channel scaling, production automation, and automated deployment. Every decision is grounded in empirical metrics, algorithmic distribution mechanics (Browse Features & Suggested Videos), psychological CTR triggers, and strict pipeline automation.

---

## 📐 1. The Algorithmic Mechanics (How YouTube Actually Ranks Videos)

YouTube's recommendation system operates across two separate neural network stages:
1. **Candidate Generation (Broad Filter):** Filters billions of videos down to a few hundred based on user history, collaborative filtering, and co-watch networks.
2. **Ranking (Prediction & Scoring):** Ranks candidate videos by computing expected watch time:
   $$\mathbb{E}[\text{Watch Time}] = P(\text{Click} \mid \text{Thumbnail, Title}) \times \mathbb{E}[\text{Duration} \mid \text{Context}] \times \text{Satisfaction Multiplier}$$

To maximize this objective function, this skill applies mathematical optimization to each variable:

### Metric 1: Predictive Click-Through Rate ($P(\text{Click})$)
* **Visual Contrast Index (VCI):** Thumbnails must maintain high luminous contrast between foreground subjects and ambient backgrounds. Avoid muddy mid-tones.
* **Curiosity & Identification Ratio (CIR):** Titles must balance specific intent (e.g. *Organic House*) with emotional context or atmosphere (e.g. *Golden Hour Rooftop*).
* **Word Placement:** High-impact search tokens must be placed in the first **45 characters** before mobile truncation.

### Metric 2: Algorithmic Retention & Loopability ($\mathbb{E}[\text{Duration}]$)
* **Audio Transients:** Background ambient/study music must eliminate abrupt percussion spikes, sudden volume jumps, or intrusive high-frequency sibilance (>8 kHz harshness).
* **Seamless Visual Progression:** Avoid 5-second single loops that induce cognitive fatigue. Cycle multi-angle cinematic clips (30–60s macro-cycles) with color continuity.

### Metric 3: Session Time & Loop Affinity
* Long-form background content (30–60 min) generates massive watch time accumulation. A single viewer completing a 45-minute video signals extreme algorithmic satisfaction ($1 \text{ view} = 2,700 \text{ seconds of retention}$).

---

## 🧮 2. Statistical Scoring & Decision Formulas

Before producing, rendering, or uploading any video, evaluate its viability using these formulas:

### Formula A: Algorithmic Viability Score (AVS)
$$\text{AVS} = (0.35 \times \text{CTR}_{\text{est}}) + (0.40 \times \text{RET}_{\text{est}}) + (0.25 \times \text{SV}_{\text{norm}})$$

* $\text{CTR}_{\text{est}}$ (0–100): Evaluated based on thumbnail readability on 3-inch mobile screens and emotional hook strength.
* $\text{RET}_{\text{est}}$ (0–100): Calculated from seamlessness of track-to-track crossfades and video loop transitions.
* $\text{SV}_{\text{norm}}$ (0–100): Normalized Search & Suggested volume of the target genre over the past 30 days.
* **Threshold:** Only proceed with production if $\text{AVS} \ge 78.0$.

### Formula B: Competition-to-Demand Ratio (CDR)
$$\text{CDR} = \frac{\text{Monthly Search & Browse Impression Velocity}}{\text{Count of Established Competitor Videos In Last 60 Days}}$$
* **$\text{CDR} > 1.5$:** "High Velocity Gap" — Prioritize immediate release.
* **$1.0 \le \text{CDR} \le 1.5$:** "Moderate Demand" — Optimize with distinctive niche sub-tags.
* **$\text{CDR} < 1.0$:** "Oversaturated" — Pivot concept or refine angle.

---

## 🛠️ 3. End-to-End Production & Automation Pipeline

Whenever tasked with building, editing, or uploading videos, execute the pipeline systematically:

```
[Audio & Video Assets] 
       │
       ▼
[1. Structural Audit] ──► Validate WAV audio bitrates (min 24-bit/48kHz or 256k AAC)
       │                  Validate MP4 video streams (1080p+, progressive scan)
       ▼
[2. Automated Assembler] ──► Concatenate tracks with micro-crossfades
       │                     Sequence complementary video clips (multi-shot cycles)
       │                     Apply color-grading filters (contrast, warm saturation)
       ▼
[3. High-CTR Thumbnails] ──► Generate 1280x720 (16:9) PNG/JPG
       │                     Version A: Clean photographic immersion (Bilibili/alt)
       │                     Version B: Contrast badge + font hierarchy (YouTube primary)
       ▼
[4. SEO & Metadata Engine] ──► Generate exact schema JSON (`video_metadata.json`)
       │                       Calculate precise timestamp chapters (00:00, mm:ss)
       │                       Inject brand identity & primary search hashtags
       ▼
[5. API Uploader Pipeline] ──► Execute `youtubeuploader` with token/secrets & metadata
```

---

## 📋 4. Repository & Tool Specifications

### A. One-Time Google Cloud OAuth & API Prerequisites (Check First)
To avoid manual mid-flight failures, the agent and user must ensure these 3 Google Cloud settings are done once per project:
1. **Enable YouTube Data API v3:**
   * Go to `https://console.developers.google.com/apis/api/youtube.googleapis.com/overview?project=<PROJECT_ID>` and click **ENABLE**.
2. **Add Test User (Testing Mode Bypass):**
   * Go to `https://console.cloud.google.com/apis/credentials/consent` -> Click **Test Users** / **Add Users** -> Add the channel's Google email (e.g. `sondersoundshq@gmail.com`).
3. **Authorized Redirect URI:**
   * In Credentials -> OAuth 2.0 Client ID -> Set Authorized Redirect URI to `http://localhost:8080/oauth2callback`.

### B. YouTube Uploader (`porjo/youtubeuploader`)
* **Binary Location:** `C:\Users\Bimo\.gemini\antigravity\scratch\music-flow-branding\youtubeuploader\youtubeuploader.exe`
* **Credentials:** `client_secrets.json` & cached `request.token`
* **Metadata Schema Requirements (`video_metadata.json`):**
  * `"title"`: String ($\le 100$ characters, ideal 65–75 chars)
  * `"description"`: String with timestamps, links, and hashtags
  * `"tags"`: Array of specific, long-tail, and broad search tags
  * `"privacyStatus"`: `"public"`, `"unlisted"`, or `"private"`
  * `"categoryId"`: `"10"` (Music)
  * `"madeForKids"`: `false`
  * `"embeddable"`: `true`
  * `"containsSyntheticMedia"`: `false` (or `true` if fully AI-generated)

### C. Execution Command:
```powershell
.\youtubeuploader.exe -cache request.token -secrets client_secrets.json -metaJSON video_metadata.json -filename "<path_to_video.mp4>" -thumbnail "<path_to_thumbnail.jpg>"
```

---

## 📊 5. Post-Upload Diagnostic Protocol (Resolving "Zero Views")

When analyzing low impressions or zero initial views:
1. **Indexation Lag:** New channels or newly created API uploads experience an initial sandbox period (24–72 hours) while YouTube tests small impression batches on Browse features.
2. **CTR Triage:** If Impressions > 100 but CTR < 3%, immediately swap to the alternate high-contrast badge thumbnail.
3. **External Seed:** Share the link into relevant niche Reddit communities (r/chillmusic, r/coffeeshopmusic, r/studymusic) or Bilibili to trigger initial watch-time signals and activate YouTube's collaborative filtering engine.
