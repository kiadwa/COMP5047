#ifndef GOOGLE_TTS_H
#define GOOGLE_TTS_H

#include <Arduino.h>

// void base64UrlEncode(const unsigned char *input, size_t length, String &output);
// void signJWT(const String &message, const char *private_key, String &signature);
// bool SetupNTPTime();
// String createJWT();
// String getAccessToken(const String &jwt);
// String requestGoogleTTS(const String &text, const String &accessToken);
// String GetJWTToken();
void RequestBackendTTS(String& text);
// void SetAudioConfig(int I2S_BCLK, int I2S_LRCLK, int I2S_DIN, int volume = 21);
// void AudioLoop();
void Pause();
void Loop();

#endif  // GOOGLE_TTS_H