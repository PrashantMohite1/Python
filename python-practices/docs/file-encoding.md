## What is file encoding?

Encoding is the scheme that maps the *characters* you see (letters, numbers, symbols, emoji) to *bytes* — the actual 0s and 1s stored on disk. A computer only understands bytes; encoding is the translation table between "human-readable text" and "raw binary."

Example: the letter `A` might be stored as the byte `01000001` (65 in decimal) under ASCII/UTF-8. The character `€` needs a different, larger byte pattern. Without an agreed-upon mapping, a file is just a meaningless stream of bytes.

## Why do we need it?

1. **Bytes have no inherent meaning.** A file on disk is just a sequence of bytes. Something has to define "byte value 65 = letter A." That something is the encoding.
2. **Different languages/symbols need different mappings.** English fits in 128 values (ASCII), but Chinese, Arabic, emoji, etc. need far more — encodings like UTF-8 or UTF-16 were built to represent virtually every character in every language.
3. **Interoperability.** If you save a file with one encoding and someone opens it assuming a different one, you get garbled text ("mojibake") — e.g., `café` turning into `cafÃ©`. Agreeing on an encoding (usually UTF-8 today) avoids this.
4. **Storage efficiency vs. universality trade-off.** ASCII is compact but limited to English. UTF-8 is a good middle ground — 1 byte for common English characters, more bytes for other scripts, while staying backward-compatible with ASCII. UTF-16/UTF-32 use fixed/wider units, common in some OS internals.

Common encodings: **ASCII**, **UTF-8** (dominant on the web and most modern systems), **UTF-16** (used internally by Windows and Java), **Latin-1/ISO-8859-1** (older Western European standard), and legacy region-specific ones like **Shift-JIS** (Japanese) or **GBK** (Chinese).

## Relation between OS and file encoding

- **The OS doesn't force a "file encoding" on you** — a file is just bytes to the filesystem. But the OS *does* have default assumptions/conventions that affect how text is created, displayed, and interpreted:
  - **Windows** historically defaulted to UTF-16 for internal APIs and often used legacy code pages (like Windows-1252) for plain text files, though modern Windows increasingly defaults to UTF-8.
  - **Linux/macOS** (Unix-like systems) have defaulted to UTF-8 for a long time, both for filenames and text file contents.
- **Filenames themselves are encoded too.** The OS encodes filenames using some scheme (UTF-8 on Linux/macOS, UTF-16 on Windows internally) — this is why moving files between systems can sometimes cause filename corruption if encodings mismatch.
- **Line endings** are a related but separate OS-level text convention (Windows uses `\r\n`, Unix uses `\n`) — not encoding itself, but often confused with it since both affect "what does this text file actually contain."
- **Programs, not the OS, ultimately decide encoding when reading/writing a file** — but they often rely on OS locale settings or defaults to *guess* the encoding if it's not explicitly specified (e.g., no BOM, no metadata).

**In short:** encoding is the character-to-byte mapping that makes text meaningful; we need it because computers only store bytes; and the OS shapes default conventions and locale settings that influence what encoding gets used, but doesn't rigidly enforce one — mismatched assumptions between systems are the classic cause of garbled text.