# ModScout 2077 — First-Launch Guide

This guide walks through setting up ModScout, connecting Nexus Mods, scanning an existing Cyberpunk 2077 installation, creating mod instances, and backing up or restoring game settings.

> **Before you start:** Close Cyberpunk 2077 before changing your mod setup or restoring settings. Make a backup before performing large changes. ModScout manages files in your game folder; always review confirmation screens before proceeding.

## 1. Locate your Cyberpunk 2077 folder

ModScout needs the game's **root installation folder** — the folder that contains `bin`, `archive`, `r6`, and the file `bin\x64\Cyberpunk2077.exe`.

Typical locations:

| Store | Common location |
| --- | --- |
| Steam | `C:\Program Files (x86)\Steam\steamapps\common\Cyberpunk 2077` |
| GOG Galaxy | Often `C:\GOG Games\Cyberpunk 2077` |
| Epic Games | The folder selected when installing the game |

Your location may be different if you chose another drive or library.

### Find it through Steam

1. Open Steam and go to **Library**.
2. Right-click **Cyberpunk 2077** → **Properties**.
3. Open **Installed Files**.
4. Choose **Browse**.
5. File Explorer opens the game folder. Keep this window open.

### Select it in ModScout

1. Open ModScout 2077.
2. Open **Tools** → **Game folder…**.
3. Select the root **Cyberpunk 2077** folder you found above — not the `bin` folder and not the game's executable.
4. Confirm the selection.

ModScout checks that the selected folder looks like a valid game installation. If it says the folder is invalid, check that `bin\x64\Cyberpunk2077.exe` exists inside it.

## 2. Get and configure a Nexus Mods API key

Nexus-connected features use your own personal API key.

1. Sign in to your account at [Nexus Mods](https://www.nexusmods.com/).
2. Open the [API key settings page](https://www.nexusmods.com/users/myaccount?tab=api%20access).
3. Find **Personal API Key** and choose **Request an API Key** if you do not already have one.
4. Copy the key.
5. In ModScout, open **Settings**.
6. Under **Nexus Mods**, paste your key into the API key field.
7. Click **Check key**. ModScout should show the connected account and test Nexus search access.

You can also use the **Get a key…** button in Settings to open the key page.

**Keep your key private.** ModScout stores it in your local configuration file (`~/.cp2077_mod_toggle.json`) and sends it to Nexus Mods when making API requests. Never post it in screenshots, logs, GitHub issues, or public commits. If it is exposed, revoke it in Nexus and create a new one.

## 3. Scan and identify your existing mods

1. Make sure the correct game folder is selected.
2. Open the **Library** tab. ModScout reads the game folder and its switched-off mod storage to build the installed-mod list.
3. Review the list. The Library shows each detected mod, whether it is ON or OFF, its installed version when known, its Nexus status, and the locations where its files were found.
4. If you have Nexus connected, choose **Match with Nexus** to look for matching Nexus pages.
5. Review suggested matches carefully. Confirm that the mod name and page are correct; do not accept an uncertain match just because the names look similar.
6. Open the **Updates** tab to review available or possible updates. Check the mod page and version details before updating.

### Helpful tips

- Use the Library search box to find a mod by name or file.
- **Smart grouping** helps group scattered files that belong to one mod. If a group looks wrong, use the mod's context menu to split or merge entries.
- Some mods may show **Not linked** if ModScout cannot confidently identify their Nexus page. You can link them manually from the context menu.
- A missing version does not always mean a mod is broken; some mods do not expose version information in a way ModScout can identify.
- Back up important files before large-scale changes. Do not update many mods at once until you are comfortable with the workflow.

## 4. Create and switch between instances

An **instance** is a named set of mods that are switched ON. For example, you might create:

- **Main** — your everyday mod setup.
- **Vanilla+** — a smaller selection of mods.
- **Testing** — mods you are trying out.

### Create an instance

1. In the top bar, open the dropdown next to the current instance name (for example, **Main**).
2. Choose **New instance…**.
3. Enter a name, such as `Vanilla+` or `Testing`.
4. Choose how to create it:
   - **Start from what is switched on right now** — copies your current ON/OFF selection.
   - **Clean slate** — starts with shared frameworks only.
   - **Copy another instance** — starts from a selected existing instance.
5. Choose **Create**.

### Switch instances

1. Open the current instance dropdown in the top bar, or open **Tools** → **Instances…**.
2. Select the instance you want.
3. Choose **Switch to** if using the Instances window.

ModScout switches the files that differ between the current and selected setups. Mods switched OFF are kept in the game's `_disabled_mods` folder rather than simply being deleted.

**Important:** Instances remember which mods are ON. By default, game saves and mod settings are shared between instances. If you want separate saves for an instance, look under **Tools** → **Saves per instance…**.

You can also use **Tools** → **This setup works** to mark a known-good setup, then **Go back to a setup that worked…** if a later change causes trouble.

## 5. Back up and restore settings

ModScout's settings backup creates a ZIP containing selected configuration files — for example, Cyber Engine Tweaks settings and hotkeys, RED4ext plugin settings, and the game's graphics and controls.

**This is a settings backup, not a full backup of your mods or the entire game.** Keep separate backups of your game folder and downloaded mod archives.

### Create a settings backup

1. Close Cyberpunk 2077.
2. In ModScout, open **Tools** → **Back up my settings…**.
3. Select the groups you want to include. ModScout shows which settings files it found.
4. Choose a destination outside the Cyberpunk 2077 game folder — ideally another drive or a cloud-synced folder.
5. Click **Back up now**.
6. Wait for the confirmation showing the ZIP path and number of files saved.
7. Keep the ZIP somewhere safe.

### Restore a settings backup

1. Close Cyberpunk 2077.
2. In ModScout, open **Tools** → **Restore settings from a backup…**.
3. Select the settings backup ZIP.
4. Review the inspection screen. It shows which files are new, changed, or already the same.
5. Select the settings groups you want to restore.
6. Confirm the restore only after reviewing what will be replaced.

Before restoring, ModScout moves files that would be replaced into `_disabled_mods\_backup`. A restore can be undone through **Tools** → **History and undo…**. Keep your own backup too, especially before restoring settings from an older installation.

### If something goes wrong

- If a restore causes a problem, open **Tools** → **History and undo…** and review the restore action.
- If a mod change breaks the game, use **Go back to a setup that worked…** if you previously marked a working setup.
- Do not delete `_disabled_mods` or its `_backup` folder while you may need to undo changes.
- If the game is running, close it before restoring settings or switching large mod setups.

## Need help?

[Open a GitHub issue](https://github.com/yasssssssin/ModScout-2077-Mod-Manger-cyberpunk-2077/issues) and include your ModScout version, Windows version, what you were trying to do, and the error message. Remove API keys, personal file paths, and other private information before sharing logs or screenshots.

ModScout 2077 is a community project and is not affiliated with CD PROJEKT RED or Nexus Mods.
