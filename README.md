# ModScout 2077

<p align="center">
  <strong>A smarter way to manage your Cyberpunk 2077 mod collection.</strong><br>
  Find manually installed mods, identify their Nexus pages, manage updates, and switch between mod setups — from one Windows app.
</p>

<p align="center">
  <a href="https://github.com/yasssssssin/ModScout-2077-Mod-Manger-cyberpunk-2077/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows-0078D6">
  <img alt="Version" src="https://img.shields.io/badge/version-3.7-informational">
  <img alt="Language" src="https://img.shields.io/badge/language-Python-3776AB">
</p>

## Download

**[Download ModScout2077.exe](https://github.com/yasssssssin/ModScout-2077-Mod-Manger-cyberpunk-2077/raw/refs/heads/main/ModScout2077.exe)**

The standalone executable is intended to run on Windows without a separate Python installation. Download it, place it somewhere you can easily find, and launch it. Windows may show a security prompt for an independently distributed executable; only run software you trust.

## What it does

- **Finds manually installed mods.** Scans common Cyberpunk 2077 mod locations and groups related files into mod entries.
- **Matches mods to Nexus Mods.** Uses conservative automatic matching; uncertain matches are presented as candidates for you to verify.
- **Checks for updates.** Shows available updates for linked mods and can install the appropriate file.
- **Installs mods.** Add a downloaded archive and let ModScout identify and install it.
- **Enables and disables mods.** Switch individual mods or whole collections on and off.
- **Uses instances.** Save named mod setups and switch between them.
- **Keeps a history.** Review changes and undo supported installs, updates, and switching operations.
- **Checks your setup.** Looks for common installation problems, missing frameworks, conflicting files, and other warnings.
- **Helps investigate crashes.** Its mod-isolation workflow can narrow down which installed mod may be causing a problem.
- **Includes extra tools.** Export/import mod lists, back up supported settings, inspect selected game logs, compare instances, and more.

Features that interact with Nexus Mods require your own Nexus Mods API key. Browse images use the optional Pillow library; without it, the app still works, but some images may not display.

## Getting started

1. Download **[ModScout2077.exe](https://github.com/yasssssssin/ModScout-2077-Mod-Manger-cyberpunk-2077/raw/refs/heads/main/ModScout2077.exe)**.
2. Run the executable.
3. Point ModScout to your Cyberpunk 2077 game folder when prompted.
4. Add your personal Nexus Mods API key in the app's settings.
5. Scan your installed mods and review any uncertain matches before relying on them.

Your API key is stored locally in `~/.cp2077_mod_toggle.json`. The application documentation in the source states that it is sent to the Nexus Mods API. **Do not share this configuration file or publish your API key.**

## Build from source

### Requirements

- Windows
- Python 3.10 or newer recommended
- Internet access for installing build tools
- Pillow (optional; enables broader image support in Browse Nexus)

### Build

1. Install Python from [python.org](https://www.python.org/downloads/) and enable **Add Python to PATH** during setup.
2. Download or clone this repository.
3. Keep `cp2077_mod_toggle.py`, `modscout.ico`, and `build_exe.bat` in the same folder.
4. Double-click `build_exe.bat`.
5. When the build finishes, find the executable in the generated `dist` folder.

The build script installs PyInstaller and attempts to install Pillow. If Pillow cannot be installed, it continues with reduced image support.

You can also run the Python application directly:

```powershell
python cp2077_mod_toggle.py
```

## Safety notes

- Back up your Cyberpunk 2077 folder and mod configuration before making large changes.
- Review candidate Nexus matches rather than accepting a guess.
- ModScout's disable/backup workflow is designed to move files rather than simply delete them, but you should still keep your own backups.
- Use a Nexus API key belonging to you. Never paste it into an issue, discussion, screenshot, or public commit.
- This is a community project and is not affiliated with CD PROJEKT RED or Nexus Mods.

## Repository contents

| File | Purpose |
| --- | --- |
| `cp2077_mod_toggle.py` | Main application source |
| `ModScout2077.exe` | Standalone Windows build |
| `build_exe.bat` | Windows build helper |
| `ModScout2077.spec` | PyInstaller configuration |
| `modscout.ico` | Application icon |
| `LICENSE` | MIT license |

## Feedback and bug reports

Found a bug or have an idea? [Open a GitHub issue](https://github.com/yasssssssin/ModScout-2077-Mod-Manger-cyberpunk-2077/issues). Please include your Windows version, the ModScout version, what you expected, what happened, and relevant error text. **Remove API keys, personal paths, and other private information from logs before posting.**

## License

ModScout 2077 is released under the [MIT License](LICENSE).
