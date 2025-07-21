# 🎙️ Audio Steganography from Text → Image → Compressed → Embedded in Audio

A Python project to **hide secret text messages inside audio files** using the pipeline:

```
Text → Image → Compressed Image → Embedded into Audio
```

This approach enhances **security and capacity** by first converting text to an image, compressing it, and then hiding it in an audio carrier using steganographic techniques.

---

## 🚀 Features

✅ Convert text to grayscale image
✅ Compress the image using PNG/JPEG/zip
✅ Embed compressed image data into audio using LSB or transform-domain steganography
✅ Extract and reconstruct the hidden text from stego-audio
✅ CLI-based and modular for easy extension
✅ Supports WAV/FLAC audio carriers

---
## 🖼️ How It Works

1️⃣ **Text to Image:**

* Uses PIL to convert text to a grayscale image for structured data representation.

2️⃣ **Image Compression:**

* Compresses the image (optional) to reduce payload size.

3️⃣ **Embedding into Audio:**

* Embeds compressed image bytes into the audio using LSB or DCT-based steganography.

4️⃣ **Extraction:**

* Recovers image bytes from the audio, decompresses, and converts back to text.

---

## 📝 License

MIT License.
Use, modify, and distribute freely for learning and research.

---

## 🤝 Contributing

Pull requests are welcome. Please open an issue for major changes or enhancements.
