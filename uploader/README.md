# Headless YouTube Uploader Setup

This module utilizes `porjo/youtubeuploader` to execute automated video uploads to YouTube via OAuth 2.0.

## Installation
Download the precompiled binary for your OS from:
https://github.com/porjo/youtubeuploader/releases

Place `youtubeuploader.exe` (or `youtubeuploader` on Unix) in this folder.

## Setup Instructions
1. Enable **YouTube Data API v3** in Google Cloud Console.
2. In OAuth Consent Screen, add your YouTube Google Account email under **Test Users**.
3. Create Credentials -> OAuth 2.0 Client ID (Desktop or Web) with redirect URI `http://localhost:8080/oauth2callback`.
4. Save the JSON as `client_secrets.json` in this directory.

## First-Run Authentication
Run the command once:
```powershell
.\youtubeuploader.exe -secrets client_secrets.json -metaJSON ..\templates\video_metadata.template.json -filename "demo.mp4"
```
Authorize once in your browser. A `request.token` will be created. All subsequent runs are 100% headless!
