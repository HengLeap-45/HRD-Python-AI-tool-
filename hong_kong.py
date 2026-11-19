"""
Karaoke player: plays an audio file and shows lyrics in sync from an .lrc file.

Usage:
    python karaoke.py hong_kong.mp3 hong_kong.lrc

.lrc format (timestamps mark when each line should appear):
    [00:12.50]first line of the song
    [00:16.00]second line of the song

Audio playback uses pygame if installed (pip install pygame).
Without pygame, the lyrics still run on a timer; start your music yourself
at the same moment you press ENTER.
"""
import os
import re
import sys
import time

TIME_TAG = re.compile(r"\[(\d+):(\d+(?:\.\d+)?)\]")


def load_lrc(path):
    """Return a sorted list of (seconds, text) from an .lrc file."""
    lines = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            tags = TIME_TAG.findall(raw)
            text = TIME_TAG.sub("", raw).strip()
            if not tags or not text:
                continue
            for minutes, seconds in tags:
                lines.append((int(minutes) * 60 + float(seconds), text))
    return sorted(lines)


def start_audio(path):
    """Start playback with pygame if available; return True on success."""
    try:
        # pyrefly: ignore[missing-import]
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        return True
    except Exception:
        return False


def main():
    if len(sys.argv) != 3:
        print("Usage: python karaoke.py <audio file> <lyrics.lrc>")
        sys.exit(1)

    audio_path, lrc_path = sys.argv[1], sys.argv[2]
    lyrics = load_lrc(lrc_path)
    if not lyrics:
        print("No timed lyric lines found in the .lrc file.")
        sys.exit(1)

    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 55)
    print("                 KARAOKE PLAYER")
    print("=" * 55)
    input("\nPress ENTER to start...")

    has_audio = start_audio(audio_path)
    if not has_audio:
        print("\n(pygame not available: start your music manually now.)")

    start = time.perf_counter()
    for timestamp, text in lyrics:
        wait = timestamp - (time.perf_counter() - start)
        if wait > 0:
            time.sleep(wait)
        print("\n" + text)

    print("\n" + "=" * 55)
    print("                  END OF SONG")
    print("=" * 55)


if __name__ == "__main__":
    main()