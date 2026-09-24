import os
import subprocess
import wave
import imageio_ffmpeg

FFMPEG_BIN = imageio_ffmpeg.get_ffmpeg_exe()
SUNSET_DIR = r"C:\Users\Bimo\Downloads\music\sunset lounge and rooftop"
OUTPUT_DIR = r"C:\Users\Bimo\.gemini\antigravity\scratch\music-flow-branding"

# Video clips in logical sequence (Rooftop golden hour -> cocktails on terrace -> wine at dusk)
CLIPS = [
    os.path.join(SUNSET_DIR, "Rooftop_bar_at_golden_hour_20260924111925.mp4"),
    os.path.join(SUNSET_DIR, "Cocktail_on_cafe_terrace_table_20260924111908.mp4"),
    os.path.join(SUNSET_DIR, "Glass_of_wine_at_rooftop_20260924111917.mp4"),
    os.path.join(SUNSET_DIR, "Cocktail_on_cafe_terrace_table_20260924111914.mp4"),
]

# Organic House 15 tracks in order
TRACKS = [f"Sunset Lounge {i:02d} - Organic House.wav" for i in range(1, 15)]
TRACKS.append("Sunset Lounge 15 (Outro) - Organic House.wav")

def format_timestamp(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins:02d}:{secs:02d}"

def main():
    print("=" * 65)
    print("Sunset Lounge & Rooftop — Production Engine")
    print("=" * 65)

    # 1. Build Audio Concat List & Chapters
    concat_audio_txt = os.path.join(OUTPUT_DIR, "sunset_audio_concat.txt")
    current_time = 0.0
    chapters = []
    
    with open(concat_audio_txt, "w", encoding="utf-8") as f:
        for t in TRACKS:
            tpath = os.path.join(SUNSET_DIR, t)
            with wave.open(tpath, "r") as w:
                dur = w.getnframes() / float(w.getframerate())
            clean_title = t.replace(".wav", "").replace("Sunset Lounge ", "Track ")
            chapters.append(f"{format_timestamp(current_time)} - {clean_title}")
            f.write(f"file '{tpath.replace(os.sep, '/')}'\n")
            current_time += dur

    total_duration_sec = current_time
    total_minutes = total_duration_sec / 60.0

    print(f"Total Organic House Duration: {total_minutes:.2f} mins ({total_duration_sec:.1f}s)")
    
    # Save Chapters
    desc_path = os.path.join(OUTPUT_DIR, "sunset_youtube_description.txt")
    with open(desc_path, "w", encoding="utf-8") as f:
        f.write("Sunset Rooftop Lounge 2026 | Deep Organic House & Golden Hour Chillout [Chill / Study / Relax]\n\n")
        f.write("Tracklist & Chapters:\n")
        for ch in chapters:
            f.write(f"{ch}\n")
        f.write("\nVisuals: Google Flow Studio (Veo 1080p)\nMusic: Google Flow Music (Lyria Organic House)\nBrand: Sonder Sounds\n")
    print(f"Saved Chapters to: {desc_path}")

    # 2. Concat Audio
    master_audio = os.path.join(OUTPUT_DIR, "sunset_master_soundtrack.m4a")
    if not os.path.exists(master_audio) or os.path.getsize(master_audio) < 1024 * 1024:
        print("\nStep 1/3: Merging 15 Organic House tracks into master audio...")
        cmd_a = [
            FFMPEG_BIN, "-y",
            "-f", "concat", "-safe", "0",
            "-i", concat_audio_txt,
            "-c:a", "aac", "-b:a", "256k",
            master_audio
        ]
        subprocess.run(cmd_a, check=True)
        print("Master soundtrack compiled successfully!")
    else:
        print("\nMaster audio already compiled.")

    # 3. Build Video Sequence Loop List (4 clips = ~40s sequence)
    concat_video_txt = os.path.join(OUTPUT_DIR, "sunset_video_concat.txt")
    with open(concat_video_txt, "w", encoding="utf-8") as f:
        # Loop the 4 clips in sequence ~66 times to exceed total_duration_sec
        for _ in range(70):
            for clip in CLIPS:
                f.write(f"file '{clip.replace(os.sep, '/')}'\n")

    # 4. Render Final Video (1080p, H.264, Color Graded)
    output_video = os.path.join(OUTPUT_DIR, "Sonder_Sounds_Sunset_Lounge_1080p_Final.mp4")
    fade_out_start = max(0, int(total_duration_sec) - 3)

    # Video filters:
    # 1. eq: boost contrast (+8%) and saturation (+15%) for warm golden hour vibrancy
    # 2. fade in (2s) and fade out at end (3s)
    vf = f"eq=contrast=1.08:saturation=1.15,fade=t=in:st=0:d=2,fade=t=out:st={fade_out_start}:d=3"
    af = f"afade=t=in:st=0:d=2,afade=t=out:st={fade_out_start}:d=3"

    print(f"\nStep 2/3: Rendering Final 43.7-Minute 1080p Video...")
    print(f"Output: {output_video}\n")

    cmd_v = [
        FFMPEG_BIN, "-y",
        "-f", "concat", "-safe", "0", "-i", concat_video_txt,
        "-i", master_audio,
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-vf", vf,
        "-af", af,
        "-t", str(int(total_duration_sec)),
        "-c:v", "libx264",
        "-preset", "veryfast",
        "-crf", "21",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "256k",
        output_video
    ]

    proc = subprocess.Popen(cmd_v, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in proc.stdout:
        if "frame=" in line or "time=" in line:
            print(f"\r  Rendering: {line.strip()}", end="", flush=True)
    proc.wait()

    if proc.returncode == 0:
        sz_mb = os.path.getsize(output_video) / (1024 * 1024)
        print("\n\n" + "=" * 65)
        print(f"SUNSET LOUNGE VIDEO CREATED SUCCESSFULLY!")
        print(f"File: {output_video}")
        print(f"Size: {sz_mb:.1f} MB")
        print(f"Duration: {total_minutes:.1f} Minutes (1080p Full HD)")
        print("=" * 65)
    else:
        print("\nError rendering video.")

if __name__ == "__main__":
    main()
