# -------------------------------------------------------------------------------------------------------------------------------------------

# voice.py — Voice input/output helpers for the Jarvis assistant.
#
# Input  : SpeechRecognition library listens via the default microphone and
#          sends audio to Google's free speech-to-text API.
# Output : gTTS (Google Text-to-Speech) converts text to MP3 audio kept in
#          an in-memory buffer (no temp files); pygame.mixer plays it back.
#          Every response is also printed to the terminal for visual feedback.

# -------------------------------------------------------------------------------------------------------------------------------------------

import io
import time

import pygame
import speech_recognition as sr
from gtts import gTTS


# -------------------------------------------------------------------------------------------------------------------------------------------
# Module-level recognizer — reused across calls to avoid re-initialization
# overhead on every `listen()` invocation.
# -------------------------------------------------------------------------------------------------------------------------------------------

_recognizer: sr.Recognizer = sr.Recognizer()

_audio_output_ready: bool = False
_audio_output_disabled: bool = False
_audio_output_reported_unavailable: bool = False


def _ensure_audio_output_ready() -> bool:
    """Best-effort pygame mixer initialization.

    Returns True when audio output is available, otherwise False.
    This never raises, so callers can safely fall back to text-only mode.
    """

    global _audio_output_ready, _audio_output_disabled, _audio_output_reported_unavailable

    if _audio_output_ready:
        return True
    if _audio_output_disabled:
        return False

    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        _audio_output_ready = True
        return True
    except Exception as e:
        _audio_output_disabled = True
        if not _audio_output_reported_unavailable:
            print(f"[Audio output unavailable: {e}]")
            _audio_output_reported_unavailable = True
        return False


# -------------------------------------------------------------------------------------------------------------------------------------------
# speak
# -------------------------------------------------------------------------------------------------------------------------------------------


def speak(text: str) -> None:
    """Convert *text* to speech and play it; also print it to the terminal.

    Uses gTTS to synthesise the audio into an in-memory MP3 buffer, then
    plays back the buffer with pygame so no temporary files are written to
    disk.  If synthesis or playback fails for any reason (e.g., no internet
    connection) the function falls back to printing only so Jarvis remains
    functional.

    Args:
        text: The string Jarvis should speak aloud and print.
    """

    # Always print so the user has a text fallback.
    print(f"\nJarvis: {text}\n")

    if not _ensure_audio_output_ready():
        return

    try:
        tts = gTTS(text=text, lang="en", slow=False)

        # Write MP3 bytes into an in-memory buffer instead of a disk file.
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)

        pygame.mixer.music.load(audio_buffer, "mp3")
        pygame.mixer.music.play()

        # Block until playback finishes so the next prompt doesn't overlap.
        while pygame.mixer.music.get_busy():
            time.sleep(0.05)

    except Exception as e:
        # If TTS fails (e.g. no internet), silently continue — text was
        # already printed above, so the user still gets the response.
        print(f"[Voice output unavailable: {e}]")


# -------------------------------------------------------------------------------------------------------------------------------------------
# listen
# -------------------------------------------------------------------------------------------------------------------------------------------


def listen() -> str | None:
    """Listen via the default microphone and return recognized text, or None.

    Opens the microphone, adjusts for ambient noise, records a phrase, then
    sends the audio to Google's speech-to-text API.  Returns the recognized
    string in lower-case on success, or None if the speech was unintelligible
    or the API could not be reached.

    Returns:
        Recognized speech as a lower-case string, or None on failure.
    """

    try:
        with sr.Microphone() as source:
            print("Listening...")
            # Briefly calibrate noise floor before each capture.
            _recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = _recognizer.listen(source, timeout=10, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                print("[No speech detected - please try again.]")
                return None
    except Exception as e:
        print(f"[Microphone unavailable: {e}]")
        return None

    try:
        text: str = _recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.lower().strip()
    except sr.UnknownValueError:
        print("[Could not understand audio - please speak clearly and try again.]")
        return None
    except sr.RequestError as e:
        print(f"[Speech recognition service unavailable: {e}]")
        return None
