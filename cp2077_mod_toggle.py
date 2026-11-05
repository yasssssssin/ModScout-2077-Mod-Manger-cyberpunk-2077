#!/usr/bin/env python3
"""
ModScout 2077  v3.7
===================

Finds the Cyberpunk 2077 mods you installed by hand, groups the scattered files
that belong together, matches them with Nexus Mods, tells you which ones have
updates, installs and updates mods for you, and lets you switch each mod ON or
OFF - or whole sets of mods at once (instances).

Grouping
  * Files are grouped by name (Nexus suffixes, versions, #/@ prefixes and
    extensions are ignored).
  * If you still have the downloaded archives, the tool opens them, compares
    every file inside with what is installed (CRC32) and links the installed
    files to the exact Nexus mod AND version.
  * "Suggested merges" finds look-alike names installed at the same time and
    lets you tick the ones that are right.
  * File lists: every Nexus download has a "Preview file contents" list. For a mod the names can't settle, the
    pages found by its keywords are checked: when the files listed there are the files you have installed (same
    paths, same sizes) the mod is linked. Scattered parts installed at the same time as a linked mod are
    joined to it the same way when their files are on that mod's page.

Matching with Nexus (precise)
  * Only a page whose name is exactly your mod's name is linked automatically.
    Translations, add-ons, patches and "Name - something" pages are never
    picked behind your back.
  * When it is not clear, you get a list of candidates (author, downloads,
    dates, why it matched) and choose; "Verify in browser" opens the page so you
    can compare the "You last downloaded a file from this mod on ..." date that
    Nexus shows you with the date the files were installed.

Nexus inside the app
  * Updates tab: one click updates a mod (the right file is chosen from the
    Nexus update chain; your old files are backed up first).
  * Browse Nexus tab: a grid of mod cards with pictures that keeps loading as you
    scroll (40 per page). Nexus-style filters: sort (most endorsed / downloaded /
    newest / recently updated), category, tag, author, installed or not, and an
    adult-content switch (hidden by default). Click a card for its page: picture
    gallery, description, files, requirements (with the ones you have ticked),
    changelog, and Download & install. The "Period" box works like the one on the Nexus website
    (24 Hours ... 1 Year, or your own From/To dates) together with every sort and with word search; when
    Nexus won't filter by date the newest mods are read and sorted here. Pictures need the optional Pillow package
    (the exe from build_exe.bat includes it); without it only small PNG/GIF show.
  * Add mod...: pick an archive; it is identified automatically and installed.
  * Premium accounts download directly. Free accounts open the Nexus page
    ("Slow download"); the file is picked up through an nxm:// link (optional
    handler in Settings) or from your Downloads folder.

Safety net (Tools menu)
  * History and undo: every install, update, switch and on/off change is written down. Undo puts the old files back
    (from _disabled_mods/_backup), the old version number and the instances; newer changes to the same files must be
    undone first. Files taken away go to a backup folder, never deleted.
  * "This setup works" remembers which mods are on (and their versions). "Go back to a setup that worked" switches the
    same mods on and off again and, if you like, undoes the updates made since.
  * Updates tab: "Skip this update" hides the version Nexus has now until a newer one appears; "Stay on this version"
    hides every update for that mod. Pinned mods are listed last, in grey.
  * Compare two instances; Disk space per mod (and moving the switched-off mods to another drive, leaving a link);
    notes, tags and colours per mod (right-click).
  * Desktop shortcut per instance: "Play - Story run" switches to that instance and starts the game without opening
    the window (or hands it to the open window).

Check-up (Tools menu)
  * Check-up: mods in the wrong folder (a loose .archive, a CET mod whose init.lua is one folder too deep, a REDmod
    without info.json), leftovers of removed mods, two versions of the same file, links to files that are gone, mods
    that need a framework that is off or missing (Codeware, ArchiveXL, TweakXL, Cyber Engine Tweaks ...), mods that
    change the same game files (and which one wins) or replace the same script function, mods whose Nexus page was
    removed, mods that look abandoned, and framework mods not updated since the game changed. Each line says what it
    means; fixes (move, put aside, switch on) are written to History and can be undone. Items with a problem get a
    warning mark in the Library, and there is a "With a warning" filter.
  * Switching a mod on offers to switch on the framework it needs too; switching a framework off lists the mods that
    need it.
  * Find the mod that crashes my game: switches half of your mods off, you start the game and say what happened,
    and it narrows down in a handful of tries (a baseline test and a final check included). The search is kept if you
    close the window; at the end everything is put back, with the culprit off if you like.
  * Read the game's logs: the RED4ext, redscript and Cyber Engine Tweaks logs, error lines only, with the mods they
    mention.
  * A game update is noticed (the game program changed) and said once, naming the mods that reach into the game and
    haven't been updated on Nexus since.

Settings, lists, saves, endorsing (Tools menu)
  * Back up my settings / Restore settings from a backup: one zip with the settings of Cyber Engine Tweaks and its mods
    (hotkeys, options), RED4ext plugins and the game's own graphics and controls - settings files only, switched-off
    mods included. Restoring shows what is new / changed / the same first, keeps every file it replaces, refuses to run
    while the game is open, ignores anything in the zip that is not a settings file in a settings place, and can be
    undone in History.
  * Export my mod list / Import a mod list: names, Nexus numbers, versions and on/off as a file for ModScout or as a
    text list for a forum post (notes only if you tick the box; no folder names). Importing compares it with what you
    have, can queue the missing downloads and can make an instance that switches the same mods on and off.
  * Saves per instance (off until you switch it on): an instance can have saves of its own. The saves folder is
    renamed aside and another one takes its place when you switch or press Play - nothing is copied (unless you ask
    for a copy) and nothing is deleted; if a step fails, the first is taken back.
  * Endorse on Nexus from the details pane or the right-click menu (and take it back), and "Endorse the mods I use" for
    the linked mods you have not endorsed yet, with Nexus's reasons if it refuses one.

Playing
  * "Play" starts the game (through Steam when it lives in Steam's folder, otherwise the game program
    itself). The arrow next to it lists your instances: pick one and it is switched on, then the game starts.
    "Play without any mods" does the same with everything off.
  * "All on" / "All off" in the Library: All off switches to a ready-made empty instance (all mods off, or all but
    the shared frameworks), so the instance you were in keeps its mods; All on takes you back to it.

Instances
  * An instance is a named set of enabled mods. Switching moves only the
    difference between the game folder and <game>/_disabled_mods/, so nothing
    is copied. Saves and per-mod settings are shared between instances (an instance can be given saves
    of its own in Tools -> Saves per instance).

Only one window
  * Starting the program again, or pressing Nexus' "Slow download" button while it is open, never opens a
    second window: the open one comes forward and takes the link.

Settings and safety
  * Your API key is stored only in ~/.cp2077_mod_toggle.json on your PC and is
    only ever sent to api.nexusmods.com.
  * OFF moves a mod's files into <game>/_disabled_mods/ with the same relative
    paths. Nothing is deleted; replaced files go to _disabled_mods/_backup/.

Command line (optional)
    python cp2077_mod_toggle.py --list
    python cp2077_mod_toggle.py --match --check-updates
    python cp2077_mod_toggle.py --disable hair --enable "*"
    python cp2077_mod_toggle.py --instances
    python cp2077_mod_toggle.py --switch "Clean run"
    python cp2077_mod_toggle.py --play "Story run"          (what a desktop shortcut runs)
    python cp2077_mod_toggle.py --make-shortcut "Story run"
"""
from __future__ import annotations

import argparse
import base64
import bisect
import concurrent.futures
import functools
import hashlib
import html
import json
import math
import os
import platform
import queue
import re
import shlex
import shutil
import socket
import string
import struct
import subprocess
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
import webbrowser
import zipfile
import zlib
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path

APP_NAME = "ModScout 2077"
APP_ID = "CP2077-Mod-Toggle"
VERSION = "3.7"
DOMAIN = "cyberpunk2077"
NEXUS_SITE = "https://www.nexusmods.com"
API_KEYS_URL = NEXUS_SITE + "/settings/api-keys"      # where a person gets their personal API key
BROWSE_PAGE = 40                       # mods per Browse page (Nexus allows up to 50)
STASH_NAME = "_disabled_mods"
STATE_NAME = "_state.json"
JOURNAL_NAME = "_journal.json"
JOURNAL_MAX = 150                     # changes remembered for the History / undo list
GOOD_KEEP = 5                          # "this setup works" snapshots kept
NOTE_COLORS = ("red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink")
CONFIG_PATH = Path.home() / ".cp2077_mod_toggle.json"
GAME_EXE = Path("bin") / "x64" / "Cyberpunk2077.exe"
NO_WINDOW = 0x08000000 if os.name == "nt" else 0

# (folder relative to game root, how to split it into units, label)
#   "files"   -> every file below the folder (any depth) is its own unit
#   "entries" -> every direct child (file OR folder) is its own unit
RULES = [
    ("archive/pc/mod", "files", "Archive"),
    ("mods", "entries", "REDmod"),
    ("r6/scripts", "entries", "Scripts"),
    ("r6/tweaks", "entries", "Tweaks"),
    ("r6/input", "files", "Input"),
    ("r6/inputs", "files", "Input"),
    ("red4ext/plugins", "entries", "RED4ext"),
    ("bin/x64/plugins/cyber_engine_tweaks/mods", "entries", "CET"),
    ("bin/x64/plugins", "entries", "ASI/DLL"),  # CET's own folder is skipped
]
IGNORED_NAMES = {"desktop.ini", "thumbs.db", ".ds_store"}

# Shared libraries other mods commonly depend on. Disabling these asks first.
CORE_KEYS = {
    "cyberenginetweaks", "red4ext", "archivexl", "tweakxl", "codeware",
    "inputloader", "nativesettingsui", "modsettings", "redscript",
    "redfilesystem", "redhottools", "equipmentex",
}

# --------------------------------------------------------------------------
# Config (API key etc. live here, never in the game folder)
# --------------------------------------------------------------------------
def load_config() -> dict:
    try:
        data = json.loads(CONFIG_PATH.read_text("utf-8"))
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def save_config(**updates):
    cfg = load_config()
    cfg.update(updates)
    try:
        CONFIG_PATH.write_text(json.dumps(cfg, indent=2), "utf-8")
        try:
            os.chmod(CONFIG_PATH, 0o600)
        except OSError:
            pass
    except OSError:
        pass


def load_saved_game():
    p = load_config().get("game")
    return p if p and is_game_dir(p) else None


def save_game(path):
    save_config(game=str(path))


# --------------------------------------------------------------------------
# Names and versions
# --------------------------------------------------------------------------
KNOWN_EXT = {
    ".archive", ".xl", ".yaml", ".yml", ".tweak", ".xml", ".ini", ".json",
    ".lua", ".reds", ".dll", ".asi", ".disabled", ".bak", ".txt",
}
LEAD_MARKERS = re.compile(r"^(?:[#!@~_\s]+|\d{1,3}[_-])+")
NEXUS_TAIL = re.compile(r"(?:[-_ ]\d+){2,}$")
VERSION_TAIL = re.compile(r"(?:[-_ .][vV]\d+(?:[._]\d+)*|[-_ ]\d+(?:\.\d+)+)$")


def pretty_name(filename: str) -> str:
    name = filename
    while True:
        stem, ext = os.path.splitext(name)
        if stem and ext.lower() in KNOWN_EXT:
            name = stem
        else:
            break
    name = LEAD_MARKERS.sub("", name) or name
    name = NEXUS_TAIL.sub("", name) or name
    name = VERSION_TAIL.sub("", name) or name
    return name.strip(" -_.") or filename


def norm_key(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower()) or text.lower()


def name_tokens(text: str) -> list:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", s)
    return [t for t in re.split(r"[^A-Za-z0-9]+", s.lower()) if t]


PRE_WORDS = ("alpha", "beta", "rc", "pre", "preview", "dev", "test", "wip", "snapshot")


def parse_version(text):
    if not text:
        return None
    t = str(text).strip().lower()
    t = re.sub(r"^(?:version|ver|v)[\s._-]*(?=\d)", "", t)
    toks = re.findall(r"\d+|[a-z]+", t)
    nums, i = [], 0
    while i < len(toks) and toks[i].isdigit():
        nums.append(int(toks[i]))
        i += 1
    if not nums:
        return None
    suffix = toks[i] if i < len(toks) else ""
    tail = tuple(int(x) for x in toks[i + 1:] if x.isdigit())
    if suffix.startswith(PRE_WORDS):
        rank = -1
    elif suffix in ("", "final", "release", "stable"):
        rank = 0
    else:
        rank = 1
    return nums, rank, (suffix if rank == 1 else ""), tail


def compare_versions(a, b):
    """-1 / 0 / 1, or None when either side can't be read as a version."""
    pa, pb = parse_version(a), parse_version(b)
    if pa is None or pb is None:
        return None
    na, nb = list(pa[0]), list(pb[0])
    n = max(len(na), len(nb))
    na += [0] * (n - len(na))
    nb += [0] * (n - len(nb))
    ka, kb = (na, pa[1], pa[2], pa[3]), (nb, pb[1], pb[2], pb[3])
    return (ka > kb) - (ka < kb)


def fmt_date(ts) -> str:
    try:
        return time.strftime("%Y-%m-%d", time.localtime(float(ts)))
    except (OverflowError, OSError, ValueError, TypeError):
        return ""


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------
def birth_time(p: Path) -> float:
    try:
        st = p.stat()
    except OSError:
        return 0.0
    bt = getattr(st, "st_birthtime", None)
    if bt:
        return float(bt)
    return float(st.st_ctime if os.name == "nt" else st.st_mtime)


@dataclass
class Unit:
    rel: str          # posix path relative to the game folder
    category: str
    is_dir: bool
    enabled: bool
    ts: float = 0.0   # when it was put there (creation time)

    def __post_init__(self):
        self.pretty = pretty_name(self.rel.rsplit("/", 1)[-1])
        self.key = norm_key(self.pretty)


@dataclass
class Mod:
    key: str
    name: str
    units: list
    core: bool
    local_name: str = ""
    nexus_id: int = 0
    nexus: dict = None
    nexus_error: str = ""
    installed_version: str = ""
    version_source: str = ""
    update: str = ""          # update | pinned | ok | maybe | unknown | "" (not linked)
    update_note: str = ""
    install_ts: float = 0.0
    pinned: str = ""          # "stay" (stay on this version) | "skip" (skip this update) | ""
    note: str = ""
    tags: list = field(default_factory=list)
    color: str = ""

    @property
    def status(self) -> str:
        on = sum(1 for u in self.units if u.enabled)
        if on == len(self.units):
            return "on"
        return "off" if on == 0 else "partial"

    @property
    def cats(self) -> list:
        seen = []
        for u in self.units:
            if u.category not in seen:
                seen.append(u.category)
        return seen

    @property
    def latest_version(self) -> str:
        return (self.nexus or {}).get("version", "") or ""

    @property
    def url(self) -> str:
        return f"{NEXUS_SITE}/{DOMAIN}/mods/{self.nexus_id}" if self.nexus_id else ""


def discover(root: Path, enabled: bool) -> list:
    """Find mod units below `root` (the game folder, or the stash folder)."""
    out, seen = [], set()

    def add(p: Path, cat: str):
        if p.name.lower() in IGNORED_NAMES:
            return
        rel = p.relative_to(root).as_posix()
        if rel in seen:
            return
        seen.add(rel)
        out.append(Unit(rel, cat, p.is_dir(), enabled, birth_time(p)))

    for rel_dir, mode, cat in RULES:
        base = root / rel_dir
        if not base.is_dir():
            continue
        try:
            if mode == "files":
                for p in sorted(base.rglob("*")):
                    if p.is_file():
                        add(p, cat)
            else:
                for p in sorted(base.iterdir()):
                    if (rel_dir == "bin/x64/plugins" and p.is_dir()
                            and p.name.lower() == "cyber_engine_tweaks"):
                        continue
                    add(p, cat)
        except OSError:
            continue
    return out


def build_groups(units: list, overrides: dict, links: dict, fuzzy: bool = True,
                 nexus_cache: dict = None) -> list:
    """Group units into mods. Priority: your own merges > Nexus link > name."""
    nexus_cache = nexus_cache or {}
    buckets = defaultdict(list)
    for u in units:
        ov = overrides.get(u.rel)
        lk = links.get(u.rel)
        if ov:
            k = "o:" + ov["id"]
        elif lk:
            k = "n:%d" % lk["id"]
        else:
            k = u.key
        buckets[k].append(u)

    # An unlinked group joins a Nexus-linked group when it has the same name.
    names = {}
    for k, us in buckets.items():
        if k.startswith("n:"):
            ks = {u.key for u in us}
            info = nexus_cache.get(k[2:])
            if info and info.get("name"):
                ks.add(norm_key(info["name"]))
            for nk in ks:
                names.setdefault(nk, k)
    for k in [k for k in buckets if not k.startswith(("n:", "o:"))]:
        if k in names:
            buckets[names[k]].extend(buckets.pop(k))

    if fuzzy:
        # Merge automatic groups whose name starts with another group's name.
        # Needs 9+ characters so short names never get swallowed.
        auto = sorted((k for k in buckets if not k.startswith(("n:", "o:"))), key=len)
        parent = {k: k for k in auto}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i, a in enumerate(auto):
            if len(a) < 9:
                continue
            for b in auto[i + 1:]:
                if b.startswith(a):
                    parent[find(b)] = find(a)
        merged = defaultdict(list)
        for k, us in buckets.items():
            merged[find(k) if k in parent else k].extend(us)
        buckets = merged

    mods = []
    for key, us in buckets.items():
        local = min(us, key=lambda u: (not u.is_dir, len(u.pretty))).pretty
        name = overrides[us[0].rel]["name"] if key.startswith("o:") else local
        core = any(u.key in CORE_KEYS for u in us)
        mods.append(Mod(key, name, us, core, local_name=local))
    mods.sort(key=lambda m: m.name.lower())
    return mods


# --------------------------------------------------------------------------
# Nexus Mods API (v1)
# --------------------------------------------------------------------------
class NexusError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status


def gql_message(data) -> str:
    """The first couple of error messages of a GraphQL reply, shortened."""
    out = []
    try:
        for e in data["errors"][:3]:
            m = re.sub(r"\s+", " ", str(e["message"])).strip()[:200]
            if m and m not in out:
                out.append(m)
    except (KeyError, TypeError, AttributeError):
        pass
    return " / ".join(out[:2])


def nexus_error_text(err) -> str:
    """A Nexus error for the person: its search engine's raw complaint (JSON, 'parse_exception') helps nobody."""
    s = re.sub(r"\s+", " ", str(err)).strip()
    if re.search(r"parse_exception|search_phase_execution|root_cause", s):
        return ("Nexus' search couldn't read this request.\n"
                "Try other words, fewer filters or another time period.")
    return s[:300]


SEARCH_DOMAIN_FIELDS = ("gameDomainName",)          # Nexus: "doesn't accept argument 'gameDomain'"
SEARCH_WRAPS = ("list", "single")                   # {x: [{...}]} or {x: {...}}
SEARCH_FIELD_SETS = ("modId name summary version", "modId name")
# (name field, comparison, spellings of the search text to try)
SEARCH_MODES = (
    ("name", "WILDCARD", (("*{}*", "title"), ("*{}*", "lower"), ("{}*", "title"),
                          ("{}", "title"), ("*{}*", "stars-lower"))),
    ("name", "MATCHES", (("{}", "title"), ("{}", "lower"))),
    ("nameStemmed", "MATCHES", (("{}", "lower"), ("{}", "title"))),
    ("nameStemmed", "WILDCARD", (("*{}*", "lower"), ("{}*", "lower"), ("*{}*", "stars-lower"))),
)
# Other ways of searching names, tried one after the other when the checked way finds nothing on the first page
# (a case-sensitive wildcard, or half a word typed): (field, comparison, spelling)
TEXT_ALTS = (
    ("name", "WILDCARD", ("*{}*", "lower")),
    ("nameStemmed", "MATCHES", ("{}", "lower")),
    ("nameStemmed", "WILDCARD", ("*{}*", "lower")),
    ("name", "MATCHES", ("{}", "title")),
    ("name", "MATCHES", ("{}", "lower")),
)


def spaced_words(text: str) -> list:
    """'NativeSettingsUI_v2' -> ['Native', 'Settings', 'UI']  (case kept, version tail dropped)"""
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", s)
    return [w for w in re.split(r"[^A-Za-z0-9]+", s) if w]


def render_term(form, text: str) -> str:
    pattern, case = form
    words = text.split()
    if case.startswith("stars"):
        body = "*".join(words)
    else:
        body = " ".join(words)
    if case.endswith("lower"):
        body = body.lower()
    elif case == "title":
        body = " ".join(w[:1].upper() + w[1:] for w in body.split(" "))
    return pattern.replace("{}", body)


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """urllib would copy the apikey header to wherever a redirect points. Don't follow any."""

    def redirect_request(self, *args, **kwargs):
        return None


class Nexus:
    """Tiny client for https://api.nexusmods.com/v1. The key is only ever sent
    to that host (or to CP2077_NEXUS_BASE, which exists for testing)."""

    DEFAULT_BASE = "https://api.nexusmods.com"

    def __init__(self, key: str, base: str = None, timeout: int = 25):
        self.key = (key or "").strip()
        base = (base or os.environ.get("CP2077_NEXUS_BASE") or self.DEFAULT_BASE).rstrip("/")
        u = urllib.parse.urlparse(base)
        local = u.hostname in ("127.0.0.1", "localhost", "::1")
        if not (local or (u.scheme == "https" and u.hostname == "api.nexusmods.com")):
            base = self.DEFAULT_BASE          # the key is never sent anywhere else
        self.base = base
        self.timeout = timeout
        self.limits = {}
        self.search_cfg = None
        self.search_failure = ""
        self.browse_cfg = None                 # which spelling of the search filter this Nexus understands
        self.browse_bad = set()                # filters / sort keys Nexus refused (they are applied here instead)
        self.browse_sort_bad = set()
        self.date_style = 0                    # index into DATE_STYLES: how this Nexus wants dates in a filter
        self.text_mode = None                  # (field, comparison, spelling) that found mods when the first choice didn't
        self.text_bad = set()
        self.search_failure_at = 0.0
        self._crawl = None                     # mods of a period read through here (see _browse_crawl)
        self.browse_fields = list(BROWSE_FIELDS)
        self._game = None
        self._opener = urllib.request.build_opener(_NoRedirect)

    def _note_limits(self, headers):
        try:
            for k in ("daily-limit", "daily-remaining", "hourly-limit", "hourly-remaining"):
                v = headers.get("x-rl-" + k)
                if v is not None:
                    self.limits[k] = int(v)
        except (ValueError, AttributeError):
            pass

    def _call(self, url: str, body=None, form=None):
        headers = {
            "apikey": self.key,
            "Accept": "application/json",
            "Application-Name": APP_ID,
            "Application-Version": VERSION,
            "User-Agent": f"{APP_ID}/{VERSION} ({platform.system()} {platform.release()})",
        }
        data = None
        if body is not None:
            data = json.dumps(body).encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif form is not None:
            data = urllib.parse.urlencode(form).encode("utf-8")
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        req = urllib.request.Request(url, data=data, headers=headers)
        try:
            with self._opener.open(req, timeout=self.timeout) as r:
                self._note_limits(r.headers)
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            self._note_limits(e.headers)
            said = ""
            if form is not None:
                try:
                    said = str(json.loads(e.read().decode("utf-8", "replace")).get("message") or "")
                except (ValueError, OSError, AttributeError):
                    pass
            if e.code == 401:
                raise NexusError(401, "Nexus rejected the API key. Check it in Settings.")
            if e.code == 403:
                raise NexusError(403, endorse_problem(said) if form is not None else
                                 "Nexus says this key isn't allowed to do that.")
            if e.code == 404:
                raise NexusError(404, "Not found on Nexus.")
            if e.code == 429:
                raise NexusError(429, "Nexus rate limit reached. Try again in about an hour.")
            detail = _clean_text(said, 160) if form is not None else ""
            if body is not None:
                try:
                    detail = gql_message(json.loads(e.read().decode("utf-8", "replace")))
                except (ValueError, OSError):
                    pass
            raise NexusError(e.code, f"Nexus returned error {e.code}." + (f" {detail}" if detail else ""))
        except urllib.error.URLError as e:
            raise NexusError(0, f"Couldn't reach Nexus ({e.reason}).")
        except (ValueError, OSError) as e:
            raise NexusError(0, f"Unexpected reply from Nexus ({e}).")

    def _get(self, path: str, params: dict = None):
        url = f"{self.base}/v1/{path}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        return self._call(url)

    # ---- search by name -------------------------------------------------------
    # The v1 API has no search. Nexus's newer GraphQL API does, but it is not formally
    # documented and its spelling has changed over time, so the first search "probes":
    # it tries the known spellings against a mod that certainly exists and keeps the
    # first one that finds it. Everything is reported, never silently ignored.
    def _gql_mods(self, cfg: dict, term: str = None, count: int = 20, offset: int = 0):
        """One search call. `cfg` says which spelling to use (see probe_search). With
        term=None only the game is filtered (used to find the right spelling)."""
        def flt(field, op, var):
            v = "{value: $%s, op: %s}" % (var, op)
            return f"{field}: [{v}]" if cfg["wrap"] == "list" else f"{field}: {v}"
        parts, decl, variables = [flt(cfg["df"], "EQUALS", "g")], "$g: String!", {"g": DOMAIN}
        if term is not None:                       # a declared variable must be used (GraphQL rule)
            parts.append(flt(cfg["nf"], cfg["op"], "t"))
            decl += ", $t: String!"
            variables["t"] = term
        q = ("query S(%s) { mods(filter: {%s}, offset: %d, count: %d) { nodes { %s } } }"
             % (decl, ", ".join(parts), offset, count, cfg["fields"]))
        data = self._call(f"{self.base}/v2/graphql", {"query": q, "variables": variables})
        if not isinstance(data, dict):
            raise NexusError(0, "Unexpected reply from Nexus search.")
        mods = (data.get("data") or {}).get("mods")
        if data.get("errors") and not mods:
            raise NexusError(400, "Nexus search: " + gql_message(data))
        out = []
        for n in (mods or {}).get("nodes") or []:
            try:
                mid = int(n.get("modId"))
            except (AttributeError, TypeError, ValueError):
                continue
            out.append({"id": mid,
                        "name": html.unescape(str(n.get("name") or "")).strip(),
                        "version": str(n.get("version") or "").strip(),
                        "summary": html.unescape(str(n.get("summary") or "")).strip()[:300]})
        return out

    def probe_search(self):
        """-> the working search spelling, or raises NexusError listing what Nexus said."""
        if self.search_cfg:
            return self.search_cfg
        if self.search_failure:
            if time.time() - self.search_failure_at < 90:      # a blip (network, busy Nexus) must not stick all session
                raise NexusError(0, self.search_failure)
            self.search_failure = ""
        seen, tried = [], 0

        def note(e):
            if str(e) not in seen:
                seen.append(str(e))
        base = None
        try:
            for df in SEARCH_DOMAIN_FIELDS:
                for wrap in SEARCH_WRAPS:
                    for fields in SEARCH_FIELD_SETS:
                        cfg = {"df": df, "wrap": wrap, "fields": fields}
                        tried += 1
                        try:
                            self._gql_mods(cfg, None, 1)
                        except NexusError as e:
                            if e.status in (401, 403, 429):
                                raise
                            note(e)
                            continue
                        base = cfg
                        break
                    if base:
                        break
                if base:
                    break
            if base:
                for nf, op, forms in SEARCH_MODES:
                    for form in forms:
                        cfg = dict(base, nf=nf, op=op, form=form)
                        tried += 1
                        try:
                            nodes = self._gql_mods(cfg, render_term(form, "cyber engine tweaks"))
                        except NexusError as e:
                            if e.status in (401, 403, 429):
                                raise
                            note(e)
                            break          # this field/comparison isn't understood: skip its other spellings
                        if any(n["id"] == 107 or "cyberenginetweaks" in norm_key(n["name"]) for n in nodes):
                            self.search_cfg = cfg
                            return cfg
        except NexusError as e:
            if e.status != 429:
                self.search_failure, self.search_failure_at = str(e), time.time()
            raise
        why = ("Nexus said: " + " | ".join(seen[:3])) if seen else \
            "Nexus answered, but its search found nothing for a mod that exists."
        self.search_failure = f"Searching Nexus by name isn't working with this key (tried {tried} ways). {why}"
        self.search_failure_at = time.time()
        raise NexusError(0, self.search_failure)

    def search(self, term: str, count: int = 20, offset: int = 0) -> list:
        cfg = self.probe_search()
        return self._gql_mods(cfg, render_term(cfg["form"], term), count, offset)

    def md5_lookup(self, md5: str) -> list:
        """Official lookup of a downloaded file by its fingerprint -> [{mod, file_details}]."""
        try:
            data = self._get(f"games/{DOMAIN}/mods/md5_search/{md5}.json")
        except NexusError as e:
            if e.status == 404:
                return []
            raise
        return [d for d in data if isinstance(d, dict)] if isinstance(data, list) else []

    def validate(self):
        return self._get("users/validate.json")

    @property
    def local(self) -> bool:
        return urllib.parse.urlparse(self.base).hostname in ("127.0.0.1", "localhost", "::1")

    def download_links(self, mod_id, file_id, key: str = "", expires: str = "") -> list:
        """Direct download addresses. Premium accounts can ask freely; everyone else needs the
        one-time key that Nexus puts in the nxm:// link after a click on its website."""
        params = {"key": key, "expires": expires} if key and expires else None
        try:
            data = self._get(f"games/{DOMAIN}/mods/{int(mod_id)}/files/{int(file_id)}/download_link.json", params)
        except NexusError as e:
            if e.status == 403:
                raise NeedsBrowser(mod_id, file_id)
            raise
        out = []
        for d in data if isinstance(data, list) else []:
            if isinstance(d, dict) and d.get("URI"):
                out.append({"name": str(d.get("short_name") or d.get("name") or ""), "url": str(d["URI"])})
        if not out:
            raise NexusError(0, "Nexus gave no download address for that file.")
        return out

    # ---- browsing: pages, sorting, filters ---------------------------------------------------------------
    # The REST list endpoints only ever return 10 mods. The GraphQL API pages (50 at a time), sorts and filters, and
    # also knows pictures, categories and tags. If it refuses something, that part is dropped and the rest still works;
    # if it is unusable the documented v3 search (no text/tag filters) and finally the 10-item lists are used.
    _FIELD_ERR = re.compile(r"Field '(\w+)' doesn't exist on type '(\w+)'|Cannot query field \"(\w+)\" on type \"(\w+)\"")

    @staticmethod
    def _drop_field(fields: list, name: str, typ: str, required) -> bool:
        for tok in list(fields):
            root = tok.split()[0]
            hit = (typ == "Mod" and root == name) or \
                  (typ != "Mod" and "{" in tok and re.search(r"\b%s\b" % re.escape(name), tok))
            if hit and root not in required:
                fields.remove(tok)
                return True
        return False

    def _gql_run(self, build, fields: list, variables: dict, root: str, required=("modId",)):
        """Send a GraphQL query; whenever Nexus says a selected field doesn't exist, drop it and ask again."""
        for _ in range(10):
            msgs = []
            try:
                data = self._call(f"{self.base}/v2/graphql", {"query": build(" ".join(fields)), "variables": variables})
            except NexusError as e:
                if e.status in (401, 403, 404, 429):
                    raise
                msgs = [str(e)]
            else:
                if not isinstance(data, dict):
                    raise NexusError(0, "Unexpected reply from Nexus.")
                got = (data.get("data") or {}).get(root)
                if got is not None:
                    return got
                msgs = [str(x.get("message", "")) for x in (data.get("errors") or []) if isinstance(x, dict)]
            changed = False
            for m in msgs:
                for g in self._FIELD_ERR.finditer(m):
                    changed |= self._drop_field(fields, g.group(1) or g.group(3), g.group(2) or g.group(4), required)
            if not changed:
                raise NexusError(400, "Nexus: " + (" / ".join(x[:200] for x in msgs[:2]) or "no answer"))
        raise NexusError(400, "Nexus kept refusing the query.")

    @staticmethod
    def _date_value(ts, style: str, end: bool = False) -> str:
        if style == "unix":
            return str(int(ts))
        if style == "date":                                        # whole days: the end day counts in full
            return time.strftime("%Y-%m-%d", time.gmtime(ts + (86400 if end else 0)))
        if style == "isoesc":                                      # the colons escaped, as a text search wants them
            return time.strftime("%Y-%m-%dT%H\\:%M\\:%SZ", time.gmtime(ts))
        return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts))

    def _filter(self, cfg: dict, term: str, category: str, tag: str, author: str, period=None) -> dict:
        def cond(field, op, value):
            v = {"value": value, "op": op}
            return {field: [v] if cfg["wrap"] == "list" else v}
        f = cond(cfg["df"], "EQUALS", DOMAIN)
        if term:
            f.update(cond(cfg["nf"], cfg["op"], render_term(cfg["form"], term)))
        for key, val in (("categoryName", category), ("tag", tag), ("author", author)):
            if val and key not in self.browse_bad:
                f.update(cond(key, "EQUALS", val))
        if period and period["field"] not in self.browse_bad and (period.get("since") or period.get("until")):
            st = DATE_STYLES[self.date_style]
            conds = []
            if period.get("since"):
                conds.append({"value": self._date_value(period["since"], st), "op": "GTE"})
            if period.get("until"):
                conds.append({"value": self._date_value(period["until"], st, True), "op": "LTE"})
            f[period["field"]] = conds
        return f

    def _next_date_style(self, period):
        """The date filter didn't work in this spelling: try the next one, or give up on it (it is done here then)."""
        if self.date_style < len(DATE_STYLES) - 1:
            self.date_style += 1
        else:
            self.browse_bad.add(period["field"])

    @staticmethod
    def _outside(nodes, period, slack=2 * 86400) -> bool:
        """True when a filtered answer holds mods from outside the period: Nexus accepted the date but ignored or
        misread it (a time in milliseconds, say). The slack covers a filter that works in whole days."""
        fld, lo, hi = period["field"], period.get("since"), period.get("until")
        for n in nodes:
            it = norm_node(n)
            d = (it["updated"] if fld == "updatedAt" else it["created"]) if it else 0
            if d and ((lo and d < lo - slack) or (hi and d > hi + slack)):
                return True
        return False

    def _text_first(self):
        """(field, comparison, spelling) for searching by words: the one probe_search checked against the real Nexus."""
        if self.text_mode:
            return self.text_mode
        try:
            cfg = self.probe_search()
        except NexusError as e:
            if e.status in (401, 403, 429):
                raise
            return ("name", "WILDCARD", ("*{}*", "title"))      # unchecked, but the other spellings follow if it finds nothing
        return (cfg["nf"], cfg["op"], cfg["form"])

    def _gql_browse(self, term, sort, category, tag, author, offset, count, period=None):
        """One page -> (nodes, total or None). Words are searched the way that was checked against Nexus; when that
        finds nothing on the first page, a few other spellings get a chance (capitals, half a word)."""
        if not term:
            return self._gql_page(None, "", sort, category, tag, author, offset, count, period)
        first = self._text_first()
        if offset > 0:                                  # later pages go on the way the first page worked
            return self._gql_page(first, term, sort, category, tag, author, offset, count, period)
        empty = None
        for i, mode in enumerate([first] + [m for m in TEXT_ALTS if m != first and m not in self.text_bad][:3]):
            try:
                nodes, total = self._gql_page(mode, term, sort, category, tag, author, offset, count, period)
            except NexusError as e:
                if i == 0 or e.status in (401, 403, 404, 429):
                    raise
                self.text_bad.add(mode)                 # this spelling is the problem: the others worked as asked
                continue
            if nodes:
                if i:
                    self.text_mode = mode               # it found them: start with it from now on
                return nodes, total
            empty = empty or (nodes, total)
        return empty

    def _gql_page(self, text, term, sort, category, tag, author, offset, count, period=None):
        """One request (with the corrections below) -> (nodes, total or None). Learns which filters, sort keys and
        date spellings this Nexus accepts; what it refuses is done here instead."""
        cfg = dict(self.browse_cfg or {"df": "gameDomainName", "wrap": "list"})
        if text:
            cfg.update(nf=text[0], op=text[1], form=text[2])
        probed = bool(self.browse_cfg)
        saved = (self.date_style, set(self.browse_bad), set(self.browse_sort_bad))
        try:
            for _ in range(10):
                used = {k for k, v in (("categoryName", category), ("tag", tag), ("author", author))
                        if v and k not in self.browse_bad}
                sort_v = None
                if sort and sort not in self.browse_sort_bad and (sort != "relevance" or term):
                    sort_v = [{sort: {"direction": "DESC"}}]
                dated = bool(period and (period.get("since") or period.get("until")) and period["field"] not in self.browse_bad)
                variables = {"filter": self._filter(cfg, term, category, tag, author, period), "sort": sort_v,
                             "offset": offset, "count": count}

                def build(sel):
                    return ("query Browse($filter: ModsFilter, $sort: [ModsSort!], $offset: Int, $count: Int) "
                            "{ mods(filter: $filter, sort: $sort, offset: $offset, count: $count) "
                            "{ totalCount nodes { %s } } }" % sel)
                try:
                    got = self._gql_run(build, self.browse_fields, variables, "mods", required=("modId", "name"))
                except NexusError as e:
                    if e.status in (401, 403, 404, 429):
                        raise
                    msg = str(e)
                    changed = False
                    for key in used:
                        if re.search(r"(?<![A-Za-z])%s(?![A-Za-z])" % key, msg):
                            self.browse_bad.add(key)
                            changed = True
                    if sort_v and ("ModsSort" in msg or (re.search(r"(?<![A-Za-z])%s(?![A-Za-z])" % sort, msg)
                                                         and not (dated and sort == period["field"]))):
                        self.browse_sort_bad.add(sort)      # (sorting by the date that is also filtered: the filter is blamed)
                        changed = True
                    if dated and not changed:           # Nexus' own wording rarely names the date: it is the suspect
                        self._next_date_style(period)
                        changed = True
                    if not changed and not probed:      # the game filter may need another spelling
                        try:
                            base = self.probe_search()
                        except NexusError:
                            base = None
                        if base:
                            cfg.update(df=base["df"], wrap=base["wrap"])
                            probed = changed = True
                    if not changed:
                        raise
                    continue
                nodes = [n for n in (got.get("nodes") or []) if isinstance(n, dict)]
                if dated and nodes and self._outside(nodes, period):
                    self._next_date_style(period)       # accepted, but not obeyed
                    continue
                self.browse_cfg = {"df": cfg["df"], "wrap": cfg["wrap"]}
                try:
                    total = int(got.get("totalCount"))
                except (TypeError, ValueError):
                    total = None
                return nodes, total
            raise NexusError(400, "Nexus kept refusing the search.")
        except NexusError:
            # a failure that is about something else must not leave wrong lessons behind
            self.date_style, self.browse_bad, self.browse_sort_bad = saved
            raise

    def _keep(self, it, category, tag, author, hide_adult) -> bool:
        if not shown_on_nexus(it) or (hide_adult and it.get("adult")):
            return False
        if category and "categoryName" in self.browse_bad and it["category"].lower() != category.lower():
            return False
        if tag and "tag" in self.browse_bad and tag.lower() not in [t.lower() for t in it["tags"]]:
            return False
        if author and "author" in self.browse_bad and it["author"].lower() != author.lower():
            return False
        return True

    def browse(self, term="", sort="endorsements", category="", tag="", author="", offset=0,
               count=BROWSE_PAGE, hide_adult=True, period=None) -> dict:
        """-> {items, total, next, more, notes}. `next` is the offset to ask for the following page.
        period: {"field": "createdAt"|"updatedAt", "since": ts, "until": ts, "label": text} or None."""
        notes, items, off, total, more = [], [], offset, None, True
        fld = period["field"] if period and (period.get("since") or period.get("until")) else ""
        if not fld:
            period = None
        undated = client = False

        def crawl():                                   # Nexus won't filter dates, and the list isn't in date order
            return bool(fld) and fld in self.browse_bad and sort != fld and fld not in self.browse_sort_bad
        try:
            if crawl():
                return self._browse_crawl(term, sort, category, tag, author, offset, count, hide_adult, period)
            attempt = 0
            while attempt < (12 if client else 4):      # hidden (adult / draft) mods are replaced by the next ones
                ask = count if attempt == 0 else (50 if client else max(count - len(items), 12))
                nodes, tot = self._gql_browse(term, sort, category, tag, author, off, ask, period)
                total = tot if tot is not None else total
                client = bool(fld) and fld in self.browse_bad        # Nexus won't filter dates: we do it here
                if crawl():
                    return self._browse_crawl(term, sort, category, tag, author, offset, count, hide_adult, period)
                full = ended = False
                for n in nodes:
                    off += 1
                    it = norm_node(n)
                    if it is None:
                        continue
                    if fld:                              # exact to the second, whatever Nexus rounded to
                        d = it["updated"] if fld == "updatedAt" else it["created"]
                        if not d:
                            undated = True
                        elif period.get("since") and d < period["since"]:
                            ended = ended or sort == fld             # newest first: everything after this is older
                            continue
                        elif period.get("until") and d > period["until"]:
                            continue
                    if self._keep(it, category, tag, author, hide_adult):
                        items.append(it)
                        if len(items) >= count:
                            full = True
                            break
                if ended:
                    more = False
                    break
                if full:
                    more = total is None or off < total
                    break
                if len(nodes) < ask or (total is not None and off >= total):
                    more = False
                    break
                attempt += 1
            for key, what in (("tag", "tag"), ("categoryName", "category"), ("author", "author")):
                if key in self.browse_bad:
                    notes.append(f"Nexus doesn't filter by {what} itself, so the {what} filter only checks what is loaded.")
            if client:
                total = None
                notes.append("Nexus didn't accept the time period itself, so I looked through the list and kept the mods "
                             "from that period" + (" (press Load more to look further)." if more else "."))
                if undated:
                    notes.append("Some mods came without a date, so they are shown regardless.")
            if sort in self.browse_sort_bad and term:
                keys, toks = {norm_key(term)}, set(name_tokens(term))
                items.sort(key=lambda it: -score_match(keys, toks, it["name"])[0])
            if (fld and not client and offset == 0 and not items and period.get("since")
                    and fld not in self.browse_sort_bad and self._period_has_mods(term, category, tag, author,
                                                                                  hide_adult, period)):
                self.browse_bad.add(fld)                # Nexus said "nothing" but there are some: its date filter can't be trusted
                return self.browse(term, sort, category, tag, author, offset, count, hide_adult, period)
            return {"items": items, "total": total, "next": off, "more": more, "notes": notes}
        except NexusError as e:
            if e.status in (401, 403, 429) or term or category or tag or author or fld:
                raise                                   # the plain lists can't do these: say so, don't show a wrong list
            first = str(e)
        return self._browse_fallback(sort, offset, count, hide_adult, first, period)

    CRAWL_PAGES = 24                                    # 24 x 50 = the newest 1,200 mods

    def _period_has_mods(self, term, category, tag, author, hide_adult, period) -> bool:
        """Nexus' date filter found nothing. Look at the newest mods without it: is that really so?"""
        fld = period["field"]
        try:
            nodes, _ = self._gql_browse(term, fld, category, tag, author, 0, 50, None)
        except NexusError:
            return False
        for n in nodes:
            it = norm_node(n)
            d = (it["updated"] if fld == "updatedAt" else it["created"]) if it else 0
            if d and d >= period["since"] and (not period.get("until") or d <= period["until"]) \
                    and self._keep(it, category, tag, author, hide_adult):
                return True
        return False

    @staticmethod
    def _rank(items, sort, term):
        """Order mods that were collected here the way Nexus would have ordered them."""
        if sort == "relevance" and term:
            keys, toks = {norm_key(term)}, set(name_tokens(term))
            items.sort(key=lambda it: -score_match(keys, toks, it["name"])[0])
            return
        key = {"endorsements": "endorsements", "downloads": "downloads", "createdAt": "created",
               "updatedAt": "updated"}.get(sort)
        if key:
            items.sort(key=lambda it: (-it[key], it["name"].lower()))

    def _browse_crawl(self, term, sort, category, tag, author, offset, count, hide_adult, period) -> dict:
        """Nexus won't filter by date, so: read the list newest first until it is older than the period, keep what
        is inside, put it in the order that was asked for, and hand it out page by page (kept for 'Load more')."""
        fld = period["field"]
        since, until = period.get("since") or 0, period.get("until") or 0
        key = (term, sort, category, tag, author, bool(hide_adult), fld, since, until)
        c = self._crawl if offset > 0 and self._crawl and self._crawl["key"] == key else None
        if c is None:
            items, seen, off, pages, done, undated = [], set(), 0, 0, False, False
            while pages < self.CRAWL_PAGES and not done:
                nodes, tot = self._gql_browse(term, fld, category, tag, author, off, 50, period)
                pages += 1
                for n in nodes:
                    off += 1
                    it = norm_node(n)
                    if it is None or it["id"] in seen:
                        continue
                    seen.add(it["id"])
                    d = it["updated"] if fld == "updatedAt" else it["created"]
                    if not d:
                        undated = True
                    elif since and d < since:
                        done = True                     # newest first: everything after this is older
                        continue
                    elif until and d > until:
                        continue
                    if self._keep(it, category, tag, author, hide_adult):
                        items.append(it)
                if not nodes or (tot is not None and off >= tot) or (tot is None and len(nodes) < 50):
                    done = True
            self._rank(items, sort, term)
            c = self._crawl = {"key": key, "items": items, "done": done, "scanned": off, "undated": undated}
        page = c["items"][offset:offset + count]
        nxt = offset + len(page)
        notes = [f"Nexus doesn't filter by date here, so I read through the newest {c['scanned']:,} mods and kept the ones "
                 f"{period_text(period)}." + ("" if c["done"] else " That's as far back as I look at once, so older "
                                              "ones in this period are missing.")]
        if c["undated"]:
            notes.append("Some mods came without a date, so they are shown regardless.")
        return {"items": page, "total": len(c["items"]) if c["done"] else None, "next": nxt,
                "more": nxt < len(c["items"]), "notes": notes}

    def _browse_fallback(self, sort, offset, count, hide_adult, why, period=None) -> dict:
        v3s = next((s[2] for s in BROWSE_SORTS if s[1] == sort), None) or "endorsements"
        v1k = next((s[3] for s in BROWSE_SORTS if s[1] == sort), None) or "trending"
        try:
            page = offset // count + 1
            r = self._call(f"{self.base}/v3/mods/search",
                           {"filters": {"games": [DOMAIN], "adult": "exclude" if hide_adult else "include"},
                            "sort": {"field": v3s, "direction": "desc"},
                            "pagination": {"type": "page", "page": page, "page_size": count}})
            d = r.get("data", r) if isinstance(r, dict) else {}
            meta = r.get("meta") if isinstance(r, dict) and isinstance(r.get("meta"), dict) else {}
            mods = d.get("mods") if isinstance(d, dict) else None
            if not isinstance(mods, list):
                raise NexusError(0, "no mods in the v3 answer")
            items = []
            for m in mods:
                if not isinstance(m, dict):
                    continue
                try:
                    mid = int(m.get("game_scoped_id") or (int(m.get("id")) & 0xFFFFFFFF))
                except (TypeError, ValueError):
                    continue
                au, ca = m.get("author"), m.get("category")
                it = {"id": mid, "name": clean_text(m.get("name"), 200), "version": clean_text(m.get("version"), 40),
                      "summary": clean_text(m.get("summary"), 400),
                      "author": clean_text(au.get("name") if isinstance(au, dict) else au, 80),
                      "downloads": int(m.get("downloads") or 0), "endorsements": int(m.get("endorsements") or 0),
                      "updated": parse_ts(m.get("updated_at")), "created": parse_ts(m.get("created_at")),
                      "adult": bool(m.get("adult")), "status": "",
                      "thumb": http_url(m.get("thumbnail_url")), "picture": http_url(m.get("thumbnail_url")),
                      "category": clean_text(ca.get("name") if isinstance(ca, dict) else ca, 60), "tags": []}
                if self._keep(it, "", "", "", hide_adult) and in_period(it, period):
                    items.append(it)
            total = next((int(meta[k]) for k in ("total", "total_count", "total_results") if str(meta.get(k, "")).isdigit()),
                         None)
            return {"items": items, "total": total, "next": offset + len(mods),
                    "more": len(mods) >= count and page < 100,
                    "notes": ["Nexus' search service didn't answer, so this is Nexus' plain list: no words, tag or "
                              "category filters right now." + (" The time period only checks this page." if period else "")]}
        except NexusError as e:
            if e.status in (401, 403, 429):
                raise
        items = [it for it in self.listing(v1k) if self._keep(it, "", "", "", hide_adult) and in_period(it, period)]
        return {"items": items, "total": len(items), "next": len(items), "more": False,
                "notes": ["Nexus only answered its basic list (10 mods, no filters): " + why[:120]]}

    def game_info(self) -> dict:
        if self._game is None:
            try:
                d = self._get(f"games/{DOMAIN}.json")
            except NexusError as e:
                if e.status in (401, 429):
                    raise
                d = {}
            self._game = d if isinstance(d, dict) else {}
        return self._game

    def categories(self) -> list:
        names = {clean_text(c.get("name"), 60) for c in (self.game_info().get("categories") or [])
                 if isinstance(c, dict) and c.get("name")}
        return sorted((n for n in names if n), key=str.lower)

    # ---- one mod's page ---------------------------------------------------------------------------------------
    def mod_page(self, mod_id: int) -> dict:
        """Everything a Nexus-style mod page shows. Only the basic REST call has to work; pictures, tags and
        requirements come from the newer APIs and are simply missing if those don't answer."""
        d = self.mod(mod_id) or {}
        out = norm_mod(d)
        out.update({"description": str(d.get("description") or ""), "gallery": [], "tags": [], "category": "",
                    "requirements": [], "notes": [], "adult": bool(d.get("contains_adult_content"))})
        try:                                                       # v3: gallery, tags, category
            r = self._call(f"{self.base}/v3/games/{DOMAIN}/mods/{int(mod_id)}")
            m = r.get("data", r) if isinstance(r, dict) else {}
            m = m.get("mod", m) if isinstance(m, dict) and isinstance(m.get("mod"), dict) else m
            if isinstance(m, dict):
                for g in (m.get("gallery_images") or [])[:12]:
                    if isinstance(g, dict):
                        url = http_url(g.get("large_thumbnail_url") or g.get("url"))
                        if url:
                            out["gallery"].append({"url": url, "thumb": http_url(g.get("thumbnail_url")) or url,
                                                   "title": clean_text(g.get("title"), 120)})
                pi = m.get("primary_image")
                if isinstance(pi, dict) and not out["picture"]:
                    out["picture"] = http_url(pi.get("large_thumbnail_url") or pi.get("url"))
                out["tags"] = [clean_text(t.get("name"), 60) for t in (m.get("tags") or [])
                               if isinstance(t, dict) and t.get("name")]
                ca = m.get("category")
                if isinstance(ca, dict) and ca.get("name"):
                    out["category"] = clean_text(ca["name"], 60)
                if m.get("adult_content") is not None:
                    out["adult"] = bool(m.get("adult_content"))
                if not out["description"] and m.get("description"):
                    out["description"] = str(m["description"])
        except NexusError as e:
            if e.status in (401, 429):
                raise
            out["notes"].append("Nexus' picture gallery isn't available right now.")
        try:                                                       # GraphQL: tags, category, requirements
            gid = self.game_info().get("id")
            if not gid:
                raise NexusError(0, "no game id")
            flt = {"modId": [{"value": str(int(mod_id)), "op": "EQUALS"}],
                   "gameId": [{"value": str(gid), "op": "EQUALS"}]}
            got = self._gql_run(lambda sel: "query Detail($filter: ModsFilter) { mods(filter: $filter, count: 1) "
                                            "{ nodes { %s } } }" % sel,
                                list(DETAIL_FIELDS), {"filter": flt}, "mods")
            node = next((n for n in (got.get("nodes") or []) if isinstance(n, dict)), {})
            if not out["tags"]:
                out["tags"] = [clean_text(t.get("name"), 60) for t in (node.get("tags") or [])
                               if isinstance(t, dict) and t.get("name")]
            mc = node.get("modCategory")
            if not out["category"] and isinstance(mc, dict):
                out["category"] = clean_text(mc.get("name"), 60)
            if not out["picture"]:
                out["picture"] = http_url(node.get("pictureUrl") or node.get("thumbnailUrl"))
            reqs = ((node.get("modRequirements") or {}).get("nexusRequirements") or {}).get("nodes") or []
            for r_ in reqs:
                if isinstance(r_, dict) and r_.get("modName"):
                    out["requirements"].append({"name": clean_text(r_["modName"], 120), "url": http_url(r_.get("url")),
                                                "notes": clean_text(r_.get("notes"), 200),
                                                "external": bool(r_.get("externalRequirement"))})
        except NexusError as e:
            if e.status in (401, 429):
                raise
        if out["picture"] and not out["gallery"]:
            out["gallery"] = [{"url": out["picture"], "thumb": out["picture"], "title": ""}]
        return out

    def listing(self, kind: str) -> list:
        """trending | latest_added | latest_updated  ->  normalised mods"""
        if kind not in ("trending", "latest_added", "latest_updated"):
            raise ValueError(kind)
        data = self._get(f"games/{DOMAIN}/mods/{kind}.json")
        mods = [norm_mod(d) for d in data if isinstance(d, dict) and d.get("mod_id")] if isinstance(data, list) else []
        return [m for m in mods if shown_on_nexus(m) and m.get("available", True)]   # drafts come back without a name

    def changelog(self, mod_id) -> dict:
        data = self._get(f"games/{DOMAIN}/mods/{int(mod_id)}/changelogs.json")
        return data if isinstance(data, dict) else {}

    def mod(self, mod_id):
        return self._get(f"games/{DOMAIN}/mods/{int(mod_id)}.json")

    def files(self, mod_id):
        return self._get(f"games/{DOMAIN}/mods/{int(mod_id)}/files.json")

    def _preview_ok(self, url: str) -> bool:
        """Only Nexus' own addresses (or the local test server) - a file list is never fetched from anywhere else."""
        u = urllib.parse.urlparse(str(url or ""))
        host = (u.hostname or "").lower()
        if u.scheme == "https" and (host == "nexusmods.com" or host.endswith(".nexusmods.com")):
            return True
        b = urllib.parse.urlparse(self.base)
        return (b.hostname in ("127.0.0.1", "localhost", "::1") and u.scheme == "http"
                and host == b.hostname and u.port == b.port)

    def preview(self, url: str):
        """The list of files inside one download (what "Preview file contents" shows on a Nexus page).
        It is a public file, so no key is sent with it."""
        if not self._preview_ok(url):
            raise NexusError(0, "That file list isn't on Nexus.")
        req = urllib.request.Request(url, headers={"Accept": "application/json",
                                                   "User-Agent": f"{APP_ID}/{VERSION}"})
        try:
            with self._opener.open(req, timeout=self.timeout) as r:
                raw = r.read(12_000_000)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                raise NexusError(429, "Nexus rate limit reached. Try again in about an hour.")
            raise NexusError(404 if e.code in (403, 404, 410) else e.code, f"No file list available ({e.code}).")
        except urllib.error.URLError as e:
            raise NexusError(0, f"Couldn't reach Nexus ({e.reason}).")
        except OSError as e:
            raise NexusError(0, f"Couldn't read the file list ({e}).")
        try:
            if raw[:2] == b"\x1f\x8b":
                raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
            return json.loads(raw.decode("utf-8-sig"))
        except (ValueError, zlib.error) as e:
            raise NexusError(404, f"The file list couldn't be read ({e}).")

    def updated(self, period="1m"):
        return self._get(f"games/{DOMAIN}/mods/updated.json", {"period": period})

    def tracked(self):
        data = self._get("user/tracked_mods.json")
        return [t for t in data if isinstance(t, dict) and t.get("domain_name") == DOMAIN] \
            if isinstance(data, list) else []

    def endorsed(self):
        data = self._get("user/endorsements.json")
        return [t for t in data if isinstance(t, dict) and t.get("domain_name") == DOMAIN] \
            if isinstance(data, list) else []

    def endorse(self, mod_id, version: str = "", abstain: bool = False) -> dict:
        """Endorse a mod (or take the endorsement back) on your Nexus account."""
        what = "abstain" if abstain else "endorse"
        ver = str(version or "").strip()[:40]
        data = self._call(f"{self.base}/v1/games/{DOMAIN}/mods/{int(mod_id)}/{what}.json",
                          form={"Version": ver, "version": ver})
        return data if isinstance(data, dict) else {}


def endorse_problem(said: str) -> str:
    """What Nexus's reason for refusing an endorsement means."""
    s = (said or "").upper()
    if "NOT_DOWNLOADED" in s:
        return ("Nexus only lets you endorse a mod you have downloaded (from its page, or through this app). "
                "Download it first, then try again.")
    if "TOO_SOON" in s:
        return "Nexus makes you wait a while (about 15 minutes) after downloading a mod before you can endorse it."
    if "OWN_MOD" in s:
        return "That is your own mod - Nexus doesn't let you endorse it."
    return "Nexus refused the endorsement." + (f" ({_clean_text(said, 120)})" if said else "")


class NeedsBrowser(Exception):
    """Nexus will only hand out this download after a click on its website (free accounts)."""

    def __init__(self, mod_id, file_id):
        super().__init__("Free accounts have to start each download on the Nexus page.")
        self.mod_id, self.file_id = int(mod_id), int(file_id)

    @property
    def url(self) -> str:
        return f"{NEXUS_SITE}/{DOMAIN}/mods/{self.mod_id}?tab=files&file_id={self.file_id}&nmm=1"


def norm_mod(d: dict) -> dict:
    def num(k):
        try:
            return int(d.get(k) or 0)
        except (TypeError, ValueError):
            return 0
    return {"id": num("mod_id"), "name": html.unescape(str(d.get("name") or "")).strip(),
            "version": str(d.get("version") or "").strip(),
            "summary": html.unescape(str(d.get("summary") or "")).strip()[:400],
            "author": html.unescape(str(d.get("author") or d.get("uploaded_by") or "")).strip(),
            "downloads": num("mod_downloads"), "endorsements": num("endorsement_count"),
            "updated": num("updated_timestamp"), "created": num("created_timestamp"),
            "picture": http_url(d.get("picture_url")), "adult": bool(d.get("contains_adult_content")),
            "status": str(d.get("status") or "").strip().lower(), "available": d.get("available", True) is not False}


# --------------------------------------------------------------------------
# Browsing Nexus: paged lists with filters, pictures, mod pages
# --------------------------------------------------------------------------
BROWSE_SORTS = [           # (label, GraphQL sort field, v3 sort field, v1 list used as the last resort)
    ("Most endorsed", "endorsements", "endorsements", "trending"),
    ("Most downloaded", "downloads", "downloads", "trending"),
    ("Recently updated", "updatedAt", "updated", "latest_updated"),
    ("Newest", "createdAt", "new", "latest_added"),
    ("Best match", "relevance", None, "trending"),
    ("Trending (top 10)", None, None, "trending"),
]
# Every field is optional except modId/name: if this Nexus doesn't know one, it is left out and the rest still works.
BROWSE_FIELDS = ("modId", "name", "version", "summary", "author", "uploader { name }", "endorsements", "downloads",
                 "updatedAt", "createdAt", "adultContent", "status", "thumbnailUrl", "pictureUrl",
                 "modCategory { name }", "tags { name }")
DETAIL_FIELDS = ("modId", "tags { name }", "modCategory { name }", "adultContent", "pictureUrl", "thumbnailUrl",
                 "modRequirements { nexusRequirements { nodes { modName url notes externalRequirement } } }")


# The "time period" box of the Nexus website. Like the website, it looks at the day a mod was uploaded - or, when
# the list is sorted by "Recently updated", at the day it was last updated.
PERIODS = (("All time", 0), ("24 Hours", 1), ("7 Days", 7), ("14 Days", 14), ("28 Days", 28), ("1 Year", 365))
CUSTOM_PERIOD = "Custom range…"
# The ways a date is written in a GraphQL filter, tried in turn. Nexus' search reads a filter as text, and the colons of
# a full time (2026-11-04T01:49:00Z) end that text early ("parse_exception"), so the plain day comes first.
DATE_STYLES = ("date", "isoesc", "iso", "unix")


def parse_user_date(text):
    """'31/10/2026' (as on Nexus), '31.10.2026', '31-10-2026' or '2026-10-31' -> date, or None."""
    t = str(text or "").strip()
    m = re.fullmatch(r"(\d{4})-(\d{1,2})-(\d{1,2})", t)
    parts = (int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None
    if not parts:
        m = re.fullmatch(r"(\d{1,2})[/.\-](\d{1,2})[/.\-](\d{4})", t)
        parts = (int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None
    try:
        return datetime(*parts).date() if parts else None
    except ValueError:
        return None


def period_range(label: str, custom_from: str = "", custom_to: str = "", now=None):
    """The box's choice -> (since, until) in unix seconds; 0 means 'no limit'. Raises ValueError with a
    sentence the user can act on when a custom date can't be read."""
    now = time.time() if now is None else now
    if label == CUSTOM_PERIOD:
        a, b = parse_user_date(custom_from), parse_user_date(custom_to)
        if custom_from.strip() and not a:
            raise ValueError("I can't read the “From” date. Write it like 31/10/2026.")
        if custom_to.strip() and not b:
            raise ValueError("I can't read the “To” date. Write it like 31/10/2026.")
        if a and b and a > b:
            a, b = b, a
        since = time.mktime((a.year, a.month, a.day, 0, 0, 0, 0, 0, -1)) if a else 0
        until = time.mktime((b.year, b.month, b.day, 23, 59, 59, 0, 0, -1)) if b else 0
        return since, until
    days = dict(PERIODS).get(label, 0)
    return (now - days * 86400, 0) if days else (0, 0)


def period_text(period: dict) -> str:
    """'uploaded in the last 7 days' - what a period means, for the note under the list."""
    if not period or not (period.get("since") or period.get("until")):
        return ""
    what = "updated" if period.get("field") == "updatedAt" else "uploaded"
    a, b = period.get("since"), period.get("until")
    if period.get("label") and period["label"] != CUSTOM_PERIOD:
        return f"{what} in the last {period['label'].lower()}"
    return f"{what} " + (f"from {fmt_date(a)} " if a else "") + (f"to {fmt_date(b)}" if b else "").strip()


def in_period(it: dict, period) -> bool:
    """Client-side check of a mod against a period. A mod whose date we don't know is kept."""
    if not period:
        return True
    d = it.get("updated") if period.get("field") == "updatedAt" else it.get("created")
    if not d:
        return True
    return not ((period.get("since") and d < period["since"]) or (period.get("until") and d > period["until"]))


def clean_text(s, n: int = 400) -> str:
    return html.unescape(re.sub(r"\s+", " ", str(s or ""))).strip()[:n]


def http_url(v) -> str:
    v = str(v or "").strip()
    return v if v.lower().startswith(("https://", "http://")) and len(v) < 1500 else ""


def parse_ts(v) -> int:
    """Nexus gives dates as ISO text (GraphQL, v3) or as unix seconds (v1)."""
    if v is None or v == "":
        return 0
    try:
        if isinstance(v, (int, float)):
            n = float(v)
        else:
            s = str(v).strip()
            if re.fullmatch(r"\d{9,14}", s):
                n = float(s)
            else:
                d = datetime.fromisoformat(s.replace("Z", "+00:00"))
                if d.tzinfo is None:
                    d = d.replace(tzinfo=timezone.utc)
                return int(d.timestamp())
        return int(n / 1000) if n > 1e11 else int(n)
    except (ValueError, OverflowError, OSError):
        return 0


def norm_node(n):
    """One mod of a GraphQL answer -> the shape the Browse tab uses (None if it isn't usable)."""
    if not isinstance(n, dict):
        return None
    try:
        mid = int(n.get("modId"))
    except (TypeError, ValueError):
        return None

    def num(k):
        try:
            return int(n.get(k) or 0)
        except (TypeError, ValueError):
            return 0
    cat = n.get("modCategory")
    cat = cat.get("name") if isinstance(cat, dict) else (cat if isinstance(cat, str) else n.get("category"))
    up = n.get("uploader") if isinstance(n.get("uploader"), dict) else {}
    tags = [clean_text(t.get("name"), 60) for t in (n.get("tags") or []) if isinstance(t, dict) and t.get("name")]
    return {"id": mid, "name": clean_text(n.get("name"), 200), "version": clean_text(n.get("version"), 40),
            "summary": clean_text(n.get("summary"), 400),
            "author": clean_text(n.get("author") or up.get("name"), 80),
            "downloads": num("downloads"), "endorsements": num("endorsements"),
            "updated": parse_ts(n.get("updatedAt")), "created": parse_ts(n.get("createdAt")),
            "adult": bool(n.get("adultContent")), "status": str(n.get("status") or "").strip().lower(),
            "thumb": http_url(n.get("thumbnailUrl")), "picture": http_url(n.get("pictureUrl")),
            "category": clean_text(cat, 60), "tags": [t for t in tags if t]}


def shown_on_nexus(it: dict) -> bool:
    """Drafts, hidden and removed pages (and entries without a name) are not mods you can open."""
    return bool(it and it.get("name")) and it.get("status", "") in ("", "published")


# ---- Nexus descriptions: BBCode (+ a little HTML) -> styled text ------------------------------------
_BB_TOKEN = re.compile(r"\[(/?)([A-Za-z*]+)(?:=([^\]]*))?\]")
_BB_SKIP = {"img", "youtube", "video", "webm", "mp4", "vimeo", "twitch", "iframe"}
_BB_STYLE = {"b": "b", "i": "i", "u": "u", "s": "s", "center": "center", "quote": "quote", "code": "code",
             "pre": "code", "heading": "h2"}


def _html_to_bb(s: str) -> str:
    s = re.sub(r"<\s*br\s*/?\s*>", "\n", s, flags=re.I)
    s = re.sub(r"</\s*(?:p|div|h[1-6]|li|tr|ul|ol)\s*>", "\n", s, flags=re.I)
    s = re.sub(r"<\s*li[^>]*>", "[*]", s, flags=re.I)
    s = re.sub(r"<\s*(?:b|strong)\s*>", "[b]", s, flags=re.I)
    s = re.sub(r"</\s*(?:b|strong)\s*>", "[/b]", s, flags=re.I)
    s = re.sub(r"<\s*(?:i|em)\s*>", "[i]", s, flags=re.I)
    s = re.sub(r"</\s*(?:i|em)\s*>", "[/i]", s, flags=re.I)
    s = re.sub(r"<\s*a\s[^>]*?href\s*=\s*[\"']([^\"']+)[\"'][^>]*>", r"[url=\1]", s, flags=re.I)
    s = re.sub(r"</\s*a\s*>", "[/url]", s, flags=re.I)
    s = re.sub(r"<\s*img\s[^>]*>", "[img]x[/img]", s, flags=re.I)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s)


def bbcode_runs(text, limit: int = 30000):
    """-> ([(text, (style, ...)), ...], [link urls]). Only text comes out: nothing is fetched or run."""
    s = _html_to_bb(str(text or ""))
    runs, links, active, stack = [], [], [], []
    size = [0]

    def emit(t, extra=()):
        if not t or size[0] > limit:
            return
        room = limit - size[0]
        if len(t) > room:
            t = t[:room]
            size[0] = limit + 1                              # too long: everything after this is dropped
        else:
            size[0] += len(t)
        if t:
            runs.append((t, tuple(active) + tuple(extra)))

    def push(name, style):
        stack.append((name, style))
        if style:
            active.append(style)

    def pop(name):
        for i in range(len(stack) - 1, -1, -1):
            if stack[i][0] == name:
                _n, style = stack.pop(i)
                if style in active:
                    active.remove(style)
                return
    pos, skip, urlcap = 0, None, None
    for m in _BB_TOKEN.finditer(s):
        chunk = s[pos:m.start()]
        pos = m.end()
        close, name, arg = bool(m.group(1)), m.group(2).lower(), m.group(3)
        if skip:
            if close and name == skip:
                emit("[picture]" if skip == "img" else "[video]", ("dim",))
                skip = None
            continue
        if urlcap is not None:
            urlcap += chunk
            if close and name == "url":
                link = urlcap.strip()
                links.append(link)
                emit(link, ("link%d" % (len(links) - 1),))
                urlcap = None
            continue
        emit(chunk)
        if name in _BB_SKIP:
            if not close:
                skip = name
            continue
        if name == "url":
            if close:
                pop("url")
            elif arg:
                links.append(arg.strip().strip("\"'"))
                push("url", "link%d" % (len(links) - 1))
            else:
                urlcap = ""
            continue
        if name in ("list", "ul", "ol"):
            if close:
                emit("\n")
            continue
        if name == "*":
            emit("\n  •  ")
            continue
        if name in ("line", "hr"):
            emit("\n" + "─" * 36 + "\n", ("dim",))
            continue
        if name == "br":
            emit("\n")
            continue
        if name == "size":
            if close:
                pop("size")
            else:
                try:
                    n = int(re.sub(r"\D", "", arg or "") or 0)
                except ValueError:
                    n = 0
                push("size", "h1" if n >= 5 else "h2" if n == 4 else "h3" if n == 3 else None)
            continue
        style = _BB_STYLE.get(name)
        if style:
            if close:
                pop(name)
                if name in ("quote", "code", "pre", "heading"):
                    emit("\n")
            else:
                if name in ("quote", "code", "pre", "heading"):
                    emit("\n")
                push(name, style)
        # anything else ([color], [font], [spoiler], ...) is ignored and its text is kept
    if skip is None:
        emit((urlcap or "") + s[pos:] if urlcap is not None else s[pos:])
    if size[0] > limit:
        runs.append(("\n…  the full description continues on Nexus", ("dim",)))
    out = []
    for t, st in runs:
        t = re.sub(r"\n{3,}", "\n\n", t)
        if t:
            out.append((t, st))
    if out:
        out[0] = (out[0][0].lstrip("\n"), out[0][1])
    return out, links


# ---- pictures: only from Nexus's own servers, small, cached on disk --------------------------------------
try:
    from PIL import Image as PILImage
    PILImage.MAX_IMAGE_PIXELS = 40_000_000
except Exception:      # noqa - without Pillow only small PNG/GIF pictures can be shown
    PILImage = None

IMG_MAX_BYTES = 8 * 1024 * 1024
_img_writes = [0]


def cache_dir() -> Path:
    return CONFIG_PATH.with_name(".cp2077_mod_toggle_cache")


def _img_get(url: str, allow_local: bool):
    """The picture's bytes, or None. No API key is sent, redirects stay on Nexus's servers, size is capped."""
    for _hop in range(4):
        if not cdn_host_ok(url, allow_local):
            return None
        req = urllib.request.Request(url, headers={"User-Agent": f"{APP_ID}/{VERSION}", "Accept": "image/*"})
        try:
            with urllib.request.build_opener(_NoRedirect).open(req, timeout=20) as r:
                try:
                    if int(r.headers.get("Content-Length") or 0) > IMG_MAX_BYTES:
                        return None
                except ValueError:
                    pass
                data = r.read(IMG_MAX_BYTES + 1)
                return data if 0 < len(data) <= IMG_MAX_BYTES else None
        except urllib.error.HTTPError as e:
            loc = e.headers.get("Location") if e.code in (301, 302, 303, 307, 308) else None
            if not loc:
                return None
            url = urllib.parse.urljoin(url, loc)
        except (urllib.error.URLError, OSError, ValueError):
            return None
    return None


def _prune_cache(limit=200 * 1024 * 1024, keep=150 * 1024 * 1024):
    try:
        files = [(p.stat().st_mtime, p.stat().st_size, p) for p in cache_dir().rglob("*.png")]
        total = sum(f[1] for f in files)
        if total <= limit:
            return
        for _m, size, p in sorted(files):
            p.unlink(missing_ok=True)
            total -= size
            if total <= keep:
                break
    except OSError:
        pass


def image_png(url: str, w: int, h: int, mode: str = "cover", allow_local: bool = False):
    """PNG bytes of a Nexus picture, resized to w x h ('cover' fills and crops, 'fit' keeps all of it).
    None when it can't be shown (not a Nexus address, too big, broken, or Pillow is missing for a JPEG)."""
    if not url or not cdn_host_ok(url, allow_local):
        return None
    key = hashlib.sha1(f"{url}|{w}|{h}|{mode}".encode()).hexdigest()
    path = cache_dir() / key[:2] / (key + ".png")
    try:
        if path.is_file():
            data = path.read_bytes()
            try:
                os.utime(path, None)
            except OSError:
                pass
            return data
    except OSError:
        pass
    raw = _img_get(url, allow_local)
    if not raw:
        return None
    png = None
    if PILImage is not None:
        try:
            import io
            import warnings
            with warnings.catch_warnings():
                warnings.simplefilter("error")                # a "decompression bomb" warning is a refusal
                im = PILImage.open(io.BytesIO(raw))
                im.draft("RGB", (w * 2, h * 2))               # JPEG shortcut; other formats ignore it
                im = im.convert("RGBA")
                iw, ih = im.size
                resample = getattr(PILImage, "Resampling", PILImage).LANCZOS
                if mode == "cover":
                    s = max(w / iw, h / ih)
                    nw, nh = max(1, round(iw * s)), max(1, round(ih * s))
                    im = im.resize((nw, nh), resample)
                    left, top = (nw - w) // 2, (nh - h) // 2
                    im = im.crop((left, top, left + w, top + h))
                else:
                    s = min(w / iw, h / ih, 2.0)
                    im = im.resize((max(1, round(iw * s)), max(1, round(ih * s))), resample)
                flat = PILImage.new("RGBA", im.size, (21, 24, 32, 255))
                flat.alpha_composite(im)
                buf = io.BytesIO()
                flat.convert("RGB").save(buf, "PNG")
                png = buf.getvalue()
        except Exception:         # noqa - broken or oversized picture: show the placeholder instead
            png = None
    elif len(raw) < 250_000:                                  # no Pillow: only PNG/GIF that already fit the box
        try:
            if raw[:8] == b"\x89PNG\r\n\x1a\n":
                iw, ih = struct.unpack(">II", raw[16:24])
            elif raw[:6] in (b"GIF87a", b"GIF89a"):
                iw, ih = struct.unpack("<HH", raw[6:10])
            else:
                iw = ih = 10 ** 6
            if iw <= w and ih <= h:
                png = raw
        except struct.error:
            png = None
    if png:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            tmp = path.with_suffix(".tmp")
            tmp.write_bytes(png)
            tmp.replace(path)
            _img_writes[0] += 1
            if _img_writes[0] % 50 == 0:
                _prune_cache()
        except OSError:
            pass
    return png


def fetch_mod_info(nx: Nexus, mod_id: int, need_files: bool) -> dict:
    d = nx.mod(mod_id) or {}
    summary = html.unescape(str(d.get("summary") or "")).strip()
    info = {
        "name": html.unescape(str(d.get("name") or "")).strip(),
        "version": str(d.get("version") or "").strip(),
        "summary": summary[:600],
        "author": html.unescape(str(d.get("author") or d.get("uploaded_by") or "")).strip(),
        "updated": int(d.get("updated_timestamp") or 0),
        "created": int(d.get("created_timestamp") or 0),
        "downloads": int(d.get("mod_downloads") or 0),
        "endorsements": int(d.get("endorsement_count") or 0),
        "fetched": time.time(),
    }
    if need_files:
        try:
            files = (nx.files(mod_id) or {}).get("files", [])
        except NexusError as e:
            if e.status in (401, 429):
                raise
            files = []
        main = [f for f in files if str(f.get("category_name") or "").upper() in ("MAIN", "UPDATE")]
        info["latest_main_ts"] = max((int(f.get("uploaded_timestamp") or 0) for f in main), default=0)
    return info


def parse_mod_ref(text: str):
    """Mod id from a Nexus link or a plain number. Returns (id, error)."""
    text = (text or "").strip()
    m = re.search(r"nexusmods\.com/(?:games/)?([a-z0-9]+)/mods/(\d+)", text, re.I)
    if m:
        if m.group(1).lower() != DOMAIN:
            return None, "That link is for a different game."
        return int(m.group(2)), ""
    if re.fullmatch(r"\d{1,8}", text):
        return int(text), ""
    return None, "Paste the Nexus page link (or just the mod number)."


def search_url(name: str) -> str:
    return f"{NEXUS_SITE}/games/{DOMAIN}/mods?keyword={urllib.parse.quote(name)}"


def open_folder(path) -> None:
    """Show a folder in the file manager."""
    try:
        if os.name == "nt":
            os.startfile(str(path))                           # noqa - Windows only
        elif sys.platform == "darwin":
            subprocess.Popen(["open", str(path)])
        else:
            subprocess.Popen(["xdg-open", str(path)])
    except (OSError, ValueError):
        pass


# --------------------------------------------------------------------------
# Download archives: link installed files to the exact Nexus mod + version
# --------------------------------------------------------------------------
ARCHIVE_EXTS = {".zip", ".7z", ".rar"}
NEXUS_ARCHIVE_RE = re.compile(
    r"^(?P<name>.+?)-(?P<id>\d{1,7})-"
    r"(?P<ver>[vV]?\d+[A-Za-z]?(?:-(?:\d+[A-Za-z]?|alpha|beta|rc\d*|hotfix|final|patch|fix))*)-"
    r"(?P<ts>\d{9,11})(?:\s*\(\d+\))?$", re.I)


def parse_nexus_filename(stem: str):
    """'Codeware-7289-1-0-3-1699999999' -> ('Codeware', 7289, '1.0.3', 1699999999)"""
    m = NEXUS_ARCHIVE_RE.match(stem)
    if not m:
        return None
    ver = m.group("ver").replace("-", ".")
    return m.group("name"), int(m.group("id")), re.sub(r"^[vV](?=\d)", "", ver), int(m.group("ts"))


# Nexus now names downloads "Mod Name-<file id>.zip" (older ones: "Name-<mod id>-<version>-<time>.zip").
NEW_ARCHIVE_RE = re.compile(r"^(?P<name>.+?)-(?P<fid>\d{3,9})(?:\s*\(\d+\))?$")


def parse_archive_name(stem: str) -> dict:
    """-> {name, mod_id, file_id, version, ts}; mod_id is only known for the older naming."""
    old = parse_nexus_filename(stem)
    if old:
        return {"name": old[0], "mod_id": old[1], "file_id": None, "version": old[2], "ts": old[3]}
    m = NEW_ARCHIVE_RE.match(stem)
    if m:
        return {"name": m.group("name").strip(), "mod_id": None, "file_id": int(m.group("fid")),
                "version": "", "ts": 0}
    return {"name": pretty_name(stem), "mod_id": None, "file_id": None, "version": "", "ts": 0}


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def pick_md5_result(results: list, size: int, title: str):
    """Choose the right answer when Nexus returns several for one fingerprint."""
    best, best_key, tk = None, None, norm_key(title)
    for r in results:
        mod, fd = r.get("mod") or {}, r.get("file_details") or {}
        try:
            mid = int(mod.get("mod_id") or fd.get("mod_id") or mod.get("id"))
        except (TypeError, ValueError):
            continue
        if mod.get("domain_name") not in (None, "", DOMAIN):
            continue
        try:
            fsize = int(fd.get("size_in_bytes") or 0) or int(float(fd.get("size_kb") or 0) * 1024)
        except (TypeError, ValueError):
            fsize = 0
        nm = html.unescape(str(mod.get("name") or "")).strip()
        key = (1 if fsize and abs(fsize - size) < 1024 else 0, 1 if norm_key(nm) == tk else 0)
        if best_key is None or key > best_key:
            try:
                ts = int(fd.get("uploaded_timestamp") or 0)
            except (TypeError, ValueError):
                ts = 0
            best_key = key
            best = {"mod_id": mid, "name": nm,
                    "version": str(fd.get("version") or fd.get("mod_version") or "").strip(),
                    "file_id": fd.get("file_id"), "ts": ts}
    return best


def make_resolver(mgr, nx: Nexus):
    """Returns resolve(path) -> {mod_id, name, version, ...} or None. It fingerprints the file (MD5)
    and asks Nexus, so it works however the download was named. Answers are remembered."""
    cache = mgr.state.setdefault("hashes", {})
    by_md5 = {v["md5"]: v for v in cache.values() if isinstance(v, dict) and v.get("md5") and v.get("mod_id")}

    def resolve(path: Path):
        st = path.stat()
        key = f"{path.name}|{st.st_size}|{int(st.st_mtime)}"
        c = cache.get(key)
        now = time.time()
        if c and (c.get("mod_id") or now - c.get("ts", 0) < 7 * 86400):
            return c if c.get("mod_id") else None
        md5 = md5_file(path)
        if md5 in by_md5:
            cache[key] = by_md5[md5]
            return by_md5[md5]
        pick = pick_md5_result(nx.md5_lookup(md5), st.st_size, parse_archive_name(path.stem)["name"])
        cache[key] = dict(pick or {}, md5=md5, ts=now)
        if pick:
            by_md5[md5] = cache[key]
        return cache[key] if pick else None
    return resolve


def find_7zip(custom: str = "") -> str:
    cands = [custom] if custom else []
    cands += [shutil.which("7z"), shutil.which("7za"), shutil.which("7zz")]
    for base in (os.environ.get("ProgramFiles"), os.environ.get("ProgramFiles(x86)")):
        if base:
            cands.append(str(Path(base) / "7-Zip" / "7z.exe"))
    for c in cands:
        if c and Path(c).exists():
            return str(c)
    return ""


def parse_7z_listing(text: str) -> list:
    """Parse `7z l -slt -ba` output into [(path, size, crc)]."""
    entries, cur = [], {}

    def flush():
        if cur.get("Path") and cur.get("Folder", "-") != "+" \
                and not cur.get("Attributes", "").startswith("D"):
            try:
                size = int(cur.get("Size") or 0)
            except ValueError:
                size = 0
            crc = None
            if cur.get("CRC"):
                try:
                    crc = int(cur["CRC"], 16)
                except ValueError:
                    pass
            entries.append((cur["Path"], size, crc))

    for line in text.splitlines():
        if not line.strip():
            flush()
            cur = {}
        elif " = " in line:
            k, v = line.split(" = ", 1)
            cur[k.strip()] = v.strip()
    flush()
    return entries


def list_entries(path: Path, seven_zip: str):
    """[(entry path, size, crc32)] or None when the archive can't be read."""
    if path.suffix.lower() == ".zip":
        try:
            with zipfile.ZipFile(path) as z:
                return [(i.filename, i.file_size, i.CRC) for i in z.infolist() if not i.is_dir()]
        except (zipfile.BadZipFile, OSError, RuntimeError, NotImplementedError):
            pass
    if seven_zip:
        try:
            r = subprocess.run([seven_zip, "l", "-slt", "-ba", str(path)], capture_output=True,
                               timeout=120, creationflags=NO_WINDOW)
            return parse_7z_listing(r.stdout.decode("utf-8", "replace"))
        except (OSError, subprocess.SubprocessError):
            pass
    return None


def find_archives(dirs, max_depth: int = 3) -> list:
    out, seen = [], set()
    for d in dirs:
        root = Path(d)
        if not root.is_dir():
            continue
        for dp, dn, fn in os.walk(root):
            if len(Path(dp).relative_to(root).parts) >= max_depth:
                dn[:] = []
            for f in fn:
                p = Path(dp) / f
                if p.suffix.lower() in ARCHIVE_EXTS and p not in seen:
                    seen.add(p)
                    out.append(p)
    return out


def crc32_file(path: Path) -> int:
    crc = 0
    with open(path, "rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                break
            crc = zlib.crc32(b, crc)
    return crc & 0xFFFFFFFF


def locate_entry(epath: str, by_lower: dict):
    """Map a path inside an archive to an installed unit (allowing wrapper folders)."""
    parts = [p for p in epath.replace("\\", "/").split("/") if p]
    for k in range(min(4, len(parts))):
        for i in range(1, len(parts) - k + 1):
            u = by_lower.get("/".join(parts[k:k + i]).lower())
            if u:
                return u, parts[k + i:]
    return None


def match_archives(units, game: Path, stash: Path, dirs, seven_zip: str, progress=None, resolve=None):
    """Compare downloaded archives with the installed files (size + CRC32 of every file).
    `resolve(path)` identifies an archive whose name doesn't carry the mod number.
    Returns (links, installed, report)."""
    progress = progress or (lambda *a: None)
    rep = {"archives": 0, "readable": 0, "skipped": 0, "needs_7zip": False, "overlap": 0,
           "by_name": 0, "by_hash": 0, "unidentified": 0, "ids": set(), "hints": {},
           "resolve_error": "", "resolver": resolve is not None}
    by_lower = {u.rel.lower(): u for u in units}
    paths = find_archives(dirs)
    rep["archives"] = len(paths)

    scans, crc_cache = [], {}
    for idx, p in enumerate(paths):
        progress(idx, len(paths), f"Reading {p.name}")
        rec = {"path": p, "info": parse_archive_name(p.stem), "per_unit": {}, "crc": 0, "paths": 0}
        entries = list_entries(p, seven_zip)
        rec["readable"] = entries is not None
        scans.append(rec)
        if entries is None:
            rep["skipped"] += 1
            if p.suffix.lower() != ".zip":
                rep["needs_7zip"] = True
            continue
        rep["readable"] += 1
        for epath, size, crc in entries:
            hit = locate_entry(epath, by_lower)
            if not hit:
                continue
            unit, rest = hit
            local = (game if unit.enabled else stash) / unit.rel
            for part in rest:
                local = local / part
            try:
                if not local.is_file():
                    continue
                lsize = local.stat().st_size
            except OSError:
                continue
            rc = rec["per_unit"].setdefault(unit.rel, [0, 0])
            rc[1] += 1
            rec["paths"] += 1
            if crc is not None and lsize == size:
                c = crc_cache.get(str(local))
                if c is None:
                    try:
                        c = crc32_file(local)
                    except OSError:
                        c = -1
                    crc_cache[str(local)] = c
                if c == crc:
                    rc[0] += 1
                    rec["crc"] += 1

    # who is each archive? the name says so for old-style downloads; otherwise ask Nexus by fingerprint
    for r in scans:
        r["ident"] = None
        if r["info"]["mod_id"]:
            r["ident"] = {"mod_id": r["info"]["mod_id"], "name": r["info"]["name"],
                          "version": r["info"]["version"], "ts": r["info"]["ts"], "how": "name",
                          "file_id": r["info"]["file_id"]}
    need = [r for r in scans if not r["ident"] and (r["paths"] > 0 or not r["readable"])]
    if need and resolve:
        stop, done = threading.Event(), [0]

        def one(r):
            if stop.is_set():
                return r, None, None
            try:
                return r, resolve(r["path"]), None
            except NexusError as e:
                if e.status in (401, 403, 429):
                    stop.set()
                return r, None, e
            except OSError:
                return r, None, None
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
            for fut in concurrent.futures.as_completed([ex.submit(one, r) for r in need]):
                r, got, err = fut.result()
                done[0] += 1
                progress(done[0], len(need), f"Identifying downloads {done[0]}/{len(need)}")
                if got:
                    r["ident"] = {"mod_id": got["mod_id"], "name": got.get("name") or r["info"]["name"],
                                  "version": got.get("version", ""), "ts": got.get("ts", 0), "how": "hash",
                                  "file_id": got.get("file_id")}
                elif err is not None and not rep["resolve_error"]:
                    rep["resolve_error"] = str(err)
    for r in scans:
        if r["ident"] and (r["paths"] or not r["readable"]):    # skip mods you no longer have installed
            rep["ids"].add(r["ident"]["mod_id"])
        if r["paths"]:
            rep["overlap"] += 1
            if r["ident"]:
                rep["by_" + r["ident"]["how"]] += 1
            else:
                rep["unidentified"] += 1
                for rel in r["per_unit"]:               # at least remember what Nexus calls it
                    rep["hints"][rel] = r["info"]["name"]

    archives = [(r["path"], r["ident"]) for r in scans]
    claims = defaultdict(list)
    for idx, r in enumerate(scans):
        if not r["ident"]:
            continue
        namekey = norm_key(pretty_name(r["ident"]["name"]))
        for rel, (ch, ph) in r["per_unit"].items():
            u = by_lower[rel.lower()]
            claims[rel].append((1 if ch else 0, 1 if u.key == namekey else 0, ph, r["ident"]["mod_id"], idx))

    links, won = {}, defaultdict(set)
    for rel, cl in claims.items():
        best = max(cl, key=lambda c: (c[0], c[1], c[2], c[4]))
        links[rel] = {"id": best[3], "src": "download"}
        won[best[3]].add(best[4])

    def arch_cmp(a, b):
        (ca, va, ta), (cb, vb, tb) = a, b
        if ca != cb:
            return (ca > cb) - (ca < cb)
        c = compare_versions(va, vb)
        if c:
            return c
        return (ta > tb) - (ta < tb)

    installed = {}
    for mid, idxs in won.items():
        cands = []
        for idx, r in enumerate(scans):
            if r["ident"] and r["ident"]["mod_id"] == mid and r["paths"] > 0:
                cands.append(((r["crc"], r["ident"]["version"], r["ident"]["ts"]), r["path"],
                              r["ident"]["version"], r["ident"].get("file_id")))
        if cands:
            cands.sort(key=functools.cmp_to_key(lambda x, y: arch_cmp(x[0], y[0])), reverse=True)
            (crc_n, _v, _t), p, ver, fid = cands[0]
            installed[mid] = {"version": ver,
                              "source": "download (verified)" if crc_n else "download",
                              "file": p.name}
            if fid:
                try:
                    installed[mid]["file_id"] = int(fid)
                except (TypeError, ValueError):
                    pass
    return links, installed, rep


# --------------------------------------------------------------------------
# Matching by name, and the update check
# --------------------------------------------------------------------------
def name_variants(name: str) -> set:
    out = {name}
    for sep in (" - ", " – ", " — ", ":", "(", "|"):
        if sep in name:
            out.add(name.split(sep)[0])
    return {v.strip() for v in out if v.strip()}


def match_names(mods, catalogue: dict) -> dict:
    """Link still-unlinked mods to Nexus mods with (nearly) the same name."""
    index = defaultdict(set)
    for mid, info in catalogue.items():
        for v in name_variants(info.get("name", "")):
            k = norm_key(v)
            if len(k) >= 4:
                index[k].add(mid)
    links = {}
    for m in mods:
        if m.nexus_id:
            continue
        keys = {u.key for u in m.units} | {norm_key(m.local_name)}
        found = None
        for ck in keys:
            ids = index.get(ck)
            if ids and len(ids) == 1:
                found = next(iter(ids))
                break
        if found is None:
            best = []
            for ck in keys:
                if len(ck) < 8:
                    continue
                for nk, ids in index.items():
                    if len(nk) < 8 or len(ids) != 1:
                        continue
                    short, long_ = (ck, nk) if len(ck) <= len(nk) else (nk, ck)
                    if short in long_ and len(short) / len(long_) >= 0.6:
                        best.append((len(short) / len(long_), next(iter(ids))))
            if best:
                best.sort(reverse=True)
                top = best[0][0]
                if len({b[1] for b in best if b[0] == top}) == 1:
                    found = best[0][1]
        if found is not None:
            for u in m.units:
                links[u.rel] = {"id": found, "src": "name"}
    return links


def default_download_dirs() -> list:
    """Where browsers put downloads, used when the user hasn't chosen a folder."""
    cands = [Path.home() / "Downloads"]
    for env in ("OneDrive", "OneDriveConsumer"):
        if os.environ.get(env):
            cands.append(Path(os.environ[env]) / "Downloads")
    out = []
    for c in cands:
        try:
            if c.is_dir() and str(c) not in out:
                out.append(str(c))
        except OSError:
            pass
    return out


LANG_WORDS = {
    "german", "deutsch", "french", "francais", "français", "spanish", "espanol", "español", "castellano",
    "italian", "italiano", "russian", "polish", "polski", "chinese", "simplified", "traditional",
    "japanese", "korean", "portuguese", "brazilian", "turkish", "arabic", "ukrainian", "czech", "dutch",
    "hungarian", "thai", "vietnamese", "swedish", "norwegian", "finnish", "danish", "romanian",
    "bulgarian", "greek", "hebrew", "hindi", "indonesian", "latam", "sapnish",
    "de", "fr", "es", "it", "ru", "pl", "zh", "cn", "tw", "ja", "jp", "ko", "kr", "pt", "br", "tr",
    "ar", "cz", "nl", "hu", "th", "vi", "sv", "fi", "ro", "bg", "he", "hi",
}
DERIV_TOKENS = {
    "translation", "translations", "translated", "localization", "localisation", "localized", "language",
    "languages", "multilingual", "lipsync", "patch", "patches", "addon", "addons", "compat",
    "compatibility", "fix", "fixes", "hotfix", "azerty", "qwertz", "retexture", "reshade", "preset",
    "presets", "config", "edit", "edits", "port", "unofficial",
}
DERIV_SUBSTR = ("addon", "translat", "lipsync", "localiz", "multilingual", "compatib", "patch", "language")


def split_title(name: str):
    """'Stealthrunner - Stealth Gameplay Expansion' -> ('Stealthrunner', 'Stealth Gameplay Expansion')"""
    parts = re.split(r"\s[-–—|]\s|\s*:\s|\s\(", name.strip(), maxsplit=1)
    if len(parts) == 1:
        return parts[0].strip(), ""
    return parts[0].strip(), parts[1].strip(" )")


def strip_version(text: str) -> str:
    return re.sub(r"[\s_-]+[vV]?\d+(?:[._]\d+)*[a-zA-Z]?$", "", text.strip()) or text.strip()


def is_derivative_text(text: str) -> bool:
    key = norm_key(text)
    if any(s in key for s in DERIV_SUBSTR):
        return True
    return bool(set(name_tokens(text)) & (LANG_WORDS | DERIV_TOKENS))


def score_match(local_keys: set, local_tokens: set, nexus_name: str):
    """How likely is it that an installed mod and a Nexus page are the same thing?
    -> (0..1, why, kind, derivative). kind: exact | base | contains | tokens.
    'Name - Spanish Translation' is the same *start* as 'Name' but is NOT the same mod,
    so only the full name counts as exact."""
    base, suffix = split_title(nexus_name)
    fkeys = {norm_key(nexus_name), norm_key(strip_version(nexus_name))}
    bkeys = {norm_key(base), norm_key(strip_version(base))}
    ntoks = set(name_tokens(nexus_name))
    deriv_suffix = bool(suffix) and is_derivative_text(suffix)
    extras = ntoks - set(local_tokens)
    deriv_extra = bool(extras & (LANG_WORDS | DERIV_TOKENS))
    full = norm_key(nexus_name)
    best = (0.0, "", "", False)
    for lk in local_keys:
        if len(lk) < 3:
            continue
        if lk in fkeys:
            return 1.0, "same name", "exact", False
        cand = None
        if suffix and lk in bkeys:
            s = 0.55 if deriv_suffix else 0.88
            cand = (s, f"same name plus “{suffix[:38]}”", "base", deriv_suffix)
        elif len(lk) >= 6:
            short, long_ = (lk, full) if len(lk) <= len(full) else (full, lk)
            if short in long_ and len(short) / len(long_) >= 0.6:
                d = deriv_suffix or deriv_extra
                s = 0.5 + 0.35 * len(short) / len(long_) - (0.3 if d else 0)
                cand = (s, "one name contains the other", "contains", d)
        if cand and cand[0] > best[0]:
            best = cand
    nt = {t for t in ntoks if t not in STOP_TOKENS and not t.isdigit()}
    lt = {t for t in local_tokens if t not in STOP_TOKENS and not t.isdigit()}
    inter = nt & lt
    if inter and (len(inter) >= 2 or any(len(t) >= 6 for t in inter)):
        jac = len(inter) / len(nt | lt)
        if jac >= 0.6:
            d = deriv_suffix or deriv_extra
            s = 0.35 + 0.5 * jac - (0.3 if d else 0)
            if s > best[0]:
                best = (s, "names share " + ", ".join(sorted(inter)), "tokens", d)
    return best


SEARCH_CAP = 250
SEARCH_PAGE = 50
SEARCH_TTL = 3 * 86400
CAND_TTL = 7 * 86400
POOL_KEEP = 10                 # pages kept per mod for the file-list step


def stem_terms(m) -> list:
    """Other names the installed files go by (a scattered mod's archive and script folder are often called differently)
    as search words."""
    out = []
    for u in m.units:
        t = " ".join(spaced_words(u.pretty))
        if len(norm_key(t)) >= 4 and t not in out:
            out.append(t)
    return out


def enrich_candidates(mgr, nx: Nexus, ids, progress=None) -> list:
    """Popularity, author and dates of candidate pages (v1 API), cached. Returns error texts."""
    progress = progress or (lambda *a: None)
    cache = mgr.state.setdefault("cands", {})
    now = time.time()
    todo = [i for i in sorted(set(ids)) if now - (cache.get(str(i)) or {}).get("ts", 0) > CAND_TTL]
    if not todo:
        return []
    stop, errors, done = threading.Event(), [], [0]

    def one(i):
        if stop.is_set():
            return
        try:
            d = nx.mod(i) or {}
        except NexusError as e:
            if e.status in (401, 429):
                stop.set()
            if e.status == 404:
                cache[str(i)] = {"gone": True, "ts": now}
            else:
                errors.append(str(e))
            return
        def num(*keys):
            for k in keys:
                try:
                    if d.get(k) is not None:
                        return int(d[k])
                except (TypeError, ValueError):
                    pass
            return 0
        cache[str(i)] = {"downloads": num("mod_downloads", "downloads"),
                         "endorsements": num("endorsement_count", "endorsements"),
                         "author": html.unescape(str(d.get("author") or d.get("uploaded_by") or "")).strip(),
                         "created": num("created_timestamp"), "updated": num("updated_timestamp"),
                         "summary": html.unescape(str(d.get("summary") or "")).strip()[:300], "ts": now}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for fut in concurrent.futures.as_completed([ex.submit(one, i) for i in todo]):
            fut.result()
            done[0] += 1
            progress(done[0], len(todo), f"Comparing candidates {done[0]}/{len(todo)}")
    return sorted(set(errors))


def search_matches(mgr, nx: Nexus, mods, progress=None, force=False, hints=None):
    """Look every unlinked mod up on Nexus by name, then choose carefully.
    -> (links to apply now, proposals for the user to confirm, info)

    A mod is linked automatically only when its full name matches exactly one page, or when
    one page clearly is the original (same base name, not a translation/add-on/patch, and far
    more popular than the rest). Everything else becomes a proposal with several candidates."""
    progress = progress or (lambda *a: None)
    info = {"searched": 0, "auto": 0, "review": 0, "error": "", "capped": 0,
            "pool": {}}                      # pool: every page the keywords found, per mod (the file-list step reads them)
    hints = hints or {}
    todo = [m for m in mods if not m.nexus_id and len(norm_key(m.name)) >= 3 and spaced_words(m.name)]
    if not todo:
        return {}, [], info
    try:
        nx.probe_search()
    except NexusError as e:
        info["error"] = str(e)
        return {}, [], info
    if len(todo) > SEARCH_CAP:
        info["capped"] = len(todo) - SEARCH_CAP
        todo = todo[:SEARCH_CAP]

    cache = mgr.state.setdefault("searches", {})
    cfg_id = json.dumps(nx.search_cfg, sort_keys=True)
    stop = threading.Event()

    def lookup(term):
        key = f"{cfg_id}|{term.lower()}"
        c = cache.get(key)
        if c and not force and time.time() - c.get("ts", 0) < SEARCH_TTL:
            return c["nodes"]
        nodes = nx.search(term, SEARCH_PAGE)
        if len(nodes) >= SEARCH_PAGE:                  # a popular word: read the next page too
            try:
                nodes += nx.search(term, SEARCH_PAGE, offset=SEARCH_PAGE)
            except NexusError as e:
                if e.status in (401, 403, 429):
                    raise
        cache[key] = {"ts": time.time(),
                      "nodes": [{"id": n["id"], "name": n["name"], "version": n["version"]} for n in nodes[:90]]}
        return cache[key]["nodes"]

    def work(m):
        if stop.is_set():
            return m, None, None
        keys = {u.key for u in m.units} | {norm_key(m.name), norm_key(m.local_name or "")}
        keys.discard("")
        all_toks = set(name_tokens(m.name))
        titles = list(dict.fromkeys(hints[u.rel] for u in m.units if u.rel in hints))
        for t in titles:                              # what the download itself was called on Nexus
            keys.add(norm_key(t))
            all_toks |= set(name_tokens(t))
        words = spaced_words(m.name)
        terms = [" ".join(spaced_words(t)) for t in titles] + [" ".join(words)]      # "Archive XL"
        if len(words) >= 2:
            terms.append("".join(words))              # "ArchiveXL" (many pages are one CamelCase word)
            long_words = sorted((w for w in words if len(w) >= 5 and w.lower() not in STOP_TOKENS
                                 and not w.isdigit()), key=len, reverse=True)
            if long_words:
                terms.append(long_words[0])           # last resort: the most distinctive word
        terms = list(dict.fromkeys(terms))
        have = {t.lower() for t in terms}
        terms += [t for t in stem_terms(m) if t.lower() not in have][:2]   # what the other installed files are called
        cands, seen = {}, {}
        try:
            for term in terms:
                for n in lookup(term):
                    seen.setdefault(n["id"], n)
                    s, why, kind, deriv = score_match(keys, all_toks, n["name"])
                    if s > cands.get(n["id"], {"score": 0.0})["score"]:
                        cands[n["id"]] = {"id": n["id"], "name": n["name"], "version": n["version"],
                                          "score": s, "why": why, "kind": kind, "deriv": deriv}
                if any(c["kind"] == "exact" for c in cands.values()):
                    break
        except NexusError as e:
            if e.status in (401, 403, 429):
                stop.set()
            return m, None, e
        # every page the keywords turned up, best name first - even those whose name looks nothing like the mod:
        # their file lists may still be the files that are installed
        nt = {t for t in all_toks if t not in STOP_TOKENS and not t.isdigit()}
        order = {i: k for k, i in enumerate(seen)}

        def rank(n):
            c = cands.get(n["id"])
            return (-(c["score"] if c else 0.0), -len(nt & set(name_tokens(n["name"]))), order[n["id"]])
        info["pool"][m.key] = [{"id": n["id"], "name": n["name"], "version": n["version"],
                                "score": (cands.get(n["id"]) or {}).get("score", 0.0)}
                               for n in sorted(seen.values(), key=rank)[:POOL_KEEP]]
        return m, sorted(cands.values(), key=lambda c: -c["score"]), None

    results, done = [], 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for fut in concurrent.futures.as_completed([ex.submit(work, m) for m in todo]):
            results.append(fut.result())
            done += 1
            progress(done, len(todo), f"Searching Nexus {done}/{len(todo)}")
    info["searched"] = sum(1 for _m, r, e in results if r is not None)
    errors = sorted({str(e) for _m, _r, e in results if e is not None})
    if errors:
        info["error"] = errors[0]

    # which mods are not settled by an exact name? those get a closer look (popularity, dates)
    need = set()
    for m, ranked, _e in results:
        good = [c for c in (ranked or []) if c["score"] >= 0.55][:5]
        exact = [c for c in good if c["kind"] == "exact"]
        if good and len(exact) != 1:
            need |= {c["id"] for c in good}
    if need and nx:
        enrich_candidates(mgr, nx, need, progress)
    ext = mgr.state.get("cands", {})

    links, props = {}, []
    for m, ranked, _e in results:
        good = [c for c in (ranked or []) if c["score"] >= 0.55]
        if not good:
            continue
        for c in good:
            x = ext.get(str(c["id"])) or {}
            c.update(downloads=x.get("downloads", 0), endorsements=x.get("endorsements", 0),
                     author=x.get("author", ""), created=x.get("created", 0), updated=x.get("updated", 0),
                     summary=x.get("summary", ""), gone=bool(x.get("gone")))
            c["flags"] = []
            if c["deriv"]:
                c["flags"].append("looks like a translation / add-on / patch")
            if m.install_ts and c["created"] and c["created"] > m.install_ts + 2 * 86400:
                c["score"] = max(0.0, c["score"] - 0.15)
                c["flags"].append("page was created after your files were installed")
        good = [c for c in good if not c.get("gone") and c["score"] >= 0.5]
        good.sort(key=lambda c: (-round(c["score"], 2), -c.get("downloads", 0)))
        good = good[:6]
        if not good:
            continue
        top = good[0]
        exact = [c for c in good if c["kind"] == "exact"]
        originals = [c for c in good if not c["deriv"] and c["score"] >= 0.7]
        auto = False
        if len(exact) == 1 and top["kind"] == "exact":
            auto = True
        elif (top["kind"] != "exact" and not top["deriv"] and top["score"] >= 0.85
              and top.get("downloads", 0) >= 500
              and all(top["downloads"] >= 5 * max(o.get("downloads", 0), 1) for o in originals if o is not top)):
            auto = True
            top["flags"].append("by far the most popular page with this name")
        if auto:
            for u in m.units:
                links[u.rel] = {"id": top["id"], "src": "name"}
            info["auto"] += 1
            continue
        near = [c for c in originals if c is not top and c["score"] >= top["score"] - 0.1]
        pick = 0 if (not top["deriv"] and top["score"] >= 0.85 and not near) else None
        if len(exact) > 1:
            why, pick = "several Nexus mods have exactly this name", None
        else:
            why = top["why"]
        props.append({"key": m.key, "mod": m.name, "rels": [u.rel for u in m.units],
                      "install_ts": m.install_ts, "cands": good, "pick": pick,
                      # the best candidate's fields, for simple consumers (CLI, tests)
                      "id": top["id"], "nexus_name": top["name"], "version": top["version"],
                      "score": round(top["score"], 2), "why": why, "ticked": pick is not None})
    props.sort(key=lambda p: (p["pick"] is None, -p["score"]))
    info["review"] = len(props)
    if len(cache) > 150:                       # keep the saved state small
        for k in sorted(cache, key=lambda k: cache[k].get("ts", 0))[:len(cache) - 150]:
            del cache[k]
    cc = mgr.state.get("cands", {})
    if len(cc) > 400:
        for k in sorted(cc, key=lambda k: cc[k].get("ts", 0))[:len(cc) - 400]:
            del cc[k]
    return links, props, info


# --------------------------------------------------------------------------
# File lists: the "Preview file contents" list of every Nexus download
# --------------------------------------------------------------------------
# A mod whose name the search can't settle is looked at differently: the pages its keywords turn up each list the
# files inside their downloads (paths and sizes). When those are the files that are installed, it is that mod.
# The list is a public file the page links to (`content_preview_link`); its exact layout isn't documented, so it is
# read leniently and a list that can't be read simply counts as "no list".
PREVIEWS_NAME = "_previews.json"
PREVIEW_TTL = 30 * 86400
PREVIEW_MISS_TTL = 5 * 86400
PREVIEW_KEEP = 160            # pages whose lists are remembered (in _disabled_mods/_previews.json)
PREVIEW_ENTRIES = 600         # entries kept per page
PREVIEW_FILES = 5             # downloads of one page whose lists are read (newest main files first)
CONTENT_PAGES = 45            # pages read in one run: each costs one request to Nexus
CONTENT_PER_MOD = 6           # pages tried for one unmatched mod
UNIFY_RESERVE = 10            # of those, kept for joining scattered parts to their mod
UNIFY_PER_MOD = 6
UNIFY_WINDOW = 900            # seconds: parts installed this close together probably came from one download
GENERIC_FILES = {"init.lua", "config.json", "settings.json", "info.json", "manifest.json", "mod.json", "main.lua",
                 "readme.txt", "readme.md", "license", "license.txt", "license.md", "changelog.txt",
                 "changelog.md", "credits.txt", "version.txt", "desktop.ini", "thumbs.db"}
PREVIEW_NAME_KEYS = ("path", "full_path", "fullpath", "filepath", "file_path", "name", "filename", "file_name")
PREVIEW_PATH_KEYS = ("path", "full_path", "fullpath", "filepath", "file_path")
PREVIEW_KID_KEYS = ("children", "files", "contents", "entries", "items", "nodes", "tree")
PREVIEW_SIZE_KEYS = (("size", 1), ("size_in_bytes", 1), ("sizeinbytes", 1), ("bytes", 1), ("filesize", 1),
                     ("file_size", 1), ("length", 1), ("size_kb", 1024))
_DIR_TYPES = {"dir", "directory", "folder", "tree", "d"}
_FILE_TYPES = {"file", "blob", "f"}
_SIZE_UNITS = {"": 1, "b": 1, "k": 1024, "kb": 1024, "kib": 1024, "m": 1 << 20, "mb": 1 << 20, "mib": 1 << 20,
               "g": 1 << 30, "gb": 1 << 30, "gib": 1 << 30}


def norm_path(s) -> str:
    return "/".join(p for p in str(s).replace("\\", "/").strip().split("/") if p and p != ".").lower()


def parse_size(v):
    """12345, "12345", "12.5 KB" -> bytes (None when it isn't a size)."""
    if v is None or isinstance(v, bool):
        return None
    if isinstance(v, (int, float)):
        return int(v) if v >= 0 else None
    m = re.fullmatch(r"\s*(\d[\d,]*(?:\.\d+)?)\s*([A-Za-z]{0,3})\s*", str(v))
    if not m or m.group(2).lower() not in _SIZE_UNITS:
        return None
    try:
        return int(float(m.group(1).replace(",", "")) * _SIZE_UNITS[m.group(2).lower()])
    except ValueError:
        return None


def _join(a: str, b: str) -> str:
    return f"{a}/{b}" if a and b else (a or b)


def parse_preview(data, limit: int = 6000) -> list:
    """[(path, size or None)] from a file list in whatever shape it comes: a tree of folders with children, a flat
    list of paths or of objects, or a mapping of path -> size."""
    out, seen = [], set()

    def add(path, size):
        p = norm_path(path)
        if p and p not in seen and len(out) < limit:
            seen.add(p)
            out.append((p, size))

    def size_in(node):
        for k, mult in PREVIEW_SIZE_KEYS:
            if k in node:
                s = parse_size(node[k])
                if s is not None:
                    return s * mult if mult != 1 and isinstance(node[k], (int, float)) else s
        return None

    def walk(node, prefix, depth=0):
        if depth > 40 or len(out) >= limit:
            return
        if isinstance(node, str):
            add(_join(prefix, node), None)
            return
        if isinstance(node, list):
            for x in node:
                walk(x, prefix, depth + 1)
            return
        if not isinstance(node, dict):
            return
        node = {str(k).lower(): v for k, v in node.items()}
        kids = next((node[k] for k in PREVIEW_KID_KEYS if isinstance(node.get(k), (list, dict)) and node[k]), None)
        key = next((k for k in PREVIEW_NAME_KEYS if isinstance(node.get(k), str) and node[k].strip()), None)
        typ = str(node.get("type") or node.get("kind") or "").lower()
        if key is None:
            if kids is not None:                          # a wrapper: {"files": [...]}
                walk(kids, prefix, depth + 1)
                return
            sz = size_in(node)
            if sz is not None and prefix:                 # {"a/b.archive": {"size": 1}}
                add(prefix, sz)
                return
            for k, v in node.items():                     # a plain mapping {"archive": {...}, "x.archive": 123}
                if isinstance(v, (dict, list)):
                    walk(v, _join(prefix, k), depth + 1)
                else:
                    add(_join(prefix, k), parse_size(v))
            return
        path = node[key] if key in PREVIEW_PATH_KEYS else _join(prefix, node[key])
        if typ in _DIR_TYPES or (kids is not None and typ not in _FILE_TYPES):
            if kids is not None:
                walk(kids, path, depth + 1)
        else:
            add(path, size_in(node))
    walk(data, "")
    return out


def previews_of(mgr) -> dict:
    """The remembered file lists {mod id: {"ts", "state": ok|none|gone, "entries": [[path, size], ...]}}."""
    pv = getattr(mgr, "_previews", None)
    if pv is None:
        try:
            pv = json.loads((mgr.stash / PREVIEWS_NAME).read_text("utf-8"))
        except (OSError, ValueError):
            pv = {}
        if not isinstance(pv, dict):
            pv = {}
        mgr._previews = pv
    return pv


def save_previews(mgr):
    pv = getattr(mgr, "_previews", None)
    if not pv:
        return
    if len(pv) > PREVIEW_KEEP:
        for k in sorted(pv, key=lambda k: pv[k].get("ts", 0))[:len(pv) - PREVIEW_KEEP]:
            del pv[k]
    try:
        mgr.stash.mkdir(exist_ok=True)
        tmp = mgr.stash / (PREVIEWS_NAME + ".tmp")
        tmp.write_text(json.dumps(pv, separators=(",", ":")), "utf-8")
        os.replace(tmp, mgr.stash / PREVIEWS_NAME)
    except (OSError, RuntimeError, ValueError):
        pass


def fetch_page_list(nx, mod_id) -> dict:
    """The file lists of one Nexus page (its newest downloads). Raises NexusError for a bad key / rate limit, or
    when Nexus can't be reached at all (so nothing wrong is remembered)."""
    now = time.time()
    try:
        files = (nx.files(mod_id) or {}).get("files", [])
    except NexusError as e:
        if e.status == 404:
            return {"ts": now, "state": "gone", "entries": []}
        raise
    order = {"MAIN": 0, "UPDATE": 1, "OPTIONAL": 2, "MISCELLANEOUS": 3, "OLD_VERSION": 4, "ARCHIVED": 5}

    def uploaded(f):
        try:
            return int(f.get("uploaded_timestamp") or 0)
        except (TypeError, ValueError):
            return 0
    links = [f for f in files if isinstance(f, dict) and f.get("content_preview_link")]
    links.sort(key=lambda f: (order.get(str(f.get("category_name") or "").upper(), 3), -uploaded(f)))
    entries, seen, got, errs = [], set(), 0, []
    for f in links[:PREVIEW_FILES]:
        try:
            data = nx.preview(str(f["content_preview_link"]))
        except NexusError as e:
            if e.status in (401, 429):
                raise
            errs.append(e)
            continue
        try:
            items = parse_preview(data)
        except (RecursionError, ValueError, TypeError, AttributeError):
            items = []
        if not items:
            continue
        got += 1
        for p, s in items:
            if p not in seen and len(entries) < PREVIEW_ENTRIES:
                seen.add(p)
                entries.append([p, s])
    if links and not got and errs and all(e.status == 0 for e in errs):
        raise errs[0]
    return {"ts": now, "state": "ok" if got else "none", "entries": entries}


def preview_fresh(rec, now: float) -> bool:
    if not isinstance(rec, dict):
        return False
    return now - rec.get("ts", 0) < (PREVIEW_TTL if rec.get("state") == "ok" else PREVIEW_MISS_TTL)


def ensure_previews(mgr, nx, ids, budget: dict, progress=None, force=False, label="Reading file lists") -> dict:
    """Make sure the file lists of these Nexus pages are known (cached ones cost nothing; every other costs one
    request, and budget["left"] says how many more may be made)."""
    progress = progress or (lambda *a: None)
    pv = previews_of(mgr)
    now = time.time()
    res = {"fetched": 0, "cached": 0, "over": 0, "errors": [], "stopped": False}
    todo = []
    for i in dict.fromkeys(ids):
        if not force and preview_fresh(pv.get(str(i)), now):
            res["cached"] += 1
        else:
            todo.append(i)
    if len(todo) > budget["left"]:
        res["over"] = len(todo) - max(0, budget["left"])
        todo = todo[:max(0, budget["left"])]
    budget["left"] -= len(todo)
    if not todo or nx is None:
        return res
    stop, done = threading.Event(), [0]

    def one(i):
        if stop.is_set():
            return i, None, None
        try:
            return i, fetch_page_list(nx, i), None
        except NexusError as e:
            if e.status in (401, 429):
                stop.set()
            return i, None, e
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        for fut in concurrent.futures.as_completed([ex.submit(one, i) for i in todo]):
            i, rec, err = fut.result()
            done[0] += 1
            progress(done[0], len(todo), f"{label} {done[0]}/{len(todo)}")
            if rec is not None:
                pv[str(i)] = rec
                res["fetched"] += 1
            elif err is not None:
                res["errors"].append(str(err))
            else:
                res["over"] += 1
    res["stopped"] = stop.is_set()
    return res


def installed_files(mgr, m, limit: int = 4000) -> list:
    """[(path below the game folder, lower case, size)] of every file of a mod, wherever it is right now."""
    out = []
    for u in m.units:
        base = mgr.game if u.enabled else mgr.stash
        root = base / u.rel
        try:
            if root.is_dir():
                for dp, _d, fs in os.walk(root):
                    for f in fs:
                        if f.lower() in IGNORED_NAMES:
                            continue
                        p = Path(dp) / f
                        out.append((p.relative_to(base).as_posix().lower(), p.stat().st_size))
                        if len(out) >= limit:
                            return out
            elif root.is_file():
                out.append((u.rel.lower(), root.stat().st_size))
        except OSError:
            continue
    return out


def is_generic_file(path: str) -> bool:
    base = path.rsplit("/", 1)[-1]
    return base in GENERIC_FILES or base.startswith(("readme", "license", "changelog"))


def compare_files(installed: list, entries: list) -> dict:
    """How well the installed files [(path, size)] agree with a page's file list [(path, size)].
    A path agrees when it is the same, or the same below a wrapper folder on either side."""
    by_base = defaultdict(list)
    for q, qs in entries:
        by_base[q.rsplit("/", 1)[-1]].append((q, qs))
    tot = found = size_cmp = size_ok = 0.0
    n = matched = strong = 0
    hit = set()
    for p, ps in installed:
        generic = is_generic_file(p)
        w = 0.25 if generic else 1.0
        tot += w
        n += 1
        best = None
        for q, qs in by_base.get(p.rsplit("/", 1)[-1], ()):
            if q == p or q.endswith("/" + p) or p.endswith("/" + q):
                if best is None or len(q) > len(best[0]):
                    best = (q, qs)
        if best is None:
            continue
        found += w
        matched += 1
        hit.add(best[0])
        stem = p.rsplit("/", 1)[-1].rsplit(".", 1)[0]
        if not generic and (best[0].count("/") >= 2 or len(stem) >= 5):
            strong += 1
        if ps is not None and best[1] is not None:
            size_cmp += w
            if abs(ps - best[1]) <= max(1.0, 0.015 * ps):
                size_ok += w
    return {"coverage": found / tot if tot else 0.0, "files": n, "matched": matched, "strong": strong,
            "size_cmp": size_cmp, "size_ok": size_ok, "share": len(hit) / len(entries) if entries else 0.0}


def contents_verdict(c: dict) -> str:
    """verified: the page lists the installed files (and it is clear which)  ·  likely: it does, but a single
    name-only match  ·  partial: part of them  ·  no"""
    if c["strong"] >= 1 and c["coverage"] >= 0.9:
        sized = c["size_cmp"] > 0 and c["size_ok"] >= 0.9 * c["size_cmp"]
        return "verified" if (c["strong"] >= 2 or sized) else "likely"
    if c["strong"] >= 1 and c["coverage"] >= 0.5:
        return "partial"
    return "no"


def files_phrase(c: dict) -> str:
    s = f"{c['matched']} of your {c['files']} file(s) are on this page's file list"
    if c["size_cmp"] > 0 and c["size_ok"] >= 0.9 * c["size_cmp"]:
        s += ", with the same sizes"
    return s


def pick_best(items: list, meta: dict):
    """items: [(page id, comparison, verdict)] that all fit. The clear winner, or None when it isn't clear."""
    if len(items) <= 1:
        return items[0] if items else None
    exact = [x for x in items if (meta.get(x[0]) or {}).get("score", 0) >= 1.0]
    if len(exact) == 1:
        return exact[0]
    ranked = sorted(items, key=lambda x: -x[1]["share"])        # the page that is mostly these files, not a big pack
    a, b = ranked[0], ranked[1]
    if a[1]["share"] >= 0.6 and a[1]["share"] - b[1]["share"] >= 0.3:
        return a
    return None


def match_by_contents(mgr, nx, props: list, pool: dict, progress=None, force=False):
    """Link mods the names couldn't settle by comparing their files with the file lists of the Nexus pages their
    keywords found, then join scattered parts to the mod whose page lists their files.
    -> (proposals, info). Links are applied to `mgr`; undecided mods become (or improve) proposals."""
    progress = progress or (lambda *a: None)
    info = {"checked": 0, "pages": 0, "cached": 0, "auto": 0, "review": 0, "unify": 0, "no_list": 0,
            "over": 0, "error": "", "note": ""}
    left = CONTENT_PAGES
    hourly = nx.limits.get("hourly-remaining") if nx is not None else None
    if hourly is not None and hourly - 12 < left:
        left = max(0, hourly - 12)
        info["note"] = f"Nexus allows only {hourly} more requests this hour, so at most {left} page(s) were read."
    budget = {"left": left}
    props = list(props)
    pv = previews_of(mgr)
    errors, looked = [], set()
    file_cache = {}

    def files_of(m):
        if m.key not in file_cache:
            file_cache[m.key] = installed_files(mgr, m)
        return file_cache[m.key]

    def usable(fl):
        return any(not is_generic_file(p) for p, _s in fl)

    def note(res, ids=()):
        looked.update(ids)
        info["pages"] += res["fetched"]
        info["cached"] += res["cached"]
        info["over"] += res["over"]
        errors.extend(res["errors"])
        if res["stopped"]:
            info["note"] = (info["note"] + " " if info["note"] else "") + \
                "Nexus stopped answering (rate limit or key), so some pages weren't read."

    # ---- 1. mods nothing has matched: compare with the pages their keywords found -------------------------------
    by_key = {p["key"]: p for p in props}
    meta, plan = {}, {}
    for p in props:
        for c in p["cands"]:
            meta[c["id"]] = c
    for lst in pool.values():
        for c in lst:
            meta.setdefault(c["id"], c)
    mods = mgr.scan()
    for m in mods:
        if m.nexus_id or not usable(files_of(m)):
            continue
        p = by_key.get(m.key)
        ids = ([c["id"] for c in p["cands"]] if p else []) + [c["id"] for c in pool.get(m.key, [])]
        ids = list(dict.fromkeys(ids))[:CONTENT_PER_MOD]
        if ids:
            plan[m.key] = (m, ids)
    wanted = []
    for k in range(CONTENT_PER_MOD):                       # every mod gets its best pages first
        for _key, (m, ids) in plan.items():
            if k < len(ids) and ids[k] not in wanted:
                wanted.append(ids[k])
    reserve = min(UNIFY_RESERVE, left // 4)                # some pages stay for step 2
    first = {"left": left - reserve}
    if wanted:
        note(ensure_previews(mgr, nx, wanted, first, progress, force, "Reading file lists on Nexus"), wanted)
    budget["left"] = left - (left - reserve - first["left"])

    links, to_enrich = {}, []
    rank = {"verified": 0, "likely": 1, "partial": 2}
    for key, (m, ids) in plan.items():
        fl = files_of(m)
        results = []
        for cid in ids:
            rec = pv.get(str(cid))
            if not isinstance(rec, dict) or rec.get("state") != "ok":
                continue
            cmp_ = compare_files(fl, [tuple(e) for e in rec.get("entries", [])])
            results.append((cid, cmp_, contents_verdict(cmp_)))
        if results:
            info["checked"] += 1
        good = [x for x in results if x[2] != "no"]
        if not good:
            continue
        p = by_key.get(m.key)
        if p is None and not any(x[2] in ("verified", "likely") for x in good):
            continue                                   # a few shared files alone are no reason to suggest a page
        win = pick_best([x for x in good if x[2] == "verified"], meta)
        if win:
            for u in m.units:
                links[u.rel] = {"id": win[0], "src": "contents"}
            if p:
                props.remove(p)
                del by_key[m.key]
            info["auto"] += 1
            continue
        # not clear enough to link alone: a proposal that shows the evidence
        old_pick = p["cands"][p["pick"]]["id"] if p and p.get("pick") is not None else None
        cdict = {c["id"]: c for c in (p["cands"] if p else [])}
        for cid, cmp_, v in good:
            c = cdict.get(cid)
            if c is None:
                nm = meta.get(cid) or {}
                c = {"id": cid, "name": nm.get("name") or f"Nexus page #{cid}", "version": nm.get("version", ""),
                     "score": 0.0, "why": "", "kind": "contents", "deriv": is_derivative_text(nm.get("name", "")),
                     "flags": [], "downloads": 0, "endorsements": 0, "author": "", "created": 0, "updated": 0,
                     "summary": "", "gone": False}
                cdict[cid] = c
                to_enrich.append(cid)
            c["contents"] = v
            c["score"] = max(c.get("score", 0.0), {"verified": 0.95, "likely": 0.8, "partial": 0.55}[v])
            c["why"] = files_phrase(cmp_) + (f"  ·  {c['why']}" if c.get("why") and c.get("kind") != "contents" else "")
        cands = sorted(cdict.values(), key=lambda c: (rank.get(c.get("contents"), 3), -round(c["score"], 2),
                                                     -c.get("downloads", 0)))[:8]
        fits = [c for c in cands if c.get("contents") in ("verified", "likely")]
        pick = 0 if len(fits) == 1 else None
        if pick is None and not fits and old_pick is not None:       # the name's favourite stays unless the files disagree
            pick = next((i for i, c in enumerate(cands) if c["id"] == old_pick), None)
        top = cands[0]
        prop = p or {"key": m.key, "mod": m.name, "rels": [u.rel for u in m.units], "install_ts": m.install_ts}
        prop.update(cands=cands, pick=pick, id=top["id"], nexus_name=top["name"], version=top["version"],
                    score=round(top["score"], 2), why=top["why"], ticked=pick is not None)
        if p is None:
            props.append(prop)
            by_key[m.key] = prop
    if to_enrich:
        try:
            enrich_candidates(mgr, nx, to_enrich[:16], progress)
        except NexusError:
            pass
        ext = mgr.state.get("cands", {})
        for p in props:
            for c in p["cands"]:
                x = ext.get(str(c["id"])) if c.get("kind") == "contents" else None
                if x:
                    c.update(downloads=x.get("downloads", 0), endorsements=x.get("endorsements", 0),
                             author=x.get("author", ""), created=x.get("created", 0), updated=x.get("updated", 0),
                             summary=x.get("summary", ""), gone=bool(x.get("gone")))
        for p in props:                                       # a page that has vanished can't be the answer
            if any(c.get("gone") for c in p["cands"]):
                keep = [c for c in p["cands"] if not c.get("gone")]
                if keep != p["cands"]:
                    chosen = p["cands"][p["pick"]]["id"] if p.get("pick") is not None else None
                    p["cands"] = keep
                    p["pick"] = next((i for i, c in enumerate(keep) if c["id"] == chosen), None)
    if links:
        mgr.apply_auto_links(links, {})

    # ---- 2. parts that belong to a linked mod: installed at the same time, files on that mod's page -------------
    mods = mgr.scan()
    file2 = {}
    linked_ts = sorted((u.ts, m.nexus_id) for m in mods if m.nexus_id for u in m.units if u.ts)
    plan2 = {}
    for m in mods:
        if m.nexus_id:
            continue
        fl = installed_files(mgr, m)
        if not usable(fl):
            continue
        file2[m.key] = fl
        near = {}
        for u in m.units:
            if not u.ts:
                continue
            lo = bisect.bisect_left(linked_ts, (u.ts - UNIFY_WINDOW, -1))
            hi = bisect.bisect_right(linked_ts, (u.ts + UNIFY_WINDOW, 1 << 60))
            for ts2, mid in linked_ts[lo:hi]:
                near[mid] = min(near.get(mid, 1e18), abs(ts2 - u.ts))
        ids = [mid for mid, _d in sorted(near.items(), key=lambda kv: kv[1])][:UNIFY_PER_MOD]
        if ids:
            plan2[m.key] = (m, ids)
    wanted = []
    for k in range(UNIFY_PER_MOD):
        for _key, (m, ids) in plan2.items():
            if k < len(ids) and ids[k] not in wanted:
                wanted.append(ids[k])
    if wanted:
        note(ensure_previews(mgr, nx, wanted, budget, progress, force, "Reading file lists of neighbouring mods"), wanted)
    links2 = {}
    for key, (m, ids) in plan2.items():
        fl = file2[m.key]
        res = []
        for cid in ids:
            rec = pv.get(str(cid))
            if isinstance(rec, dict) and rec.get("state") == "ok":
                cmp_ = compare_files(fl, [tuple(e) for e in rec.get("entries", [])])
                v = contents_verdict(cmp_)
                if v in ("verified", "likely"):
                    res.append((cid, cmp_, v))
        win = pick_best(res, meta)
        if win:
            for u in m.units:
                links2[u.rel] = {"id": win[0], "src": "contents"}
            info["unify"] += 1
            props[:] = [p for p in props if p["key"] != m.key]
    if links2:
        mgr.apply_auto_links(links2, {})

    info["no_list"] = sum(1 for i in looked if isinstance(pv.get(str(i)), dict) and pv[str(i)].get("state") == "none")
    info["review"] = sum(1 for p in props if any(c.get("contents") for c in p["cands"]))
    props.sort(key=lambda p: (p["pick"] is None, -p["score"]))
    if errors:
        info["error"] = sorted(set(errors))[0]
    save_previews(mgr)
    return props, info


def compute_update(installed: str, info: dict, install_ts: float):
    """-> (state, note). state: update | ok | maybe | unknown"""
    latest = (info or {}).get("version", "")
    if installed and latest:
        c = compare_versions(installed, latest)
        if c is None:
            if installed.strip().lower() == latest.strip().lower():
                return "ok", ""
            return "maybe", f"Version text differs ({installed} vs {latest})"
        return ("update", f"{installed} -> {latest}") if c < 0 else ("ok", "")
    latest_ts = (info or {}).get("latest_main_ts") or (info or {}).get("updated") or 0
    if install_ts and latest_ts and latest_ts > install_ts + 2 * 86400:
        return "maybe", f"Updated on Nexus {fmt_date(latest_ts)}, after you installed it"
    return "unknown", ""


def fetch_infos(mgr, nx: Nexus, ids, progress=None) -> list:
    """Fetch mod details into the cache with a few parallel requests. Returns error texts."""
    progress = progress or (lambda *a: None)
    ids = list(ids)
    errors = []
    if not ids:
        return errors
    stop = threading.Event()

    def one(i):
        if stop.is_set():
            return i, None, None
        need_files = not mgr.state["installed"].get(str(i), {}).get("version")
        try:
            return i, fetch_mod_info(nx, i, need_files), None
        except NexusError as e:
            if e.status in (401, 429):
                stop.set()
            return i, None, e

    done = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(one, i) for i in ids]
        for fut in concurrent.futures.as_completed(futs):
            i, info, err = fut.result()
            done += 1
            progress(done, len(ids), f"Reading Nexus pages {done}/{len(ids)}")
            if info:
                mgr.state["nexus"][str(i)] = info
            elif err is not None:
                if err.status == 404:
                    mgr.state["nexus"][str(i)] = {"error": "not_found", "name": "", "fetched": time.time()}
                else:
                    errors.append(str(err))
    return sorted(set(errors))


def refresh_nexus(mgr, nx: Nexus, ids=None, force=False, progress=None) -> list:
    """Update cached Nexus info for linked mods. Uses one cheap 'recently updated'
    call so only changed mods are re-read."""
    ids = set(ids) if ids else {l["id"] for l in mgr.state["links"].values()}
    cache = mgr.state["nexus"]
    updated = {}
    if not force:
        try:
            updated = {int(u["mod_id"]): u for u in (nx.updated("1m") or [])}
        except (NexusError, KeyError, TypeError, ValueError):
            updated = {}
    now = time.time()
    todo = []
    for i in sorted(ids):
        c = cache.get(str(i))
        if force or not c:
            todo.append(i)
            continue
        age = now - c.get("fetched", 0)
        if c.get("error"):
            if age > 7 * 86400:
                todo.append(i)
            continue
        u = updated.get(i)
        if u and max(int(u.get("latest_file_update") or 0), int(u.get("latest_mod_activity") or 0)) > c.get("fetched", 0):
            todo.append(i)
        elif age > 25 * 86400 or (not updated and age > 12 * 3600):
            todo.append(i)
        elif not mgr.state["installed"].get(str(i), {}).get("version") and "latest_main_ts" not in c:
            todo.append(i)
    errors = fetch_infos(mgr, nx, todo, progress)
    mgr.state["last_check"] = now
    return errors


def run_match(mgr, nx, cfg: dict, progress=None, force=False) -> dict:
    """1) your downloaded archives (exact), 2) names against the mods you tracked/endorsed,
    3) a Nexus name search for whatever is left (uncertain ones become proposals to confirm),
    then read the Nexus pages. Always returns plain-language notes saying what happened."""
    progress = progress or (lambda *a: None)
    rep = {"archives": 0, "archive_mods": 0, "name_mods": 0, "search_mods": 0, "skipped": 0,
           "needs_7zip": False, "catalogue": 0, "errors": [], "notes": [], "proposals": [],
           "user": "", "dirs": [], "auto_dirs": False, "arch": None,
           "tracked": None, "endorsed": None, "search": None, "key_error": "", "contents": None}
    arch_ids, hints = set(), {}
    had_key = nx is not None

    if nx:                                              # is the key good?
        try:
            me = nx.validate() or {}
            rep["user"] = str(me.get("name") or "")
            rep["premium"] = bool(me.get("is_premium"))
        except NexusError as e:
            rep["key_error"] = str(e)
            rep["errors"].append(str(e))
            nx = None                                   # nothing else will work with it

    dirs = [d for d in cfg.get("download_dirs", []) if d]
    if not dirs:
        dirs = default_download_dirs()
        rep["auto_dirs"] = bool(dirs)
    rep["dirs"] = dirs
    if dirs:
        links, installed, arep = match_archives(mgr.units(), mgr.game, mgr.stash, dirs,
                                                find_7zip(cfg.get("seven_zip", "")), progress,
                                                make_resolver(mgr, nx) if nx else None)
        mgr.apply_auto_links(links, installed)
        rep.update(archives=arep["archives"], skipped=arep["skipped"], needs_7zip=arep["needs_7zip"],
                   arch=arep)
        rep["archive_mods"] = len({l["id"] for l in links.values()})
        arch_ids, hints = set(arep["ids"]), arep["hints"]
        if arep["resolve_error"]:
            rep["errors"].append(arep["resolve_error"])

    if nx:
        ids = set(arch_ids)
        try:
            tracked, endorsed = nx.tracked(), nx.endorsed()
            rep["tracked"], rep["endorsed"] = len(tracked), len(endorsed)
            for t in tracked + endorsed:
                try:
                    ids.add(int(t["mod_id"]))
                except (KeyError, TypeError, ValueError):
                    pass
        except NexusError as e:
            rep["errors"].append(str(e))
            if e.status in (401, 429):
                nx = None
        if nx:
            linked = {l["id"] for l in mgr.state["links"].values()}
            todo = [i for i in ids if str(i) not in mgr.state["nexus"] and i not in linked]
            rep["errors"] += fetch_infos(mgr, nx, todo, progress)
            catalogue = {i: mgr.state["nexus"][str(i)] for i in ids
                         if mgr.state["nexus"].get(str(i), {}).get("name")}
            rep["catalogue"] = len(catalogue)
            new = match_names(mgr.scan(), catalogue)
            mgr.apply_auto_links(new, {})
            rep["name_mods"] = len({l["id"] for l in new.values()})
    if nx:
        slinks, props, srep = search_matches(mgr, nx, mgr.scan(), progress, force, hints)
        mgr.apply_auto_links(slinks, {})
        rep["search_mods"], rep["proposals"], rep["search"] = srep["auto"], props, srep
        if srep["error"] and not srep["searched"]:
            rep["errors"].append(srep["error"])
        if cfg.get("content_match", True):             # what the names can't settle, the files can
            try:
                rep["proposals"], rep["contents"] = match_by_contents(mgr, nx, props, srep.get("pool", {}),
                                                                      progress, force)
                if rep["contents"]["error"]:
                    rep["errors"].append("File lists: " + rep["contents"]["error"])
            except NexusError as e:
                rep["errors"].append("File lists: " + str(e))
        rep["errors"] += refresh_nexus(mgr, nx, progress=progress)
    mgr.save()

    mods = mgr.scan()
    rep["linked"] = sum(1 for m in mods if m.nexus_id)
    rep["total"] = len(mods)
    rep["errors"] = sorted(set(rep["errors"]))
    rep["notes"] = match_notes(rep, had_key)
    return rep


def match_notes(rep: dict, had_key: bool) -> list:
    """Say, step by step, what the matching found - so a zero is never a mystery."""
    n = []
    if rep["key_error"]:
        n.append("✗ Your Nexus key was refused: " + rep["key_error"])
    elif rep["user"]:
        n.append(f"✓ Nexus key works (signed in as {rep['user']}).")
    elif not had_key:
        n.append("• No Nexus key is set, so only your downloaded files were used. Add the key in "
                 "Settings to match by name and to check for updates.")
    # downloads
    a = rep.get("arch")
    if not rep["dirs"]:
        n.append("• No downloads folder found. Add the folder where your mod .zip files are "
                 "(Settings) - that is the most exact way to match.")
    else:
        where = ", ".join(rep["dirs"][:2]) + (" …" if len(rep["dirs"]) > 2 else "")
        auto = " (your Downloads folder - add others in Settings)" if rep["auto_dirs"] else ""
        if not rep["archives"]:
            n.append(f"• Downloads: no .zip/.7z/.rar files found in {where}{auto}.")
        else:
            matched = rep["archive_mods"]
            n.append(f"{'✓' if matched else '•'} Downloads: found {rep['archives']} archive(s) in {where}{auto}; "
                     f"{matched} installed mod(s) matched exactly.")
            if a and a["by_hash"]:
                n.append(f"   {a['by_hash']} archive(s) were identified by their file fingerprint, so it doesn't "
                         "matter what they're called.")
            if a and a["overlap"] == 0 and rep["archives"]:
                n.append("   None of those archives contain files that are installed right now.")
            if a and a["unidentified"]:
                if a["resolver"] and not a["resolve_error"]:
                    n.append(f"   {a['unidentified']} archive(s) match installed files but Nexus doesn't know them "
                             "(changed or removed files) - they were matched by name instead.")
                elif not a["resolver"]:
                    n.append(f"   {a['unidentified']} archive(s) match installed files but their names don't say "
                             "which mod they are. Add your Nexus key (Settings) and they'll be identified.")
        if rep["needs_7zip"]:
            n.append(f"• {rep['skipped']} .7z/.rar download(s) couldn't be opened. Install 7-Zip to include them.")
    # your lists
    if rep["tracked"] is not None:
        if rep["tracked"] + rep["endorsed"] == 0:
            n.append("• Your Nexus lists: you haven't endorsed or tracked any Cyberpunk 2077 mods, so there "
                     "was nothing to compare names with.")
        else:
            n.append(f"{'✓' if rep['name_mods'] else '•'} Your Nexus lists: {rep['endorsed']} endorsed + "
                     f"{rep['tracked']} tracked; {rep['name_mods']} of your mods matched them by name.")
    s = rep["search"]
    if s is not None:
        if s["error"] and not s["searched"]:
            n.append("✗ Name search: " + s["error"])
        elif s["searched"] or s["auto"]:
            line = (f"✓ Name search: looked up {s['searched']} mod(s) on Nexus; {s['auto']} linked "
                    f"automatically, {s['review']} need your OK")
            if s["capped"]:
                line += f" ({s['capped']} more not searched - run it again)"
            if s["error"]:
                line += f". Some lookups failed: {s['error']}"
            n.append(line + ".")
    c = rep.get("contents")
    if c is not None and (c["checked"] or c["unify"] or c["pages"] or c["cached"]):
        did = c["auto"] + c["unify"]
        n.append(f"{'✓' if did else '•'} File lists: compared {c['checked']} mod(s) with the file lists on their "
                 f"possible Nexus pages ({c['pages']} page(s) read, {c['cached']} remembered); {c['auto']} linked "
                 f"because the files are the same, {c['review']} suggestion(s) with file evidence.")
        if c["unify"]:
            n.append(f"   {c['unify']} scattered part(s) were joined to the mod whose page lists their files.")
        if c["no_list"]:
            n.append(f"   {c['no_list']} page(s) have no file list on Nexus, so they couldn't be compared.")
        if c["over"]:
            n.append(f"   {c['over']} more page(s) are left for the next run (a limit keeps your hourly Nexus "
                     "requests from running out).")
        if c["note"]:
            n.append("   " + c["note"])
    for e in rep["errors"]:
        if not any(e in line for line in n):
            n.append("✗ " + e)
    n.append(f"→ {rep.get('linked', 0)} of {rep.get('total', 0)} mods are linked to Nexus.")
    return n


# --------------------------------------------------------------------------
# Manager: scanning, toggling, remembered choices
# --------------------------------------------------------------------------
def same_file(a: Path, b: Path) -> bool:
    """True when two files have exactly the same content."""
    try:
        if a.stat().st_size != b.stat().st_size:
            return False
        with open(a, "rb") as fa, open(b, "rb") as fb:
            while True:
                x, y = fa.read(1 << 20), fb.read(1 << 20)
                if x != y:
                    return False
                if not x:
                    return True
    except OSError:
        return False


def path_size(p: Path) -> int:
    """Bytes in a file or a whole folder (links are not followed)."""
    try:
        p = Path(p)
        if p.is_symlink():
            return 0
        if p.is_file():
            return p.stat().st_size
        total = 0
        for root, _dirs, files in os.walk(p):
            for f in files:
                try:
                    total += os.lstat(os.path.join(root, f)).st_size
                except OSError:
                    pass
        return total
    except OSError:
        return 0


def human_size(n) -> str:
    try:
        n = float(n)
    except (TypeError, ValueError):
        return ""
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if n < 1024 or unit == "TB":
            return f"{n:.0f} {unit}" if unit in ("B", "KB") else f"{n:.1f} {unit}"
        n /= 1024
    return ""


def is_link_dir(p: Path) -> bool:
    """A folder that is really a link to somewhere else (a symlink, or a Windows junction)."""
    try:
        p = Path(p)
        if p.is_symlink():
            return True
        isj = getattr(os.path, "isjunction", None)
        if isj and isj(p):
            return True
        return os.name == "nt" and p.exists() and os.path.realpath(p) != os.path.abspath(p)
    except OSError:
        return False


def make_dir_link(link: Path, target: Path):
    """Make `link` point to the folder `target` (a junction on Windows - no administrator needed)."""
    if os.name == "nt":
        r = subprocess.run(["cmd", "/c", "mklink", "/J", str(link), str(target)], capture_output=True, text=True,
                           creationflags=NO_WINDOW)
        if r.returncode != 0 or not Path(link).exists():
            raise OSError((r.stdout + r.stderr).strip() or "mklink failed")
    else:
        os.symlink(str(target), str(link), target_is_directory=True)


def copy_tree_checked(src: Path, dst: Path, progress=None):
    """Copy a whole folder and check that every file arrived with the same size; otherwise raise."""
    progress = progress or (lambda *a: None)
    src, dst = Path(src), Path(dst)
    files = [(Path(r) / f) for r, _d, fs in os.walk(src) for f in fs]
    dst.mkdir(parents=True, exist_ok=True)
    for i, f in enumerate(files):
        rel = f.relative_to(src)
        out = dst / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, out)
        if out.stat().st_size != f.stat().st_size:
            raise OSError(f"{rel}: the copy is not the same size")
        progress(i + 1, len(files), f"Copying {i + 1}/{len(files)}")
    for r, ds, _fs in os.walk(src):                       # empty folders too
        for d in ds:
            (dst / (Path(r) / d).relative_to(src)).mkdir(parents=True, exist_ok=True)
    if sum(1 for _r, _d, fs in os.walk(dst) for _f in fs) != len(files):
        raise OSError("the copy has a different number of files")


# --------------------------------------------------------------------------
# Check-up: wrong places, leftovers, requirements, conflicts, abandoned/removed mods, game patch;
# the log reader; the "which mod crashes my game" search
# --------------------------------------------------------------------------
# Shared frameworks: where their files are (any one found = installed) and which unit in the library they are.
FRAMEWORKS = {
    "red4ext":   {"label": "RED4ext", "any": ["red4ext/RED4ext.dll", "bin/x64/winmm.dll"], "unit": None},
    "redscript": {"label": "redscript", "any": ["red4ext/plugins/redscript", "engine/tools/scc.exe"],
                  "unit": "red4ext/plugins/redscript"},
    "archivexl": {"label": "ArchiveXL", "any": ["red4ext/plugins/ArchiveXL"], "unit": "red4ext/plugins/archivexl"},
    "tweakxl":   {"label": "TweakXL", "any": ["red4ext/plugins/TweakXL"], "unit": "red4ext/plugins/tweakxl"},
    "codeware":  {"label": "Codeware", "any": ["red4ext/plugins/Codeware"], "unit": "red4ext/plugins/codeware"},
    "cet":       {"label": "Cyber Engine Tweaks", "any": ["bin/x64/plugins/cyber_engine_tweaks.asi"],
                  "unit": "bin/x64/plugins/cyber_engine_tweaks.asi"},
}
CET_MODS = "bin/x64/plugins/cyber_engine_tweaks/mods"
UNSURE_FW = ("red4ext", "redscript")      # found by file names that may differ between versions: never block on them
ABANDONED_DAYS = 730                 # a mod page not touched for two years
PATCH_GRACE = 3 * 86400              # updated up to three days before the game changed: probably made for it
PATCH_NOTICE_DAYS = 90               # how long a game update is mentioned in the check-up
SCAN_FILE_MAX = 400 * 1024
SCAN_FILES_PER_UNIT = 80
RED_REPLACE = re.compile(r"@replaceMethod\s*\(\s*([A-Za-z_]\w*)\s*\)\s*(?:(?:public|private|protected|final|static|native|cb|exec|quest|const)\s+)*func\s+([A-Za-z_]\w*)")
CET_GETMOD = re.compile(r"""GetMod\s*\(\s*["']([^"']{2,60})["']\s*\)""")
_FILE_CACHE = {}                      # (path, size, mtime) -> what the file needs / replaces
_HASH_CACHE = {}                      # (path, size, mtime) -> the file names inside an .archive
MAX_CONFLICT_LINES = 30               # more than this many overlapping pairs: the rest is summarised


def _exists_ci(root: Path, rel: str) -> bool:
    """Does `rel` exist below `root`, ignoring upper/lower case (so it also works off Windows)?"""
    cur = Path(root)
    for part in rel.split("/"):
        try:
            names = {n.lower(): n for n in os.listdir(cur)}
        except OSError:
            return False
        n = names.get(part.lower())
        if n is None:
            return False
        cur = cur / n
    return True


def _read_text(p: Path, limit: int = SCAN_FILE_MAX) -> str:
    try:
        with open(p, "rb") as f:
            return f.read(limit).decode("utf-8", "ignore")
    except OSError:
        return ""


def _unit_files(path: Path, exts=None) -> list:
    """The file(s) of a unit: itself, or up to SCAN_FILES_PER_UNIT files below it (lua/reds/… only when `exts`)."""
    if path.is_file():
        return [path]
    out = []
    for root, _dirs, files in os.walk(path):
        for f in sorted(files):
            if exts is None or f.lower().rsplit(".", 1)[-1] in exts:
                out.append(Path(root) / f)
                if len(out) >= SCAN_FILES_PER_UNIT:
                    return out
    return out


def _file_info(f: Path, rel: str) -> dict:
    """What one file tells us: frameworks it needs (key -> why), CET mods it names, scripts methods it replaces."""
    try:
        st = f.stat()
    except OSError:
        return {"needs": {}, "refs": [], "replaces": []}
    sig = (str(f), st.st_size, int(st.st_mtime))
    got = _FILE_CACHE.get(sig)
    if got is not None:
        return got
    name = f.name.lower()
    ext = name.rsplit(".", 1)[-1] if "." in name else ""
    rl = rel.lower()
    needs, refs, repl = {}, [], []
    if ext == "reds":
        needs["redscript"] = "contains redscript (.reds) files"
        text = _read_text(f)
        if re.search(r"^\s*import\s+Codeware\b", text, re.M):
            needs["codeware"] = "imports Codeware in its scripts"
        repl = sorted({(c, m) for c, m in RED_REPLACE.findall(text)})
    elif ext in ("yaml", "yml") and rl.startswith("r6/tweaks"):
        needs["tweakxl"] = "contains TweakXL tweak files"
    elif ext == "xl":
        needs["tweakxl" if rl.startswith("r6/tweaks") else "archivexl"] = "contains .xl files"
    elif ext == "lua" and CET_MODS in rl:
        needs["cet"] = "is a Cyber Engine Tweaks mod"
        refs = sorted({m.strip() for m in CET_GETMOD.findall(_read_text(f))})
    elif ext == "dll" and rl.startswith("red4ext/plugins"):
        needs["red4ext"] = "is a RED4ext plugin"
    got = {"needs": needs, "refs": refs, "replaces": repl}
    if len(_FILE_CACHE) > 20000:
        _FILE_CACHE.clear()
    _FILE_CACHE[sig] = got
    return got


def archive_hashes(path: Path):
    """archive_hashes_raw, remembered while the file stays the same."""
    try:
        st = path.stat()
    except OSError:
        return None
    sig = (str(path), st.st_size, int(st.st_mtime))
    if sig in _HASH_CACHE:
        return _HASH_CACHE[sig]
    got = archive_hashes_raw(path)
    if got is None or len(got) <= 20000:
        if len(_HASH_CACHE) > 400:
            _HASH_CACHE.clear()
        _HASH_CACHE[sig] = got
    return got


def archive_hashes_raw(path: Path):
    """The names (as 64-bit hashes) of the game files an .archive contains, or None if it can't be read.
    Reads only the header and the file table of the RDAR format, and checks that what it read is shaped like one
    (every entry's segment ranges must fit) before trusting it."""
    try:
        size = path.stat().st_size
        with open(path, "rb") as f:
            head = f.read(40)
            if len(head) < 40 or head[:4] != b"RDAR":
                return None
            idx_pos, idx_size = struct.unpack_from("<QI", head, 8)
            if not (28 <= idx_size <= 256 << 20) or idx_pos < 40 or idx_pos + idx_size > size:
                return None
            f.seek(idx_pos)
            hdr = f.read(28)
            if len(hdr) < 28:
                return None
            fto, _fts, _crc, count, segs, deps = struct.unpack("<IIQIII", hdr)
            if not (0 < count <= 2_000_000) or count * 56 > idx_size:
                return None
            for off in dict.fromkeys((28, fto)):                 # right after the header; or where the header says
                if off < 28 or off + count * 56 > idx_size:
                    continue
                f.seek(idx_pos + off)
                raw = f.read(count * 56)
                if len(raw) < count * 56:
                    continue
                hashes, good = [], 0
                for i in range(count):
                    h, _ts, _inl, s0, s1, d0, d1 = struct.unpack_from("<QQIIIII", raw, i * 56)
                    hashes.append(h)
                    if s0 <= s1 <= segs and d0 <= d1 <= deps:
                        good += 1
                hs = {h for h in hashes if h not in (0, 0xFFFFFFFFFFFFFFFF)}
                if good >= 0.98 * count and len(hs) >= 0.9 * count:
                    return hs
        return None
    except (OSError, struct.error):
        return None


def finding(kind: str, sev: str, title: str, detail: str = "", mod: str = "", fix=None, **extra) -> dict:
    f = {"kind": kind, "sev": sev, "title": title, "detail": detail, "mod": mod, "fix": fix}
    f.update(extra)
    f.setdefault("mods", [mod] if mod else [])
    f["id"] = hashlib.md5(f"{kind}|{mod}|{title}".encode("utf-8")).hexdigest()[:10]
    return f


class _CheckUp:
    """Everything the check-up knows how to look for. Mixed into Manager."""
    LOOSE_DIRS = ("", "archive", "archive/pc", "bin", "bin/x64", "r6")

    # --- frameworks and what mods need -------------------------------------------------------------------
    def fw_status(self, key: str) -> str:
        """on | off (switched off, waiting in _disabled_mods) | missing"""
        spec = FRAMEWORKS[key]
        if any(_exists_ci(self.game, p) for p in spec["any"]):
            return "on"
        if any(_exists_ci(self.stash, p) for p in spec["any"]):
            return "off"
        return "missing"

    def fw_mod(self, key: str, mods: list):
        prefix = FRAMEWORKS[key]["unit"]
        if not prefix:
            return None
        for m in mods:
            for u in m.units:
                r = u.rel.lower()
                if r == prefix or r.startswith(prefix + "/"):
                    return m
        return None

    def mod_needs(self, m: Mod) -> dict:
        """{"fw": {key: why}, "refs": {name: file}, "replaces": {(class, func)}} - read from the files of the mod."""
        fw, refs, repl = {}, {}, set()
        own = {k for k in FRAMEWORKS if FRAMEWORKS[k]["unit"] and any(
            u.rel.lower() == FRAMEWORKS[k]["unit"] or u.rel.lower().startswith(FRAMEWORKS[k]["unit"] + "/")
            for u in m.units)}
        for u in m.units:
            root = self.game if u.enabled else self.stash
            for f in _unit_files(root / u.rel, {"reds", "lua", "yaml", "yml", "xl", "dll"}):
                info = _file_info(f, u.rel)
                for k, why in info["needs"].items():
                    if k not in own:
                        fw.setdefault(k, why)
                for r in info["refs"]:
                    refs.setdefault(r, f.name)
                repl.update(info["replaces"])
        return {"fw": fw, "refs": refs, "replaces": repl}

    def needs_map(self, mods: list) -> dict:
        return {m.key: self.mod_needs(m) for m in mods}

    def enable_plan(self, mods: list, all_mods: list = None) -> dict:
        """Before switching `mods` on: the framework mods that are off and needed (to switch on too), and the
        frameworks that are not installed at all. -> {"also": [Mod], "missing": [label], "why": {mod name: [labels]}}"""
        all_mods = all_mods or self.scan()
        also, missing, why = [], [], {}
        chosen = {m.key for m in mods}
        for m in mods:
            for key in self.mod_needs(m)["fw"]:
                st = self.fw_status(key)
                if st == "on" or (st == "missing" and key in UNSURE_FW):
                    continue
                label = FRAMEWORKS[key]["label"]
                why.setdefault(m.name, []).append(label)
                fm = self.fw_mod(key, all_mods) if st == "off" else None
                if fm and fm.key not in chosen and fm not in also:
                    also.append(fm)
                elif st == "missing" and label not in missing:
                    missing.append(label)
        return {"also": also, "missing": missing, "why": why}

    def dependents(self, framework_mods: list, all_mods: list = None) -> dict:
        """Before switching framework mods off: {framework label: [names of the mods that are on and need it]}"""
        all_mods = all_mods or self.scan()
        out = {}
        gone = {m.key for m in framework_mods}
        keys = {k for k in FRAMEWORKS for m in framework_mods if self.fw_mod(k, [m])}
        if not keys:
            return out
        for m in all_mods:
            if m.key in gone or m.status == "off":
                continue
            need = self.mod_needs(m)["fw"]
            for k in keys & set(need):
                out.setdefault(FRAMEWORKS[k]["label"], []).append(m.name)
        return {k: sorted(v, key=str.lower) for k, v in out.items()}

    # --- the check-up itself ------------------------------------------------------------------------------
    def check_up(self) -> list:
        mods = self.scan()
        out = []
        for part in (self._check_places, self._check_requirements, self._check_conflicts, self._check_nexus):
            try:
                out += part(mods)
            except OSError as e:                               # one unreadable folder must not hide the rest
                out.append(finding("error", "info", "A part of the check-up couldn't finish", str(e)))
        rank = {"problem": 0, "warn": 1, "info": 2}
        out.sort(key=lambda f: (rank[f["sev"]], f["kind"], f["mod"].lower(), f["title"]))
        seen = Counter()
        for f in out:                                          # every line needs its own id (the window keys rows by it)
            seen[f["id"]] += 1
            if seen[f["id"]] > 1:
                f["id"] += f"-{seen[f['id']]}"
        return out

    def _check_places(self, mods: list) -> list:
        out, game = [], self.game
        if is_link_dir(self.stash) and not self.stash.is_dir():
            out.append(finding("stash-lost", "problem", "The switched-off mods can't be reached",
                               f"The folder {STASH_NAME} points to a drive or folder that isn't there right now: "
                               f"{os.path.realpath(self.stash)}. Connect that drive again, or your switched-off mods "
                               "(and their Nexus links) look as if they were gone."))
            return out                                         # nothing else can be judged
        for d in self.LOOSE_DIRS:                              # mod archives lying where the game never looks
            base = game / d if d else game
            try:
                names = sorted(os.listdir(base))
            except OSError:
                continue
            for n in names:
                low = n.lower()
                rel = f"{d}/{n}" if d else n
                if not (base / n).is_file():
                    continue
                if low.endswith(".archive"):
                    out.append(finding("wrong-place", "problem", f"{n} is in the wrong folder",
                                       f"It is in “{d or 'the game folder'}”, but the game only loads mod archives from "
                                       "archive/pc/mod, so this one does nothing there.",
                                       fix={"action": "move", "rel": rel, "to": "archive/pc/mod/" + n,
                                            "label": "Move it to archive/pc/mod"}, rels=[rel]))
                elif low.endswith(".xl"):
                    out.append(finding("wrong-place", "warn", f"{n} is in an unusual folder",
                                       f"It is in “{d or 'the game folder'}”. ArchiveXL .xl files belong next to their .archive "
                                       "in archive/pc/mod, TweakXL ones in r6/tweaks - check the mod's page for which.",
                                       rels=[rel]))
        for root, prefix in ((game, ""), (self.stash, STASH_NAME + "/")):          # CET folders, in use or switched off
            base = root / CET_MODS
            if not base.is_dir():
                continue
            on = prefix == ""
            for d in sorted(base.iterdir(), key=lambda p: p.name.lower()):
                rel = prefix + f"{CET_MODS}/{d.name}"
                if d.is_file():
                    if d.suffix.lower() == ".lua":
                        out.append(finding("wrong-place", "warn", f"{d.name} is loose in the CET mods folder",
                                           "A CET mod needs its own folder with an init.lua inside.", rels=[rel]))
                    continue
                if _exists_ci(d, "init.lua"):
                    continue
                inner = [c for c in sorted(d.iterdir()) if c.is_dir() and _exists_ci(c, "init.lua")]
                if inner:
                    out.append(finding("wrong-place", "problem", f"{d.name}: init.lua is one folder too deep",
                                       f"The mod's init.lua is in “{d.name}/{inner[0].name}”, but Cyber Engine Tweaks only "
                                       f"looks for “{d.name}/init.lua”. Move the contents of the inner folder up one level "
                                       "(or put the inner folder in the mods folder by itself).", mod=d.name, rels=[rel]))
                    continue
                files = [p.name for p in d.rglob("*") if p.is_file()][:40]
                if any(n.lower().endswith(".lua") for n in files):
                    out.append(finding("wrong-place", "warn", f"{d.name} has Lua files but no init.lua",
                                       "Cyber Engine Tweaks needs an init.lua in the mod's own folder to start it.",
                                       mod=d.name, rels=[rel]))
                elif on or True:
                    out.append(finding("leftover", "info", f"{d.name}: only settings are left (no init.lua)",
                                       "This folder has no mod in it any more - probably the saved settings or database of "
                                       "a mod you removed" + (": " + ", ".join(files[:4]) if files else " (it is empty)") +
                                       ". It does no harm. You can put it aside to keep the folder tidy.",
                                       mod=d.name, fix={"action": "aside", "rels": [rel], "label": "Put it aside"},
                                       rels=[rel]))
        red = game / "red4ext/plugins"
        if red.is_dir():
            for p in sorted(red.iterdir()):
                if p.is_file() and p.suffix.lower() == ".dll":
                    out.append(finding("wrong-place", "warn", f"{p.name} is not in a folder of its own",
                                       "RED4ext loads a plugin from red4ext/plugins/<name>/<name>.dll. A DLL placed "
                                       "directly in plugins is probably not loaded.", rels=[f"red4ext/plugins/{p.name}"]))
        modsdir = game / "mods"
        if modsdir.is_dir():
            for d in sorted(modsdir.iterdir()):
                if d.is_dir() and not _exists_ci(d, "info.json"):
                    out.append(finding("wrong-place", "warn", f"REDmod “{d.name}” has no info.json",
                                       "A REDmod folder needs an info.json; without it the game ignores the mod.",
                                       mod=d.name, rels=[f"mods/{d.name}"]))
        # two versions of the same mod next to each other
        groups = defaultdict(list)
        for u in self.units():
            if u.enabled and u.category == "Archive" and not u.is_dir:
                kind = "xl" if u.rel.lower().endswith(".xl") else "archive"
                groups[(u.rel.rsplit("/", 1)[0].lower(), u.key, kind)].append(u)
        for (_d, key, _k), us in sorted(groups.items()):
            if len(us) < 2 or not key:
                continue
            newest = max(us, key=lambda u: self._mtime(u))
            older = [u for u in us if u is not newest]
            names = ", ".join(Path(u.rel).name for u in sorted(us, key=lambda u: u.rel.lower()))
            out.append(finding("duplicate", "warn", f"Possibly two versions of the same mod: {us[0].pretty}",
                               f"These files have the same name apart from a version number: {names}. If they are an "
                               f"old and a new version, only the newest (“{Path(newest.rel).name}”) should stay.",
                               mod=us[0].pretty, rels=[u.rel for u in us],
                               fix={"action": "aside", "rels": [u.rel for u in older],
                                    "label": f"Put the older one aside ({', '.join(Path(u.rel).name for u in older)})"}))
        have = {u.rel for u in self.units()}                  # Nexus links to files that no longer exist
        gone = sorted(r for r in self.state["links"] if r not in have)
        if gone:
            out.append(finding("stale", "info", f"{len(gone)} remembered mod file(s) are gone",
                               "Links to Nexus (and instance entries) exist for files that are no longer in your game or "
                               "in the switched-off folder - the mod was removed by hand. Forgetting them keeps the lists "
                               "tidy: " + ", ".join(Path(r).name for r in gone[:6]) + (" …" if len(gone) > 6 else ""),
                               fix={"action": "forget", "rels": gone, "label": "Forget them"}, rels=gone))
        return out

    @staticmethod
    def _mtime(u) -> float:
        return u.ts

    def _check_requirements(self, mods: list) -> list:
        out = []
        cet_present = {}
        for root, on in ((self.game, True), (self.stash, False)):
            base = root / CET_MODS
            if base.is_dir():
                for d in base.iterdir():
                    cet_present.setdefault(d.name.lower(), "on" if on else "off")
        by_fw = defaultdict(list)                              # framework key -> [(mod, why)]
        for m in mods:
            if m.status == "off":
                continue
            need = self.mod_needs(m)
            for key, why in need["fw"].items():
                by_fw[key].append((m, why))
            own = {u.rel.rsplit("/", 1)[-1].lower() for u in m.units} | {m.name.lower()}
            for name, fname in sorted(need["refs"].items()):
                st = cet_present.get(name.lower())
                if st == "on" or name.lower() in own:
                    continue
                if st == "off":
                    target = next((x for x in mods if any(u.rel.lower().rsplit("/", 1)[-1] == name.lower() for u in x.units)), None)
                    out.append(finding("requirement", "warn", f"{m.name} uses the CET mod “{name}”, which is switched off",
                                       f"{fname} asks for “{name}”. If that is only an optional extra, you can ignore this.",
                                       mod=m.name, fix={"action": "enable", "mod_keys": [target.key], "label": f"Switch “{name}” on"}
                                       if target else None))
                else:
                    out.append(finding("requirement", "info", f"{m.name} refers to the CET mod “{name}”, which isn't installed",
                                       f"{fname} asks for “{name}”. If that is an optional extra, ignore this.", mod=m.name,
                                       search=name))
        for key, lst in by_fw.items():
            st = self.fw_status(key)
            if st == "on":
                continue
            label = FRAMEWORKS[key]["label"]
            names = sorted({m.name for m, _w in lst}, key=str.lower)
            who = ", ".join(names[:5]) + (f" and {len(names) - 5} more" if len(names) > 5 else "")
            why = lst[0][1]
            if st == "off":
                fm = self.fw_mod(key, mods)
                out.append(finding("requirement", "problem", f"{label} is switched off, but {len(names)} mod{'s' if len(names) != 1 else ''} need{'s' if len(names) == 1 else ''} it",
                                   f"Needed by: {who} (for example {lst[0][0].name} {why}).", mod=label, mods=names,
                                   fix={"action": "enable", "mod_keys": [fm.key], "label": f"Switch {label} on"} if fm else None))
            else:
                sure = key not in UNSURE_FW
                out.append(finding("requirement", "problem" if sure else "warn",
                                   f"{label} isn't installed, but {len(names)} mod{'s' if len(names) != 1 else ''} need{'s' if len(names) == 1 else ''} it" if sure else
                                   f"{len(names)} mod{'s' if len(names) != 1 else ''} need{'s' if len(names) == 1 else ''} {label} and I couldn't find it",
                                   f"Needed by: {who} (for example {lst[0][0].name} {why}). I looked for: "
                                   f"{', '.join(FRAMEWORKS[key]['any'])}. Get it from Nexus Mods (search “{label}”).",
                                   mod=label, mods=names, search=label))
        return out

    def _check_conflicts(self, mods: list) -> list:
        owner = {u.rel: m for m in mods for u in m.units}
        out = []
        arch = sorted((u for u in self.units() if u.enabled and u.category == "Archive" and u.rel.lower().endswith(".archive")),
                      key=lambda u: (u.rel.rsplit("/", 1)[-1].lower(), u.rel.lower()))
        index = defaultdict(list)
        unread = 0
        for u in arch:
            hs = archive_hashes(self.game / u.rel)
            if hs is None:
                unread += 1
            for h in hs or ():
                index[h].append(u)
        if unread:
            out.append(finding("conflict", "info", f"{unread} of {len(arch)} archive file(s) couldn't be compared",
                               "Their file list couldn't be read (they may be damaged, empty, or built in a way I don't "
                               "know), so overlaps with other mods aren't checked for those."))
        pairs = Counter()
        for us in index.values():
            if 1 < len(us) <= 12:
                for i, a in enumerate(us):
                    for b in us[i + 1:]:
                        pairs[(a.rel, b.rel)] += 1
        per_mods = {}
        for (a, b), n in pairs.items():
            ma, mb = owner.get(a), owner.get(b)
            if not ma or not mb or ma is mb:
                continue
            cur = per_mods.setdefault((ma.key, mb.key), {"a": ma, "b": mb, "n": 0, "files": []})
            cur["n"] += n
            cur["files"].append((a, b))
        ranked = sorted(per_mods.values(), key=lambda c: (-c["n"], c["a"].name.lower(), c["b"].name.lower()))
        if len(ranked) > MAX_CONFLICT_LINES:
            out.append(finding("conflict", "info", f"{len(ranked) - MAX_CONFLICT_LINES} more pairs of mods overlap",
                               f"Only the {MAX_CONFLICT_LINES} pairs that share the most game files are listed. If you have "
                               "several appearance or texture mods that all change the same things, this is expected."))
        for c in ranked[:MAX_CONFLICT_LINES]:
            a_file, b_file = c["files"][0]
            out.append(finding("conflict", "warn", f"{c['a'].name} and {c['b'].name} change the same game files",
                               f"{c['n']} game file(s) are in both archives. Archives load in alphabetical order of their "
                               f"file names, so “{Path(b_file).name}” ({c['b'].name}) is expected to win over "
                               f"“{Path(a_file).name}” ({c['a'].name}). To make the other one win, rename it so it sorts "
                               "later (for example start its name with a z). This order is the usual one, not something "
                               "I could check in the game.", mod=c["a"].name, mods=[c["a"].name, c["b"].name],
                               rels=[a_file, b_file]))
        repl = defaultdict(dict)
        for m in mods:
            if m.status == "off":
                continue
            for cls_func in self.mod_needs(m)["replaces"]:
                repl[cls_func][m.key] = m
        for (cls, func), by in sorted(repl.items()):
            if len(by) > 1:
                names = sorted((m.name for m in by.values()), key=str.lower)
                out.append(finding("conflict", "problem", f"{' and '.join(names[:3])} both replace {cls}.{func}",
                                   "Each of these mods replaces the same script function. Only one of them can work; the "
                                   "script compiler may report an error at start, or one mod silently loses. Switch one "
                                   "of them off, or look for a compatibility patch.", mod=names[0], mods=names))
        cutoff = time.time() - 60 * 86400
        for e in self.journal():
            if e.get("overwrote") and not e.get("undone") and e["ts"] >= cutoff:
                by = defaultdict(list)
                for o in e["overwrote"]:
                    by[o.get("mod") or "another mod"].append(o["rel"])
                for owner_name, rels in by.items():
                    out.append(finding("conflict", "info", f"{e.get('mod', 'A mod')} replaced {len(rels)} file(s) of {owner_name}",
                                       f"When it was installed ({fmt_date(e['ts'])}), these files already existed: "
                                       + ", ".join(Path(r).name for r in rels[:5]) +
                                       (" …" if len(rels) > 5 else "") + ". The old copies were kept (History → Undo puts them back).",
                                       mod=e.get("mod", "")))
        return out

    def _check_nexus(self, mods: list) -> list:
        out = []
        game = self.state.get("game") or {}
        patched = game.get("patched") or 0
        now = time.time()
        if patched and now - patched < PATCH_NOTICE_DAYS * 86400:
            out.append(finding("game-patch", "info", f"Cyberpunk 2077 changed on {fmt_date(patched)}",
                               "The game program was updated (or repaired) since this app first saw it. Mods that reach "
                               "into the game itself - frameworks, RED4ext plugins, CET - can stop working until their "
                               "authors update them; they are listed below when Nexus shows no update since."))
        for m in mods:
            if not m.nexus_id:
                continue
            info = self.state["nexus"].get(str(m.nexus_id))
            if not info:
                continue
            if info.get("error"):
                out.append(finding("removed", "warn", f"{m.name}: its Nexus page was removed or is hidden",
                                   "The page can't be found any more, so you won't get updates or a changelog for it. "
                                   "The files you have are fine; keep them. (If your key was just entered wrongly, the "
                                   "same message can appear - check Settings.)", mod=m.name, nexus_id=m.nexus_id))
                continue
            if m.status == "off":
                continue
            upd = info.get("updated") or 0
            if not upd:
                continue
            fragile = m.core or any(u.category in ("RED4ext", "ASI/DLL", "CET", "Scripts") for u in m.units)
            age = (now - upd) / 86400
            if patched and upd < patched - PATCH_GRACE and fragile:
                out.append(finding("abandoned", "warn", f"{m.name} hasn't been updated since the game changed",
                                   f"Its Nexus page was last updated on {fmt_date(upd)}; the game changed around {fmt_date(patched)}. "
                                   "It reaches into the game, so check its page (comments, posts) to see whether it still "
                                   "works with this version.", mod=m.name, nexus_id=m.nexus_id))
            elif age >= ABANDONED_DAYS:
                out.append(finding("abandoned", "info", f"{m.name}: no update on Nexus for {int(age // 365)} years",
                                   f"Last updated on {fmt_date(upd)}. That's not a problem by itself - plenty of mods are "
                                   "finished - but nobody is fixing it if it breaks.", mod=m.name, nexus_id=m.nexus_id))
        return out

    # --- fixes: every one can be undone in History ---------------------------------------------------------------
    def fix(self, f: dict) -> dict:
        fx = (f or {}).get("fix") or {}
        act = fx.get("action")
        game = self.game
        errors = []
        if act in ("move", "aside"):
            stamp = time.strftime("%Y%m%d-%H%M%S")
            aside = self.stash / BACKUP_NAME / f"{stamp}-check-up"
            pairs = [(fx["rel"], fx["to"])] if act == "move" else \
                [(r, None) for r in fx.get("rels", [])]
            done = []
            for rel, dest in pairs:
                src = game / rel
                if dest is None:
                    n = 1
                    dst = aside / rel
                    while dst.exists():
                        n += 1
                        dst = aside / f"{rel}.{n}"
                    dest_rel = dst.relative_to(game).as_posix()
                else:
                    dst, dest_rel = game / dest, dest
                try:
                    if not (src.exists() or src.is_symlink()):
                        raise FileNotFoundError("it isn't there any more")
                    if dst.exists():
                        raise FileExistsError(f"{dest_rel} already exists")
                    if not (_inside(game, src) and _inside(game, dst)):
                        raise OSError("outside the game folder")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), str(dst))
                    done.append([rel, dest_rel])
                except OSError as e:
                    errors.append(f"{rel}: {e}")
            if done:
                what = f"Moved {Path(done[0][0]).name} to archive/pc/mod" if act == "move" else \
                    "Put aside " + (Path(done[0][0]).name if len(done) == 1 else f"{len(done)} items")
                self.journal_add("fix", what, moves=done)
                self._prune_stash()
            return {"ok": bool(done) and not errors, "text": what if done else "Nothing was changed.", "errors": errors}
        if act == "forget":
            rels = set(fx.get("rels", []))
            for r in rels:
                self.state["links"].pop(r, None)
            used = {l["id"] for l in self.state["links"].values()}
            for mid in list(self.state["installed"]):
                if int(mid) not in used:
                    self.state["installed"].pop(mid, None)
            for inst in self.state["instances"].values():
                inst["on"] = [r for r in inst.get("on", []) if r not in rels]
                inst["off"] = [r for r in inst.get("off", []) if r not in rels]
            self.save()
            return {"ok": True, "text": f"Forgot {len(rels)} remembered file(s).", "errors": []}
        if act == "enable":
            mods = [m for m in self.scan() if m.key in set(fx.get("mod_keys", []))]
            self.begin_trail()
            for m in mods:
                _n, errs = self.set_enabled(m, True)
                errors += errs
            self.log_toggle(mods, True)
            return {"ok": bool(mods) and not errors, "text": "Switched on " + ", ".join(m.name for m in mods), "errors": errors}
        return {"ok": False, "text": "There is nothing to fix automatically.", "errors": []}

    def _undo_fix(self, e: dict) -> list:
        errors = []
        for orig, new in e.get("moves", []):
            src, dst = self.game / new, self.game / orig
            try:
                if dst.exists():
                    raise FileExistsError("something is there already")
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dst))
            except OSError as ex:
                errors.append(f"{orig}: {ex}")
        return errors

    # --- the game itself ------------------------------------------------------------------------------------------------
    def game_signature(self) -> dict:
        try:
            st = (self.game / GAME_EXE).stat()
            return {"size": st.st_size, "mtime": int(st.st_mtime)}
        except OSError:
            return {}

    def check_game_patch(self) -> dict:
        """Remember what the game program looks like. -> {"changed": bool (new since last time), "patched": ts or 0}"""
        sig = self.game_signature()
        saved = self.state.get("game") or {}
        if not sig:
            return {"changed": False, "patched": saved.get("patched", 0)}
        if not saved.get("sig"):
            self.state["game"] = {"sig": sig, "seen": time.time(), "patched": 0, "acked": True}
            self.save()
            return {"changed": False, "patched": 0}
        if saved["sig"] != sig:
            now = time.time()
            self.state["game"] = {"sig": sig, "prev": saved["sig"], "seen": now,
                                  "patched": min(sig["mtime"], now), "acked": False}
            self.save()
            return {"changed": True, "patched": self.state["game"]["patched"]}
        return {"changed": not saved.get("acked", True), "patched": saved.get("patched", 0)}

    def ack_game_patch(self):
        if isinstance(self.state.get("game"), dict):
            self.state["game"]["acked"] = True
            self.save()

    def stale_after_patch(self, mods: list = None) -> list:
        """Switched-on mods that reach into the game and whose Nexus page wasn't updated since the game changed."""
        patched = (self.state.get("game") or {}).get("patched") or 0
        if not patched:
            return []
        out = []
        for m in mods or self.scan():
            info = self.state["nexus"].get(str(m.nexus_id)) if m.nexus_id else None
            if not info or info.get("error") or m.status == "off":
                continue
            fragile = m.core or any(u.category in ("RED4ext", "ASI/DLL", "CET", "Scripts") for u in m.units)
            upd = info.get("updated") or 0
            if fragile and upd and upd < patched - PATCH_GRACE:
                out.append(m)
        return out

    # --- logs ---------------------------------------------------------------------------------------------------------------
    LOG_PLACES = (("red4ext", True), ("r6/logs", False), ("bin/x64/plugins/cyber_engine_tweaks", False))
    LOG_ERROR = re.compile(r"(?i)(\b(error|fatal|critical|exception)\b|failed to|unresolved|could not|couldn't)")

    def read_logs(self, mods: list = None, max_age_days: int = 30, tail: int = 400 * 1024) -> dict:
        """Read the end of the RED4ext, redscript and CET logs and point at the mods their errors mention.
        -> {"files": [{rel, mtime}], "lines": [{log, text, mods}], "suspects": [(mod name, count)], "unknown": n}"""
        mods = mods or self.scan()
        files = []
        for rel, deep in self.LOG_PLACES:
            base = self.game / rel
            if not base.is_dir():
                continue
            it = base.rglob("*.log") if deep else base.glob("*.log")
            for p in it:
                try:
                    st = p.stat()
                except OSError:
                    continue
                if st.st_size and time.time() - st.st_mtime <= max_age_days * 86400:
                    files.append((p, st))
        files.sort(key=lambda x: -x[1].st_mtime)
        pats = []                                              # (needle, mod) - from file paths and names
        for m in mods:
            for u in m.units:
                pats.append((u.rel.lower(), m))
                base = u.rel.rsplit("/", 1)[-1].lower().rsplit(".", 1)[0]
                if len(base) >= 5:
                    pats.append((base, m))
        out = {"files": [], "lines": [], "suspects": [], "unknown": 0}
        counts, seen = Counter(), set()
        for p, st in files[:40]:
            out["files"].append({"rel": p.relative_to(self.game).as_posix(), "mtime": st.st_mtime})
            try:
                with open(p, "rb") as f:
                    f.seek(max(0, st.st_size - tail))
                    text = f.read().decode("utf-8", "ignore")
            except OSError:
                continue
            for line in text.splitlines():
                if not self.LOG_ERROR.search(line):
                    continue
                low = line.lower().replace("\\", "/")
                hit = []
                for needle, m in pats:
                    if len(needle) >= 5 and needle in low and m.name not in hit:
                        hit.append(m.name)
                for b in re.findall(r"\[([^\]]{3,40})\]", line):
                    k = norm_key(b)
                    for m in mods:
                        if k and (k == norm_key(m.name) or any(k == u.key for u in m.units)) and m.name not in hit:
                            hit.append(m.name)
                text_line = re.sub(r"\s+", " ", line).strip()[:300]
                sig = (p.name, re.sub(r"\d", "#", text_line))
                if sig in seen:
                    continue
                seen.add(sig)
                if len(out["lines"]) < 300:
                    out["lines"].append({"log": p.name, "rel": p.relative_to(self.game).as_posix(), "text": text_line, "mods": hit})
                for h in hit:
                    counts[h] += 1
                if not hit:
                    out["unknown"] += 1
        out["suspects"] = counts.most_common()
        return out


BISECT_INSTANCE = "Before crash search"


class CrashFinder:
    """Finds the mod that makes the game crash, by halving. The app switches mods on and off; you start the game,
    and tell the app whether it crashed. Steps:
      1. baseline - only the frameworks on. If it still crashes, no ordinary mod is to blame.
      2. halving  - half of the suspects on (plus the ones already cleared); crash -> the culprit is in that half,
                    no crash -> those are cleared, look at the rest.
      3. confirm  - everything on except the one found; if the game runs, that mod is it.
    The search is kept in the state file, so closing the window doesn't lose it, and the setup from before the search
    is kept (as the instance “Before crash search” and inside the search itself) until you choose to put it back."""

    def __init__(self, mgr):
        self.mgr = mgr

    @property
    def st(self) -> dict:
        return self.mgr.state.get("bisect") or {}

    def active(self) -> bool:
        return bool(self.st.get("phase") in ("testing", "found"))

    def suspects_now(self, mods: list = None) -> list:
        mods = mods if mods is not None else self.mgr.scan()
        return [m for m in mods if m.status != "off" and not m.core]

    def start(self, mods: list = None) -> dict:
        mgr = self.mgr
        mgr.ensure_instances()
        mgr.sync_active()
        mods = mods if mods is not None else mgr.scan()
        on = [m for m in mods if m.status != "off"]
        suspects = [{"name": m.name, "rels": [u.rel for u in m.units]} for m in on if not m.core]
        keep = sorted({u.rel for m in on if m.core for u in m.units})
        if len(suspects) < 2:
            raise ValueError("There are fewer than two switched-on mods besides the frameworks, so there is nothing to "
                             "narrow down. Try the game with those mods off.")
        snap = mgr.snapshot()
        mgr.state["instances"][BISECT_INSTANCE] = dict(snap, created=time.time())
        mgr.state["bisect"] = {"phase": "testing", "step": "baseline", "start": snap,
                               "active_before": mgr.state.get("active", ""), "keep": keep, "good": [],
                               "cand": suspects, "half": [], "tests": 0, "total": len(suspects),
                               "culprit": None, "outcome": "", "errors": []}
        mgr.save()
        self._apply(keep, "only the frameworks on")
        return self.st

    def _apply(self, on_rels, what: str):
        st = self.st
        on = set(on_rels)
        off = (set(st["start"]["on"]) | set(st["start"]["off"])) - on
        mgr = self.mgr
        mgr._trail.clear()
        moved, errors = mgr.apply_plan(mgr.plan_for({"on": sorted(on), "off": sorted(off)}, "Crash search"))
        mgr._trail.clear()
        st["tests"] += 1
        st["what"] = what
        st["errors"] = errors
        mgr.sync_active()
        mgr.save()

    def _apply_half(self):
        st = self.st
        cand = st["cand"]
        half = cand[:max(1, len(cand) // 2)]
        st["half"] = [c["name"] for c in half]
        rels = set(st["keep"])
        for c in st["good"] + half:
            rels |= set(c["rels"])
        self._apply(rels, f"{len(half)} of {len(cand)} suspects on")

    def _apply_confirm(self):
        st = self.st
        culprit = st["cand"][0]
        rels = set(st["start"]["on"]) - set(culprit["rels"])
        self._apply(rels, f"everything on except {culprit['name']}")

    def answer(self, crashed: bool) -> dict:
        """The game crashed (or showed the problem) with the current test setup: True. It ran fine: False."""
        st = self.st
        if st.get("phase") != "testing":
            raise ValueError("No search is running.")
        step = st.get("step")
        if step == "baseline":
            if crashed:                                    # nothing ordinary is on and it still goes wrong
                st.update(phase="found", culprit=None, outcome="frameworks")
                self.mgr.save()
                return st
            st["step"] = "halve"
            self._apply_half()
            return st
        if step == "halve":
            half_names = set(st["half"])
            half = [c for c in st["cand"] if c["name"] in half_names]
            rest = [c for c in st["cand"] if c["name"] not in half_names]
            if crashed:
                st["cand"] = half
            else:
                st["good"] = st["good"] + half
                st["cand"] = rest
            if len(st["cand"]) == 1:
                st["step"] = "confirm"
                self._apply_confirm()
            else:
                self._apply_half()
            return st
        if step == "confirm":
            if crashed:                                    # still wrong without it: not (only) this mod
                st.update(phase="found", culprit=None, outcome="several")
            else:
                st.update(phase="found", culprit=st["cand"][0]["name"], outcome="confirmed")
            self.mgr.save()
            return st
        raise ValueError("The search is in an unknown state.")

    def remaining(self) -> int:
        """About how many more tests it takes."""
        st = self.st
        n = len(st.get("cand", []))
        step = st.get("step")
        halves = math.ceil(math.log2(n)) if n > 1 else 0
        if step == "baseline":
            return 1 + halves + 1
        if step == "halve":
            return halves + 1
        return 1 if step == "confirm" else 0

    def finish(self, keep_off: bool = False) -> dict:
        """Put every mod back the way it was when the search started. `keep_off`: the culprit stays off."""
        st = self.st
        if not st:
            return {"moved": 0, "errors": []}
        mgr = self.mgr
        culprit = next((c for c in st.get("cand", []) if c["name"] == st.get("culprit")), None)
        start = {"on": list(st["start"]["on"]), "off": list(st["start"]["off"])}
        if keep_off and culprit:
            cr = set(culprit["rels"])
            start["on"] = [r for r in start["on"] if r not in cr]
            start["off"] = sorted(set(start["off"]) | cr)
        mgr._trail.clear()
        moved, errors = mgr.apply_plan(mgr.plan_for(start, "Before crash search"))
        trail = mgr.take_trail()
        before = st.get("active_before", "")
        if errors:
            return {"moved": moved, "errors": errors}
        mgr.state["bisect"] = {}
        mgr.state["instances"].pop(BISECT_INSTANCE, None)
        if before in mgr.state["instances"]:
            mgr.state["active"] = before
        mgr.sync_active()
        mgr.save()
        mgr.journal_add("restore", "Crash search finished: mods put back" +
                        (f"; “{culprit['name']}” stays off" if keep_off and culprit else ""),
                        active_before=before, active_after=mgr.state.get("active", ""), **trail)
        return {"moved": moved, "errors": []}


# --------------------------------------------------------------------------
# Round 3: settings backup, mod lists, one set of saves per instance, endorsing
# --------------------------------------------------------------------------
SETTINGS_EXTS = frozenset({"json", "ini", "toml", "xml", "yaml", "yml", "cfg", "conf", "sqlite3", "db"})
SETTINGS_MAX_FILE = 64 << 20
SETTINGS_MAX_TOTAL = 1 << 30
SETTINGS_MAX_FILES = 6000
SETTINGS_MANIFEST = "modscout-settings.json"
# key, label, where ("game" = below the game folder, "user" = the game's settings folder), folder, extensions, skipped folders,
# ticked by default
SETTINGS_GROUPS = (
    ("cet", "Cyber Engine Tweaks and the settings of its mods", "game", "bin/x64/plugins/cyber_engine_tweaks",
     SETTINGS_EXTS, frozenset({"logs"}), True),
    ("plugins", "Settings of RED4ext plugins", "game", "red4ext/plugins",
     frozenset({"toml", "ini", "json", "yaml", "yml", "cfg", "conf"}), frozenset(), True),
    ("user", "The game's own settings (graphics, controls) in your user folder", "user", "",
     frozenset({"json", "xml", "ini"}), frozenset(), True),
    ("r6cfg", "Input and other files in r6/config (includes files of the game itself - restore only on the same game version)",
     "game", "r6/config", SETTINGS_EXTS, frozenset(), False),
)
LIST_FORMAT = "modscout-list"
LIST_MAX_BYTES = 8 << 20
LIST_MAX_MODS = 3000
SAVE_SHARED = "shared"
SAVES_MARK = " (ModScout - "
ENDORSE_STATES = ("Endorsed", "Abstained", "Undecided")


def default_user_settings_dir():
    """Where the game keeps its own settings (UserSettings.json ...) - %LOCALAPPDATA%\\CD Projekt Red\\Cyberpunk 2077."""
    base = os.environ.get("LOCALAPPDATA")
    return Path(base) / "CD Projekt Red" / "Cyberpunk 2077" if base else None


def default_saves_dir():
    """Where the game keeps its saves on Windows - Saved Games\\CD Projekt Red\\Cyberpunk 2077."""
    if os.name != "nt":
        return None
    return Path.home() / "Saved Games" / "CD Projekt Red" / "Cyberpunk 2077"


def file_crc(path: Path) -> int:
    crc = 0
    with open(path, "rb") as f:
        while True:
            b = f.read(1 << 20)
            if not b:
                return crc & 0xFFFFFFFF
            crc = zlib.crc32(b, crc)


def _clean_text(v, limit=120) -> str:
    return re.sub(r"[\x00-\x1f\x7f\s]+", " ", str(v or "")).strip()[:limit]


class _Round3:
    """Settings backup, mod lists, saves per instance. Mixed into Manager."""

    # --- settings backup ----------------------------------------------------------------------------------
    def user_settings_dir(self):
        p = load_config().get("user_settings_dir") or ""
        return Path(p) if p else default_user_settings_dir()

    def _settings_roots(self, root: str):
        if root == "user":
            u = self.user_settings_dir()
            return [("user", u)] if u else []
        return [("game", self.game), ("off", self.stash)]

    def settings_files(self, key: str) -> list:
        """[(path, name inside the zip, size)] for one group of settings."""
        spec = next(g for g in SETTINGS_GROUPS if g[0] == key)
        _k, _label, where, folder, exts, skip, _default = spec
        out = []
        for tag, root in self._settings_roots(where):
            base = Path(root) / folder if folder else Path(root)
            if not base.is_dir():
                continue
            for dirpath, dirs, files in os.walk(base):
                dirs[:] = [d for d in sorted(dirs) if d.lower() not in skip and not is_link_dir(Path(dirpath) / d)]
                if where == "user":
                    dirs[:] = []
                for f in sorted(files):
                    p = Path(dirpath) / f
                    if f.lower().rsplit(".", 1)[-1] not in exts or p.is_symlink():
                        continue
                    try:
                        size = p.stat().st_size
                    except OSError:
                        continue
                    if size > SETTINGS_MAX_FILE:
                        continue
                    out.append((p, f"{tag}/{p.relative_to(root).as_posix()}", size))
        return out

    def settings_inventory(self) -> list:
        out = []
        for key, label, where, folder, _e, _s, default in SETTINGS_GROUPS:
            fl = self.settings_files(key)
            out.append({"key": key, "label": label, "default": default, "files": len(fl), "size": sum(s for _p, _n, s in fl),
                        "where": "your user folder" if where == "user" else folder})
        return out

    def settings_backup(self, dest_dir, keys=None, progress=None) -> dict:
        """Zip the settings (not the mods) into `dest_dir`, which must be outside the game folder.
        -> {"path", "files", "size", "skipped": [..]}"""
        progress = progress or (lambda *a: None)
        dest = Path(dest_dir).expanduser()
        if _inside(self.game, dest) or dest.resolve() == self.game.resolve():
            raise ValueError("Pick a folder outside the game folder - the point is that the backup survives a reinstall.")
        keys = [k for k in (keys if keys is not None else [g[0] for g in SETTINGS_GROUPS if g[6]])]
        files, groups = [], {}
        for k in keys:
            fl = self.settings_files(k)
            groups[k] = len(fl)
            files += fl
        if not files:
            raise ValueError("There are no settings files to back up with the choices made.")
        if len(files) > SETTINGS_MAX_FILES or sum(s for _p, _n, s in files) > SETTINGS_MAX_TOTAL:
            raise ValueError("That is more settings than I'm willing to pack (over 1 GB or 6000 files). Untick a group.")
        dest.mkdir(parents=True, exist_ok=True)
        final = dest / f"ModScout settings {time.strftime('%Y-%m-%d %H%M%S')}.zip"
        n = 1
        while final.exists():
            n += 1
            final = dest / f"ModScout settings {time.strftime('%Y-%m-%d %H%M%S')} ({n}).zip"
        tmp = final.with_name(final.name + ".part")
        skipped = []
        try:
            with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
                for i, (p, name, _size) in enumerate(files):
                    progress(i, len(files), p.name)
                    try:
                        z.write(p, name)
                    except OSError as e:
                        skipped.append(f"{p.name}: {e}")
                z.writestr(SETTINGS_MANIFEST, json.dumps({
                    "format": 1, "app": f"{APP_NAME} {VERSION}", "created": time.time(), "game": str(self.game),
                    "groups": groups}, indent=1))
            os.replace(tmp, final)
        finally:
            try:
                if tmp.exists():
                    tmp.unlink()
            except OSError:
                pass
        return {"path": str(final), "files": len(files) - len(skipped), "size": final.stat().st_size, "skipped": skipped}

    def _settings_target(self, name: str):
        """Where a name inside a settings zip would be restored: (group key, root, target path), or None if it isn't
        something this app writes."""
        if not name or "\\" in name or name.startswith("/") or ":" in name or "\0" in name:
            return None
        parts = name.split("/")
        if len(parts) < 2 or any(p in ("", ".", "..") for p in parts):
            return None
        tag, rel_parts = parts[0], parts[1:]
        rel = "/".join(rel_parts)
        ext = rel_parts[-1].lower().rsplit(".", 1)[-1] if "." in rel_parts[-1] else ""
        for key, _label, where, folder, exts, skip, _d in SETTINGS_GROUPS:
            if where == "user":
                u = self.user_settings_dir()
                if tag == "user" and u and len(rel_parts) == 1 and ext in exts:
                    return key, u, u / rel
                continue
            if tag not in ("game", "off"):
                continue
            if not (rel == folder or rel.startswith(folder + "/")) or ext not in exts:
                continue
            if any(p.lower() in skip for p in rel_parts[:-1]):
                continue
            root = self.game if tag == "game" else self.stash
            # `rel` has no "..", ".", empty, drive or backslash parts (checked above), so this can't leave `root` by
            # name; whether something on disk along the way is a link is checked separately, with its own message.
            return key, root, root / rel
        return None

    @staticmethod
    def _link_on_way(root: Path, target: Path) -> bool:
        """True when the file, or any folder between `root` and it, is a link (root itself may be one on purpose:
        the switched-off mods' folder can have been moved to another drive and linked back)."""
        try:
            rel = target.relative_to(root)
        except ValueError:
            return True
        cur = root
        for part in rel.parts:
            cur = cur / part
            if cur.is_symlink() or (cur.exists() and is_link_dir(cur)):
                return True
        return False

    def settings_inspect(self, zip_path) -> dict:
        """Read a settings zip without changing anything: what is in it, and what would change.
        -> {"created", "game", "entries": [{name, group, target, size, status, crc}], "skipped": [..], "counts": {...}}"""
        zp = Path(zip_path)
        try:
            z = zipfile.ZipFile(zp)
        except (OSError, zipfile.BadZipFile) as e:
            raise ValueError(f"That isn't a settings backup I can open ({e}).")
        with z:
            try:
                man = json.loads(z.read(SETTINGS_MANIFEST).decode("utf-8"))
            except (KeyError, ValueError, UnicodeDecodeError):
                raise ValueError("That zip isn't a ModScout settings backup (no modscout-settings.json inside).")
            if not isinstance(man, dict) or man.get("format") != 1:
                raise ValueError("That backup was made by a different version of the app and I can't read it.")
            entries, skipped = [], []
            infos = [i for i in z.infolist() if i.filename != SETTINGS_MANIFEST and not i.is_dir()]
            if len(infos) > SETTINGS_MAX_FILES:
                raise ValueError("That backup has far more files than a settings backup should.")
            total = 0
            for info in infos:
                tgt = self._settings_target(info.filename)
                if tgt is None:
                    skipped.append(f"{info.filename} (not a place I restore settings to)")
                    continue
                if (info.external_attr >> 16) & 0o170000 == 0o120000:
                    skipped.append(f"{info.filename} (a link)")
                    continue
                if info.file_size > SETTINGS_MAX_FILE:
                    skipped.append(f"{info.filename} (too big)")
                    continue
                total += info.file_size
                key, root, target = tgt
                if self._link_on_way(root, target):
                    skipped.append(f"{info.filename} (the place on disk is a link)")
                    continue
                if target.is_file():
                    try:
                        same = target.stat().st_size == info.file_size and file_crc(target) == info.CRC
                    except OSError:
                        same = False
                    status = "same" if same else "changed"
                elif target.exists():
                    skipped.append(f"{info.filename} (a folder is in the way)")
                    continue
                else:
                    status = "new"
                entries.append({"name": info.filename, "group": key, "target": target, "size": info.file_size, "status": status})
            if total > SETTINGS_MAX_TOTAL:
                raise ValueError("That backup unpacks to more than 1 GB; I won't restore it.")
        counts = Counter(e["status"] for e in entries)
        return {"created": man.get("created", 0), "game": str(man.get("game", "")), "entries": entries, "skipped": skipped,
                "counts": dict(counts), "groups": Counter(e["group"] for e in entries), "path": str(zp)}

    def settings_restore(self, zip_path, keys=None, progress=None) -> dict:
        """Put settings from a backup back. Every file that would be replaced is first moved to
        _disabled_mods/_backup/<time>-settings-restore, and the restore can be undone from History.
        -> {"restored": n, "errors": [..], "backup": str}"""
        progress = progress or (lambda *a: None)
        if game_running():
            raise ValueError("Cyberpunk 2077 is running. Close the game first.")
        insp = self.settings_inspect(zip_path)
        todo = [e for e in insp["entries"] if e["status"] != "same" and (keys is None or e["group"] in set(keys))]
        if not todo:
            return {"restored": 0, "errors": [], "backup": ""}
        stamp = time.strftime("%Y%m%d-%H%M%S")
        bak = self.stash / BACKUP_NAME / f"{stamp}-settings-restore"
        n = 1
        while bak.exists():
            n += 1
            bak = self.stash / BACKUP_NAME / f"{stamp}-settings-restore-{n}"
        moves, created, errors = [], [], []
        with zipfile.ZipFile(zip_path) as z:
            for i, e in enumerate(todo):
                target = e["target"]
                progress(i, len(todo), target.name)
                held = None
                try:
                    if target.exists():
                        held = bak / f"{i:04d}-{target.name}"
                        held.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(target), str(held))
                    target.parent.mkdir(parents=True, exist_ok=True)
                    tmp = target.with_name(target.name + ".cp2077tmp")
                    try:
                        with z.open(e["name"]) as src, open(tmp, "wb") as out:
                            left = SETTINGS_MAX_FILE
                            while True:
                                b = src.read(1 << 20)
                                if not b:
                                    break
                                left -= len(b)
                                if left < 0:
                                    raise OSError("the file is bigger than it says")
                                out.write(b)
                        os.replace(tmp, target)
                    finally:
                        if tmp.exists():
                            try:
                                tmp.unlink()
                            except OSError:
                                pass
                    (moves.append([str(target), str(held)]) if held else created.append(str(target)))
                except OSError as ex:
                    errors.append(f"{target.name}: {ex}")
                    if held is not None and held.exists() and not target.exists():
                        try:
                            shutil.move(str(held), str(target))
                        except OSError:
                            pass
        if moves or created:
            self.journal_add("settings", f"Restored {len(moves) + len(created)} settings file(s) from {Path(zip_path).name}",
                             abs_moves=moves, abs_created=created, backup=str(bak))
        return {"restored": len(moves) + len(created), "errors": errors, "backup": str(bak) if moves else ""}

    def _undo_settings(self, e: dict) -> list:
        aside = self.stash / BACKUP_NAME / (time.strftime("%Y%m%d-%H%M%S") + "-undo-settings")
        errors = []
        for i, p in enumerate(e.get("abs_created", [])):
            try:
                p = Path(p)
                if p.is_file():
                    dst = aside / "removed" / f"{i:04d}-{p.name}"
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(p), str(dst))
            except OSError as ex:
                errors.append(f"{Path(p).name}: {ex}")
        for i, (orig, held) in enumerate(e.get("abs_moves", [])):
            try:
                orig, held = Path(orig), Path(held)
                if orig.exists():
                    dst = aside / "replaced" / f"{i:04d}-{orig.name}"
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(orig), str(dst))
                shutil.move(str(held), str(orig))
            except OSError as ex:
                errors.append(f"{Path(orig).name}: {ex}")
        self._prune_stash()
        return errors

    # --- mod lists ------------------------------------------------------------------------------------------------
    def export_list(self, path, fmt: str = "json", name: str = "", include_notes: bool = False) -> dict:
        """Write the mods you have as a list somebody else can read (and the app can import). -> {"path", "mods"}"""
        text, n = self.list_text(fmt, name, include_notes)
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, "utf-8")
        return {"path": str(p), "mods": n}

    def list_text(self, fmt: str = "json", name: str = "", include_notes: bool = False):
        """The mod list as text: 'json' (the app can import it) or 'text' (Markdown for a forum or chat). -> (text, mods)"""
        mods = self.scan()
        title = _clean_text(name, 80) or "My Cyberpunk 2077 mods"
        active = self.state.get("active", "")
        rows = []
        for m in mods:
            row = {"name": m.name, "nexus_id": int(m.nexus_id or 0), "version": m.installed_version or "",
                   "enabled": m.status == "on", "framework": bool(m.core)}
            if include_notes:
                if m.note:
                    row["note"] = m.note
                if m.tags:
                    row["tags"] = list(m.tags)
            rows.append(row)
        if fmt == "json":
            doc = {"format": LIST_FORMAT, "version": 1, "game": DOMAIN, "app": f"{APP_NAME} {VERSION}", "name": title,
                   "created": time.time(), "instance": active, "mods": rows}
            text = json.dumps(doc, indent=1, ensure_ascii=False)
        else:
            lines = [f"# {title}", "", f"Made with {APP_NAME} on {fmt_date(time.time())}"
                     + (f" - setup “{active}”" if active else ""), ""]
            linked = [r for r in rows if r["nexus_id"]]
            other = [r for r in rows if not r["nexus_id"]]
            lines.append(f"## On Nexus Mods ({len(linked)})")
            for r in linked:
                lines.append(f"- [{r['name']}]({NEXUS_SITE}/{DOMAIN}/mods/{r['nexus_id']})"
                             + (f" - {r['version']}" if r["version"] else "") + ("" if r["enabled"] else " (switched off)")
                             + (f" - {r['note']}" if r.get("note") else ""))
            if other:
                lines += ["", f"## Not linked to Nexus ({len(other)})"]
                for r in other:
                    lines.append(f"- {r['name']}" + ("" if r["enabled"] else " (switched off)"))
            text = "\n".join(lines) + "\n"
        return text, len(rows)

    def read_list(self, path) -> dict:
        """Read a mod list written by export_list, treating everything in it as untrusted text."""
        p = Path(path)
        try:
            if p.stat().st_size > LIST_MAX_BYTES:
                raise ValueError("That file is far too big for a mod list.")
            doc = json.loads(p.read_text("utf-8-sig"))
        except OSError as e:
            raise ValueError(f"I couldn't read that file ({e}).")
        except ValueError as e:
            if "too big" in str(e):
                raise
            raise ValueError("That file isn't a mod list the app can read (it has to be the .json version).")
        if not isinstance(doc, dict) or doc.get("format") != LIST_FORMAT or not isinstance(doc.get("mods"), list):
            raise ValueError("That file isn't a ModScout mod list.")
        if str(doc.get("game", DOMAIN)) != DOMAIN:
            raise ValueError("That list is for a different game.")
        rows = []
        for r in doc["mods"][:LIST_MAX_MODS]:
            if not isinstance(r, dict) or not _clean_text(r.get("name")):
                continue
            try:
                nid = int(r.get("nexus_id") or 0)
            except (TypeError, ValueError):
                nid = 0
            rows.append({"name": _clean_text(r["name"]), "nexus_id": nid if 0 < nid < 10 ** 9 else 0,
                         "version": _clean_text(r.get("version"), 40), "enabled": bool(r.get("enabled", True)),
                         "framework": bool(r.get("framework")), "note": _clean_text(r.get("note"), 200),
                         "tags": [_clean_text(t, 24) for t in (r.get("tags") or [])[:8] if isinstance(t, str)]})
        return {"name": _clean_text(doc.get("name"), 80) or "Mod list", "created": doc.get("created") or 0,
                "instance": _clean_text(doc.get("instance"), 40), "mods": rows}

    def compare_list(self, lst: dict) -> list:
        """Each mod of the list against your library. state: same | older (you have an older version) | newer |
        missing (on Nexus, not here) | name (matched by name) | absent (not on Nexus, not here)"""
        mods = self.scan()
        by_id = {m.nexus_id: m for m in mods if m.nexus_id}
        by_name = {m.name.lower(): m for m in mods}
        out = []
        for r in lst["mods"]:
            local = by_id.get(r["nexus_id"]) if r["nexus_id"] else None
            state = ""
            if local:
                c = compare_versions(local.installed_version, r["version"]) if local.installed_version and r["version"] else None
                state = "same" if c in (None, 0) else ("older" if c < 0 else "newer")
            elif r["name"].lower() in by_name:
                local, state = by_name[r["name"].lower()], "name"
            else:
                state = "missing" if r["nexus_id"] else "absent"
            out.append(dict(r, state=state, local=local, local_version=local.installed_version if local else ""))
        return out

    def list_to_instance(self, rows: list, name: str) -> str:
        """A new instance with the list's on/off choices, for the mods you have. Frameworks stay as they are."""
        name = self.create_instance(name, "current")
        mods = self.scan()
        want = {r["local"].key: r["enabled"] for r in rows if r.get("local")}
        on, off = set(), set()
        for m in mods:
            if m.core:
                (on if m.status != "off" else off).update(u.rel for u in m.units)
            elif want.get(m.key):
                on.update(u.rel for u in m.units)
            else:
                off.update(u.rel for u in m.units)
        inst = self.state["instances"][name]
        inst["on"], inst["off"] = sorted(on), sorted(off)
        self.save()
        return name

    # --- endorsing ---------------------------------------------------------------------------------------------------
    def endorse_status(self, mod_id) -> str:
        """Endorsed | Abstained | Undecided, as last read from Nexus or set by this app; '' if never read."""
        if not self.state.get("endorse_checked"):
            return ""
        return (self.state["endorse"].get(str(mod_id)) or {}).get("status", "Undecided")

    def endorse_refresh(self, nx) -> int:
        """Read which mods you have endorsed from your Nexus account. -> how many are endorsed"""
        seen = {}
        for t in nx.endorsed():
            try:
                mid = int(t.get("mod_id"))
            except (TypeError, ValueError):
                continue
            status = str(t.get("status") or t.get("endorse_status") or "Endorsed").strip().capitalize()
            seen[str(mid)] = status if status in ENDORSE_STATES else "Endorsed"
        now = time.time()
        self.state["endorse"] = {k: {"status": v, "ts": now} for k, v in seen.items()}
        self.state["endorse_checked"] = now
        self.save()
        return sum(1 for v in seen.values() if v == "Endorsed")

    def endorse_do(self, nx, mod_id, version: str = "", abstain: bool = False) -> str:
        nx.endorse(mod_id, version, abstain)
        status = "Abstained" if abstain else "Endorsed"
        self.state["endorse"][str(int(mod_id))] = {"status": status, "ts": time.time()}
        self.state.setdefault("endorse_checked", time.time())
        self.save()
        return status

    def endorse_candidates(self, mods: list = None) -> list:
        """Mods that are linked to Nexus and that you haven't endorsed (as far as is known)."""
        mods = mods if mods is not None else self.scan()
        return [m for m in mods if m.nexus_id and not m.nexus_error and self.endorse_status(m.nexus_id) != "Endorsed"]

    def endorse_many(self, nx, mods: list, progress=None) -> dict:
        """Endorse each mod. Stops at once if Nexus rejects the key or the rate limit is reached.
        -> {"done": [names], "failed": [(name, why)], "stopped": why or ""}"""
        progress = progress or (lambda *a: None)
        out = {"done": [], "failed": [], "stopped": ""}
        for i, m in enumerate(mods):
            progress(i, len(mods), m.name)
            try:
                self.endorse_do(nx, m.nexus_id, m.installed_version or m.latest_version)
                out["done"].append(m.name)
            except NexusError as e:
                if e.status in (401, 429):
                    out["stopped"] = str(e)
                    break
                out["failed"].append((m.name, str(e)))
        return out

    # --- one set of saves per instance ---------------------------------------------------------------------------
    def saves_dir(self):
        p = load_config().get("saves_dir") or ""
        return Path(p) if p else default_saves_dir()

    def _saves(self) -> dict:
        st = self.state.setdefault("saves", {})
        st.setdefault("on", False)
        if not isinstance(st.get("owners"), list):
            st["owners"] = []
        if not isinstance(st.get("folders"), dict):
            st["folders"] = {}
        if not isinstance(st.get("live"), str):
            st["live"] = SAVE_SHARED
        return st

    def saves_set_of(self, instance: str) -> str:
        st = self._saves()
        return instance if instance in st["owners"] else SAVE_SHARED

    def _saves_folder(self, live: Path, set_name: str) -> Path:
        """The folder a set of saves rests in while it isn't the live one."""
        st = self._saves()
        if set_name not in st["folders"]:
            base = f"{live.name}{SAVES_MARK}{clean_folder_name(set_name)[:40]})"
            name, n = base, 1
            while name in st["folders"].values():
                n += 1
                name = f"{base[:-1]} {n})"
            st["folders"][set_name] = name
        return live.with_name(st["folders"][set_name])

    def saves_status(self) -> dict:
        st = self._saves()
        live = self.saves_dir()
        sets = []
        if live and live.parent.is_dir():
            kept = sorted((k for k in st["folders"] if k != SAVE_SHARED and k not in st["owners"]), key=str.lower)
            for name in [SAVE_SHARED] + sorted(st["owners"], key=str.lower) + kept:
                folder = live if name == st["live"] else self._saves_folder(live, name)
                kids = [c for c in folder.iterdir() if c.is_dir()] if folder.is_dir() else []
                sets.append({"set": name, "live": name == st["live"], "path": str(folder), "saves": len(kids),
                             "owner": name in st["owners"], "kept": name in kept})
        return {"dir": str(live) if live else "", "exists": bool(live and live.is_dir()), "on": st["on"],
                "owners": list(st["owners"]), "live": st["live"], "want": self.saves_set_of(self.state.get("active", "")),
                "sets": sets}

    def saves_swap_to(self, target: str) -> bool:
        """Make `target` the set in the live saves folder: the live folder is renamed to rest under its own set's
        name, and the target's folder takes its place. Nothing is copied or deleted. -> True if anything moved"""
        st = self._saves()
        live = self.saves_dir()
        cur = st["live"]
        if cur == target:
            return False
        if game_running():
            raise ValueError("Cyberpunk 2077 is running. Close the game first.")
        if live is None or not live.parent.is_dir():
            raise ValueError("I can't find the folder your saves are kept in. Set it in Tools → Saves per instance.")
        cur_dir, tgt_dir = self._saves_folder(live, cur), self._saves_folder(live, target)
        if cur_dir.exists():
            raise ValueError(f"“{cur_dir.name}” already exists next to your saves; I won't put anything on top of it.")
        moved_out = False
        try:
            if live.exists():
                os.rename(live, cur_dir)
                moved_out = True
            if tgt_dir.exists():
                os.rename(tgt_dir, live)
            else:
                live.mkdir()
        except OSError as e:
            if moved_out and not live.exists():
                try:
                    os.rename(cur_dir, live)
                except OSError:
                    pass
            raise ValueError(f"The saves folder couldn't be switched ({e}). Nothing was changed. "
                             "(Is the game, a cloud-sync program or a file window using it?)")
        st["live"] = target
        self.save()
        return True

    def saves_sync(self) -> bool:
        """Before the game starts: the live saves must be the set of the running instance."""
        st = self._saves()
        if not st["on"] or self.saves_dir() is None:
            return False
        return self.saves_swap_to(self.saves_set_of(self.state.get("active", "")))

    def saves_turn(self, on: bool):
        """Switch the feature on or off. Off: the shared saves are put back in the live folder first."""
        st = self._saves()
        if not on and st["on"] and st["live"] != SAVE_SHARED:
            self.saves_swap_to(SAVE_SHARED)
        st["on"] = bool(on)
        self.save()

    def saves_give(self, instance: str, copy: bool = False):
        """From now on `instance` has a set of saves of its own (it takes effect when the saves are next synced - at the
        next switch or play). copy=True: it starts with a copy of the saves that are in use now; otherwise it starts empty."""
        st = self._saves()
        live = self.saves_dir()
        if instance not in self.state["instances"]:
            raise ValueError("There is no such instance.")
        if instance in st["owners"]:
            return
        if live is None or not live.parent.is_dir():
            raise ValueError("I can't find the folder your saves are kept in. Set it in Tools → Saves per instance.")
        dest = self._saves_folder(live, instance)
        if copy and live.is_dir():
            if game_running():
                raise ValueError("Cyberpunk 2077 is running. Close the game first.")
            if dest.exists():
                raise ValueError(f"“{dest.name}” already exists next to your saves; I won't use it.")
            tmp = dest.with_name(dest.name + ".part")
            if tmp.exists():
                raise ValueError(f"A leftover folder next to your saves is in the way: {tmp.name}")
            shutil.copytree(live, tmp)
            os.rename(tmp, dest)
        st["owners"].append(instance)
        self.save()

    def saves_release(self, instance: str) -> str:
        """The instance goes back to the shared saves. Its own set is kept where it is (and comes back if it is given a
        set again). -> where that set is"""
        st = self._saves()
        live = self.saves_dir()
        if instance not in st["owners"]:
            return ""
        where = ""
        if live is not None:
            where = str(live if st["live"] == instance else self._saves_folder(live, instance))
        st["owners"].remove(instance)
        self.save()
        return where


class Manager(_CheckUp, _Round3):
    def __init__(self, game):
        self.game = Path(game)
        self.stash = self.game / STASH_NAME
        self.state = self._load()
        self.merged = []            # messages about copies that were found in both places and merged (see move_units)
        self._trail = []            # (rel, switched on?) for every unit move_units moved - read by take_trail()
        self._journal = None        # the History list, loaded when first needed
        self._jlock = threading.RLock()

    def _load(self) -> dict:
        try:
            state = json.loads((self.stash / STATE_NAME).read_text("utf-8"))
        except (OSError, ValueError):
            state = {}
        if not isinstance(state, dict):
            state = {}
        for k in ("overrides", "links", "installed", "nexus", "searches", "hashes", "cands", "instances",
                  "pins", "notes", "game", "bisect", "saves", "endorse"):
            if not isinstance(state.get(k), dict):
                state[k] = {}
        if not isinstance(state.get("good"), list):
            state["good"] = []
        if not isinstance(state.get("active"), str):
            state["active"] = ""
        state.setdefault("last_check", 0)
        return state

    def save(self):
        self.stash.mkdir(exist_ok=True)
        tmp = self.stash / (STATE_NAME + ".tmp")
        for attempt in range(4):                     # a background install may change the dict meanwhile
            try:
                data = json.dumps(self.state, separators=(",", ":"))
                break
            except RuntimeError:
                if attempt == 3:
                    raise
                time.sleep(0.05)
        tmp.write_text(data, "utf-8")
        os.replace(tmp, self.stash / STATE_NAME)

    def units(self) -> list:
        us = discover(self.game, True)
        if self.stash.is_dir():
            us += discover(self.stash, False)
        return us

    def scan(self, fuzzy: bool = True) -> list:
        mods = build_groups(self.units(), self.state["overrides"], self.state["links"],
                            fuzzy, self.state["nexus"])
        for m in mods:
            self._attach(m)
            self._attach_note(m)
        mods.sort(key=lambda m: m.name.lower())
        return mods

    def _attach(self, m: Mod):
        links = self.state["links"]
        ids = Counter(links[u.rel]["id"] for u in m.units if u.rel in links)
        tss = [u.ts for u in m.units if u.ts]
        m.install_ts = min(tss) if tss else 0.0
        if not ids:
            return
        mid = ids.most_common(1)[0][0]
        m.nexus_id = mid
        info = self.state["nexus"].get(str(mid))
        inst = self.state["installed"].get(str(mid)) or {}
        m.installed_version = inst.get("version", "")
        m.version_source = inst.get("source", "")
        if info and info.get("error"):
            m.nexus_error = "This page was not found on Nexus (removed or hidden?)."
            m.update = "unknown"
        elif info:
            m.nexus = info
            if info.get("name") and not m.key.startswith("o:"):
                m.name = info["name"]
            m.update, m.update_note = compute_update(m.installed_version, info, m.install_ts)
            pin = self.state["pins"].get(str(mid))
            if pin:
                mode = pin.get("mode")
                if mode == "stay" or (mode == "skip" and pin.get("version") == m.latest_version):
                    m.pinned = mode
                    if m.update in ("update", "maybe"):
                        m.update = "pinned"
                        m.update_note = (f"You chose to stay on this version (Nexus has {m.latest_version})."
                                         if mode == "stay" else f"You skipped version {m.latest_version}.")
        else:
            m.update = "unknown"

    # --- on/off ---------------------------------------------------------
    def set_enabled(self, mod: Mod, enable: bool):
        return self.move_units(mod.units, enable)

    def move_units(self, units, enable: bool):
        moved, errors = 0, []
        aside = None
        for u in units:
            if u.enabled == enable:
                continue
            src_root, dst_root = (self.stash, self.game) if enable else (self.game, self.stash)
            src, dst = src_root / u.rel, dst_root / u.rel
            try:
                if not src.exists():
                    raise FileNotFoundError("source is missing")
                if dst.exists() or dst.is_symlink():
                    # The same mod is in both places (an update or another mod put it back while the old copy
                    # was switched off). Nothing may be lost, so the two are merged, never overwritten.
                    if aside is None:
                        aside = self.stash / BACKUP_NAME / (time.strftime("%Y%m%d-%H%M%S") + "-two-copies")
                    count = {"same": 0, "newer": 0, "aside": 0}
                    self._merge_into(src, dst, aside / u.rel, count)
                    bits = []
                    if count["same"]:
                        bits.append(f"{count['same']} identical file(s) dropped")
                    if count["newer"] or count["aside"]:
                        bits.append(f"{count['newer'] + count['aside']} that differed: the newer one is used, the "
                                    f"other is kept in {STASH_NAME}/{BACKUP_NAME}")
                    self.merged.append(f"{u.rel}: found in both places, merged" + (" (" + "; ".join(bits) + ")" if bits else ""))
                else:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(src), str(dst))
                moved += 1
                if len(self._trail) < 50000:
                    self._trail.append((u.rel, enable))
            except OSError as e:
                errors.append(f"{u.rel}: {e}")
        if enable:
            self._prune_stash()
        return moved, errors

    def _merge_into(self, src: Path, dst: Path, aside: Path, count: dict):
        """Move `src` onto `dst`, which already exists. Folders are merged file by file; a file that is the same
        is simply dropped from `src`; one that differs is kept as the newer of the two, and the older goes to
        `aside` - so every version is still on disk afterwards."""
        def put_aside(p: Path):
            aside.parent.mkdir(parents=True, exist_ok=True)
            target = aside
            n = 1
            while target.exists():
                target = aside.with_name(f"{aside.name}.{n}")
                n += 1
            shutil.move(str(p), str(target))
        if not (dst.exists() or dst.is_symlink()):
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            return
        src_dir = src.is_dir() and not src.is_symlink()
        dst_dir = dst.is_dir() and not dst.is_symlink()
        if src_dir and dst_dir:
            for child in sorted(src.iterdir()):
                self._merge_into(child, dst / child.name, aside / child.name, count)
            try:
                src.rmdir()
            except OSError:
                pass
        elif src.is_file() and dst.is_file() and not src.is_symlink() and not dst.is_symlink():
            if same_file(src, dst):
                src.unlink()
                count["same"] += 1
            elif src.stat().st_mtime > dst.stat().st_mtime:      # the one being moved is newer: it replaces the other
                put_aside(dst)
                shutil.move(str(src), str(dst))
                count["newer"] += 1
            else:                                                  # the one already there is newer: keep it
                put_aside(src)
                count["aside"] += 1
        else:                                                      # a file against a folder: keep what is there
            put_aside(src)
            count["aside"] += 1

    def _prune_stash(self):
        if not self.stash.is_dir():
            return
        for dirpath, _dirs, _files in os.walk(self.stash, topdown=False):
            p = Path(dirpath)
            if p == self.stash:
                continue
            try:
                if not any(p.iterdir()):
                    p.rmdir()
            except OSError:
                pass

    # --- remembered grouping choices -------------------------------------
    def merge(self, mods: list, name: str):
        gid = uuid.uuid4().hex[:8]
        for m in mods:
            for u in m.units:
                self.state["overrides"][u.rel] = {"id": gid, "name": name}
        self.save()

    def split(self, mod: Mod):
        for u in mod.units:
            self.state["overrides"][u.rel] = {"id": uuid.uuid4().hex[:8], "name": u.pretty}
            self.state["links"].pop(u.rel, None)
        self.save()

    # --- Nexus links ------------------------------------------------------
    def link(self, mods: list, mod_id: int, version: str = ""):
        for m in mods:
            for u in m.units:
                self.state["links"][u.rel] = {"id": int(mod_id), "src": "manual"}
        if version:
            self.state["installed"][str(mod_id)] = {"version": version.strip(), "source": "you entered it"}
        self.save()

    def unlink(self, mods: list):
        for m in mods:
            for u in m.units:
                self.state["links"].pop(u.rel, None)
        self.save()

    def apply_auto_links(self, links: dict, installed: dict):
        for rel, l in links.items():
            cur = self.state["links"].get(rel)
            if cur and cur.get("src") == "manual":
                continue
            self.state["links"][rel] = l
        for mid, inst in installed.items():
            cur = self.state["installed"].get(str(mid))
            if cur and cur.get("source") == "you entered it":
                continue
            self.state["installed"][str(mid)] = inst

    # --- instances ------------------------------------------------------------
    # An instance is a named set of switched-on mods ("Story run", "Vanilla+", "Testing").
    # Nothing is copied: every mod's files stay in the game folder (on) or in _disabled_mods (off),
    # and switching instance simply moves the difference. That is the same idea as keeping all
    # mods somewhere else and putting back the ones an instance needs - minus the copying.
    def snapshot(self) -> dict:
        us = self.units()
        return {"on": sorted(u.rel for u in us if u.enabled), "off": sorted(u.rel for u in us if not u.enabled)}

    def ensure_instances(self):
        """The first time, the current setup becomes the instance 'Main'."""
        if not self.state["instances"]:
            self.state["instances"]["Main"] = dict(self.snapshot(), created=time.time())
            self.state["active"] = "Main"
            self.save()
        elif self.state["active"] not in self.state["instances"]:
            self.state["active"] = sorted(self.state["instances"])[0]

    def sync_active(self):
        """The running instance always mirrors what is switched on right now."""
        a = self.state["active"]
        if a in self.state["instances"]:
            snap = self.snapshot()
            cur = self.state["instances"][a]
            if cur.get("on") != snap["on"] or cur.get("off") != snap["off"]:
                cur.update(snap)
                self.save()

    def create_instance(self, name: str, mode: str = "current", source: str = "") -> str:
        """mode: current (what is on now) | frameworks (only the shared frameworks) | copy (of `source`)."""
        name = re.sub(r"\s+", " ", name or "").strip()[:40]
        if not name:
            raise ValueError("Give the instance a name.")
        if name.lower() in {n.lower() for n in self.state["instances"]}:
            raise ValueError(f"There is already an instance called “{name}”.")
        self.ensure_instances()
        if mode == "copy" and source in self.state["instances"]:
            inst = {k: list(v) for k, v in self.state["instances"][source].items() if k in ("on", "off")}
        elif mode == "frameworks":
            core = {u.rel for m in self.scan() for u in m.units if m.core}
            us = self.units()
            inst = {"on": sorted(u.rel for u in us if u.rel in core),
                    "off": sorted(u.rel for u in us if u.rel not in core)}
        else:
            self.sync_active()
            inst = self.snapshot()
        inst["created"] = time.time()
        self.state["instances"][name] = inst
        self.save()
        return name

    VANILLA, FRAMEWORKS = "Vanilla (no mods)", "Frameworks only"

    def all_off_instance(self, keep_frameworks: bool) -> str:
        """(Re)make the ready-made instance with every mod off - or every mod except the shared frameworks -
        and return its name. Switching to it is "All off"; the instance you were in keeps its mods."""
        self.ensure_instances()
        name = self.FRAMEWORKS if keep_frameworks else self.VANILLA
        core = {u.rel for m in self.scan() if m.core for u in m.units} if keep_frameworks else set()
        us = self.units()
        self.state["instances"][name] = {"on": sorted(u.rel for u in us if u.rel in core),
                                         "off": sorted(u.rel for u in us if u.rel not in core),
                                         "created": time.time()}
        self.save()
        return name

    def remember_return(self):
        """Before 'All off': note the instance to go back to (never one of the ready-made empty ones)."""
        a = self.state.get("active")
        if a in self.state["instances"] and a not in (self.VANILLA, self.FRAMEWORKS):
            self.state["return_to"] = a
            self.save()

    def return_target(self):
        """The instance 'All on' can take you back to, if you are in a ready-made empty one."""
        r = self.state.get("return_to")
        if self.state.get("active") in (self.VANILLA, self.FRAMEWORKS) and r in self.state["instances"]:
            return r
        return None

    def rename_instance(self, old: str, new: str):
        new = re.sub(r"\s+", " ", new or "").strip()[:40]
        if not new or old not in self.state["instances"]:
            raise ValueError("Give the instance a name.")
        if new != old and new.lower() in {n.lower() for n in self.state["instances"]}:
            raise ValueError(f"There is already an instance called “{new}”.")
        self.state["instances"][new] = self.state["instances"].pop(old)
        if self.state["active"] == old:
            self.state["active"] = new
        self.save()

    def delete_instance(self, name: str):
        if len(self.state["instances"]) <= 1:
            raise ValueError("You need at least one instance.")
        if name == self.state["active"]:
            raise ValueError("Switch to another instance first.")
        self.state["instances"].pop(name, None)
        self.save()

    def instance_plan(self, name: str) -> dict:
        """What switching to `name` would change. Mods the instance has never seen are switched off,
        except the shared frameworks, which are left as they are."""
        return self.plan_for(self.state["instances"][name], name)

    def plan_for(self, inst: dict, name: str = "") -> dict:
        """instance_plan for any {"on": [...], "off": [...]} set (an instance, or a 'this setup works' snapshot)."""
        on, off = set(inst.get("on", [])), set(inst.get("off", []))
        mods = self.scan()
        owner = {u.rel: m for m in mods for u in m.units}
        core = {u.rel for m in mods if m.core for u in m.units}
        enable, disable = [], []
        for u in self.units():
            if u.rel in on:
                want = True
            elif u.rel in off or u.rel not in core:
                want = False
            else:
                continue
            if want and not u.enabled:
                enable.append(u)
            elif not want and u.enabled:
                disable.append(u)
        names = lambda us: sorted({owner[u.rel].name for u in us if u.rel in owner}, key=str.lower)
        return {"name": name, "enable": enable, "disable": disable,
                "enable_mods": names(enable), "disable_mods": names(disable)}

    def switch_instance(self, name: str):
        """-> (units moved, errors)"""
        plan = self.instance_plan(name)
        before = self.state.get("active", "")
        swapped_from = None
        if self._saves()["on"] and self.saves_dir() is not None:      # this instance may have saves of its own
            was = self._saves()["live"]
            try:
                if self.saves_swap_to(self.saves_set_of(name)):
                    swapped_from = was
            except ValueError as e:
                return 0, [f"Saves: {e}"]
        self._trail.clear()
        moved, errors = self.apply_plan(plan)
        trail = self.take_trail()
        if errors and swapped_from is not None:
            try:
                self.saves_swap_to(swapped_from)
            except ValueError:
                pass
        if not errors:
            self.state["active"] = name
            self.sync_active()
            self.save()
        if trail["turned_on"] or trail["turned_off"] or before != name:
            self.journal_add("switch", f"Switched to “{name}”" + (f" (from “{before}”)" if before and before != name else ""),
                             active_before=before, active_after=name if not errors else before, **trail)
        return moved, errors

    def apply_plan(self, plan: dict):
        """Carry out a plan from plan_for / instance_plan: switch off first, then on. -> (moved, errors)"""
        moved, errors = 0, []
        for units, en in ((plan["disable"], False), (plan["enable"], True)):
            n, errs = self.move_units(units, en)
            moved += n
            errors += errs
        return moved, errors

    def take_trail(self) -> dict:
        """Everything move_units moved since the trail was last cleared -> {"turned_on": [rels], "turned_off": [rels]}"""
        trail, self._trail = self._trail, []
        return {"turned_on": [r for r, en in trail if en], "turned_off": [r for r, en in trail if not en]}

    def instances_after_install(self, old_rels, new_rels, gone_rels=()):
        """Keep every instance in step when a mod is updated or installed."""
        old, new, gone = set(old_rels), list(new_rels), set(gone_rels)
        for name, inst in self.state["instances"].items():
            on, off = set(inst.get("on", [])), set(inst.get("off", []))
            if old and (old & on):
                on |= set(new)
            elif old and (old & off):
                off |= set(new)
            elif name == self.state["active"]:
                on |= set(new)
            on -= gone
            off -= gone
            inst["on"], inst["off"] = sorted(on), sorted(off)

    # ======================================================================
    # History + undo, last known good, update pins, notes, compare, disk use
    # ======================================================================
    # --- history (the journal lives in its own file so the state file stays small) ----------------
    def _journal_load(self) -> list:
        if self._journal is None:
            try:
                data = json.loads((self.stash / JOURNAL_NAME).read_text("utf-8"))
            except (OSError, ValueError):
                data = []
            self._journal = [e for e in data if isinstance(e, dict) and e.get("id")] if isinstance(data, list) else []
        return self._journal

    def _journal_save(self):
        self.stash.mkdir(exist_ok=True)
        tmp = self.stash / (JOURNAL_NAME + ".tmp")
        tmp.write_text(json.dumps(self._journal, separators=(",", ":")), "utf-8")
        os.replace(tmp, self.stash / JOURNAL_NAME)

    def journal(self) -> list:
        """Everything remembered, newest first."""
        with self._jlock:
            return list(reversed(self._journal_load()))

    def journal_get(self, entry_id):
        with self._jlock:
            return next((e for e in self._journal_load() if e["id"] == entry_id), None)

    def journal_add(self, kind: str, text: str, **data) -> dict:
        with self._jlock:
            j = self._journal_load()
            e = {"id": uuid.uuid4().hex[:10], "ts": time.time(), "kind": kind, "text": text}
            e.update(data)
            j.append(e)
            while len(j) > JOURNAL_MAX:        # keep installs and updates longest: they are the ones with backups
                idx = next((i for i, x in enumerate(j[:-1]) if x.get("kind") not in ("install", "update")), 0)
                j.pop(idx)
            try:
                self._journal_save()
            except OSError:
                pass
            return e

    def begin_trail(self):
        self._trail.clear()

    def log_toggle(self, mods, enable: bool):
        """Call after switching `mods` on/off one by one (begin_trail() before) - one History line for the lot."""
        trail = self.take_trail()
        if not (trail["turned_on"] or trail["turned_off"]):
            return None
        names = sorted({m.name for m in mods}, key=str.lower)
        what = names[0] if len(names) == 1 else f"{len(names)} mods"
        return self.journal_add("toggle", f"Turned {'on' if enable else 'off'} {what}", mods=names[:12], **trail)

    UNDOABLE = ("install", "update", "toggle", "switch", "restore", "fix", "settings")

    def undo_check(self, e: dict) -> str:
        """'' when this change can be undone now, otherwise a sentence saying why not."""
        if e.get("undone"):
            return "Already undone."
        if e.get("kind") not in self.UNDOABLE:
            return "This line is only a note."
        if e["kind"] in ("install", "update"):
            j = self._journal_load()
            pos = next((i for i, x in enumerate(j) if x["id"] == e["id"]), len(j))
            mine = set(e.get("created", [])) | {o for o, _b in e.get("moves", [])}
            if not mine:
                return "Nothing to undo."
            for _orig, bak in e.get("moves", []):
                if not (self.game / bak).exists():
                    return "The saved copy of the old files is no longer there (old backups were cleaned up)."
            for x in j[pos + 1:]:
                if x["kind"] in ("install", "update") and not x.get("undone") and \
                        (set(x.get("created", [])) | {o for o, _b in x.get("moves", [])}) & mine:
                    return f"“{x['text']}” came later and changed the same files - undo that one first."
        elif e["kind"] == "settings":
            if not (e.get("abs_moves") or e.get("abs_created")):
                return "That change moved no files."
            for _orig, held in e.get("abs_moves", []):
                if not Path(held).exists():
                    return "The saved copy of the old settings is no longer there (old backups were cleaned up)."
        elif e["kind"] == "fix":
            if not e.get("moves"):
                return "That change moved no files."
            for orig, new in e["moves"]:
                if not (self.game / new).exists():
                    return "The moved file is no longer where it was put."
                if (self.game / orig).exists():
                    return f"Something is already at {orig}."
        elif not (e.get("turned_on") or e.get("turned_off")):
            return "That change moved no files."
        return ""

    def undo(self, entry_id: str) -> dict:
        """Go back to how things were before that change. Nothing is deleted: files taken away go to
        _disabled_mods/_backup/…-undo-…  -> {"ok", "text", "errors"}"""
        with self._jlock:
            e = self.journal_get(entry_id)
            if not e:
                return {"ok": False, "text": "That entry is gone.", "errors": []}
            why = self.undo_check(e)
            if why:
                return {"ok": False, "text": why, "errors": []}
            if e["kind"] in ("install", "update"):
                errors = self._undo_install(e)
            elif e["kind"] == "fix":
                errors = self._undo_fix(e)
            elif e["kind"] == "settings":
                errors = self._undo_settings(e)
            else:
                errors = self._undo_moves(e)
            if errors:
                return {"ok": False, "text": "Some files couldn't be moved back.", "errors": errors}
            e["undone"] = True
            self.journal_add("undo", f"Undid: {e['text']}", of=e["id"])
            return {"ok": True, "text": f"Undid: {e['text']}", "errors": []}

    def _undo_moves(self, e: dict) -> list:
        now = {u.rel: u for u in self.units()}
        back_off = [now[r] for r in e.get("turned_on", []) if r in now and now[r].enabled]
        back_on = [now[r] for r in e.get("turned_off", []) if r in now and not now[r].enabled]
        errors = []
        for units, en in ((back_off, False), (back_on, True)):
            _n, errs = self.move_units(units, en)
            errors += errs
        self._trail.clear()
        if e.get("active_before") in self.state["instances"]:
            self.state["active"] = e["active_before"]
        self.sync_active()
        self.save()
        return errors

    def _undo_install(self, e: dict) -> list:
        game = self.game
        aside = self.stash / BACKUP_NAME / (time.strftime("%Y%m%d-%H%M%S") + "-undo-" +
                                            clean_folder_name(e.get("mod") or "mod")[:24])
        errors = []
        for rel in e.get("created", []):                         # the new files go aside, they are not deleted
            for root, tag in ((game, ""), (self.stash, "switched-off/")):
                p = root / rel
                try:
                    if p.is_file() or p.is_symlink():
                        dst = aside / "removed" / (tag + rel)
                        dst.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(p), str(dst))
                except OSError as ex:
                    errors.append(f"{rel}: {ex}")
        for orig, bak in e.get("moves", []):                     # the old ones come back
            src, dst = game / bak, game / orig
            try:
                if dst.exists() or dst.is_symlink():
                    keep = aside / "in the way" / orig
                    keep.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(dst), str(keep))
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src), str(dst))
            except OSError as ex:
                errors.append(f"{orig}: {ex}")
        for d in sorted(e.get("made_dirs", []), key=len, reverse=True):      # folders the install created
            try:
                (game / d).rmdir()
            except OSError:
                pass
        if errors:
            return errors
        links = self.state["links"]
        for rel, l in (e.get("prev_links") or {}).items():
            if l:
                links[rel] = l
            else:
                links.pop(rel, None)
        mid = e.get("mod_id")
        if mid:
            if e.get("prev_installed"):
                self.state["installed"][str(mid)] = e["prev_installed"]
            else:
                self.state["installed"].pop(str(mid), None)
        affected = set(e.get("prev_links") or {})
        for name, inst in self.state["instances"].items():
            prev = (e.get("prev_inst") or {}).get(name) or {}
            on = (set(inst.get("on", [])) - affected) | set(prev.get("on", []))
            off = (set(inst.get("off", [])) - affected) | set(prev.get("off", []))
            inst["on"], inst["off"] = sorted(on), sorted(off)
        if e.get("was_enabled") is False:                         # the mod was switched off before: it stays off
            old = set(e.get("old_rels", []))
            self.move_units([u for u in self.units() if u.rel in old and u.enabled], False)
        self._trail.clear()
        self._prune_stash()
        self.sync_active()
        self.save()
        return []

    def capture_before_install(self, rels, mod_id) -> dict:
        """What the install is about to change in the state, so that Undo can put it back."""
        rels = set(rels)
        inst = self.state["installed"].get(str(mod_id)) if mod_id else None
        return {"prev_links": {r: (dict(self.state["links"][r]) if r in self.state["links"] else None) for r in rels},
                "prev_installed": dict(inst) if isinstance(inst, dict) else None,
                "prev_inst": {n: {"on": sorted(set(i.get("on", [])) & rels), "off": sorted(set(i.get("off", [])) & rels)}
                              for n, i in self.state["instances"].items()}}

    # --- last known good ----------------------------------------------------------------------------
    def good_save(self, note: str = "") -> dict:
        """'This setup works': remember which mods are on (and which versions are installed)."""
        self.ensure_instances()
        self.sync_active()
        snap = self.snapshot()
        on_mods = [m for m in self.scan() if m.status != "off"]
        rec = {"id": uuid.uuid4().hex[:8], "ts": time.time(), "note": (note or "").strip()[:80],
               "active": self.state.get("active", ""), "on": snap["on"], "off": snap["off"], "mods_on": len(on_mods),
               "versions": {k: v.get("version", "") for k, v in self.state["installed"].items() if isinstance(v, dict)}}
        self.state["good"].insert(0, rec)
        del self.state["good"][GOOD_KEEP:]
        self.save()
        self.journal_add("good", f"Marked this setup as working ({len(on_mods)} mod{'s' if len(on_mods) != 1 else ''} on)",
                         good_id=rec["id"])
        return rec

    def good_get(self, good_id=None):
        goods = self.state["good"]
        if good_id is None:
            return goods[0] if goods else None
        return next((g for g in goods if g.get("id") == good_id), None)

    def good_delete(self, good_id):
        self.state["good"] = [g for g in self.state["good"] if g.get("id") != good_id]
        self.save()

    def good_changes(self, rec: dict) -> dict:
        """What going back to `rec` would do: the plan (mods to switch on/off) and the updates made since."""
        plan = self.plan_for(rec, "Last known good")
        versions = []
        for mid, then in (rec.get("versions") or {}).items():
            now = (self.state["installed"].get(mid) or {}).get("version", "")
            if now != then:
                versions.append({"mod_id": mid, "name": (self.state["nexus"].get(mid) or {}).get("name") or f"mod {mid}",
                                 "then": then, "now": now})
        ups = [e for e in self._journal_load() if e["kind"] == "update" and e["ts"] > rec["ts"] and not e.get("undone")]
        plan.update(rec=rec, versions=versions, updates=list(reversed(ups)))
        return plan

    def good_restore(self, good_id=None, undo_updates: bool = True) -> dict:
        """Put the mods back the way they were when the setup was marked as working. Updates made since are
        undone too (newest first) when `undo_updates` and their backups are still there."""
        rec = self.good_get(good_id)
        if not rec:
            raise ValueError("Nothing is marked as working yet.")
        undone, skipped = [], []
        if undo_updates:
            ups = [e for e in reversed(self._journal_load())
                   if e["kind"] == "update" and e["ts"] > rec["ts"] and not e.get("undone")]
            for e in ups:
                r = self.undo(e["id"])
                (undone if r["ok"] else skipped).append(e["text"] if r["ok"] else f"{e['text']} - {r['text']}")
        before = self.state.get("active", "")
        plan = self.plan_for(rec, "Last known good")
        self._trail.clear()
        moved, errors = self.apply_plan(plan)
        trail = self.take_trail()
        self.sync_active()
        self.save()
        self.journal_add("restore", "Went back to the setup marked as working", good_id=rec["id"],
                         active_before=before, active_after=before, **trail)
        return {"moved": moved, "errors": errors, "undone": undone, "skipped": skipped, "plan": plan}

    # --- pin or skip an update ----------------------------------------------------------------------------
    def pin(self, mod: Mod, mode: str):
        """mode: 'stay' (never offer updates for this mod) | 'skip' (hide only the version Nexus has now)."""
        if mode not in ("stay", "skip"):
            raise ValueError("mode must be 'stay' or 'skip'")
        if not mod.nexus_id:
            raise ValueError("Link the mod to its Nexus page first.")
        self.state["pins"][str(mod.nexus_id)] = {"mode": mode, "version": mod.latest_version,
                                                 "ts": time.time(), "name": mod.name}
        self.save()

    def unpin(self, mod: Mod):
        self.state["pins"].pop(str(mod.nexus_id), None)
        self.save()

    # --- notes, tags and colours ----------------------------------------------------------------------------
    def note_key(self, m: Mod) -> str:
        return f"n{m.nexus_id}" if m.nexus_id else "u:" + min((u.rel for u in m.units), default="")

    def _attach_note(self, m: Mod):
        n = self.state["notes"].get(self.note_key(m))
        if isinstance(n, dict):
            m.note = str(n.get("note") or "")
            m.tags = [str(t) for t in (n.get("tags") or []) if t]
            m.color = n.get("color") if n.get("color") in NOTE_COLORS else ""

    def set_note(self, mods, note=None, tags=None, color=None):
        """Change what you wrote about one or several mods. None = leave as it is; ''/[] = clear."""
        if isinstance(mods, Mod):
            mods = [mods]
        for m in mods:
            key = self.note_key(m)
            cur = dict(self.state["notes"].get(key) or {})
            if note is not None:
                cur["note"] = str(note).strip()[:2000]
            if tags is not None:
                clean = []
                for t in tags:
                    t = re.sub(r"\s+", " ", str(t)).strip()[:24]
                    if t and t.lower() not in {x.lower() for x in clean}:
                        clean.append(t)
                cur["tags"] = clean[:8]
            if color is not None:
                cur["color"] = color if color in NOTE_COLORS else ""
            if cur.get("note") or cur.get("tags") or cur.get("color"):
                self.state["notes"][key] = cur
            else:
                self.state["notes"].pop(key, None)
        self.save()

    # --- compare two instances -------------------------------------------------------------------------------
    def compare_instances(self, a: str, b: str) -> dict:
        """Which mods are on in one instance and not in the other.
        -> {"a", "b", "only_a": [names], "only_b": [names], "differ": [names], "same_on": n, "same_off": n}"""
        self.ensure_instances()
        self.sync_active()
        for n in (a, b):
            if n not in self.state["instances"]:
                raise ValueError(f"There is no instance called “{n}”.")
        mods = self.scan()
        core = {u.rel for m in mods if m.core for u in m.units}

        def mod_state(inst: dict, m: Mod):
            on, off = set(inst.get("on", [])), set(inst.get("off", []))
            seen = []
            for u in m.units:
                if u.rel in on:
                    seen.append(True)
                elif u.rel in off or u.rel not in core:
                    seen.append(False)
            if not seen:
                return None
            return "on" if all(seen) else ("off" if not any(seen) else "mixed")
        ia, ib = self.state["instances"][a], self.state["instances"][b]
        out = {"a": a, "b": b, "only_a": [], "only_b": [], "differ": [], "same_on": 0, "same_off": 0}
        for m in mods:
            sa, sb = mod_state(ia, m), mod_state(ib, m)
            if sa is None or sb is None or sa == sb:
                if sa == sb == "on":
                    out["same_on"] += 1
                elif sa == sb == "off":
                    out["same_off"] += 1
                continue
            if sb == "off":
                out["only_a"].append(m.name)
            elif sa == "off":
                out["only_b"].append(m.name)
            else:
                out["differ"].append(m.name)
        for k in ("only_a", "only_b", "differ"):
            out[k].sort(key=str.lower)
        return out

    # --- disk use and moving the switched-off mods to another drive ------------------------------------
    def disk_usage(self) -> dict:
        rows = []
        for m in self.scan():
            on = off = 0
            for u in m.units:
                size = path_size((self.game if u.enabled else self.stash) / u.rel)
                if u.enabled:
                    on += size
                else:
                    off += size
            rows.append({"key": m.key, "name": m.name, "status": m.status, "on": on, "off": off, "total": on + off})
        rows.sort(key=lambda r: (-r["total"], r["name"].lower()))
        free = 0
        try:
            free = shutil.disk_usage(self.game).free
        except OSError:
            pass
        return {"rows": rows, "mods_total": sum(r["total"] for r in rows),
                "stash_total": path_size(self.stash), "backups": path_size(self.stash / BACKUP_NAME),
                "downloads": path_size(self.stash / DOWNLOADS_NAME), "free": free,
                "stash_link": os.path.realpath(self.stash) if is_link_dir(self.stash) else ""}

    def backup_folders(self) -> list:
        """The backup folders (every install and every undo makes one), oldest first."""
        out = []
        root = self.stash / BACKUP_NAME
        if root.is_dir():
            for d in sorted(root.iterdir()):
                if d.is_dir():
                    out.append({"path": d, "name": d.name, "size": path_size(d), "ts": d.stat().st_mtime})
        return sorted(out, key=lambda x: x["ts"])

    def prune_backups(self, days: int) -> tuple:
        """Delete backup folders older than `days` days (they only matter for Undo). -> (folders, bytes freed)"""
        cutoff = time.time() - days * 86400
        n = freed = 0
        for b in self.backup_folders():
            if b["ts"] < cutoff and _inside(self.stash / BACKUP_NAME, b["path"]):
                shutil.rmtree(b["path"], ignore_errors=True)
                n += 1
                freed += b["size"]
        return n, freed

    def move_stash(self, dest_parent, progress=None) -> str:
        """Move the folder with the switched-off mods to another drive and leave a link behind, so everything
        (instances, switching, History) works unchanged. -> the new location."""
        progress = progress or (lambda *a: None)
        dest_parent = Path(dest_parent)
        if game_running():
            raise ValueError("Cyberpunk 2077 is running. Close the game first.")
        if not dest_parent.is_dir():
            raise ValueError("Pick a folder that exists.")
        if is_link_dir(self.stash):
            raise ValueError("The switched-off mods are already on another drive. Move them back first.")
        self.stash.mkdir(exist_ok=True)
        target = dest_parent / (STASH_NAME + "_" + clean_folder_name(self.game.name)[:30])
        if _inside(self.stash, target) or _inside(self.game, target):
            raise ValueError("Pick a folder outside the game folder.")
        if target.exists() and any(target.iterdir()):
            raise ValueError(f"“{target}” already has files in it. Pick another folder.")
        size = path_size(self.stash)
        try:
            if shutil.disk_usage(dest_parent).free < size * 1.05 + (50 << 20):
                raise ValueError("There isn't enough free space in that folder's drive.")
        except OSError as ex:
            raise ValueError(f"Can't use that folder: {ex}")
        try:
            copy_tree_checked(self.stash, target, progress)
        except OSError as ex:                                   # nothing has changed in the game folder yet
            shutil.rmtree(target, ignore_errors=True)
            raise ValueError(f"The copy didn't work, so nothing was moved: {ex}")
        old = self.game / (STASH_NAME + ".moving")
        try:
            os.replace(self.stash, old)
        except OSError as ex:
            shutil.rmtree(target, ignore_errors=True)
            raise ValueError(f"The folder couldn't be taken out of the game folder (is something using it?): {ex}")
        try:
            make_dir_link(self.stash, target)
        except OSError as ex:
            os.replace(old, self.stash)
            shutil.rmtree(target, ignore_errors=True)
            raise ValueError(f"Windows wouldn't create the link, so nothing was moved: {ex}")
        shutil.rmtree(old, ignore_errors=True)
        return str(target)

    def unmove_stash(self, progress=None) -> str:
        """Bring the switched-off mods back into the game folder. -> the folder."""
        progress = progress or (lambda *a: None)
        if game_running():
            raise ValueError("Cyberpunk 2077 is running. Close the game first.")
        if not is_link_dir(self.stash):
            raise ValueError("The switched-off mods are already inside the game folder.")
        target = Path(os.path.realpath(self.stash))
        try:
            if shutil.disk_usage(self.game).free < path_size(target) * 1.05 + (50 << 20):
                raise ValueError("There isn't enough free space on the game's drive.")
        except OSError as ex:
            raise ValueError(f"Can't check the free space: {ex}")
        back = self.game / (STASH_NAME + ".back")
        shutil.rmtree(back, ignore_errors=True)
        try:
            copy_tree_checked(target, back, progress)
        except OSError as ex:
            shutil.rmtree(back, ignore_errors=True)
            raise ValueError(f"The copy didn't work, so nothing was moved: {ex}")
        try:
            if self.stash.is_symlink():
                os.unlink(self.stash)
            else:
                os.rmdir(self.stash)                     # a Windows junction
            os.replace(back, self.stash)
        except OSError as ex:
            shutil.rmtree(back, ignore_errors=True)
            raise ValueError(f"The link couldn't be replaced, so nothing was moved: {ex}")
        shutil.rmtree(target, ignore_errors=True)
        return str(self.stash)


# --------------------------------------------------------------------------
# Suggested merges
# --------------------------------------------------------------------------
STOP_TOKENS = {
    "mod", "mods", "pack", "patch", "fix", "the", "and", "for", "of", "cyberpunk", "cet",
    "reds", "redscript", "archive", "menu", "settings", "ui", "extra", "extras", "plus",
    "lite", "addon", "compat", "compatibility", "v2", "v1",
}


def _name_score(a: list, b: list):
    if not a or not b:
        return 0, ""
    p = 0
    for x, y in zip(a, b):
        if x != y:
            break
        p += 1
    sa, sb = set(a), set(b)
    common = {t for t in sa & sb if t not in STOP_TOKENS and len(t) >= 3}
    if p >= 2 and common:
        return 3, "names share '" + " ".join(a[:p]) + "'"
    if min(len(sa), len(sb)) >= 2 and (sa <= sb or sb <= sa) and common:
        return 3, "one name contains the other"
    long_common = sorted((t for t in common if len(t) >= 6), key=len, reverse=True)
    if long_common:
        return 2, "both mention '" + long_common[0] + "'"
    return 0, ""


def _min_gap(a: list, b: list) -> float:
    i = j = 0
    best = float("inf")
    while i < len(a) and j < len(b):
        best = min(best, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return best


def suggest_merges(mods: list, limit: int = 80) -> list:
    """Pairs of mods whose names look related AND whose files were installed
    around the same time. Returns [{'a','b','score','why'}]."""
    info = []
    for m in mods:
        if m.core:
            continue
        toks = name_tokens(m.local_name)
        ts = sorted(u.ts for u in m.units if u.ts)
        info.append((m, toks, ts))
    out = []
    for i in range(len(info)):
        ma, ta, tsa = info[i]
        for j in range(i + 1, len(info)):
            mb, tb, tsb = info[j]
            if ma.nexus_id and mb.nexus_id and ma.nexus_id != mb.nexus_id:
                continue
            ns, nwhy = _name_score(ta, tb)
            if not ns or not tsa or not tsb:
                continue
            gap = _min_gap(tsa, tsb)
            tscore = 3 if gap <= 120 else 1 if gap <= 1800 else 0
            if (ns >= 3 and tscore >= 1) or (ns >= 2 and tscore >= 3):
                when = ("at the same time" if gap < 5 else
                        f"{int(gap)} s apart" if gap < 120 else f"{int(gap // 60)} min apart")
                out.append({"a": ma, "b": mb, "score": ns + tscore,
                            "why": f"{nwhy}; installed {when}"})
    out.sort(key=lambda s: -s["score"])
    return out[:limit]


# --------------------------------------------------------------------------
# Game folder detection
# --------------------------------------------------------------------------
def is_game_dir(p) -> bool:
    return (Path(p) / GAME_EXE).exists()


def find_game_dirs() -> list:
    cands = []
    if os.name == "nt":
        drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
        suffixes = [
            r"Program Files (x86)\Steam\steamapps\common\Cyberpunk 2077",
            r"Program Files\Steam\steamapps\common\Cyberpunk 2077",
            r"SteamLibrary\steamapps\common\Cyberpunk 2077",
            r"Steam\steamapps\common\Cyberpunk 2077",
            r"GOG Games\Cyberpunk 2077",
            r"Program Files (x86)\GOG Galaxy\Games\Cyberpunk 2077",
            r"Program Files\Epic Games\Cyberpunk2077",
            r"Games\Cyberpunk 2077",
        ]
        for d in drives:
            for s in suffixes:
                cands.append(Path(d) / s)
        vdf = Path(r"C:\Program Files (x86)\Steam\steamapps\libraryfolders.vdf")
        try:
            for lib in re.findall(r'"path"\s+"([^"]+)"', vdf.read_text("utf-8", "ignore")):
                cands.append(Path(lib.replace("\\\\", "\\")) / "steamapps" / "common" / "Cyberpunk 2077")
        except OSError:
            pass
    seen, found = set(), []
    for c in cands:
        if str(c) not in seen and is_game_dir(c):
            seen.add(str(c))
            found.append(c)
    return found


def game_running() -> bool:
    if os.name != "nt":
        return False
    try:
        out = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq Cyberpunk2077.exe", "/NH"],
            capture_output=True, text=True, creationflags=NO_WINDOW).stdout
        return "cyberpunk2077.exe" in out.lower()
    except Exception:
        return False


# ---- starting the game ------------------------------------------------------------------------------------
STEAM_APPID = "1091500"
LAUNCH_METHODS = (("auto", "Automatic (Steam if the game is in Steam's folder)"),
                  ("exe", "Start the game program directly"),
                  ("steam", "Through Steam"))


class LaunchError(Exception):
    pass


def launch_plan(game_dir, method: str = "auto", args: str = "") -> dict:
    exe = Path(game_dir) / GAME_EXE
    if not exe.exists():
        raise LaunchError("Cyberpunk2077.exe isn't in the game folder. Pick the folder again with Tools → “Game folder…”.")
    flags = [a for a in str(args or "").split() if a][:12]
    in_steam = "steamapps" in {p.lower() for p in Path(game_dir).parts}
    via = "steam" if method == "steam" or (method == "auto" and in_steam) else "exe"
    plan = {"exe": exe, "args": flags, "via": via}
    if via == "steam":
        plan["url"] = f"steam://run/{STEAM_APPID}" + (f"//{urllib.parse.quote(' '.join(flags), safe='-_.')}/" if flags else "")
    return plan


def open_external(url: str):
    if os.name == "nt":
        os.startfile(url)                          # noqa - Windows only; hands the steam:// link to Steam
    elif not webbrowser.open(url):
        raise OSError("nothing handles that link")


def launch_game(game_dir, method: str = "auto", args: str = "", opener=None, spawn=None) -> str:
    """Start Cyberpunk 2077 and return a sentence for the status bar. Raises LaunchError."""
    plan = launch_plan(game_dir, method, args)
    if plan["via"] == "steam":
        try:
            (opener or open_external)(plan["url"])
            return "Starting Cyberpunk 2077 through Steam…"
        except Exception:                          # noqa - Steam isn't installed here: start the program itself
            pass
    kw = {"cwd": str(plan["exe"].parent), "env": scrub_frozen_env(dict(os.environ)), "close_fds": True}
    if os.name == "nt":
        kw["creationflags"] = 0x00000008 | 0x00000200            # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    else:
        kw["start_new_session"] = True
    try:
        (spawn or subprocess.Popen)([str(plan["exe"])] + plan["args"], **kw)
    except OSError as e:
        raise LaunchError(f"Windows wouldn't start the game: {e}")
    return "Starting Cyberpunk 2077…"


# ---- desktop shortcuts: "Play - Story run" -----------------------------------------------------------------
def safe_filename(text: str) -> str:
    return re.sub(r'[\\/:*?"<>|\x00-\x1f]+', "_", text or "").strip(" .")[:60] or "Play"


def self_command() -> list:
    """The command that starts this program: the exe when it is the packaged one, else pythonw + this file."""
    if getattr(sys, "frozen", False):
        return [sys.executable]
    exe = Path(sys.executable)
    pyw = exe.with_name("pythonw.exe")
    return [str(pyw if pyw.exists() else exe), str(Path(__file__).resolve())]


def shortcut_command(game, instance: str) -> list:
    return self_command() + ["--game", str(game), "--play"] + ([instance] if instance else [])


def desktop_dir() -> Path:
    if os.name == "nt":
        try:
            r = subprocess.run(["powershell", "-NoProfile", "-NonInteractive", "-Command",
                                "[Environment]::GetFolderPath('Desktop')"], capture_output=True, text=True,
                               timeout=15, creationflags=NO_WINDOW)
            p = Path(r.stdout.strip())
            if r.stdout.strip() and p.is_dir():
                return p
        except Exception:                                    # noqa - fall back to the plain folder name
            pass
    d = Path.home() / "Desktop"
    return d if d.is_dir() else Path.home()


def make_shortcut(game, instance: str, folder=None, runner=None, windows=None) -> Path:
    """Put "Play - <instance>" on the desktop (or in `folder`). Double-clicking it switches to that instance
    and starts the game, without opening the manager. An empty `instance` starts the game as it is."""
    windows = (os.name == "nt") if windows is None else windows
    folder = Path(folder) if folder else desktop_dir()
    folder.mkdir(parents=True, exist_ok=True)
    label = f"Play - {instance}" if instance else "Play Cyberpunk 2077"
    cmd = shortcut_command(game, instance)
    icon = Path(game) / GAME_EXE
    if windows:
        path = folder / (safe_filename(label) + ".lnk")
        script = ("$s=(New-Object -ComObject WScript.Shell).CreateShortcut($env:MS_LNK);"
                  "$s.TargetPath=$env:MS_EXE;$s.Arguments=$env:MS_ARGS;$s.WorkingDirectory=$env:MS_DIR;"
                  "$s.IconLocation=$env:MS_ICON;$s.Description=$env:MS_DESC;$s.Save()")
        env = dict(os.environ, MS_LNK=str(path), MS_EXE=cmd[0], MS_ARGS=subprocess.list2cmdline(cmd[1:]),
                   MS_DIR=str(Path(game) / "bin" / "x64"), MS_ICON=f"{icon},0",
                   MS_DESC=f"{APP_NAME}: {label}")
        r = (runner or subprocess.run)(["powershell", "-NoProfile", "-NonInteractive", "-Command", script], env=env,
                                       capture_output=True, text=True, timeout=30, creationflags=NO_WINDOW)
        if r.returncode != 0 or not path.exists():
            raise OSError((r.stdout + r.stderr).strip()[:300] or "Windows couldn't create the shortcut")
    else:
        path = folder / (safe_filename(label) + ".desktop")
        path.write_text("[Desktop Entry]\nType=Application\nName=" + label + "\nExec=" + shlex.join(cmd) +
                        "\nTerminal=false\nIcon=" + str(icon) + "\n", "utf-8")
        path.chmod(0o755)
    return path


def play_headless(game, instance: str, cfg: dict = None, progress=None, launcher=None):
    """Switch to `instance` (if given) and start the game - with no window. -> (ok, sentence)"""
    cfg = cfg if cfg is not None else load_config()
    if not game or not is_game_dir(game):
        return False, "I can't find the game folder. Open the manager once and pick it with Tools → “Game folder…”."
    if game_running():
        return False, "Cyberpunk 2077 is already running."
    note = ""
    if instance:
        mgr = Manager(game)
        mgr.ensure_instances()
        mgr.sync_active()
        target = {n.lower(): n for n in mgr.state["instances"]}.get(instance.lower())
        if not target:
            return False, (f"There is no instance called “{instance}” (it may have been renamed). You have: "
                           + ", ".join(sorted(mgr.state["instances"], key=str.lower)))
        if target != mgr.state["active"]:
            plan = mgr.instance_plan(target)
            if progress:
                progress(f"Getting “{target}” ready…")
            _moved, errs = mgr.switch_instance(target)
            if errs:
                return False, f"Couldn't switch to “{target}”, so the game was not started: {errs[0]}"
            note = f"“{target}”: {len(plan['enable_mods'])} mod(s) on, {len(plan['disable_mods'])} off. "
    try:
        Manager(game).saves_sync()                       # no-op unless "saves per instance" is switched on
    except ValueError as e:
        return False, f"Your saves couldn't be set up for this instance, so the game was not started: {e}"
    try:
        msg = (launcher or launch_game)(game, cfg.get("launch_method", "auto"), cfg.get("launch_args", ""))
    except LaunchError as e:
        return False, str(e)
    return True, note + msg


def play_cli(args) -> int:
    """`--play NAME`: what a desktop shortcut runs."""
    cfg = load_config()
    game = args.game or load_saved_game() or (find_game_dirs() or [None])[0]
    name = (args.play or "").strip()
    if _tell_running({"play": name}):                       # the manager is open: it does this itself, with its window
        return 0
    result = {}

    def work(progress=None):
        result["r"] = play_headless(game, name, cfg, progress)
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
    except Exception:                                       # noqa - no window possible: plain text
        work()
        ok, msg = result["r"]
        print(msg)
        return 0 if ok else 1
    root.withdraw()
    root.title(APP_NAME)
    root.configure(bg=THEME["bg"])
    label = tk.Label(root, text="Getting your mods ready…", bg=THEME["bg"], fg=THEME["fg"], padx=36, pady=26)
    label.pack()
    shown = {"v": False}
    t = threading.Thread(target=lambda: work(lambda text: result.update(text=text)), daemon=True)
    t.start()
    ticks = {"n": 0}

    def poll():
        ticks["n"] += 1
        if t.is_alive():
            if ticks["n"] >= 7 and not shown["v"]:           # only show a window if it takes a moment
                shown["v"] = True
                root.deiconify()
                root.attributes("-topmost", True)
            if result.get("text"):
                label.configure(text=result["text"])
            root.after(100, poll)
            return
        ok, msg = result.get("r") or (False, "Something went wrong.")
        if not ok:
            root.deiconify()
            messagebox.showerror(APP_NAME, msg)
        root.destroy()
    root.after(100, poll)
    root.mainloop()
    return 0 if (result.get("r") or (False,))[0] else 1


# --------------------------------------------------------------------------
# Installing, updating and downloading mods
# --------------------------------------------------------------------------
class InstallError(Exception):
    pass


GAME_ROOTS = {"archive", "bin", "r6", "red4ext", "engine", "mods"}
DOC_EXTS = {".txt", ".md", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".url", ".rtf",
            ".html", ".htm", ".docx", ".nfo"}
RESERVED_NAMES = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
MAX_UNPACKED = 8 << 30
MAX_ENTRIES = 30000
BACKUP_NAME = "_backup"
DOWNLOADS_NAME = "_downloads"
TMP_NAME = "_tmp"


def safe_parts(epath: str):
    """Path parts of an archive entry, or None if the entry could escape the game folder."""
    raw = epath.replace("\\", "/")
    if raw.startswith("/") or re.match(r"^[A-Za-z]:", raw):
        return None
    parts = [p for p in raw.split("/") if p not in ("", ".")]
    for p in parts:
        if p == ".." or ":" in p or "\x00" in p or p.endswith((" ", ".")) \
                or p.split(".")[0].upper() in RESERVED_NAMES:
            return None
    return parts or None


def clean_folder_name(text: str) -> str:
    t = re.sub(r'[\\/:*?"<>|\x00-\x1f]+', " ", text or "").strip(" .")
    return re.sub(r"\s+", " ", t)[:60] or "Mod"


def plan_layout(entries, fallback: str = "Mod"):
    """Where does every file of a mod archive go in the game folder?
    entries: [(path inside the archive, size)]  ->  ({entry path: destination relative to the game}, skipped)
    Mod authors zip the game's own folder layout (archive/pc/mod/…, bin/x64/…, r6/…, red4ext/…), often
    inside a wrapper folder. Loose files with no layout are placed by type. Anything unsafe stops the install."""
    mapped, loose, skipped = {}, [], []
    for epath, _size in entries:
        parts = safe_parts(epath)
        if parts is None:
            raise InstallError(f"This archive contains an unsafe path ({epath!r}); nothing was installed.")
        low = [p.lower() for p in parts]
        dest = None
        for i in range(min(4, len(parts) - 1)):
            if low[i] in GAME_ROOTS and (low[i] != "bin" or (i + 1 < len(low) and low[i + 1] == "x64")):
                dest = "/".join(parts[i:])
                break
        if dest:
            mapped[epath] = dest
        elif os.path.splitext(parts[-1])[1].lower() in DOC_EXTS:
            skipped.append(epath)
        else:
            loose.append((epath, parts))
    if loose and not mapped:
        folder = clean_folder_name(fallback)
        exts = {os.path.splitext(p[-1])[1].lower() for _e, p in loose}
        inits = sorted((p for _e, p in loose if p[-1].lower() == "init.lua"), key=len)
        if inits:                                                   # a Cyber Engine Tweaks mod
            top = inits[0][:-1]
            base = "bin/x64/plugins/cyber_engine_tweaks/mods/"
            for e, p in loose:
                if not top:
                    mapped[e] = base + folder + "/" + "/".join(p)
                elif p[:len(top)] == top:
                    mapped[e] = base + top[-1] + "/" + "/".join(p[len(top):])
                else:
                    skipped.append(e)
        elif exts <= {".archive", ".xl"}:
            for e, p in loose:
                mapped[e] = "archive/pc/mod/" + p[-1]
        elif ".reds" in exts:
            for e, p in loose:
                mapped[e] = "r6/scripts/" + folder + "/" + p[-1]
        elif exts <= {".dll", ".asi"}:
            for e, p in loose:
                mapped[e] = "bin/x64/plugins/" + p[-1]
        else:
            names = ", ".join(sorted(p[-1] for _e, p in loose)[:4])
            raise InstallError("I can't tell where these files belong in the game folder "
                               f"({names}…). Install this one by hand.")
    elif loose:
        skipped += [e for e, _p in loose]
    if not mapped:
        raise InstallError("There is nothing to install in this archive (no game files found).")
    return mapped, skipped


def _inside(base: Path, target: Path) -> bool:
    try:
        target.resolve().relative_to(base.resolve())
        return True
    except (ValueError, OSError):
        return False


def preview_archive(mgr, archive: Path, seven_zip: str = "", fallback: str = ""):
    """What installing this archive would do, without touching anything."""
    entries = list_entries(archive, seven_zip)
    if entries is None:
        raise InstallError("I can't open this archive." + (" Install 7-Zip to open .7z and .rar files."
                                                          if archive.suffix.lower() != ".zip" else ""))
    mapped, skipped = plan_layout([(e, s) for e, s, _c in entries], fallback or pretty_name(archive.stem))
    clash = [d for d in mapped.values() if (mgr.game / d).exists() or (mgr.stash / d).exists()]
    return {"files": len(mapped), "skipped": len(skipped), "overwrites": len(clash),
            "dests": sorted(set(mapped.values()))}


class _Txn:
    """Remembers what an install changed so that a failure leaves the game folder as it was."""

    def __init__(self, mgr, label: str):
        self.mgr = mgr
        stamp = time.strftime("%Y%m%d-%H%M%S")
        self.backup = mgr.stash / BACKUP_NAME / f"{stamp}-{clean_folder_name(label)[:30]}"
        n = 1
        while self.backup.exists():                # two installs in the same second must not share (and overwrite) a backup
            n += 1
            self.backup = mgr.stash / BACKUP_NAME / f"{stamp}-{clean_folder_name(label)[:30]}-{n}"
        self.created, self.moved = [], []          # created paths; (original, backup) pairs
        self.made_dirs = []

    def back_up(self, path: Path, rel: str):
        dst = self.backup / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(path), str(dst))
        self.moved.append((path, dst))

    def mkdirs(self, d: Path):
        todo = []
        while not d.exists() and d != d.parent:
            todo.append(d)
            d = d.parent
        for p in reversed(todo):
            p.mkdir(exist_ok=True)
            self.made_dirs.append(p)

    def rollback(self):
        for p in reversed(self.created):
            try:
                p.unlink()
            except OSError:
                pass
        for orig, bak in reversed(self.moved):
            try:
                orig.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(bak), str(orig))
            except OSError:
                pass
        for d in reversed(self.made_dirs):
            try:
                d.rmdir()
            except OSError:
                pass


def _copy_stream(src, dst_path: Path, budget: list, cancel=None):
    tmp = dst_path.with_name(dst_path.name + ".cp2077tmp")
    try:
        with open(tmp, "wb") as out:
            while True:
                if cancel is not None and cancel.is_set():
                    raise InstallError("Cancelled.")
                b = src.read(1 << 20)
                if not b:
                    break
                budget[0] -= len(b)
                if budget[0] < 0:
                    raise InstallError("This archive unpacks to far more data than it says; stopped.")
                out.write(b)
        os.replace(tmp, dst_path)
    finally:
        try:
            if tmp.exists():
                tmp.unlink()
        except OSError:
            pass


def install_archive(mgr, archive: Path, seven_zip: str = "", fallback: str = "", replace_rels=None,
                    progress=None, cancel=None) -> dict:
    """Unpack a mod archive into the game folder - safely.
      * only paths inside the game folder are written (no '..', drive letters, links)
      * files that would be overwritten are moved to _disabled_mods/_backup/<time>-<mod>/ first
      * if anything fails, every change is undone
      * `replace_rels` (the old version's files): old single files the new version no longer ships
        are moved to the backup too, so an old and a new copy never load together
    -> {"rels": [...], "removed": [...], "backup": str, "overwritten": n}"""
    progress = progress or (lambda *a: None)
    archive = Path(archive)
    if game_running():
        raise InstallError("Cyberpunk 2077 is running. Close the game first.")
    entries = list_entries(archive, seven_zip)
    if entries is None:
        raise InstallError("I can't open this archive." + (" Install 7-Zip to open .7z and .rar files."
                                                          if archive.suffix.lower() != ".zip" else ""))
    if len(entries) > MAX_ENTRIES:
        raise InstallError("This archive has an unusually large number of files; I won't unpack it.")
    mapped, _skipped = plan_layout([(e, s) for e, s, _c in entries], fallback or pretty_name(archive.stem))
    if sum(s for e, s, _c in entries if e in mapped) > MAX_UNPACKED:
        raise InstallError("This archive is unpacking to more than 8 GB; I won't unpack it.")
    game = mgr.game
    for dest in mapped.values():
        if not _inside(game, game / dest):
            raise InstallError(f"Unsafe destination {dest!r}; nothing was installed.")
    txn = _Txn(mgr, fallback or pretty_name(archive.stem))
    tmp_dir = None
    overwritten = 0
    done = []
    try:
        names = sorted(mapped)
        budget = [MAX_UNPACKED]
        zf = None
        if archive.suffix.lower() == ".zip":
            try:
                zf = zipfile.ZipFile(archive)
            except (zipfile.BadZipFile, OSError):
                zf = None
        if zf is None:
            if not seven_zip:
                raise InstallError("Install 7-Zip to open this archive.")
            tmp_dir = mgr.stash / TMP_NAME / uuid.uuid4().hex[:8]
            tmp_dir.mkdir(parents=True, exist_ok=True)
            progress(0, 1, "Unpacking…")
            r = subprocess.run([seven_zip, "x", "-y", "-aoa", f"-o{tmp_dir}", str(archive)],
                               capture_output=True, timeout=1800, creationflags=NO_WINDOW)
            if r.returncode not in (0, 1):
                raise InstallError("7-Zip couldn't unpack this archive.")
        infos = {}
        if zf is not None:
            infos = {i.filename: i for i in zf.infolist()}
        for n, e in enumerate(names):
            progress(n, len(names), f"Installing {n + 1}/{len(names)}")
            dest = mapped[e]
            target = game / dest
            if target.is_dir():
                raise InstallError(f"{dest} is a folder in your game, but the mod wants a file there.")
            if target.exists():
                txn.back_up(target, dest)
                overwritten += 1
            stashed = mgr.stash / dest
            if stashed.exists() and stashed.is_file():           # a switched-off older copy
                txn.back_up(stashed, "switched-off copy/" + dest)
            txn.mkdirs(target.parent)
            if zf is not None:
                info = infos[e]
                if info.flag_bits & 1:
                    raise InstallError("This archive is password protected.")
                if (info.external_attr >> 16) & 0o170000 == 0o120000:
                    raise InstallError("This archive contains a link, which I won't unpack.")
                with zf.open(info) as src:
                    _copy_stream(src, target, budget, cancel)
            else:
                src_path = tmp_dir / e.replace("\\", "/")
                if not _inside(tmp_dir, src_path) or not src_path.is_file():
                    raise InstallError(f"7-Zip didn't produce {e}.")
                with open(src_path, "rb") as src:
                    _copy_stream(src, target, budget, cancel)
            txn.created.append(target)
            done.append(dest)
        if zf is not None:
            zf.close()
        removed = []
        newset = set(done)
        for rel in replace_rels or []:
            if rel in newset or any(d.startswith(rel + "/") for d in newset):
                continue
            for root in (game, mgr.stash):
                old = root / rel
                if old.is_file() and _inside(root, old):
                    txn.back_up(old, rel)
                    removed.append(rel)
                    break
    except Exception as e:
        txn.rollback()
        if isinstance(e, (InstallError, KeyboardInterrupt)):
            raise
        if isinstance(e, (OSError, zipfile.BadZipFile, subprocess.SubprocessError, RuntimeError)):
            raise InstallError(f"Install failed and was undone: {e}")
        raise
    finally:
        if tmp_dir is not None:
            shutil.rmtree(tmp_dir, ignore_errors=True)
            try:
                (mgr.stash / TMP_NAME).rmdir()
            except OSError:
                pass
    progress(len(done), len(done), "Installed")

    def rel_of(path):
        try:
            return Path(path).relative_to(game).as_posix()
        except ValueError:
            return None
    moves = [[a, b] for a, b in ((rel_of(o), rel_of(bk)) for o, bk in txn.moved) if a and b]
    made = [r for r in (rel_of(d) for d in txn.made_dirs) if r]
    return {"rels": sorted(newset), "removed": removed, "overwritten": overwritten,
            "backup": str(txn.backup) if (txn.moved or removed) else "", "moves": moves, "made_dirs": made}


def unit_for(rel: str, units) -> object:
    """The unit (a file or a folder) that contains this installed file."""
    best = None
    for u in units:
        if rel == u.rel or rel.startswith(u.rel + "/"):
            if best is None or len(u.rel) > len(best.rel):
                best = u
    return best


def finish_install(mgr, result: dict, mod_id=None, version: str = "", file_id=None, file_name: str = "",
                   old_unit_rels=(), was_enabled: bool = True, label: str = "") -> list:
    """Link what was just installed to its Nexus page, remember the version, keep the on/off state
    and the instances in step, and write the change to History (so it can be undone). -> the new units"""
    units = mgr.units()
    new_units, seen = [], set()
    for rel in result["rels"]:
        u = unit_for(rel, units)
        if u and u.rel not in seen:
            seen.add(u.rel)
            new_units.append(u)
    before = mgr.capture_before_install(set(result["rels"]) | seen | set(old_unit_rels) | set(result["removed"]), mod_id)
    for rel in result["removed"]:
        mgr.state["links"].pop(rel, None)
    if mod_id:
        for u in new_units:
            mgr.state["links"][u.rel] = {"id": int(mod_id), "src": "install"}
        inst = {"version": version, "source": "installed by this app", "ts": time.time()}
        if file_id:
            inst["file_id"] = int(file_id)
        if file_name:
            inst["file"] = file_name
        mgr.state["installed"][str(mod_id)] = inst
    if not was_enabled and new_units:
        mgr.move_units([u for u in new_units if u.enabled], False)
    mgr.instances_after_install(old_unit_rels, [u.rel for u in new_units], result["removed"])
    mgr.save()
    name = label or (mgr.state["nexus"].get(str(mod_id)) or {}).get("name") or \
        (new_units[0].pretty if new_units else "a mod")
    updating = bool(old_unit_rels) or bool(before["prev_installed"])
    ver = f" {version}" if version else ""
    overwrote = []                         # files of other mods that this install replaced (for the conflict view)
    for orig, _bak in result.get("moves", []):
        prev = next((l for r, l in before["prev_links"].items() if l and (orig == r or orig.startswith(r + "/"))), None)
        if prev and mod_id and int(prev.get("id", 0)) == int(mod_id):
            continue                       # its own older file
        owner = (mgr.state["nexus"].get(str(prev["id"])) or {}).get("name", "") if prev else ""
        overwrote.append({"rel": orig, "mod": owner})
    mgr.journal_add("update" if updating else "install",
                    f"Updated {name}" + (f" to {version}" if version else "") if updating else f"Installed {name}{ver}",
                    mod=name, mod_id=int(mod_id) if mod_id else None, version=version,
                    created=list(result["rels"]), moves=result.get("moves", []), made_dirs=result.get("made_dirs", []),
                    backup=result.get("backup", ""), old_rels=list(old_unit_rels), was_enabled=bool(was_enabled),
                    overwrote=overwrote, **before)
    return new_units


# ---- which file of a mod to install / update to ------------------------------------------------
ACTIVE_CATS = ("MAIN", "UPDATE", "OPTIONAL", "MISCELLANEOUS")


def file_version(f: dict) -> str:
    return str(f.get("mod_version") or f.get("version") or "").strip()


def plan_update(files_json: dict, installed_file_id=None, installed_version: str = "") -> dict:
    """Pick the file an update should install.
    -> {"target": file|None, "options": [files], "current": file|None, "why": str}
    Nexus records which file replaced which ('file_updates'); following that chain from the file you
    have is exact. Without it the choice is the current MAIN file - and if there are several, the user picks."""
    files = [f for f in (files_json or {}).get("files", []) if isinstance(f, dict)]
    active = [f for f in files if str(f.get("category_name") or "").upper() in ACTIVE_CATS]
    by_id = {}
    for f in files:
        try:
            by_id[int(f.get("file_id"))] = f
        except (TypeError, ValueError):
            pass
    steps = {}
    for u in (files_json or {}).get("file_updates", []) or []:
        try:
            steps[int(u["old_file_id"])] = int(u["new_file_id"])
        except (KeyError, TypeError, ValueError):
            pass
    cur_id = None
    try:
        cur_id = int(installed_file_id) if installed_file_id else None
    except (TypeError, ValueError):
        pass
    if cur_id is None and installed_version:
        want = installed_version.strip()
        same = []
        for f in files:
            if file_version(f) == want or str(f.get("version") or "") == want:
                try:
                    same.append(int(f["file_id"]))
                except (KeyError, TypeError, ValueError):
                    pass
        # a file Nexus says was replaced is the best evidence of "the one you have"
        cur_id = next((i for i in same if i in steps), None) or \
            next((i for i in same if by_id[i] in active), None) or (same[0] if same else None)
    sort_key = lambda f: (bool(f.get("is_primary")), int(f.get("uploaded_timestamp") or 0))
    options = sorted([f for f in active if str(f.get("category_name")).upper() in ("MAIN", "UPDATE")],
                     key=sort_key, reverse=True) or sorted(active, key=sort_key, reverse=True)
    out = {"target": None, "options": options, "current": by_id.get(cur_id) if cur_id else None, "why": ""}
    if cur_id:
        nxt, hops = cur_id, 0
        while nxt in steps and hops < 25:
            nxt, hops = steps[nxt], hops + 1
        if nxt != cur_id and nxt in by_id and by_id[nxt] in active:
            out.update(target=by_id[nxt], why="Nexus says this file replaced the one you have.")
            return out
        if nxt == cur_id and cur_id in by_id and by_id[cur_id] in active and len(options) <= 1:
            out["why"] = "The file you have is still the current one."
            return out
    mains = [f for f in options if str(f.get("category_name")).upper() in ("MAIN", "UPDATE")]
    if len(mains) == 1:
        out.update(target=mains[0], why="The mod has one main file.")
    elif len(mains) > 1:
        primary = [f for f in mains if f.get("is_primary")]
        if len(primary) == 1 and not cur_id:
            out.update(target=primary[0], why="Nexus marks this as the main file.")
        else:
            out["why"] = "The mod has several main files - pick the one you use."
    elif len(options) == 1:
        out.update(target=options[0], why="The mod has one file.")
    return out


def file_label(f: dict) -> str:
    size = ""
    try:
        kb = float(f.get("size_kb") or 0) or float(f.get("size_in_bytes") or 0) / 1024
        size = f"  ·  {kb / 1024:.1f} MB" if kb >= 1024 else (f"  ·  {kb:.0f} KB" if kb else "")
    except (TypeError, ValueError):
        pass
    return (f"{f.get('name') or f.get('file_name') or 'file'}  ·  v{file_version(f) or '?'}  ·  "
            f"{str(f.get('category_name') or '').title()}{size}")


# ---- downloading ---------------------------------------------------------------------------------
def cdn_host_ok(url: str, allow_local: bool = False) -> bool:
    """Downloads may only come from Nexus's own servers (https). Tests may use localhost."""
    u = urllib.parse.urlparse(url)
    h = (u.hostname or "").lower()
    if u.scheme == "https" and any(h == d or h.endswith("." + d) for d in ("nexusmods.com", "nexus-cdn.com")):
        return True
    return allow_local and u.scheme in ("http", "https") and h in ("127.0.0.1", "localhost", "::1")


class _CheckedRedirect(urllib.request.HTTPRedirectHandler):
    def __init__(self, allow_local):
        self.allow_local = allow_local

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if not cdn_host_ok(newurl, self.allow_local):
            raise urllib.error.URLError("redirected to a server that isn't Nexus")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def safe_file_name(name: str) -> str:
    name = urllib.parse.unquote(name or "").replace("\\", "/").rsplit("/", 1)[-1]
    name = re.sub(r'[\\/:*?"<>|\x00-\x1f]+', "_", name).strip(" .")
    return name[:150] or "download.zip"


def download_file(url: str, dest_dir: Path, name: str = "", allow_local: bool = False,
                  progress=None, cancel=None, timeout: int = 30) -> Path:
    """Download from a Nexus address into dest_dir. The API key is never sent with this request."""
    if not cdn_host_ok(url, allow_local):
        raise NexusError(0, "The download address isn't a Nexus server, so I didn't use it.")
    progress = progress or (lambda *a: None)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    fname = safe_file_name(name or urllib.parse.urlparse(url).path)
    dest = dest_dir / fname
    n = 1
    while dest.exists():
        n += 1
        stem, ext = os.path.splitext(fname)
        dest = dest_dir / f"{stem} ({n}){ext}"
    part = dest.with_name(dest.name + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": f"{APP_ID}/{VERSION}"})
    opener = urllib.request.build_opener(_CheckedRedirect(allow_local))
    try:
        with opener.open(req, timeout=timeout) as r, open(part, "wb") as out:
            total = int(r.headers.get("Content-Length") or 0)
            if total:
                try:
                    if shutil.disk_usage(dest_dir).free < total * 2:
                        raise NexusError(0, "Not enough free disk space for this download.")
                except OSError:
                    pass
            got = 0
            while True:
                if cancel is not None and cancel.is_set():
                    raise NexusError(0, "Cancelled.")
                b = r.read(1 << 18)
                if not b:
                    break
                out.write(b)
                got += len(b)
                progress(got, total or got, f"Downloading {got / 1048576:.1f} MB"
                         + (f" of {total / 1048576:.1f} MB" if total else ""))
            if total and got != total:
                raise NexusError(0, "The download was cut off. Try again.")
        os.replace(part, dest)
    except urllib.error.HTTPError as e:
        raise NexusError(e.code, f"The download server answered {e.code}.")
    except urllib.error.URLError as e:
        raise NexusError(0, f"Couldn't download ({e.reason}).")
    except OSError as e:
        raise NexusError(0, f"Couldn't save the download ({e}).")
    finally:
        try:
            if part.exists():
                part.unlink()
        except OSError:
            pass
    if dest.suffix.lower() == ".zip":
        try:
            with zipfile.ZipFile(dest) as z:
                if z.testzip() is not None:
                    raise zipfile.BadZipFile("damaged entry")
        except (zipfile.BadZipFile, OSError) as e:
            dest.unlink(missing_ok=True)
            raise NexusError(0, f"The downloaded file is damaged ({e}). Try again.")
    return dest


def find_new_download(dirs, since: float, mod_id: int, file_id: int, file_name: str, seen: dict):
    """Free accounts can also just save the file in their browser: spot it in the Downloads folder.
    Only a finished file (same size on two looks, no .crdownload/.part next to it) that is named like
    this mod/file is returned."""
    want = (file_name or "").lower()
    for p in find_archives(dirs, max_depth=1):
        try:
            st = p.stat()
        except OSError:
            continue
        if st.st_mtime < since - 5 or st.st_size <= 0:
            continue
        info = parse_archive_name(p.stem)
        base = re.sub(r"\s*\(\d+\)$", "", p.name.lower())
        if not (info["file_id"] == file_id or info["mod_id"] == mod_id or (want and base == want)):
            continue
        if any((p.parent / (p.name + ext)).exists() for ext in (".crdownload", ".part", ".download", ".tmp")) \
                or p.with_suffix(".crdownload").exists():
            continue
        sig = (st.st_size, int(st.st_mtime))
        if seen.get(str(p)) == sig:
            return p
        seen[str(p)] = sig
    return None


def parse_nxm(url: str):
    """nxm://cyberpunk2077/mods/107/files/12345?key=…&expires=…  ->  dict, or None"""
    m = re.match(r"^nxm://([a-z0-9]+)/mods/(\d{1,9})/files/(\d{1,12})(?:\?(.*))?$", (url or "").strip(), re.I)
    if not m or m.group(1).lower() != DOMAIN:
        return None
    q = urllib.parse.parse_qs(m.group(4) or "")
    key = (q.get("key") or [""])[0]
    exp = (q.get("expires") or [""])[0]
    if (key and not re.fullmatch(r"[A-Za-z0-9_\-=.+/]{3,300}", key)) or (exp and not exp.isdigit()):
        return None
    return {"mod_id": int(m.group(2)), "file_id": int(m.group(3)), "key": key, "expires": exp}


def download_dir_for(mgr, cfg: dict) -> Path:
    for d in [cfg.get("save_dir")] + list(cfg.get("download_dirs") or []):
        if d and Path(d).is_dir():
            return Path(d)
    dd = default_download_dirs()
    return Path(dd[0]) if dd else mgr.stash / DOWNLOADS_NAME


def install_downloaded(mgr, cfg: dict, path: Path, mod_id, file_obj: dict = None, mod_name: str = "",
                       existing: Mod = None, progress=None, cancel=None) -> dict:
    """Install an archive that is already on disk. If `existing` (the same mod, already installed) is
    given this is an update: its files are replaced, a switched-off mod is switched on for the install
    and off again afterwards, so it stays off."""
    path = Path(path)
    old_rels = [u.rel for u in existing.units] if existing else []
    was_on = existing.status != "off" if existing else True
    off_rels = {u.rel for u in existing.units if not u.enabled} if existing else set()
    if off_rels:
        _n, errs = mgr.move_units([u for u in existing.units if not u.enabled], True)
        if errs:
            raise InstallError("Couldn't switch the mod on to update it: " + errs[0])
    try:
        res = install_archive(mgr, path, find_7zip(cfg.get("seven_zip", "")), mod_name or pretty_name(path.stem),
                              old_rels or None, progress, cancel)
        file_obj = file_obj or {}
        version = file_version(file_obj)
        new_units = finish_install(mgr, res, mod_id, version, file_obj.get("file_id"), path.name, old_rels, was_on,
                                   label=mod_name or "")
    except Exception:
        if off_rels:
            mgr.move_units([u for u in mgr.units() if u.rel in off_rels and u.enabled], False)
        raise
    res.update(archive=str(path), units=[u.rel for u in new_units], version=version)
    return res


def fetch_and_install(mgr, nx: Nexus, cfg: dict, mod_id: int, file_obj: dict, key: str = "", expires: str = "",
                      existing: Mod = None, mod_name: str = "", progress=None, cancel=None) -> dict:
    """Get one file from Nexus and install it. Raises NeedsBrowser when a free account must click first."""
    progress = progress or (lambda *a: None)
    progress(0, 1, "Asking Nexus for the download…")
    links = nx.download_links(mod_id, int(file_obj["file_id"]), key, expires)
    path = download_file(links[0]["url"], download_dir_for(mgr, cfg), file_obj.get("file_name") or "",
                         allow_local=nx.local, progress=progress, cancel=cancel)
    return install_downloaded(mgr, cfg, path, mod_id, file_obj, mod_name, existing, progress, cancel)


def identify_archive(mgr, nx, path: Path) -> dict:
    """What is this archive that the user wants to add?
    -> {"mod_id", "name", "version", "file_id", "how", "cands": [...]}   how: fingerprint | file name | name | unknown"""
    info = parse_archive_name(path.stem)
    out = {"mod_id": None, "name": info["name"], "version": info["version"], "file_id": info["file_id"],
           "how": "unknown", "cands": []}
    if nx is not None:
        try:
            pick = pick_md5_result(nx.md5_lookup(md5_file(path)), path.stat().st_size, info["name"])
        except (NexusError, OSError):
            pick = None
        if pick:
            out.update(mod_id=pick["mod_id"], name=pick["name"] or info["name"], version=pick["version"] or info["version"],
                       file_id=pick.get("file_id") or info["file_id"], how="fingerprint")
            return out
    if info["mod_id"]:
        out.update(mod_id=info["mod_id"], how="file name")
        return out
    if nx is not None:
        words = spaced_words(info["name"])
        keys, toks = {norm_key(info["name"])}, set(name_tokens(info["name"]))
        found = {}
        try:
            for term in dict.fromkeys([" ".join(words), "".join(words)] if len(words) > 1 else [" ".join(words)]):
                for n in nx.search(term, SEARCH_PAGE) if term else []:
                    s, why, kind, deriv = score_match(keys, toks, n["name"])
                    if s >= 0.5 and s > found.get(n["id"], {"score": 0})["score"]:
                        found[n["id"]] = {"id": n["id"], "name": n["name"], "version": n["version"], "score": s,
                                          "why": why, "kind": kind, "deriv": deriv, "flags": []}
        except NexusError:
            pass
        cands = sorted(found.values(), key=lambda c: -c["score"])[:6]
        out["cands"] = cands
        exact = [c for c in cands if c["kind"] == "exact"]
        if len(exact) == 1:
            out.update(mod_id=exact[0]["id"], how="name", name=exact[0]["name"])
    return out


def add_archive(mgr, nx, cfg: dict, path: Path, mod_id=None, version: str = "", file_id=None,
                progress=None) -> dict:
    """Install an archive the user picked, and link it to Nexus when we know which mod it is."""
    path = Path(path)
    res = install_archive(mgr, path, find_7zip(cfg.get("seven_zip", "")), pretty_name(path.stem), None, progress)
    new_units = finish_install(mgr, res, mod_id, version, file_id, path.name, (), True, label=pretty_name(path.stem))
    res.update(units=[u.rel for u in new_units])
    return res


# ---- the Nexus "Mod Manager Download" button (nxm:// links) ------------------------------------
def nxm_command() -> str:
    if getattr(sys, "frozen", False):
        return f'"{sys.executable}" "%1"'
    exe = Path(sys.executable)
    pyw = exe.with_name("pythonw.exe")
    return f'"{pyw if pyw.exists() else exe}" "{Path(__file__).resolve()}" "%1"'


def nxm_current() -> str:
    """The program Windows currently starts for nxm:// links ('' if none / not Windows)."""
    if os.name != "nt":
        return ""
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"nxm\shell\open\command") as k:
            return str(winreg.QueryValue(k, None))
    except OSError:
        return ""


def nxm_register() -> str:
    """Make this app the one Windows starts for nxm:// links (current user only). -> '' or an error."""
    if os.name != "nt":
        return "Only available on Windows."
    try:
        import winreg
        base = r"Software\Classes\nxm"
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, base) as k:
            winreg.SetValue(k, None, winreg.REG_SZ, "URL:NXM Protocol")
            winreg.SetValueEx(k, "URL Protocol", 0, winreg.REG_SZ, "")
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, base + r"\shell\open\command") as k:
            winreg.SetValue(k, None, winreg.REG_SZ, nxm_command())
        return ""
    except OSError as e:
        return f"Couldn't change the Windows setting ({e})."


def nxm_restore(previous: str) -> str:
    if os.name != "nt":
        return "Only available on Windows."
    try:
        import winreg
        if previous:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\nxm\shell\open\command") as k:
                winreg.SetValue(k, None, winreg.REG_SZ, previous)
        else:
            for sub in (r"\shell\open\command", r"\shell\open", r"\shell", ""):
                try:
                    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, r"Software\Classes\nxm" + sub)
                except OSError:
                    pass
        return ""
    except OSError as e:
        return f"Couldn't change the Windows setting ({e})."


IPC_PATH = Path.home() / ".cp2077_mod_toggle.ipc"

# A one-file .exe built with PyInstaller leaves a few private variables in its environment. Everything the app
# starts inherits them - the browser, the game, 7-Zip. When that browser later starts this .exe again (Nexus'
# "Slow download" button -> nxm:// link) the new copy thinks it is a child of the old one and looks for its files in
# the old copy's temporary folder, which is gone:  "Failed to load Python DLL ...\_MEI...\python3xx.dll".
# So the app removes the variables from its own environment and asks any new copy to start as an independent one.
PYI_VARS = ("_MEIPASS2", "_PYI_ARCHIVE_FILE", "_PYI_PARENT_PROCESS_LEVEL", "_PYI_LINUX_PROCESS_NAME",
            "_PYI_APPLICATION_HOME_DIR", "_PYI_SPLASH_IPC")


def scrub_frozen_env(env=None):
    """Make `env` (default: this process) safe to hand to other programs. Returns it."""
    env = os.environ if env is None else env
    for k in PYI_VARS:
        env.pop(k, None)
    env["PYINSTALLER_RESET_ENVIRONMENT"] = "1"
    return env


class InstanceServer:
    """Lets a second start hand over to the window that is already open: the browser launching an nxm://
    link, or a double-click on the icon. Local only, with a random token, and it only accepts nxm:// links,
    "show yourself" and "are you there?"."""

    def __init__(self, on_url, path: Path = None, on_show=None, on_play=None):
        self.on_url = on_url
        self.on_show = on_show
        self.on_play = on_play
        self.path = Path(path or IPC_PATH)
        self.token = uuid.uuid4().hex
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen(4)
        self.port = self.sock.getsockname()[1]
        try:
            self.path.write_text(json.dumps({"port": self.port, "token": self.token, "pid": os.getpid()}), "utf-8")
            os.chmod(self.path, 0o600)
        except OSError:
            pass
        threading.Thread(target=self._loop, daemon=True).start()

    def _loop(self):
        while True:
            try:
                conn, _addr = self.sock.accept()
            except OSError:
                return
            try:
                conn.settimeout(3)
                data = json.loads(conn.recv(16384).decode("utf-8", "replace") or "{}")
                if isinstance(data, dict) and data.get("token") == self.token:
                    if data.get("nxm") is not None:
                        if parse_nxm(str(data["nxm"])):
                            self.on_url(str(data["nxm"]))
                            conn.sendall(b"ok")
                    elif data.get("show"):
                        if self.on_show:
                            self.on_show()
                        conn.sendall(b"ok")
                    elif data.get("ping"):
                        conn.sendall(b"ok")
                    elif "play" in data and isinstance(data["play"], str) and len(data["play"]) <= 80:
                        if self.on_play:                      # a desktop shortcut while the window is open
                            self.on_play(data["play"])
                            conn.sendall(b"ok")
            except (OSError, ValueError):
                pass
            finally:
                conn.close()

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass
        try:
            if json.loads(self.path.read_text("utf-8")).get("token") == self.token:
                self.path.unlink()
        except (OSError, ValueError):
            pass


def _tell_running(msg: dict, path: Path = None) -> bool:
    try:
        info = json.loads(Path(path or IPC_PATH).read_text("utf-8"))
        with socket.create_connection(("127.0.0.1", int(info["port"])), timeout=1.5) as c:
            c.sendall(json.dumps(dict(msg, token=info["token"])).encode("utf-8"))
            c.settimeout(3)
            return c.recv(8) == b"ok"
    except (OSError, ValueError, KeyError, TypeError):
        return False


def send_to_running(url: str, path: Path = None) -> bool:
    """Give an nxm:// link to the app that is already open. True if it accepted it."""
    return _tell_running({"nxm": url}, path)


def show_running(path: Path = None) -> bool:
    """Ask the app that is already open to come to the front. True if there was one."""
    return _tell_running({"show": True}, path)


def hand_over_nxm(url: str, path: Path = None, tries: int = 8, wait: float = 0.5) -> bool:
    """A link arrives while no window may want to open: True once an open copy has taken it (or None of
    the copies can be reached at all, in which case False says 'start the window yourself')."""
    for i in range(max(1, tries)):
        if send_to_running(url, path):
            return True
        if not _tell_running({"ping": True}, path):      # nobody is listening: no copy is open
            return False
        time.sleep(wait)                                 # a copy is open but busy starting or closing: try again
    return False


# ---- "Did you download this?" check on the Nexus page ------------------------------------------------
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct",
                                      "nov", "dec"], 1)}


def parse_page_date(text: str):
    """Pull a date out of what the user copied from the Nexus page ('You last downloaded a file from
    this mod on 26 Oct 2026') -> timestamp at local noon, or None."""
    t = (text or "").strip()
    m = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", t)
    y = mo = d = None
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    else:
        m = re.search(r"(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]{3,9})\.?,?\s+(\d{4})", t)
        if m and m.group(2)[:3].lower() in MONTHS:
            d, mo, y = int(m.group(1)), MONTHS[m.group(2)[:3].lower()], int(m.group(3))
        else:
            m = re.search(r"([A-Za-z]{3,9})\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})", t)
            if m and m.group(1)[:3].lower() in MONTHS:
                mo, d, y = MONTHS[m.group(1)[:3].lower()], int(m.group(2)), int(m.group(3))
    if y is None:
        return None
    try:
        return time.mktime((y, mo, d, 12, 0, 0, 0, 0, -1))
    except (OverflowError, ValueError):
        return None


def date_fit(install_ts: float, page_ts: float):
    """Compare the day the files were put on this PC with the day Nexus says you last downloaded
    from the page. -> (verdict, sentence). verdict: same | close | later | far"""
    if not install_ts or not page_ts:
        return "far", "I can't compare without both dates."
    days = (page_ts - install_ts) / 86400.0
    if abs(days) < 1.0:
        return "same", "Same day - this is almost certainly the right page."
    if -30 <= days < -1:
        return "close", (f"You downloaded {abs(int(round(days)))} day(s) before the files appeared on this PC "
                         "- normal if you installed later. Likely the right page.")
    if 1 <= days <= 400:
        return "later", ("Nexus says you downloaded from this page AFTER these files were installed. It may "
                         "be a newer download of the same mod (an update you haven't installed), or a different mod.")
    return "far", "These dates are far apart, so this is probably not the page these files came from."


def update_mod(mgr, nx: Nexus, cfg: dict, mod: Mod, file_obj: dict, key: str = "", expires: str = "",
               progress=None, cancel=None) -> dict:
    """Update one linked mod to `file_obj`."""
    return fetch_and_install(mgr, nx, cfg, mod.nexus_id, file_obj, key, expires, existing=mod,
                             mod_name=mod.name, progress=progress, cancel=cancel)


# --------------------------------------------------------------------------
# Command line
# --------------------------------------------------------------------------
def match_mods(mods, patterns):
    if any(p == "*" for p in patterns):
        return list(mods)
    pats = [p.lower() for p in patterns]
    return [m for m in mods if any(p in m.name.lower() or p in m.local_name.lower()
                                   or p in norm_key(m.name) for p in pats)]


def cli(args) -> int:
    for stream in (sys.stdout, sys.stderr):        # old Windows consoles can't print ✓ → …
        try:
            stream.reconfigure(errors="replace")
        except Exception:
            pass
    cfg = load_config()
    game = args.game or load_saved_game() or (find_game_dirs() or [None])[0]
    if not game or not is_game_dir(game):
        print("Could not find the game folder. Pass --game \"<path to Cyberpunk 2077>\".")
        return 2
    mgr = Manager(game)
    key = args.api_key or os.environ.get("NEXUS_API_KEY") or cfg.get("api_key", "")
    nx = Nexus(key) if key else None
    if args.downloads:
        cfg["download_dirs"] = list(args.downloads)
    if args.match:
        rep = run_match(mgr, nx, cfg, lambda i, n, t="": None, force=args.force)
        for line in rep["notes"]:
            print(line)
        if rep["proposals"]:
            print("\nNot sure about these (open the app, 'Review matches', to confirm - or use the Nexus page "
                  "number with the Link option):")
            for p in rep["proposals"]:
                print(f"  {p['mod'][:30]:30} -> {p['nexus_name'][:36]:36} {NEXUS_SITE}/{DOMAIN}/mods/{p['id']}"
                      f"  ({int(p['score'] * 100)}%)")
        print()
    if args.check_updates:
        if not nx:
            print("No API key. Use --api-key, NEXUS_API_KEY, or set it in the app's Settings.")
        else:
            for e in refresh_nexus(mgr, nx, force=args.force):
                print("  !", e)
            mgr.save()
    if args.make_shortcut:
        mgr.ensure_instances()
        names = {n.lower(): n for n in mgr.state["instances"]}
        target = names.get(args.make_shortcut.lower())
        if not target:
            print(f"No instance called {args.make_shortcut!r}. You have: {', '.join(sorted(mgr.state['instances']))}")
            return 2
        try:
            print("Shortcut created:", make_shortcut(game, target))
        except OSError as e:
            print("Couldn't create the shortcut:", e)
            return 1
        return 0
    if args.instances or args.switch:
        mgr.ensure_instances()
        mgr.sync_active()
        if args.switch:
            names = {n.lower(): n for n in mgr.state["instances"]}
            target = names.get(args.switch.lower())
            if not target:
                print(f"No instance called {args.switch!r}. You have: {', '.join(sorted(mgr.state['instances']))}")
                return 2
            if game_running():
                print("Cyberpunk2077.exe is running - close the game first.")
                return 3
            plan = mgr.instance_plan(target)
            moved, errs = mgr.switch_instance(target)
            print(f"Switched to {target}: {len(plan['enable_mods'])} mod(s) on, {len(plan['disable_mods'])} off")
            for e in errs:
                print("   !", e)
        for n in sorted(mgr.state["instances"], key=str.lower):
            print(("* " if n == mgr.state["active"] else "  ") + f"{n}  ({len(mgr.state['instances'][n].get('on', []))} on)")
        return 0
    for flag, enable in (("enable", True), ("disable", False)):
        pats = getattr(args, flag)
        if not pats:
            continue
        if not enable and game_running():
            print("Cyberpunk2077.exe is running - close the game first.")
            return 3
        for m in match_mods(mgr.scan(fuzzy=not args.no_fuzzy), pats):
            moved, errs = mgr.set_enabled(m, enable)
            print(f"{'Enabled ' if enable else 'Disabled'} {m.name}: {moved} moved")
            for e in errs:
                print("   !", e)
    mods = mgr.scan(fuzzy=not args.no_fuzzy)
    if args.suggest:
        for s in suggest_merges(mods):
            print(f"{s['a'].name}  +  {s['b'].name}   ({s['why']})")
    if args.list or args.match or args.check_updates or not (args.enable or args.disable or args.suggest):
        lab = {"update": "UPDATE", "ok": "ok", "maybe": "check?", "unknown": "-", "pinned": "pinned", "": "not linked"}
        print(f"{'STATE':8} {'MOD':34} {'INSTALLED':10} {'LATEST':10} NEXUS")
        for m in mods:
            fw = " [framework]" if m.core else ""
            print(f"{m.status.upper():8} {(m.name + fw)[:34]:34} {(m.installed_version or '-')[:10]:10} "
                  f"{(m.latest_version or '-')[:10]:10} {lab[m.update]}")
        print(f"\n{len(mods)} mods, {sum(1 for m in mods if m.update == 'update')} with updates")
    return 0


# --------------------------------------------------------------------------
# GUI
# --------------------------------------------------------------------------
THEME = dict(
    bg="#0d0f13", panel="#151820", panel2="#1c2029", line="#272c37", sel="#2a3040",
    fg="#e9ebf1", muted="#8890a4", accent="#fcee0a", accent_fg="#101010", hover="#fff35c",
    green="#3ddc84", amber="#ffb020", orange="#ff9f43", red="#ff5d5d", cyan="#4fd8ff",
    tint="#2b2515",
)
NOTE_TINT = {"red": "#4a2226", "orange": "#4a3320", "yellow": "#47421c", "green": "#1f4030", "cyan": "#1c3f48",
             "blue": "#232f55", "purple": "#3b2750", "pink": "#4d2440"}          # row backgrounds
NOTE_DOT = {"": "#1c2029", "red": "#e5484d", "orange": "#f08a24", "yellow": "#e6c229", "green": "#3ddc84",
            "cyan": "#4fd8ff", "blue": "#5b7cff", "purple": "#a66bff", "pink": "#ff6bb5"}   # the swatches
STATE_LABEL = {"on": "●  ON", "off": "○  OFF", "partial": "◐  PARTIAL"}
UPDATE_LABEL = {"update": "▲  Update", "ok": "✓  Latest", "maybe": "?  Check", "unknown": "—", "pinned": "⏸  Pinned",
                "": "Not linked"}
UPDATE_RANK = {"update": 0, "maybe": 1, "unknown": 2, "pinned": 3, "ok": 4, "": 5}
FILTERS = ["All", "Enabled", "Disabled", "Partial", "Frameworks", "Updates available", "Pinned", "Not linked to Nexus",
           "With a note, tag or colour", "With a warning"]


def human_count(n) -> str:
    try:
        n = int(n)
    except (TypeError, ValueError):
        return ""
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M".replace(".0M", "M")
    if n >= 10_000:
        return f"{n // 1000}k"
    if n >= 1_000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def fmt_dt(ts) -> str:
    try:
        return time.strftime("%d %b %Y, %H:%M", time.localtime(float(ts)))
    except (OverflowError, OSError, ValueError, TypeError):
        return ""


def source_text(src: str) -> str:
    return {"download (verified)": "verified against your download",
            "download": "from your download's file name"}.get(src, src)


def make_app(game_arg=None, nxm_arg=None):
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox

    try:  # crisp text on high-DPI Windows screens
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass

    T = THEME
    FONT = os.environ.get("CP2077_FONT") or "Segoe UI"

    def font(size=10, bold=False):
        return (FONT, size, "bold") if bold else (FONT, size)

    def dark_titlebar(win):
        try:
            import ctypes
            win.update_idletasks()
            hwnd = ctypes.windll.user32.GetParent(win.winfo_id())
            for attr in (20, 19):
                v = ctypes.c_int(1)
                if ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, attr, ctypes.byref(v), ctypes.sizeof(v)) == 0:
                    break
        except Exception:
            pass

    def apply_theme(root):
        s = ttk.Style(root)
        try:
            s.theme_use("clam")
        except tk.TclError:
            return
        root.configure(bg=T["bg"])
        base = font(10)
        s.configure(".", background=T["bg"], foreground=T["fg"], fieldbackground=T["panel2"],
                    bordercolor=T["line"], lightcolor=T["bg"], darkcolor=T["bg"],
                    troughcolor=T["panel"], focuscolor=T["bg"], font=base)
        s.configure("TFrame", background=T["bg"])
        s.configure("TLabel", background=T["bg"], foreground=T["fg"])
        s.configure("TButton", background=T["panel2"], foreground=T["fg"], borderwidth=0,
                    focusthickness=0, padding=(14, 7), relief="flat")
        s.map("TButton", background=[("active", T["sel"]), ("disabled", T["panel"])],
              foreground=[("disabled", T["muted"])])
        s.configure("Accent.TButton", background=T["accent"], foreground=T["accent_fg"], font=font(10, True))
        s.map("Accent.TButton", background=[("active", T["hover"]), ("disabled", "#5c5a1a")],
              foreground=[("disabled", "#2a2a2a")])
        s.configure("TMenubutton", background=T["panel2"], foreground=T["fg"], padding=(14, 7),
                    borderwidth=0, arrowcolor=T["muted"], relief="flat")
        s.map("TMenubutton", background=[("active", T["sel"])])
        s.configure("TEntry", fieldbackground=T["panel2"], foreground=T["fg"], insertcolor=T["fg"],
                    bordercolor=T["line"], padding=7)
        s.map("TEntry", bordercolor=[("focus", T["accent"])])
        s.configure("TCombobox", fieldbackground=T["panel2"], background=T["panel2"], foreground=T["fg"],
                    arrowcolor=T["muted"], bordercolor=T["line"], padding=6)
        s.map("TCombobox", fieldbackground=[("readonly", T["panel2"])],
              foreground=[("readonly", T["fg"])], selectbackground=[("readonly", T["panel2"])],
              selectforeground=[("readonly", T["fg"])])
        root.option_add("*TCombobox*Listbox.background", T["panel2"])
        root.option_add("*TCombobox*Listbox.foreground", T["fg"])
        root.option_add("*TCombobox*Listbox.selectBackground", T["accent"])
        root.option_add("*TCombobox*Listbox.selectForeground", T["accent_fg"])
        root.option_add("*TCombobox*Listbox.font", font(10))
        s.configure("TCheckbutton", background=T["bg"], foreground=T["fg"], focuscolor=T["bg"])
        s.map("TCheckbutton", background=[("active", T["bg"])],
              indicatorcolor=[("selected", T["accent"]), ("!selected", T["panel2"])])
        s.configure("Treeview", background=T["panel"], fieldbackground=T["panel"], foreground=T["fg"],
                    rowheight=34, borderwidth=0, relief="flat", font=base)
        s.configure("Treeview.Heading", background=T["panel2"], foreground=T["muted"], relief="flat",
                    borderwidth=0, padding=(12, 9), font=font(9, True))
        s.map("Treeview", background=[("selected", T["sel"])], foreground=[("selected", T["fg"])])
        s.map("Treeview.Heading", background=[("active", T["sel"])])
        try:
            s.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])
        except tk.TclError:
            pass
        for orient in ("Vertical", "Horizontal"):
            s.configure(f"{orient}.TScrollbar", background=T["panel2"], troughcolor=T["panel"],
                        bordercolor=T["panel"], arrowcolor=T["muted"], relief="flat", gripcount=0)
            s.map(f"{orient}.TScrollbar", background=[("active", T["sel"])])
        s.configure("Horizontal.TProgressbar", troughcolor=T["panel"], background=T["accent"],
                    bordercolor=T["panel"], lightcolor=T["accent"], darkcolor=T["accent"], thickness=6)

    def label(parent, text="", fg=None, bg=None, size=10, bold=False, **kw):
        return tk.Label(parent, text=text, fg=fg or T["fg"], bg=bg or T["bg"], font=font(size, bold),
                        anchor=kw.pop("anchor", "w"), **kw)

    def themed_menu(parent):
        return tk.Menu(parent, tearoff=0, bg=T["panel2"], fg=T["fg"], activebackground=T["accent"],
                       activeforeground=T["accent_fg"], relief="flat", borderwidth=0, font=font(10))

    class App(tk.Tk):
        def __init__(self):
            super().__init__()
            self.title(APP_NAME)
            self.geometry("1320x800")
            self.minsize(1000, 620)
            self.cfg = load_config()
            self.mgr = None
            self.mods = []
            self.proposals = []
            self.busy = False
            self.sort_col, self.sort_rev = "name", False
            self.fuzzy = tk.BooleanVar(value=True)
            self.search = tk.StringVar()
            self.filter = tk.StringVar(value="All")
            self.status = tk.StringVar()
            self.path_var = tk.StringVar()
            self.stats = tk.StringVar()
            self.findings, self._warn_mods = [], {}            # last check-up, and {mod name: [its warnings]}
            self._checking, self._checkup_waiters, self.banner = False, [], None
            try:
                apply_theme(self)
            except tk.TclError:
                pass
            dark_titlebar(self)
            self._init_jobs()
            self._build()
            self.protocol("WM_DELETE_WINDOW", self.on_close)
            game = game_arg or load_saved_game() or (find_game_dirs() or [None])[0]
            if game and is_game_dir(game):
                self.set_game(game)
            else:
                self.status.set("Pick your Cyberpunk 2077 folder with Tools → “Game folder…”.")
            if nxm_arg:
                self.after(700, lambda: self.handle_nxm(nxm_arg))
            else:
                self.after(600, self.first_run_key)         # no key yet: ask for it right away
            if not self.cfg.get("api_key"):
                self.status.set((self.status.get() + "   ").strip() +
                                "  Add your Nexus API key in Settings to match mods and check for updates.")
            elif self.mgr and self.cfg.get("auto_check", True) and self.mgr.state["links"] \
                    and time.time() - self.mgr.state.get("last_check", 0) > 12 * 3600:
                self.after(900, lambda: self.check_updates(silent=True))

        # ---- layout --------------------------------------------------------
        def _build(self):
            hdr = tk.Frame(self, bg=T["bg"])
            hdr.pack(fill="x", padx=26, pady=(18, 0))
            logo = tk.Frame(hdr, bg=T["bg"])
            logo.pack(side="left")
            label(logo, "ModScout", T["accent"], size=21, bold=True).pack(side="left")
            label(logo, "  2077", T["fg"], size=21).pack(side="left")
            tabs = tk.Frame(hdr, bg=T["bg"])
            tabs.pack(side="left", padx=(38, 0), pady=(8, 0))
            self.tab = {}
            for key, text in (("lib", "Library"), ("upd", "Updates"), ("browse", "Browse Nexus"),
                              ("dl", "Downloads")):
                cell = tk.Frame(tabs, bg=T["bg"], cursor="hand2")
                cell.pack(side="left", padx=(0, 4))
                lb = tk.Label(cell, text=text, fg=T["muted"], bg=T["bg"], font=font(11, True), padx=13, pady=6,
                              cursor="hand2")
                lb.pack()
                bar = tk.Frame(cell, bg=T["bg"], height=3)
                bar.pack(fill="x")
                for w in (cell, lb, bar):
                    w.bind("<Button-1>", lambda _e, k=key: self.show_page(k))
                self.tab[key] = (lb, bar, text)
            right = tk.Frame(hdr, bg=T["bg"])
            right.pack(side="right")
            self.play_menu_btn = ttk.Menubutton(right, text="▾", width=2)
            self.play_menu_btn.pack(side="right")
            self.play_menu = themed_menu(self.play_menu_btn)
            self.play_menu_btn["menu"] = self.play_menu
            self.play_menu.configure(postcommand=self._fill_play_menu)
            self.play_btn = ttk.Button(right, text="Play", style="Accent.TButton", command=self.play)
            self.play_btn.pack(side="right", padx=(0, 2))
            ttk.Button(right, text="Settings", command=self.open_settings).pack(side="right", padx=(0, 14))
            self.tools_btn = ttk.Menubutton(right, text="Tools  ▾")
            self.tools_btn.pack(side="right", padx=(0, 8))
            self.tools_menu = themed_menu(self.tools_btn)
            self.tools_btn["menu"] = self.tools_menu
            self.tools_menu.configure(postcommand=self._fill_tools_menu)
            self.inst_btn = ttk.Menubutton(right, text="◈  Main  ▾")
            self.inst_btn.pack(side="right", padx=(0, 8))
            self.inst_menu = themed_menu(self.inst_btn)
            self.inst_btn["menu"] = self.inst_menu
            self.inst_menu.configure(postcommand=self._fill_instance_menu)
            self.shortcut_menu = themed_menu(self.inst_menu)
            prow = tk.Frame(self, bg=T["bg"])                       # game folder on the left, the counts on the right
            prow.pack(fill="x", padx=28, pady=(2, 0))
            self.stats_lbl = tk.Label(prow, textvariable=self.stats, fg=T["muted"], bg=T["bg"], font=font(10))
            self.stats_lbl.pack(side="right")
            tk.Label(prow, textvariable=self.path_var, fg=T["muted"], bg=T["bg"], font=font(9),
                     anchor="w").pack(side="left", fill="x", expand=True)

            sf = tk.Frame(self, bg=T["bg"])                       # packed first so it always keeps its place
            sf.pack(side="bottom", fill="x", padx=26, pady=(6, 14))
            tk.Label(sf, textvariable=self.status, fg=T["muted"], bg=T["bg"], font=font(9),
                     anchor="w").pack(side="left", fill="x", expand=True)
            self.pbar = ttk.Progressbar(sf, mode="determinate", length=220, style="Horizontal.TProgressbar")

            self.host = tk.Frame(self, bg=T["bg"])
            self.host.pack(fill="both", expand=True)
            self.pages = {"lib": self._build_library(), "upd": self._build_updates(),
                          "browse": self._build_browse(), "dl": self._build_downloads()}
            self.page = ""
            self.show_page("lib")
            self.bind("<Control-f>", lambda _e: (self.show_page("lib"), self.search_entry.focus_set()))
            self.bind("<F5>", lambda _e: self.refresh())

        def show_page(self, key):
            for fr in self.pages.values():
                fr.pack_forget()
            self.pages[key].pack(fill="both", expand=True)
            self.page = key
            for k, (lb, bar, _t) in self.tab.items():
                lb.configure(fg=T["accent"] if k == key else T["muted"])
                bar.configure(bg=T["accent"] if k == key else T["bg"])
            if key == "upd":
                self.populate_updates()
            elif key == "browse":
                self._browse_shown()

        def _browse_shown(self):
            if self.b_view == "list" and not self.browse_items and not self.b_loading:
                self.browse_start()
            elif self.b_have_sig is not None and frozenset(self._b_have()) != self.b_have_sig and self.b_view == "list":
                self._browse_render()                    # mods were installed or removed since the cards were drawn

        def _sync_tabs(self):
            n = sum(1 for m in self.mods if m.update == "update")
            active = sum(1 for j in self.jobs if j["status"] in ("queued", "downloading", "installing", "waiting"))
            for key, text in (("upd", "Updates" + (f"  ({n})" if n else "")),
                              ("dl", "Downloads" + (f"  ({active})" if active else ""))):
                self.tab[key][0].configure(text=text)

        # ---- Library page ---------------------------------------------------------
        def _build_library(self):
            lib = tk.Frame(self.host, bg=T["bg"])
            bar = tk.Frame(lib, bg=T["bg"])
            bar.pack(fill="x", padx=26, pady=(14, 10))
            e = ttk.Entry(bar, textvariable=self.search, width=34, font=font(10))
            e.pack(side="left")
            self.search_entry = e
            ph = tk.Label(e, text="Search mods or files…  (Ctrl+F)", fg=T["muted"], bg=T["panel2"], font=font(10))

            def placeholder(*_):
                if self.search.get() or self.focus_get() is e:
                    ph.place_forget()
                else:
                    ph.place(x=10, rely=0.5, anchor="w")
            ph.bind("<Button-1>", lambda _e: e.focus_set())
            e.bind("<FocusIn>", placeholder)
            e.bind("<FocusOut>", placeholder)
            self.search.trace_add("write", placeholder)
            placeholder()
            self.search.trace_add("write", lambda *_: self.populate())
            cb = ttk.Combobox(bar, textvariable=self.filter, state="readonly", width=20, values=FILTERS)
            cb.pack(side="left", padx=10)
            cb.bind("<<ComboboxSelected>>", lambda _e: self.populate())
            ttk.Checkbutton(bar, text="Smart grouping", variable=self.fuzzy,
                            command=self.refresh).pack(side="left", padx=6)
            ttk.Button(bar, text="Add mod…", command=self.add_mod).pack(side="right")
            self.btn_match = ttk.Button(bar, text="Match with Nexus", style="Accent.TButton",
                                        command=self.match_nexus)
            self.btn_match.pack(side="right", padx=8)
            self.btn_props = ttk.Button(bar, text="Review matches", command=self.proposals_dialog)

            body = tk.Frame(lib, bg=T["bg"])
            body.pack(fill="both", expand=True, padx=26)
            tf = tk.Frame(body, bg=T["panel"])
            tf.pack(side="left", fill="both", expand=True)
            cols = [("state", "STATUS", 118, "w"), ("name", "MOD", 320, "w"),
                    ("installed", "INSTALLED", 118, "w"), ("latest", "LATEST", 104, "w"),
                    ("update", "UPDATE", 122, "w"), ("where", "INSTALLED IN", 200, "w")]
            self.col_titles = {c: t for c, t, _w, _a in cols}
            self.tree = ttk.Treeview(tf, columns=[c[0] for c in cols], show="headings", selectmode="extended")
            for c, t, w, a in cols:
                self.tree.heading(c, text=t, anchor="w", command=lambda c=c: self.sort_by(c))
                self.tree.column(c, width=w, anchor=a, stretch=(c == "name"), minwidth=60)
            sb = ttk.Scrollbar(tf, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscrollcommand=sb.set)
            self.tree.pack(side="left", fill="both", expand=True)
            sb.pack(side="right", fill="y")
            self.tree.tag_configure("off", foreground=T["muted"])
            self.tree.tag_configure("partial", foreground=T["amber"])
            self.tree.tag_configure("update", background=T["tint"])
            for c, bgc in NOTE_TINT.items():
                self.tree.tag_configure("c_" + c, background=bgc)
            self.tree.bind("<<TreeviewSelect>>", self.show_details)
            self.tree.bind("<ButtonRelease-1>", self.on_click)
            self.tree.bind("<space>", lambda _e: (self.toggle(), "break")[1])
            self.tree.bind("<Return>", lambda _e: (self.toggle(), "break")[1])
            self.tree.bind("<Button-3>", self.on_right_click)

            dp = tk.Frame(body, bg=T["panel"], width=360)
            dp.pack(side="right", fill="y", padx=(16, 0))
            dp.pack_propagate(False)
            inner = tk.Frame(dp, bg=T["panel"])
            inner.pack(fill="both", expand=True, padx=20, pady=18)
            self.d_name = label(inner, "", bg=T["panel"], size=15, bold=True, wraplength=310, justify="left")
            self.d_name.pack(fill="x")
            self.d_by = label(inner, "", T["muted"], T["panel"], size=9)
            self.d_by.pack(fill="x", pady=(2, 10))
            self.d_status = label(inner, "", T["muted"], T["panel"], size=10, bold=True, wraplength=310, justify="left")
            self.d_status.pack(fill="x")
            self.d_versions = label(inner, "", T["fg"], T["panel"], size=10, wraplength=310, justify="left")
            self.d_versions.pack(fill="x", pady=(8, 0))
            self.d_summary = label(inner, "", T["muted"], T["panel"], size=9, wraplength=310, justify="left")
            self.d_summary.pack(fill="x", pady=(10, 0))
            self.d_note = label(inner, "", T["cyan"], T["panel"], size=9, wraplength=310, justify="left")
            self.d_note.pack(fill="x", pady=(8, 0))
            brow = tk.Frame(inner, bg=T["panel"])
            brow.pack(fill="x", pady=(12, 12))
            self.d_btn = ttk.Button(brow, text="Open on Nexus", command=self.open_nexus)
            self.d_btn.pack(side="left")
            self.d_update = ttk.Button(brow, text="Update", style="Accent.TButton", command=self.update_selected)
            erow = tk.Frame(inner, bg=T["panel"])
            erow.pack(fill="x")
            self.d_endorse = ttk.Button(erow, text="Endorse on Nexus", command=self.endorse_selected)
            label(inner, "FILES", T["muted"], T["panel"], size=8, bold=True).pack(fill="x", pady=(8, 0))
            ff = tk.Frame(inner, bg=T["panel"])
            ff.pack(fill="both", expand=True, pady=(4, 0))
            self.d_files = tk.Text(ff, height=6, wrap="none", state="disabled", relief="flat", bd=0,
                                   bg=T["panel"], fg=T["fg"], font=("Consolas", 9), highlightthickness=0,
                                   cursor="arrow", insertwidth=0)
            fsb = ttk.Scrollbar(ff, orient="vertical", command=self.d_files.yview)
            self.d_files.configure(yscrollcommand=fsb.set)
            self.d_files.pack(side="left", fill="both", expand=True)
            fsb.pack(side="right", fill="y")
            self.d_files.tag_configure("on", foreground=T["green"])
            self.d_files.tag_configure("off", foreground=T["muted"])

            act = tk.Frame(lib, bg=T["bg"])
            act.pack(fill="x", padx=26, pady=(12, 4))
            ttk.Button(act, text="Enable", style="Accent.TButton",
                       command=lambda: self.apply(self.selected(), True)).pack(side="left")
            ttk.Button(act, text="Disable",
                       command=lambda: self.apply(self.selected(), False)).pack(side="left", padx=8)
            ttk.Button(act, text="Toggle", command=self.toggle).pack(side="left")
            mb = ttk.Menubutton(act, text="More  ▾")
            mb.pack(side="right")
            ttk.Button(act, text="All off", command=self.all_off).pack(side="right", padx=(0, 8))
            ttk.Button(act, text="All on", command=self.all_on).pack(side="right", padx=(0, 8))
            ttk.Button(act, text="✓  This setup works", command=self.mark_good).pack(side="right", padx=(0, 8))
            self.more = themed_menu(mb)
            mb["menu"] = self.more
            self._fill_menu(self.more)
            self.ctx = themed_menu(self)
            self._fill_menu(self.ctx)
            return lib

        # ---- small helpers for the other pages ------------------------------------------------
        def _table(self, parent, cols, height=None, select="extended"):
            """A themed Treeview with a scrollbar. cols: [(id, title, width, anchor, stretch)]"""
            fr = tk.Frame(parent, bg=T["panel"])
            tv = ttk.Treeview(fr, columns=[c[0] for c in cols], show="headings", selectmode=select)
            for c, t, w, a, st in cols:
                tv.heading(c, text=t, anchor=a)
                tv.column(c, width=w, anchor=a, stretch=st, minwidth=40)
            sb = ttk.Scrollbar(fr, orient="vertical", command=tv.yview)
            tv.configure(yscrollcommand=sb.set)
            tv.pack(side="left", fill="both", expand=True)
            sb.pack(side="right", fill="y")
            if height:
                tv.configure(height=height)
            return fr, tv

        def _page_head(self, page, title, sub=""):
            top = tk.Frame(page, bg=T["bg"])
            top.pack(fill="x", padx=26, pady=(16, 10))
            left = tk.Frame(top, bg=T["bg"])
            left.pack(side="left", fill="x", expand=True)
            t = label(left, title, T["fg"], size=14, bold=True)
            t.pack(fill="x")
            s = label(left, sub, T["muted"], size=9, wraplength=720, justify="left")
            s.pack(fill="x", pady=(2, 0))
            return top, t, s

        # ---- Updates page --------------------------------------------------------------------------
        def _build_updates(self):
            f = tk.Frame(self.host, bg=T["bg"])
            top, self.upd_title, self.upd_sub = self._page_head(f, "Updates", "")
            ttk.Button(top, text="Update all", style="Accent.TButton", command=self.update_all).pack(side="right")
            ttk.Button(top, text="Update selected", command=lambda: self.update_mods(self.upd_selected())
                       ).pack(side="right", padx=8)
            ttk.Button(top, text="Check now", command=self.check_updates).pack(side="right")
            fr, self.upd_tree = self._table(f, [
                ("mod", "MOD", 300, "w", True), ("installed", "YOU HAVE", 110, "w", False),
                ("latest", "LATEST", 110, "w", False), ("when", "UPDATED ON NEXUS", 150, "w", False),
                ("note", "", 340, "w", True)])
            fr.pack(fill="both", expand=True, padx=26)
            self.upd_tree.tag_configure("update", foreground=T["orange"])
            self.upd_tree.tag_configure("maybe", foreground=T["amber"])
            self.upd_tree.tag_configure("pinned", foreground=T["muted"])
            self.upd_tree.bind("<Double-1>", lambda _e: self.update_mods(self.upd_selected()))
            row = tk.Frame(f, bg=T["bg"])
            row.pack(fill="x", padx=26, pady=(10, 4))
            ttk.Button(row, text="What changed?", command=self.show_changelog).pack(side="left")
            ttk.Button(row, text="Open on Nexus", command=self.open_upd_page).pack(side="left", padx=8)
            ttk.Button(row, text="Skip this update", command=lambda: self.pin_selected("skip")).pack(side="left")
            ttk.Button(row, text="Stay on this version", command=lambda: self.pin_selected("stay")).pack(side="left", padx=8)
            ttk.Button(row, text="Unpin", command=self.unpin_selected).pack(side="left")
            self.upd_hint = label(f, "", T["muted"], size=9, wraplength=1100, justify="left")
            self.upd_hint.pack(fill="x", padx=28, pady=(6, 0))
            return f

        def upd_selected(self):
            by = {m.key: m for m in self.mods}
            return [by[i] for i in self.upd_tree.selection() if i in by]

        def populate_updates(self):
            tv = self.upd_tree
            keep = set(tv.selection())
            tv.delete(*tv.get_children())
            rows = [m for m in self.mods if m.update in ("update", "maybe", "pinned")]
            rows.sort(key=lambda m: (UPDATE_RANK[m.update], m.name.lower()))
            for m in rows:
                info = m.nexus or {}
                note = ("A newer version is on Nexus." if m.update == "update" else m.update_note) or ""
                tv.insert("", "end", iid=m.key, tags=(m.update,), values=(
                    m.name, m.installed_version or "unknown", m.latest_version or "—",
                    fmt_date(info.get("updated")) or "—", note))
            tv.selection_set([k for k in keep if tv.exists(k)])
            n = sum(1 for m in rows if m.update == "update")
            npin = sum(1 for m in rows if m.update == "pinned")
            self.upd_title.configure(text=f"{n} update{'s' if n != 1 else ''} available" if n else "Everything is up to date")
            linked = sum(1 for m in self.mods if m.nexus_id)
            last = self.mgr.state.get("last_check", 0) if self.mgr else 0
            self.upd_sub.configure(text=(f"{linked} of {len(self.mods)} mods are linked to Nexus"
                                         + (f"  ·  last checked {time.strftime('%d %b %H:%M', time.localtime(last))}" if last else "")
                                         + (f"  ·  {npin} pinned (listed last, in grey)" if npin else "")
                                         + ("  ·  “possible” updates only mean the page changed after you installed."
                                            if any(m.update == 'maybe' for m in rows) else "")))
            self.upd_hint.configure(text=(
                "How updating works: the app asks Nexus which file replaced yours, downloads it, backs up what it "
                "overwrites (_disabled_mods/_backup), installs it, and keeps the mod switched on or off as it was.  "
                "Premium accounts download straight away. With a free account Nexus needs one click per mod on its "
                "website (“Slow download”) - the app opens the page and takes over from there.  “Skip this update” hides "
                "the version Nexus has now until a newer one comes out; “Stay on this version” hides every update for "
                "that mod. Every update can be undone in Tools → History."))
            self._sync_tabs()

        def update_all(self):
            mods = [m for m in self.mods if m.update == "update" and m.nexus_id]
            if not mods:
                messagebox.showinfo(APP_NAME, "No updates are waiting. Press “Check now” to look again.")
                return
            if messagebox.askyesno(APP_NAME, f"Update {len(mods)} mod(s)?\n\nEach one is backed up first and "
                                   "keeps its on/off state."):
                self.update_mods(mods, ask=False)

        def update_selected(self):
            self.update_mods([m for m in self.selected() if m.nexus_id])

        def open_upd_page(self):
            sel = self.upd_selected()
            if len(sel) == 1 and sel[0].nexus_id:
                webbrowser.open(sel[0].url)

        def show_changelog(self):
            sel = self.upd_selected() or [m for m in self.selected() if m.nexus_id]
            nx = self.nexus_client()
            if len(sel) != 1 or not nx or not sel[0].nexus_id:
                messagebox.showinfo(APP_NAME, "Select one mod to read its changelog.")
                return
            m = sel[0]
            self.bg(lambda: nx.changelog(m.nexus_id), lambda data: self._changelog_dialog(m, data),
                    lambda e: messagebox.showwarning(APP_NAME, str(e)))

        def _changelog_dialog(self, m, data):
            d = self.dialog(f"Changelog - {m.name}", 640, 520, resizable=True)
            tk.Label(d, text=m.name, fg=T["fg"], bg=T["bg"], font=font(13, True), anchor="w").pack(
                fill="x", padx=24, pady=(20, 8))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=24, pady=16)
            txt = tk.Text(d, wrap="word", relief="flat", bd=0, bg=T["panel"], fg=T["fg"], font=font(10),
                          padx=14, pady=10, highlightthickness=0)
            txt.pack(fill="both", expand=True, padx=24)
            vers = sorted(data, key=functools.cmp_to_key(lambda a, b: compare_versions(a, b) or 0), reverse=True)
            txt.tag_configure("v", foreground=T["accent"], font=font(10, True))
            for v in vers:
                txt.insert("end", f"{v}\n", "v")
                lines = data[v] if isinstance(data[v], list) else [str(data[v])]
                for line in lines:
                    txt.insert("end", "  • " + html.unescape(re.sub(r"<[^>]+>", "", str(line))).strip() + "\n")
                txt.insert("end", "\n")
            if not vers:
                txt.insert("end", "The author hasn't written a changelog on Nexus.")
            txt.configure(state="disabled")
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")

        # ---- Browse Nexus page ------------------------------------------------------------------------
        CARD_W, CARD_IMG_H, CARD_H, CARD_GAP = 236, 132, 264, 14
        MAX_BROWSE = 480                       # cards kept on screen; narrow the filters to see others
        ALL_CATS = "All categories"
        SHOW_CHOICES = ("All mods", "Not installed", "Installed")

        def _build_browse(self):
            f = tk.Frame(self.host, bg=T["bg"])
            self.browse_items, self.browse_sel = [], None
            self.browse_q = tk.StringVar()
            self.b_sort = tk.StringVar(value=BROWSE_SORTS[0][0])
            self.b_cat = tk.StringVar(value=self.ALL_CATS)
            self.b_tag, self.b_author = tk.StringVar(), tk.StringVar()
            self.b_show = tk.StringVar(value=self.SHOW_CHOICES[0])
            self.b_period = tk.StringVar(value=PERIODS[0][0])
            self.b_from, self.b_to = tk.StringVar(), tk.StringVar()
            self.b_hide_adult = tk.BooleanVar(value=bool(self.cfg.get("hide_adult", True)))
            self.b_gen, self.b_loading, self.b_more = 0, False, False
            self.b_total, self.b_next, self.b_q, self.b_notes = None, 0, {}, []
            self.b_cards, self.b_cols, self.b_colmax = [], 0, 1
            self.b_view, self.b_sort_touched, self.b_have_sig = "list", False, None
            self.b_seen_tags, self.b_cats, self.b_cats_seen = Counter(), [], set()
            self.img_mem, self.img_wait, self.blank_img, self.img_local = {}, {}, {}, False
            self.img_pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
            self.mp_gen = 0

            lv = self.b_list = tk.Frame(f, bg=T["bg"])
            lv.pack(fill="both", expand=True)
            bar = tk.Frame(lv, bg=T["bg"])
            bar.pack(fill="x", padx=26, pady=(14, 6))
            e = ttk.Entry(bar, textvariable=self.browse_q, width=36, font=font(10))
            e.pack(side="left")
            e.bind("<Return>", lambda _e: self.browse_run())
            self.b_entry = e
            ttk.Button(bar, text="Search", style="Accent.TButton", command=self.browse_run).pack(side="left", padx=8)
            label(bar, "Sort by", T["muted"], size=9).pack(side="left", padx=(12, 6))
            cb = ttk.Combobox(bar, textvariable=self.b_sort, state="readonly", width=17,
                              values=[s[0] for s in BROWSE_SORTS])
            cb.pack(side="left")
            cb.bind("<<ComboboxSelected>>", self._b_sort_picked)
            label(bar, "Period", T["muted"], size=9).pack(side="left", padx=(14, 6))
            self.b_period_cb = ttk.Combobox(bar, textvariable=self.b_period, state="readonly", width=15,
                                            values=[n for n, _d in PERIODS] + [CUSTOM_PERIOD])
            self.b_period_cb.pack(side="left")
            self.b_period_cb.bind("<<ComboboxSelected>>", self._b_period_picked)
            ttk.Button(bar, text="Reset filters", command=self.browse_reset).pack(side="left", padx=12)
            self.b_count = label(bar, "", T["muted"], size=9)
            self.b_count.pack(side="right")

            bar2 = tk.Frame(lv, bg=T["bg"])
            bar2.pack(fill="x", padx=26, pady=(0, 8))
            label(bar2, "Category", T["muted"], size=9).pack(side="left", padx=(0, 6))
            self.b_cat_cb = ttk.Combobox(bar2, textvariable=self.b_cat, state="readonly", width=24,
                                         values=[self.ALL_CATS])
            self.b_cat_cb.pack(side="left")
            self.b_cat_cb.bind("<<ComboboxSelected>>", lambda _e: self.browse_run())
            label(bar2, "Tag", T["muted"], size=9).pack(side="left", padx=(16, 6))
            self.b_tag_cb = ttk.Combobox(bar2, textvariable=self.b_tag, width=17, values=[""])
            self.b_tag_cb.pack(side="left")
            self.b_tag_cb.bind("<<ComboboxSelected>>", lambda _e: self.browse_run())
            self.b_tag_cb.bind("<Return>", lambda _e: self.browse_run())
            label(bar2, "Author", T["muted"], size=9).pack(side="left", padx=(16, 6))
            ea = ttk.Entry(bar2, textvariable=self.b_author, width=15, font=font(10))
            ea.pack(side="left")
            ea.bind("<Return>", lambda _e: self.browse_run())
            label(bar2, "Show", T["muted"], size=9).pack(side="left", padx=(16, 6))
            sh = ttk.Combobox(bar2, textvariable=self.b_show, state="readonly", width=13, values=self.SHOW_CHOICES)
            sh.pack(side="left")
            sh.bind("<<ComboboxSelected>>", lambda _e: self._browse_render())
            ttk.Checkbutton(bar2, text="Hide adult content", variable=self.b_hide_adult,
                            command=self._adult_toggled).pack(side="left", padx=18)

            rr = self.b_range_row = tk.Frame(lv, bg=T["bg"])            # only shown for "Custom range…"
            label(rr, "From", T["muted"], size=9).pack(side="left", padx=(0, 6))
            ef = ttk.Entry(rr, textvariable=self.b_from, width=12, font=font(10))
            ef.pack(side="left")
            label(rr, "To", T["muted"], size=9).pack(side="left", padx=(14, 6))
            et = ttk.Entry(rr, textvariable=self.b_to, width=12, font=font(10))
            et.pack(side="left")
            ttk.Button(rr, text="Go", style="Accent.TButton", command=self.browse_run).pack(side="left", padx=12)
            label(rr, "day/month/year, for example 31/10/2026", T["muted"], size=9).pack(side="left")
            for e_ in (ef, et):
                e_.bind("<Return>", lambda _e: self.browse_run())
            self.b_bar2 = bar2

            gw = tk.Frame(lv, bg=T["bg"])
            gw.pack(fill="both", expand=True, padx=26)
            cv = self.b_canvas = tk.Canvas(gw, bg=T["bg"], highlightthickness=0, yscrollincrement=40)
            vsb = ttk.Scrollbar(gw, orient="vertical", command=cv.yview)
            cv.configure(yscrollcommand=lambda lo, hi: self._b_scrolled(vsb, lo, hi))
            vsb.pack(side="right", fill="y")
            cv.pack(side="left", fill="both", expand=True)
            self.b_inner = tk.Frame(cv, bg=T["bg"])
            self.b_win = cv.create_window((0, 0), window=self.b_inner, anchor="nw")
            self.b_inner.bind("<Configure>", lambda _e: cv.configure(scrollregion=cv.bbox("all")))
            cv.bind("<Configure>", self._b_resized)
            for ev in ("<MouseWheel>", "<Button-4>", "<Button-5>"):
                self.bind_all(ev, self._b_wheel, add="+")

            foot = tk.Frame(lv, bg=T["bg"])
            foot.pack(fill="x", padx=26, pady=(6, 0))
            self.b_more_btn = ttk.Button(foot, text="Load more", command=self.browse_more)
            self.b_foot = label(foot, "", T["muted"], size=9, wraplength=1000, justify="left")
            self.b_foot.pack(side="left", fill="x", expand=True)

            self.b_page = self._build_modpage(f)
            self.b_files_data = []
            return f

        # -- helpers -------------------------------------------------------------------------------------
        def _blank(self, w, h):
            if (w, h) not in self.blank_img:
                im = tk.PhotoImage(width=w, height=h)
                im.put(T["panel2"], to=(0, 0, w, h))
                self.blank_img[(w, h)] = im
            return self.blank_img[(w, h)]

        def _photo(self, png):
            if not png:
                return None
            try:
                return tk.PhotoImage(data=base64.b64encode(png))
            except tk.TclError:
                return None

        def _load_image(self, url, w, h, mode, cb):
            """Show a Nexus picture: cb(photo or None) runs on the screen thread when it is ready."""
            key = (url, w, h, mode)
            if not url:
                cb(None)
                return
            if key in self.img_mem:
                cb(self.img_mem[key])
                return
            waiters = self.img_wait.setdefault(key, [])
            waiters.append(cb)
            if len(waiters) > 1:
                return
            local = self.img_local

            def done(png):
                photo = self._photo(png)
                if len(self.img_mem) > 400:
                    self.img_mem.pop(next(iter(self.img_mem)))
                if photo:
                    self.img_mem[key] = photo
                for fn in self.img_wait.pop(key, []):
                    try:
                        fn(photo)
                    except tk.TclError:
                        pass                       # the card was closed while the picture was on its way

            def work():
                try:
                    png = image_png(url, w, h, mode, local)
                except Exception:      # noqa - a picture that fails just stays a placeholder
                    png = None
                self.job_q.put(("cb", done, png))
            try:
                self.img_pool.submit(work)
            except RuntimeError:
                self.img_wait.pop(key, None)

        def _show_view(self, which):
            self.b_view = which
            self.b_list.pack_forget()
            self.b_page.pack_forget()
            (self.b_list if which == "list" else self.b_page).pack(fill="both", expand=True)

        def _b_wheel(self, e):
            if self.page != "browse" or self.b_view != "list":
                return
            if not str(e.widget).startswith(str(self.b_canvas.master)):      # only while the pointer is on the grid
                return
            up = getattr(e, "num", 0) == 4 or getattr(e, "delta", 0) > 0
            self.b_canvas.yview_scroll(-3 if up else 3, "units")

        def _b_scrolled(self, vsb, lo, hi):
            vsb.set(lo, hi)
            if float(hi) > 0.93 and self.b_more and not self.b_loading and self.b_cards:
                self.after_idle(self.browse_more)

        def _b_resized(self, e):
            self.b_canvas.itemconfigure(self.b_win, width=e.width)
            cols = max(1, e.width // (self.CARD_W + self.CARD_GAP))
            if cols != self.b_cols:
                self.b_cols = cols
                self._regrid()

        def _regrid(self):
            cols = max(1, self.b_cols)
            for i, c in enumerate(self.b_cards):
                c.grid(row=i // cols, column=i % cols, padx=self.CARD_GAP // 2, pady=self.CARD_GAP // 2, sticky="n")
            for c in range(max(cols, self.b_colmax)):
                self.b_inner.columnconfigure(c, weight=1 if c < cols else 0)
            self.b_colmax = cols

        def _b_message(self, text, button=None):
            for w in self.b_inner.grid_slaves():
                if getattr(w, "_is_msg", False):
                    w.destroy()
            box = tk.Frame(self.b_inner, bg=T["bg"])
            box._is_msg = True
            tk.Label(box, text=text, fg=T["muted"], bg=T["bg"], font=font(11), wraplength=620,
                     justify="center").pack(pady=(60, 10))
            if button:
                ttk.Button(box, text=button[0], command=button[1]).pack()
            box.grid(row=0, column=0, columnspan=max(1, self.b_cols), sticky="n", pady=10)

        def _b_have(self):
            return {m.nexus_id for m in self.mods if m.nexus_id}

        def _b_pass(self, it, have=None):
            have = self._b_have() if have is None else have
            if self.b_hide_adult.get() and it.get("adult"):
                return False
            show = self.b_show.get()
            return not ((show == "Not installed" and it["id"] in have) or (show == "Installed" and it["id"] not in have))

        # -- running a search ---------------------------------------------------------------------------
        def browse_start(self):
            nx = self.nexus_client(ask=False)
            if not nx:
                self._b_message("Add your Nexus API key in Settings to browse Nexus here.",
                                ("Open Settings", self.open_settings))
                return
            if not self.b_cats:
                self.bg(nx.categories, self._set_cats, lambda _e: None)
            self.browse_run()

        def _set_cats(self, cats):
            self.b_cats = list(cats)
            self._refresh_filter_values()

        def _refresh_filter_values(self):
            self.b_tag_cb["values"] = [""] + [t for t, _n in self.b_seen_tags.most_common(60)]
            names = sorted(set(self.b_cats) | self.b_cats_seen, key=str.lower)
            self.b_cat_cb["values"] = [self.ALL_CATS] + names

        def _b_sort_picked(self, *_):
            self.b_sort_touched = True
            self.browse_run()

        def _b_period_picked(self, *_):
            if self.b_period.get() == CUSTOM_PERIOD:
                if not self.b_from.get().strip() and not self.b_to.get().strip():
                    today = datetime.now()
                    self.b_to.set(today.strftime("%d/%m/%Y"))
                    self.b_from.set((today - timedelta(days=30)).strftime("%d/%m/%Y"))
                self.b_range_row.pack(fill="x", padx=26, pady=(0, 8), after=self.b_bar2)
            else:
                self.b_range_row.pack_forget()
            self.browse_run()

        def _adult_toggled(self):
            v = bool(self.b_hide_adult.get())
            self.cfg["hide_adult"] = v
            save_config(hide_adult=v)
            self.browse_run()

        def browse_reset(self):
            self.browse_q.set("")
            self.b_cat.set(self.ALL_CATS)
            self.b_tag.set("")
            self.b_author.set("")
            self.b_show.set(self.SHOW_CHOICES[0])
            self.b_sort.set(BROWSE_SORTS[0][0])
            self.b_period.set(PERIODS[0][0])
            self.b_range_row.pack_forget()
            self.b_sort_touched = False
            self.browse_run()

        def _browse_query(self):
            term = self.browse_q.get().strip()
            words = spaced_words(term) or ([term] if term else [])
            row = next((s for s in BROWSE_SORTS if s[0] == self.b_sort.get()), BROWSE_SORTS[0])
            cat = self.b_cat.get()
            label_ = self.b_period.get()
            since, until = period_range(label_, self.b_from.get(), self.b_to.get())     # ValueError: unreadable date
            period = ({"field": "updatedAt" if row[1] == "updatedAt" else "createdAt", "since": since, "until": until,
                       "label": label_} if (since or until) else None)
            return {"term": " ".join(words), "words": words, "sort": row[1],
                    "category": "" if cat == self.ALL_CATS else cat, "tag": self.b_tag.get().strip(),
                    "author": self.b_author.get().strip(), "hide_adult": bool(self.b_hide_adult.get()),
                    "period": period}

        def _browse_clear(self):
            for w in self.b_inner.winfo_children():
                w.destroy()
            self.b_cards = []
            self.browse_items = []
            self.b_next, self.b_total, self.b_more, self.b_notes = 0, None, False, []
            self.b_canvas.yview_moveto(0)
            self.b_more_btn.pack_forget()

        def browse_run(self, *_):
            nx = self.nexus_client()
            if not nx:
                return
            self.img_local = nx.local
            if self.b_view != "list":
                self._show_view("list")
            term = self.browse_q.get().strip()
            if term and not self.b_sort_touched:
                self.b_sort.set("Best match")
            elif not term and self.b_sort.get() == "Best match":
                self.b_sort.set(BROWSE_SORTS[0][0])
            try:
                q = self._browse_query()
            except ValueError as e:
                self.status.set(str(e))
                messagebox.showinfo(APP_NAME, str(e))
                return
            self.b_gen += 1
            self.b_q = q
            self._browse_clear()
            self._browse_fetch(nx, 0, True)

        def browse_more(self):
            if self.b_loading or not self.b_more:
                return
            nx = self.nexus_client(ask=False)
            if nx:
                self._browse_fetch(nx, self.b_next, False)

        def _browse_fetch(self, nx, offset, reset):
            self.b_loading, gen, q = True, self.b_gen, dict(self.b_q)
            self.b_foot.configure(text="Loading…" if reset else "Loading more…")
            self.b_more_btn.pack_forget()

            def work():
                if q["sort"] is None:                      # "Trending": Nexus' own top-10 list
                    items = nx.listing("trending")
                    return {"items": items, "total": len(items), "next": len(items), "more": False,
                            "notes": ["Trending is Nexus' own top-10 list: no pages and no filters."]}
                kw = dict(sort=q["sort"], category=q["category"], tag=q["tag"], author=q["author"],
                          offset=offset, count=BROWSE_PAGE, hide_adult=q["hide_adult"], period=q["period"])
                res = nx.browse(term=q["term"], **kw)
                if not res["items"] and offset == 0 and len(q["words"]) > 1:
                    res = nx.browse(term="".join(q["words"]), **kw)        # "NativeSettings" style names
                return res
            self.bg(work, lambda r: self._browse_loaded(gen, r, reset), lambda e: self._browse_failed(gen, e))

        def _browse_failed(self, gen, err):
            if gen != self.b_gen:
                return
            self.b_loading = False
            self.b_foot.configure(text="")
            if not self.browse_items:
                self.b_count.configure(text="")
                self._b_message(f"Couldn't load Nexus:\n{nexus_error_text(err)}", ("Try again", self.browse_run))
            self.status.set(nexus_error_text(err).replace("\n", " "))

        def _browse_loaded(self, gen, res, reset):
            if gen != self.b_gen:
                return
            self.b_loading = False
            known = {i["id"] for i in self.browse_items}
            new = [it for it in res["items"] if it["id"] not in known]
            self.browse_items += new
            self.b_next, self.b_total, self.b_notes = res["next"], res["total"], res["notes"]
            self.b_more = bool(res["more"]) and len(self.browse_items) < self.MAX_BROWSE and self.b_next < 2000
            for it in new:
                self.b_seen_tags.update(it.get("tags", []))
                if it.get("category"):
                    self.b_cats_seen.add(it["category"])
            self._refresh_filter_values()
            added = self._browse_add_cards(new)
            self._browse_footer()
            if not self.b_cards and not self.b_more:
                self._b_message("Nothing found.\nTry other words, or press “Reset filters”.")
            elif not added and self.b_more:
                self.after(80, self.browse_more)           # everything on this page was filtered out

        def _browse_footer(self):
            bits = [f"{len(self.b_cards)} shown"]
            if self.b_total:
                bits.append(f"{self.b_total:,} on Nexus")
            self.b_count.configure(text="  ·  ".join(bits))
            pt = period_text(self.b_q.get("period")) if self.b_q.get("sort") else ""
            txt = "  ".join(([f"Mods {pt}."] if pt else []) + list(self.b_notes))
            if PILImage is None:
                txt = (txt + "  Pictures need the Pillow add-on; the .exe has it.").strip()
            self.b_foot.configure(text=txt)
            self.b_more_btn.pack_forget()
            if self.b_more and not self.b_loading:
                self.b_more_btn.pack(side="right")

        def _browse_render(self):
            """Rebuild the grid from what is loaded (after changing 'Show')."""
            for w in self.b_inner.winfo_children():
                w.destroy()
            self.b_cards = []
            self.b_have_sig = frozenset(self._b_have())
            self._browse_add_cards(self.browse_items)
            self._browse_footer()
            if not self.b_cards:
                self._b_message("Nothing to show with this filter." if self.browse_items else "")
            self.b_canvas.yview_moveto(0)

        # -- cards ----------------------------------------------------------------------------------------
        def _browse_add_cards(self, items):
            have = self._b_have()
            self.b_have_sig = frozenset(have)
            n = 0
            for w in self.b_inner.grid_slaves():
                if getattr(w, "_is_msg", False):
                    w.destroy()
            for it in items:
                if self._b_pass(it, have):
                    self.b_cards.append(self._make_card(it, it["id"] in have))
                    n += 1
            self._regrid()
            return n

        def _make_card(self, it, mine):
            W, P = self.CARD_W, T["panel"]
            card = tk.Frame(self.b_inner, bg=P, width=W, height=self.CARD_H, cursor="hand2")
            card.pack_propagate(False)
            img = tk.Label(card, bg=T["panel2"], image=self._blank(W, self.CARD_IMG_H), bd=0)
            img.pack()
            if mine:
                tk.Label(img, text=" ✓ In your library ", bg=T["green"], fg="#06210f",
                         font=font(8, True)).place(x=8, y=8)
            if it.get("adult"):
                tk.Label(img, text=" 18+ ", bg=T["red"], fg="#ffffff", font=font(8, True)).place(relx=1.0, x=-8, y=8,
                                                                                               anchor="ne")
            tk.Label(card, text=it["name"], bg=P, fg=T["fg"], font=font(10, True), wraplength=W - 26,
                     justify="left", anchor="nw", height=2).pack(fill="x", padx=12, pady=(10, 0))
            meta = "  ·  ".join(x for x in (it.get("author"), it.get("category")) if x)
            tk.Label(card, text=meta if len(meta) < 40 else meta[:38] + "…", bg=P, fg=T["muted"], font=font(9),
                     anchor="w").pack(fill="x", padx=12, pady=(2, 0))
            stats = "  ·  ".join(x for x in (
                f"{human_count(it['downloads'])} downloads" if it.get("downloads") else "",
                f"{human_count(it['endorsements'])} endorsed" if it.get("endorsements") else "") if x)
            tk.Label(card, text=stats, bg=P, fg=T["fg"], font=font(9), anchor="w").pack(fill="x", padx=12, pady=(4, 0))
            if it.get("updated"):
                tk.Label(card, text=f"Updated {fmt_date(it['updated'])}", bg=P, fg=T["muted"], font=font(9),
                         anchor="w").pack(fill="x", padx=12, pady=(1, 0))
            card._img, card._it = img, it

            def hover(on):
                col = T["panel2"] if on else P
                card.configure(bg=col)
                for w in card.winfo_children():
                    if w is not img:
                        w.configure(bg=col)

            def leave(_e):
                x, y = card.winfo_pointerxy()
                w = card.winfo_containing(x, y)
                if w is None or not str(w).startswith(str(card)):
                    hover(False)
            card.bind("<Enter>", lambda _e: hover(True))
            card.bind("<Leave>", leave)

            def tie(w):
                w.bind("<Button-1>", lambda _e, i=it: self.open_modpage(i))
                for c in w.winfo_children():
                    tie(c)
            tie(card)

            def set_img(photo, it=it):
                if not img.winfo_exists():
                    return
                if photo:
                    img.configure(image=photo)
                    img.image = photo
                else:
                    initials = "".join(w[0] for w in it["name"].split()[:2]).upper() or "?"
                    img.configure(text=initials, fg=T["muted"], font=font(26, True), compound="center")
            self._load_image(it.get("thumb") or it.get("picture"), W, self.CARD_IMG_H, "cover", set_img)
            return card

        # ---- one mod's page ------------------------------------------------------------------------------
        def _rich_text(self, parent):
            fr = tk.Frame(parent, bg=T["panel"])
            txt = tk.Text(fr, wrap="word", relief="flat", bd=0, bg=T["panel"], fg=T["fg"], font=font(10), padx=16,
                          pady=12, highlightthickness=0, cursor="arrow", spacing1=1, spacing3=2)
            sb = ttk.Scrollbar(fr, orient="vertical", command=txt.yview)
            txt.configure(yscrollcommand=sb.set)
            sb.pack(side="right", fill="y")
            txt.pack(side="left", fill="both", expand=True)
            for tag, kw in {"b": dict(font=font(10, True)), "i": dict(font=(FONT, 10, "italic")),
                            "u": dict(underline=True), "s": dict(overstrike=True),
                            "h1": dict(font=font(16, True), foreground=T["accent"], spacing1=10),
                            "h2": dict(font=font(13, True), foreground=T["fg"], spacing1=8),
                            "h3": dict(font=font(11, True), foreground=T["accent"], spacing1=6),
                            "center": dict(justify="center"), "dim": dict(foreground=T["muted"]),
                            "quote": dict(lmargin1=18, lmargin2=18, foreground=T["muted"]),
                            "code": dict(font=("Consolas", 10), background=T["panel2"])}.items():
                txt.tag_configure(tag, **kw)
            txt.configure(state="disabled")
            return fr, txt

        def _fill_rich(self, txt, runs, links=()):
            txt.configure(state="normal")
            txt.delete("1.0", "end")
            for t in list(txt.tag_names()):
                if t.startswith("link"):
                    txt.tag_delete(t)
            for i, url in enumerate(links):
                tag = f"link{i}"
                txt.tag_configure(tag, foreground=T["cyan"], underline=True)
                txt.tag_bind(tag, "<Button-1>", lambda _e, u=url: self._open_link(u))
                txt.tag_bind(tag, "<Enter>", lambda _e: txt.configure(cursor="hand2"))
                txt.tag_bind(tag, "<Leave>", lambda _e: txt.configure(cursor="arrow"))
            for text_, styles in runs:
                txt.insert("end", text_, styles)
            txt.configure(state="disabled")

        def _open_link(self, url):
            if str(url).lower().startswith(("http://", "https://")):      # never anything else
                webbrowser.open(url)

        def _build_modpage(self, parent):
            pg = tk.Frame(parent, bg=T["bg"])
            top = tk.Frame(pg, bg=T["bg"])
            top.pack(fill="x", padx=26, pady=(14, 8))
            ttk.Button(top, text="←  Back to results", command=self.modpage_back).pack(side="left")
            self.mp_note = label(top, "", T["muted"], size=9)
            self.mp_note.pack(side="left", padx=14)
            body = tk.Frame(pg, bg=T["bg"])
            body.pack(fill="both", expand=True, padx=26)
            side = tk.Frame(body, bg=T["panel"], width=372)
            side.pack(side="right", fill="y", padx=(16, 0))
            side.pack_propagate(False)
            left = tk.Frame(body, bg=T["bg"])
            left.pack(side="left", fill="both", expand=True)
            self.mp_left = left

            hero_box = tk.Frame(left, bg=T["panel"], height=290)
            hero_box.pack(fill="x")
            hero_box.pack_propagate(False)
            self.mp_hero = tk.Label(hero_box, bg=T["panel"], fg=T["muted"], font=font(11), bd=0)
            self.mp_hero.place(relx=0.5, rely=0.5, anchor="center")
            self.mp_strip = tk.Frame(left, bg=T["bg"])
            self.mp_strip.pack(fill="x", pady=(8, 0))
            tabs = tk.Frame(left, bg=T["bg"])
            tabs.pack(fill="x", pady=(6, 0))
            content = tk.Frame(left, bg=T["panel"])
            content.pack(fill="both", expand=True)
            self.mp_tabs, self.mp_tab_btn = {}, {}
            d_fr, self.mp_desc = self._rich_text(content)
            c_fr, self.mp_log = self._rich_text(content)
            f_fr, self.mp_files = self._table(content, [
                ("name", "FILE", 280, "w", True), ("ver", "VERSION", 90, "w", False), ("kind", "TYPE", 110, "w", False),
                ("size", "SIZE", 80, "e", False), ("when", "UPLOADED", 100, "w", False)], select="browse")
            r_fr, self.mp_reqs = self._table(content, [
                ("name", "NEEDS", 240, "w", True), ("note", "NOTE", 260, "w", True),
                ("have", "IN YOUR LIBRARY", 120, "w", False)], select="browse")
            self.mp_files.bind("<<TreeviewSelect>>", self._mp_file_picked)
            self.mp_files.tag_configure("old", foreground=T["muted"])
            self.mp_reqs.bind("<Double-1>", self._mp_req_open)
            for key, text, fr in (("desc", "Description", d_fr), ("files", "Files", f_fr),
                                  ("reqs", "Requirements", r_fr), ("log", "Changelog", c_fr)):
                self.mp_tabs[key] = fr
                b = tk.Label(tabs, text=text, fg=T["muted"], bg=T["bg"], font=font(10, True), padx=14, pady=6,
                             cursor="hand2")
                b.pack(side="left")
                b.bind("<Button-1>", lambda _e, k=key: self._mp_tab(k))
                self.mp_tab_btn[key] = b

            inner = tk.Frame(side, bg=T["panel"])
            inner.pack(fill="both", expand=True, padx=20, pady=18)
            self.b_name = label(inner, "", bg=T["panel"], size=15, bold=True, wraplength=330, justify="left")
            self.b_name.pack(fill="x")
            self.b_by = tk.Label(inner, text="", fg=T["cyan"], bg=T["panel"], font=font(10), anchor="w", cursor="hand2")
            self.b_by.pack(fill="x", pady=(2, 8))
            self.b_by.bind("<Button-1>", lambda _e: self._mp_filter("author", self.browse_sel.get("author", "")))
            self.mp_chips = tk.Frame(inner, bg=T["panel"])
            self.mp_chips.pack(fill="x")
            self.mp_statbox = tk.Frame(inner, bg=T["panel"])
            self.mp_statbox.pack(fill="x", pady=(12, 0))
            self.b_sum = label(inner, "", T["muted"], T["panel"], size=9, wraplength=330, justify="left")
            self.b_sum.pack(fill="x", pady=(10, 0))
            label(inner, "FILE TO INSTALL", T["muted"], T["panel"], size=8, bold=True).pack(fill="x", pady=(16, 4))
            self.b_file = tk.StringVar()
            self.b_files = ttk.Combobox(inner, textvariable=self.b_file, state="readonly", values=[])
            self.b_files.pack(fill="x")
            self.b_note = label(inner, "", T["muted"], T["panel"], size=9, wraplength=330, justify="left")
            self.b_note.pack(fill="x", pady=(8, 0))
            row = tk.Frame(inner, bg=T["panel"])
            row.pack(fill="x", pady=(14, 0))
            ttk.Button(row, text="Open on Nexus", command=self.browse_open).pack(side="left")
            self.b_install = ttk.Button(row, text="Download & install", style="Accent.TButton",
                                        command=self.browse_install)
            self.b_install.pack(side="right")
            self._mp_tab("desc")
            return pg

        def _mp_tab(self, key):
            for k, fr in self.mp_tabs.items():
                fr.pack_forget()
                self.mp_tab_btn[k].configure(fg=T["accent"] if k == key else T["muted"])
            self.mp_tabs[key].pack(fill="both", expand=True)

        def modpage_back(self):
            self.mp_gen += 1
            self._show_view("list")
            if self.b_have_sig is not None and frozenset(self._b_have()) != self.b_have_sig:
                self._browse_render()                # things were installed meanwhile: refresh the badges

        def _mp_filter(self, kind, value):
            if not value:
                return
            {"tag": self.b_tag, "author": self.b_author, "category": self.b_cat}[kind].set(value)
            self.browse_run()

        def _mp_fill_basic(self, it):
            self.b_name.configure(text=it["name"])
            self.b_by.configure(text=f"by {it['author']}" if it.get("author") else "")
            for w in self.mp_chips.winfo_children():
                w.destroy()
            used, row, col = 0, 0, 0
            chips = ([("category", it["category"])] if it.get("category") else []) + \
                    [("tag", t) for t in it.get("tags", [])[:14]]
            for kind, text in chips:
                wpx = len(text) * 7 + 24
                if used + wpx > 330 and used:
                    row, col, used = row + 1, 0, 0
                c = tk.Label(self.mp_chips, text=text, bg=T["panel2"], fg=T["accent"] if kind == "category" else T["muted"],
                             font=font(9), padx=8, pady=2, cursor="hand2")
                c.grid(row=row, column=col, padx=(0, 6), pady=(0, 6), sticky="w")
                c.bind("<Button-1>", lambda _e, k=kind, v=text: self._mp_filter(k, v))
                col, used = col + 1, used + wpx + 6
            for w in self.mp_statbox.winfo_children():
                w.destroy()
            rows = [("Version", it.get("version", "")),
                    ("Downloads", f"{it['downloads']:,}" if it.get("downloads") else ""),
                    ("Endorsements", f"{it['endorsements']:,}" if it.get("endorsements") else ""),
                    ("Updated", fmt_date(it["updated"]) if it.get("updated") else ""),
                    ("Created", fmt_date(it["created"]) if it.get("created") else ""),
                    ("Adult content", "Yes" if it.get("adult") else "")]
            for i, (k, v) in enumerate([r for r in rows if r[1]]):
                tk.Label(self.mp_statbox, text=k, fg=T["muted"], bg=T["panel"], font=font(9), anchor="w", width=13).grid(
                    row=i, column=0, sticky="w", pady=1)
                tk.Label(self.mp_statbox, text=v, fg=T["fg"], bg=T["panel"], font=font(10), anchor="w").grid(
                    row=i, column=1, sticky="w", pady=1)
            self.b_sum.configure(text=it.get("summary", ""))
            mine = next((m for m in self.mods if m.nexus_id == it["id"]), None)
            self.b_note.configure(text=(f"Already in your library (v{mine.installed_version or '?'}). "
                                        "Installing again updates it." if mine else "Loading the file list…"))
            self.b_install.configure(text="Update" if mine else "Download & install")

        def open_modpage(self, it):
            self.mp_gen += 1
            gen = self.mp_gen
            self.browse_sel = dict(it)
            self._mp_fill_basic(it)
            self.b_files["values"] = []
            self.b_file.set("")
            self.b_files_data = []
            self.mp_note.configure(text="")
            self.mp_hero.configure(image="", text="Loading picture…")
            self.mp_hero.image = None
            for w in self.mp_strip.winfo_children():
                w.destroy()
            self._fill_rich(self.mp_desc, [("Loading the description…", ("dim",))])
            self._fill_rich(self.mp_log, [])
            self.mp_files.delete(*self.mp_files.get_children())
            self.mp_reqs.delete(*self.mp_reqs.get_children())
            self._mp_tab("desc")
            self._show_view("page")
            self.update_idletasks()
            self._mp_hero(it.get("picture") or it.get("thumb"), gen)
            nx = self.nexus_client(ask=False)
            if not nx:
                return
            self.img_local = nx.local

            def work():
                out = {"page": nx.mod_page(it["id"]), "files": {}, "changes": {}}
                for key, fn in (("files", lambda: nx.files(it["id"]) or {}), ("changes", lambda: nx.changelog(it["id"]))):
                    try:
                        out[key] = fn()
                    except NexusError as e:
                        if e.status in (401, 429):
                            raise
                return out
            self.bg(work, lambda r: self._mp_loaded(gen, r),
                    lambda e: gen == self.mp_gen and (self.mp_note.configure(text=str(e)),
                                                       self._fill_rich(self.mp_desc, [(str(e), ("dim",))])))

        def _mp_hero(self, url, gen):
            w = max(360, min(900, self.mp_left.winfo_width() - 6))

            def show(photo):
                if gen != self.mp_gen or not self.mp_hero.winfo_exists():
                    return
                if photo:
                    self.mp_hero.configure(image=photo, text="")
                    self.mp_hero.image = photo
                else:
                    self.mp_hero.configure(image="", text="No picture")
            self._load_image(url, w, 290, "fit", show)

        def _mp_loaded(self, gen, r):
            if gen != self.mp_gen:
                return
            page, files, changes = r["page"], r["files"], r["changes"]
            sel = self.browse_sel
            sel.update({k: v for k, v in page.items() if v and k not in ("notes", "requirements", "gallery", "description")})
            self._mp_fill_basic(sel)
            if page.get("notes"):
                self.mp_note.configure(text="  ".join(page["notes"]))
            runs, links = bbcode_runs(page.get("description"))
            self._fill_rich(self.mp_desc, runs or [("The author hasn't written a description.", ("dim",))], links)
            gal = page.get("gallery") or []
            if gal:
                self._mp_hero(gal[0]["url"], gen)
            for w in self.mp_strip.winfo_children():
                w.destroy()
            if len(gal) > 1:
                for g in gal[:9]:
                    lb = tk.Label(self.mp_strip, bg=T["panel2"], image=self._blank(96, 54), bd=0, cursor="hand2")
                    lb.pack(side="left", padx=(0, 6))
                    lb.bind("<Button-1>", lambda _e, u=g["url"]: self._mp_hero(u, gen))
                    self._load_image(g["thumb"], 96, 54, "cover",
                                     lambda ph, lb=lb: (ph and lb.winfo_exists()) and (lb.configure(image=ph),
                                                                                       setattr(lb, "image", ph)))
            # files: the table, and the one to install
            plan = plan_update(files, None, "")
            opts = plan["options"] or [f for f in files.get("files", []) if isinstance(f, dict)]
            self.b_files_data = opts
            self.b_files["values"] = [file_label(f) for f in opts]
            tgt = plan["target"] or (opts[0] if opts else None)
            if tgt in opts:
                self.b_files.current(opts.index(tgt))
            for f in sorted((x for x in files.get("files", []) if isinstance(x, dict)),
                            key=lambda x: -int(x.get("uploaded_timestamp") or 0)):
                cat = str(f.get("category_name") or "").title()
                size = f"{int(f['size_kb']) / 1024:.1f} MB" if f.get("size_kb") else ""
                self.mp_files.insert("", "end", iid=str(f.get("file_id")), values=(
                    f.get("name") or f.get("file_name") or "", file_version(f), cat, size,
                    fmt_date(f.get("uploaded_timestamp")) if f.get("uploaded_timestamp") else ""),
                    tags=("old",) if cat.upper() in ("OLD_VERSION", "ARCHIVED") else ())
            mine = next((m for m in self.mods if m.nexus_id == sel["id"]), None)
            if not opts:
                self.b_note.configure(text="This mod has no downloadable files.")
            elif not mine:
                self.b_note.configure(text=plan["why"] or "Choose the file you want.")
            # requirements
            have = self._b_have()
            for q in page.get("requirements", []):
                ref = parse_mod_ref(q.get("url", ""))[0] if q.get("url") else None
                self.mp_reqs.insert("", "end", iid=q.get("url") or f"r{len(self.mp_reqs.get_children())}",
                                    values=(q["name"], q.get("notes", ""), "✓ yes" if ref in have else ""))
            if not page.get("requirements"):
                self.mp_reqs.insert("", "end", iid="none", values=("Nothing listed on the page.", "", ""))
            # changelog
            vers = sorted(changes or {}, key=functools.cmp_to_key(lambda a, b: compare_versions(a, b) or 0), reverse=True)
            log = []
            for v in vers:
                log.append((f"{v}\n", ("h3",)))
                lines = changes[v] if isinstance(changes[v], list) else [str(changes[v])]
                for line in lines:
                    log.append(("  •  " + html.unescape(re.sub(r"<[^>]+>", "", str(line))).strip() + "\n", ()))
                log.append(("\n", ()))
            self._fill_rich(self.mp_log, log or [("The author hasn't written a changelog on Nexus.", ("dim",))])

        def _mp_file_picked(self, *_):
            sel = self.mp_files.selection()
            if not sel:
                return
            for i, f in enumerate(self.b_files_data):
                if str(f.get("file_id")) == sel[0]:
                    self.b_files.current(i)
                    return

        def _mp_req_open(self, *_):
            sel = self.mp_reqs.selection()
            if sel and sel[0].startswith("http"):
                self._open_link(sel[0])

        def browse_open(self):
            if self.browse_sel:
                webbrowser.open(f"{NEXUS_SITE}/{DOMAIN}/mods/{self.browse_sel['id']}")

        def browse_install(self):
            it = self.browse_sel
            if not it or not self.b_files_data:
                messagebox.showinfo(APP_NAME, "Pick a mod and a file first.")
                return
            i = self.b_files.current()
            f = self.b_files_data[i if i >= 0 else 0]
            self.add_job("install", it["id"], it["name"], f, confirm=False)
            self.show_page("dl")

        # ---- Downloads page ----------------------------------------------------------------------------
        def _build_downloads(self):
            f = tk.Frame(self.host, bg=T["bg"])
            top, _t, _s = self._page_head(f, "Downloads",
                                          "Everything the app downloads or installs for you shows up here.")
            ttk.Button(top, text="Clear finished", command=self.clear_jobs).pack(side="right")
            ttk.Button(top, text="Cancel", command=self.cancel_job).pack(side="right", padx=8)
            ttk.Button(top, text="Open Nexus page", command=self.open_job_page).pack(side="right")
            fr, self.job_tree = self._table(f, [
                ("mod", "MOD", 300, "w", True), ("ver", "VERSION", 100, "w", False),
                ("status", "STATUS", 130, "w", False), ("msg", "DETAILS", 520, "w", True)], select="browse")
            fr.pack(fill="both", expand=True, padx=26)
            for tag, col in (("done", T["green"]), ("error", T["red"]), ("waiting", T["amber"]),
                             ("cancelled", T["muted"]), ("downloading", T["cyan"]), ("installing", T["cyan"])):
                self.job_tree.tag_configure(tag, foreground=col)
            self.dl_hint = label(f, "", T["muted"], size=9, wraplength=1100, justify="left")
            self.dl_hint.pack(fill="x", padx=28, pady=(10, 0))
            self._sync_dl_hint()
            return f

        def _sync_dl_hint(self):
            reg = nxm_current() if os.name == "nt" else ""
            mine = bool(reg) and Path(sys.argv[0]).name.lower() in reg.lower()
            base = ("Free Nexus account? When a download needs it, the Nexus page opens: press “Slow download” "
                    "(or “Manual download” and save the file). ")
            if os.name == "nt":
                base += ("With “Use this app for Nexus downloads” (Settings) the click hands the file straight "
                         "to this app; otherwise just save the file in your Downloads folder and the app picks it up. "
                         + ("(This app is set up for Nexus download buttons.)" if mine else ""))
            else:
                base += "Save the file into your Downloads folder and the app picks it up."
            self.dl_hint.configure(text=base)

        def _job_row(self, j):
            st = {"queued": "Queued", "downloading": "Downloading", "installing": "Installing", "waiting": "Needs your click",
                  "done": "Done", "error": "Failed", "cancelled": "Cancelled"}[j["status"]]
            vals = (j["name"], j.get("version", ""), st, j.get("msg", ""))
            tv = self.job_tree
            if tv.exists(str(j["id"])):
                tv.item(str(j["id"]), values=vals, tags=(j["status"],))
            else:
                tv.insert("", 0, iid=str(j["id"]), values=vals, tags=(j["status"],))

        def clear_jobs(self):
            for j in list(self.jobs):
                if j["status"] in ("done", "error", "cancelled"):
                    self.jobs.remove(j)
                    if self.job_tree.exists(str(j["id"])):
                        self.job_tree.delete(str(j["id"]))
            self._sync_tabs()

        def _sel_job(self):
            sel = self.job_tree.selection()
            return next((j for j in self.jobs if sel and str(j["id"]) == sel[0]), None)

        def cancel_job(self):
            j = self._sel_job()
            if j and j["status"] in ("queued", "downloading", "waiting", "installing"):
                j["cancel"].set()
                if j["status"] in ("waiting", "queued"):
                    j["status"], j["msg"] = "cancelled", "Cancelled."
                    self._job_row(j)
                    self._sync_tabs()

        def open_job_page(self):
            j = self._sel_job()
            if j and j.get("page"):
                webbrowser.open(j["page"])
            elif j:
                webbrowser.open(f"{NEXUS_SITE}/{DOMAIN}/mods/{j['mod_id']}")

        # ---- running downloads and installs in the background ---------------------------------------------
        def _init_jobs(self):
            self.jobs, self.job_q, self.work_q = [], queue.Queue(), queue.Queue()
            self.mgr_lock = threading.Lock()
            self.worker = None
            self.job_seq = 0
            self.seen_files = {}
            self.ipc = None
            try:
                self.ipc = InstanceServer(lambda u: self.job_q.put(("nxm", u)), on_show=lambda: self.job_q.put(("show",)),
                                          on_play=lambda n: self.job_q.put(("play", n)))
            except OSError:
                pass
            self.after(120, self._pump)
            self.after(2500, self._watch_downloads)

        def bg(self, fn, done, fail=None):
            """Run a small lookup off the screen thread; done/fail run back on it."""
            def run():
                try:
                    r = fn()
                except Exception as e:      # noqa - shown to the user
                    self.job_q.put(("cb", fail or (lambda err: self.status.set(str(err))), e))
                else:
                    self.job_q.put(("cb", done, r))
            threading.Thread(target=run, daemon=True).start()

        def call_ui(self, fn):
            """From a worker thread: run fn on the screen thread and wait for its answer."""
            ev, box = threading.Event(), {}
            self.job_q.put(("call", fn, ev, box))
            ev.wait(900)
            return box.get("v")

        def _pump(self):
            try:
                while True:
                    msg = self.job_q.get_nowait()
                    kind = msg[0]
                    try:
                        if kind == "upd":
                            j = next((x for x in self.jobs if x["id"] == msg[1]), None)
                            if j:
                                self._job_row(j)
                        elif kind == "fin":
                            j = next((x for x in self.jobs if x["id"] == msg[1]), None)
                            if j:
                                self._job_row(j)
                                if j["status"] == "done":
                                    self.refresh()
                                    self.status.set(f"{j['name']}: {j['msg']}")
                                    self.populate_updates()
                                self._sync_tabs()
                        elif kind == "open":
                            webbrowser.open(msg[1])
                        elif kind == "call":
                            try:
                                msg[3]["v"] = msg[1]()
                            finally:
                                msg[2].set()
                        elif kind == "cb":
                            msg[1](msg[2])
                        elif kind == "nxm":
                            self.handle_nxm(msg[1])
                        elif kind == "show":
                            self.bring_to_front()
                        elif kind == "play":                    # a desktop shortcut while this window is open
                            self.bring_to_front()
                            self.play(instance=msg[1] or None, confirm=False)
                    except Exception as e:   # noqa - never let one bad message stop the loop
                        self.status.set(f"Something went wrong: {e}")
            except queue.Empty:
                pass
            self.after(120, self._pump)

        def _watch_downloads(self):
            try:
                waiting = [j for j in self.jobs if j["status"] == "waiting" and not j.get("path")]
                if waiting:
                    dirs = [d for d in (self.cfg.get("download_dirs") or []) if d] + default_download_dirs()
                    for j in waiting:
                        p = find_new_download(dirs, j["since"], j["mod_id"], int(j["file"]["file_id"]),
                                              j["file"].get("file_name", ""), self.seen_files)
                        if p:
                            j["path"], j["status"], j["msg"] = p, "queued", f"Found {p.name} in your downloads."
                            self._job_row(j)
                            self.work_q.put(j["id"])
                            self._ensure_worker()
            finally:
                self.after(2500, self._watch_downloads)

        def add_job(self, kind, mod_id, name, file, path=None, confirm=False, version=""):
            self.job_seq += 1
            j = {"id": self.job_seq, "kind": kind, "mod_id": int(mod_id) if mod_id else None, "name": name,
                 "file": file, "path": Path(path) if path else None, "status": "queued", "msg": "Waiting its turn…",
                 "version": version or (file_version(file) if file else ""), "key": "", "expires": "",
                 "cancel": threading.Event(), "confirm": confirm, "since": time.time(), "page": ""}
            self.jobs.append(j)
            self._job_row(j)
            self._sync_tabs()
            self.work_q.put(j["id"])
            self._ensure_worker()
            return j

        def _ensure_worker(self):
            if self.worker is None or not self.worker.is_alive():
                self.worker = threading.Thread(target=self._work_loop, daemon=True)
                self.worker.start()

        def _work_loop(self):
            while True:
                try:
                    jid = self.work_q.get(timeout=20)
                except queue.Empty:
                    return
                j = next((x for x in self.jobs if x["id"] == jid), None)
                if j is None or j["status"] in ("cancelled", "done"):
                    continue
                self._run_job(j)

        def _run_job(self, j):
            def push(kind="upd"):
                self.job_q.put((kind, j["id"]))

            def prog(i, n, t=""):
                j["msg"] = t or j["msg"]
                push()
            key = self.cfg.get("api_key", "").strip()
            nx = Nexus(key) if key else None
            try:
                if j["cancel"].is_set():
                    raise InstallError("Cancelled.")
                if j["file"] is None and nx is not None:                  # from an nxm:// link: look the file up
                    j["status"], j["msg"] = "downloading", "Asking Nexus about this file…"
                    push()
                    info = nx.mod(j["mod_id"]) or {}
                    j["name"] = html.unescape(str(info.get("name") or j["name"]))
                    fid = j.get("file_id")
                    files = (nx.files(j["mod_id"]) or {}).get("files", [])
                    j["file"] = next((f for f in files if int(f.get("file_id", 0)) == fid), None)
                    if not j["file"]:
                        raise InstallError("Nexus doesn't list that file any more.")
                    j["version"] = file_version(j["file"])
                    if j["confirm"] and not self.call_ui(lambda: messagebox.askyesno(
                            APP_NAME, f"Nexus asked this app to install:\n\n{j['name']}  (v{j['version'] or '?'})\n\n"
                            "Install it?")):
                        raise InstallError("You chose not to install it.")
                if j["path"] is None:
                    if nx is None:
                        raise InstallError("Add your Nexus key in Settings to download.")
                    j["status"], j["msg"] = "downloading", "Asking Nexus for the download…"
                    push()
                    try:
                        links = nx.download_links(j["mod_id"], int(j["file"]["file_id"]), j["key"], j["expires"])
                    except NeedsBrowser as nb:
                        j["status"], j["since"] = "waiting", time.time()
                        j["page"] = nb.url
                        j["msg"] = ("Press “Slow download” on the Nexus page that just opened. "
                                    "Or save the file into your Downloads folder.")
                        push()
                        self.job_q.put(("open", nb.url))
                        return
                    cfgd = dict(self.cfg)
                    j["path"] = download_file(links[0]["url"], download_dir_for(self.mgr, cfgd),
                                              j["file"].get("file_name") or "", nx.local, prog, j["cancel"])
                j["status"], j["msg"] = "installing", "Installing…"
                push()
                with self.mgr_lock:
                    existing = next((m for m in self.mgr.scan() if m.nexus_id == j["mod_id"]), None) \
                        if j["mod_id"] else None
                    res = install_downloaded(self.mgr, dict(self.cfg), j["path"], j["mod_id"], j["file"],
                                             j["name"], existing, prog, j["cancel"])
                n = len(res["rels"])
                j["status"] = "done"
                j["msg"] = (f"Installed v{res['version']}" if res["version"] else "Installed") + \
                    f"  ·  {n} file(s)" + (f"  ·  {res['overwritten']} replaced (backup kept)" if res["overwritten"] else "")
            except NeedsBrowser:
                raise
            except (NexusError, InstallError) as e:
                j["status"], j["msg"] = ("cancelled", "Cancelled.") if "ancel" in str(e) else ("error", str(e))
            except Exception as e:  # noqa - shown, never silent
                j["status"], j["msg"] = "error", f"Unexpected problem: {e}"
            push("fin")

        def bring_to_front(self):
            """Bring this window forward (a second start, or a Nexus link, asked for it). Never opens a new one."""
            try:
                if self.state() == "iconic":
                    self.deiconify()
                self.lift()
                self.attributes("-topmost", True)            # Windows only lets a window forward this way
                self.after(250, lambda: self.attributes("-topmost", False))
                self.focus_force()
            except tk.TclError:
                pass

        def handle_nxm(self, url):
            n = parse_nxm(url)
            if not n:
                self.status.set("Ignored a Nexus link I don't understand.")
                return
            self.bring_to_front()
            waiting = next((j for j in self.jobs if j["status"] == "waiting" and j["mod_id"] == n["mod_id"]
                            and j["file"] and int(j["file"]["file_id"]) == n["file_id"]), None)
            if waiting:
                waiting["key"], waiting["expires"] = n["key"], n["expires"]
                waiting["status"], waiting["msg"] = "queued", "Got the go-ahead from Nexus…"
                self._job_row(waiting)
                self.work_q.put(waiting["id"])
                self._ensure_worker()
            else:
                if not self.mgr:
                    messagebox.showinfo(APP_NAME, "Pick your game folder first, then try the download again.")
                    return
                j = self.add_job("install", n["mod_id"], f"Mod {n['mod_id']}", None, confirm=True)
                j["file_id"], j["key"], j["expires"] = n["file_id"], n["key"], n["expires"]
            self.show_page("dl")

        def _ready(self):
            """Common checks before changing the game folder."""
            if not self.mgr:
                messagebox.showinfo(APP_NAME, "Pick your game folder first.")
                return False
            if game_running():
                messagebox.showwarning(APP_NAME, "Cyberpunk 2077 is running. Close the game first.")
                return False
            return True

        def update_mods(self, mods, ask=True):
            mods = [m for m in mods if m.nexus_id]
            if not mods:
                messagebox.showinfo(APP_NAME, "Select a mod that is linked to Nexus.")
                return
            nx = self.nexus_client()
            if not nx or not self._ready():
                return

            def work(p):
                out = []
                for i, m in enumerate(mods):
                    p(i, len(mods), f"Looking up files for {m.name}…")
                    inst = self.mgr.state["installed"].get(str(m.nexus_id), {})
                    out.append((m, plan_update(nx.files(m.nexus_id), inst.get("file_id"), m.installed_version)))
                return out

            def done(plans):
                started, skipped = 0, []
                for m, plan in plans:
                    f = plan["target"]
                    if f is None and len(plan["options"]) > 1 and ask:
                        f = self.choose_file(m, plan)
                    elif f is None and len(plan["options"]) > 1:
                        skipped.append(f"{m.name} (several main files - choose it yourself)")
                        continue
                    if f is None:
                        if not plan["options"]:
                            skipped.append(f"{m.name} (no downloadable file)")
                        elif plan["current"]:
                            skipped.append(f"{m.name} (Nexus says you already have its newest file)")
                        continue
                    self.add_job("update", m.nexus_id, m.name, f)
                    started += 1
                if skipped:
                    messagebox.showinfo(APP_NAME, "Not updated:\n\n• " + "\n• ".join(skipped[:12]))
                if started:
                    self.status.set(f"{started} update(s) queued - see Downloads.")
                    self.show_page("dl")
            self.start_job("Looking up the files…", work, done)

        def choose_file(self, mod, plan):
            """Several main files: let the user pick. -> file dict or None"""
            d = self.dialog("Which file?", 660, 380)
            tk.Label(d, text=f"{mod.name} has more than one main file.\nPick the one you use:",
                     fg=T["fg"], bg=T["bg"], font=font(11), justify="left", anchor="w").pack(fill="x", padx=24, pady=(22, 10))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=24, pady=18)
            lb = tk.Listbox(d, height=8, bg=T["panel2"], fg=T["fg"], relief="flat", bd=0, highlightthickness=1,
                            highlightbackground=T["line"], highlightcolor=T["accent"], selectbackground=T["accent"],
                            selectforeground=T["accent_fg"], font=font(10), activestyle="none", exportselection=False)
            lb.pack(fill="both", expand=True, padx=24)
            for f in plan["options"]:
                lb.insert("end", file_label(f))
            lb.selection_set(0)
            out = {"f": None}

            def ok(_e=None):
                s = lb.curselection()
                if s:
                    out["f"] = plan["options"][s[0]]
                d.destroy()
            ttk.Button(row, text="Install this one", style="Accent.TButton", command=ok).pack(side="right")
            ttk.Button(row, text="Cancel", command=d.destroy).pack(side="right", padx=8)
            lb.bind("<Double-1>", ok)
            self.wait_window(d)
            return out["f"]

        def _fill_menu(self, m):
            m.add_command(label="Update this mod", command=self.update_selected)
            pin = themed_menu(m)
            pin.add_command(label="Skip this update", command=lambda: self.pin_selected("skip"))
            pin.add_command(label="Stay on this version", command=lambda: self.pin_selected("stay"))
            pin.add_command(label="Unpin", command=self.unpin_selected)
            m.add_cascade(label="Pin or skip an update", menu=pin)
            m.add_separator()
            m.add_command(label="Notes, tags and colour…", command=self.notes_dialog)
            col = themed_menu(m)
            col.add_command(label="No colour", command=lambda: self.set_color(""))
            for c in NOTE_COLORS:
                col.add_command(label=c.capitalize(), command=lambda c=c: self.set_color(c))
            m.add_cascade(label="Colour", menu=col)
            m.add_separator()
            m.add_command(label="Link to a Nexus page…", command=self.link_dialog)
            m.add_command(label="Open on Nexus", command=self.open_nexus)
            m.add_command(label="Endorse on Nexus (or take it back)", command=self.endorse_selected)
            m.add_command(label="Unlink from Nexus", command=self.unlink)
            m.add_separator()
            m.add_command(label="Merge selected", command=self.merge)
            m.add_command(label="Split", command=self.split)
            m.add_command(label="Rename…", command=self.rename)
            m.add_separator()
            m.add_command(label="All on", command=self.all_on)
            m.add_command(label="All off…", command=self.all_off)
            m.add_separator()
            m.add_command(label="Suggested merges…", command=self.suggestions_dialog)
            m.add_command(label="Re-read all Nexus info", command=lambda: self.check_updates(force=True))

        # ---- data -----------------------------------------------------------
        def pick_game(self):
            path = filedialog.askdirectory(title="Select your Cyberpunk 2077 folder")
            if not path:
                return
            if not is_game_dir(path):
                messagebox.showwarning(APP_NAME, "That doesn't look like the game folder.\n"
                                       "It should contain bin\\x64\\Cyberpunk2077.exe.")
                return
            self.set_game(path)

        def set_game(self, path):
            self.mgr = Manager(path)
            self.path_var.set(str(path))
            save_game(path)
            self.findings, self._warn_mods = [], {}
            self.hide_banner()
            self.refresh()
            self.after(1500, self._startup_checks)

        def refresh(self):
            if not self.mgr:
                return
            self.mods = self.mgr.scan(fuzzy=self.fuzzy.get())
            self.mgr.ensure_instances()
            self.mgr.sync_active()
            self._sync_instance_btn()
            self.populate()
            n = sum(len(m.units) for m in self.mods)
            self.status.set(f"Found {len(self.mods)} mods ({n} files and folders scanned).")

        def sorted_mods(self):
            keyf = {
                "state": lambda m: (m.status, m.name.lower()),
                "name": lambda m: m.name.lower(),
                "installed": lambda m: (m.installed_version == "", m.installed_version, m.name.lower()),
                "latest": lambda m: (m.latest_version == "", m.latest_version, m.name.lower()),
                "update": lambda m: (UPDATE_RANK[m.update], m.name.lower()),
                "where": lambda m: (", ".join(m.cats), m.name.lower()),
            }[self.sort_col]
            return sorted(self.mods, key=keyf, reverse=self.sort_rev)

        def sort_by(self, col):
            self.sort_rev = (not self.sort_rev) if col == self.sort_col else False
            self.sort_col = col
            for c, t in self.col_titles.items():
                arrow = ("  ▼" if self.sort_rev else "  ▲") if c == col else ""
                self.tree.heading(c, text=t + arrow)
            self.populate()

        def _passes(self, m, q, f):
            if f == "Enabled" and m.status != "on":
                return False
            if f == "Disabled" and m.status != "off":
                return False
            if f == "Partial" and m.status != "partial":
                return False
            if f == "Frameworks" and not m.core:
                return False
            if f == "Updates available" and m.update not in ("update", "maybe"):
                return False
            if f == "Not linked to Nexus" and m.nexus_id:
                return False
            if f == "Pinned" and not m.pinned:
                return False
            if f == "With a note, tag or colour" and not (m.note or m.tags or m.color):
                return False
            if f == "With a warning" and m.name not in self._warn_mods:
                return False
            if q:
                hay = (m.name + " " + m.local_name + " " + " ".join(u.rel for u in m.units) + " " + m.note + " "
                       + " ".join(m.tags)).lower()
                if q not in hay:
                    return False
            return True

        def populate(self):
            keep = set(self.tree.selection())
            self.tree.delete(*self.tree.get_children())
            q = self.search.get().strip().lower()
            f = self.filter.get()
            shown = 0
            for m in self.sorted_mods():
                if not self._passes(m, q, f):
                    continue
                tags = [m.status]
                if m.color:
                    tags.append("c_" + m.color)
                elif m.update == "update":
                    tags.append("update")
                name = (m.name + ("   · framework" if m.core else "") + ("   ✎" if m.note else "")
                        + ("   ⚠" if m.name in self._warn_mods else "")
                        + ("   " + " ".join("#" + t for t in m.tags[:3]) if m.tags else ""))
                self.tree.insert("", "end", iid=m.key, tags=tags, values=(
                    STATE_LABEL[m.status], name, m.installed_version or "—",
                    m.latest_version or "—", UPDATE_LABEL[m.update], ", ".join(m.cats)))
                shown += 1
            still = [k for k in keep if self.tree.exists(k)]
            if still:
                self.tree.selection_set(still)
            on = sum(1 for m in self.mods if m.status == "on")
            ups = sum(1 for m in self.mods if m.update == "update")
            linked = sum(1 for m in self.mods if m.nexus_id)
            self.stats.set(f"{len(self.mods)} mods  ·  {on} on  ·  {len(self.mods) - on} off  ·  "
                           f"{linked} linked  ·  {ups} update{'s' if ups != 1 else ''}")
            self.show_details()
            self._sync_tabs()
            if self.page == "upd":
                self.populate_updates()

        def selected(self):
            by = {m.key: m for m in self.mods}
            return [by[i] for i in self.tree.selection() if i in by]

        def select_name(self, name):
            for m in self.mods:
                if m.name == name and self.tree.exists(m.key):
                    self.tree.selection_set([m.key])
                    self.tree.see(m.key)
                    self.show_details()
                    return

        def show_details(self, *_):
            mods = self.selected()
            self.d_files.configure(state="normal")
            self.d_files.delete("1.0", "end")
            self.d_btn.state(["disabled"])
            self.d_update.pack_forget()
            self.d_endorse.pack_forget()
            if not mods:
                self.d_name.configure(text="Select a mod")
                self.d_by.configure(text="")
                self.d_status.configure(text="")
                self.d_versions.configure(text="Click the ON/OFF cell, press Space, or use the buttons below.\n"
                                               "Ctrl/Shift-click selects several.")
                self.d_summary.configure(text="")
                self.d_note.configure(text="")
            elif len(mods) > 1:
                self.d_note.configure(text="")
                self.d_name.configure(text=f"{len(mods)} mods selected")
                self.d_by.configure(text="")
                self.d_status.configure(text="")
                self.d_versions.configure(text="")
                self.d_summary.configure(text="")
            else:
                m = mods[0]
                info = m.nexus or {}
                self.d_name.configure(text=m.name)
                self.d_by.configure(text=(f"by {info['author']}" if info.get("author") else
                                          (f"files named “{m.local_name}”" if m.local_name != m.name else "")))
                colors = {"update": T["orange"], "ok": T["green"], "maybe": T["amber"], "pinned": T["cyan"],
                          "unknown": T["muted"], "": T["muted"]}
                text = {
                    "update": f"Update available   {m.installed_version or '?'}  →  {m.latest_version}",
                    "ok": "Up to date",
                    "maybe": "Possibly outdated" + (f"\n{m.update_note}" if m.update_note else ""),
                    "unknown": "Linked to Nexus · nothing to compare yet" if not m.nexus_error else m.nexus_error,
                    "pinned": ("Pinned: staying on this version" if m.pinned == "stay" else "Update skipped")
                              + (f"\n{m.update_note}" if m.update_note else ""),
                    "": "Not linked to Nexus",
                }[m.update]
                self.d_status.configure(text=text, fg=colors[m.update])
                lines = []
                if m.nexus_id:
                    lines.append(f"Installed:  {m.installed_version or 'unknown'}"
                                 + (f"  ({source_text(m.version_source)})" if m.version_source and m.installed_version else ""))
                    lines.append(f"Latest:  {m.latest_version or 'unknown'}")
                    if info.get("updated"):
                        lines.append(f"Last updated on Nexus:  {fmt_date(info['updated'])}")
                if m.install_ts:
                    lines.append(f"Files installed:  {fmt_date(m.install_ts)}")
                endorsed = self.mgr.endorse_status(m.nexus_id) if m.nexus_id else ""
                if endorsed == "Endorsed":
                    lines.append("You have endorsed this mod on Nexus")
                if m.nexus_id and not m.nexus_error:
                    self.d_endorse.configure(text="Take back my endorsement" if endorsed == "Endorsed" else "Endorse on Nexus")
                    self.d_endorse.state(["!disabled"])
                    self.d_endorse.pack(side="left", pady=(0, 10))
                self.d_versions.configure(text="\n".join(lines))
                self.d_summary.configure(text=info.get("summary", ""))
                bits = []
                if m.pinned:
                    bits.append("⏸ Pinned: " + ("staying on this version" if m.pinned == "stay" else "update skipped"))
                if m.tags:
                    bits.append("Tags: " + ", ".join(m.tags))
                if m.note:
                    bits.append("✎ " + m.note)
                for f in self._warn_mods.get(m.name, [])[:4]:
                    bits.append("⚠ " + f["title"])
                self.d_note.configure(text="\n".join(bits))
                self.d_btn.state(["!disabled"])
                self.d_btn.configure(text="Open on Nexus" if m.nexus_id else "Find on Nexus")
                if m.update == "update" and m.nexus_id:
                    self.d_update.configure(text=f"Update to {m.latest_version}" if m.latest_version else "Update")
                    self.d_update.pack(side="left", padx=(8, 0))
                for u in sorted(m.units, key=lambda u: u.rel.lower()):
                    self.d_files.insert("end", ("● " if u.enabled else "○ ") + u.rel + ("/" if u.is_dir else "") + "\n",
                                        "on" if u.enabled else "off")
            self.d_files.configure(state="disabled")

        # ---- on/off ---------------------------------------------------------------
        def on_click(self, event):
            if self.tree.identify_region(event.x, event.y) != "cell":
                return
            if self.tree.identify_column(event.x) != "#1" or event.state & 0x5:
                return
            iid = self.tree.identify_row(event.y)
            mod = next((m for m in self.mods if m.key == iid), None)
            if mod:
                self.apply([mod], mod.status != "on")

        def on_right_click(self, event):
            iid = self.tree.identify_row(event.y)
            if iid and iid not in self.tree.selection():
                self.tree.selection_set([iid])
            try:
                self.ctx.tk_popup(event.x_root, event.y_root)
            finally:
                self.ctx.grab_release()

        def toggle(self):
            mods = self.selected()
            self.apply([m for m in mods if m.status != "on"], True)
            self.apply([m for m in mods if m.status == "on"], False)

        def disable_all_but_core(self):
            targets = [m for m in self.mods if not m.core]
            if targets and messagebox.askyesno(
                    APP_NAME, f"Disable {len(targets)} mods and keep the frameworks "
                    "(CET, RED4ext, ArchiveXL, …) on?\n\nHandy for finding which mod breaks the game."):
                self.apply(targets, False, confirm_core=False)

        def choose(self, title, text, labels, width=640):
            """A small question with several buttons. -> index of the button pressed (the first one is the
            highlighted answer), or None if the window was closed."""
            d = self.dialog(title, width, 270)
            tk.Label(d, text=title, fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text=text, fg=T["fg"], bg=T["bg"], font=font(10), anchor="w", justify="left",
                     wraplength=width - 52).pack(fill="x", padx=26, pady=(6, 10))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            out = {"v": None}

            def pick(i):
                out["v"] = i
                d.destroy()
            for i, lab in enumerate(labels):
                ttk.Button(row, text=lab, style="Accent.TButton" if i == 0 else "TButton",
                           command=lambda i=i: pick(i)).pack(side="right", padx=(8, 0))
            d.bind("<Escape>", lambda _e: d.destroy())
            self.wait_window(d)
            return out["v"]

        def all_on(self):
            """Every mod on - or, right after 'All off', the choice to go back to the set you had."""
            if not self._ready():
                return
            back = self.mgr.return_target()
            if back:
                pick = self.choose("All on", f"Everything is off right now. You can go back to “{back}” (your mods "
                                             f"the way you left them), or turn on every one of the {len(self.mods)} mods.",
                                   [f"Go back to “{back}”", f"Turn on all {len(self.mods)}", "Cancel"])
                if pick == 0:
                    self.switch_to(back, confirm=False)
                    return
                if pick != 1:
                    return
            else:
                off = [m for m in self.mods if m.status != "on"]
                if not off:
                    self.status.set("Every mod is already on.")
                    return
                if not messagebox.askyesno(APP_NAME, f"Turn on all {len(off)} mod(s) that are off?"):
                    return
            self.apply(self.mods, True, check_needs=False)

        def all_off(self):
            """Every mod off (or all but the frameworks) by switching to a ready-made empty instance, so the
            instance you were in keeps its mods and 'All on' / the instance menu bring them back."""
            if not self._ready():
                return
            on = [m for m in self.mods if m.status != "off"]
            if not on:
                self.status.set("Every mod is already off.")
                return
            was = self.mgr.state["active"]
            pick = self.choose("All off", f"Turn off {len(on)} mod(s)?\n\nNothing is deleted. “{was}” keeps its set of "
                                          "mods: press All on, or pick it in the instance menu at the top, to get them back.",
                               ["Turn everything off", "Keep the frameworks on (CET, RED4ext…)", "Cancel"])
            if pick not in (0, 1):
                return
            self.mgr.remember_return()
            name = self.mgr.all_off_instance(keep_frameworks=(pick == 1))
            self.switch_to(name, confirm=False, force=True)

        def apply(self, mods, enable, confirm_core=True, check_needs=True):
            if not self.mgr or not mods:
                return
            if self.busy:
                self.status.set("Busy - wait for the current task to finish.")
                return
            if game_running():
                messagebox.showwarning(APP_NAME, "Cyberpunk 2077 is running. Close the game first.")
                return
            if enable and confirm_core and check_needs:         # not for "All on": that restores a whole set on purpose
                plan = self.mgr.enable_plan(mods, self.mods)
                if plan["also"] or plan["missing"]:
                    mods = self._ask_requirements(mods, plan)
                    if not mods:
                        return
            if not enable and confirm_core:
                core = [m for m in mods if m.core]
                if core:
                    names = ", ".join(m.name for m in core[:6])
                    deps = self.mgr.dependents(core, [x for x in self.mods if x not in mods])
                    extra = ""
                    if deps:
                        extra = "\n\nSwitched on and needing them:\n" + "\n".join(
                            f"•  {k}: {', '.join(v[:6])}{' …' if len(v) > 6 else ''}" for k, v in deps.items())
                    yes = messagebox.askyesno(
                        APP_NAME, f"These are shared frameworks other mods may need:\n\n{names}{extra}\n\n"
                        "Yes = disable them too.\nNo = leave them on and disable the rest.")
                    if not yes:
                        mods = [m for m in mods if not m.core]
                        if not mods:
                            return
            if not self.mgr_lock.acquire(blocking=False):
                messagebox.showinfo(APP_NAME, "An install is running. Try again when it has finished.")
                return
            self.configure(cursor="watch")
            self.update_idletasks()
            moved, errors = 0, []
            self.mgr.merged = []
            try:
                self.mgr.begin_trail()
                for m in mods:
                    n, errs = self.mgr.set_enabled(m, enable)
                    moved += n
                    errors += errs
                self.mgr.log_toggle(mods, enable)
            finally:
                self.configure(cursor="")
                self.mgr_lock.release()
            self.refresh()
            self.status.set(f"{'Enabled' if enable else 'Disabled'} {len(mods)} mod(s), "
                            f"{moved} file(s)/folder(s) moved.")
            if errors:
                messagebox.showerror(APP_NAME, f"{len(errors)} problem(s):\n\n" + "\n".join(errors[:10]) +
                                     ("\n…" if len(errors) > 10 else ""))
            self._merge_report()

        # ---- grouping ---------------------------------------------------------------
        def ask_text(self, title, prompt, initial="", ok="OK", width=460, extra=None):
            """Small themed input dialog. Returns the text or None."""
            result = {"v": None}
            d = self.dialog(title, width, 190 + (extra or 0))
            tk.Label(d, text=prompt, fg=T["fg"], bg=T["bg"], font=font(10), anchor="w",
                     wraplength=width - 48, justify="left").pack(fill="x", padx=24, pady=(22, 8))
            var = tk.StringVar(value=initial)
            e = ttk.Entry(d, textvariable=var)
            e.pack(fill="x", padx=24)
            e.focus_set()
            e.select_range(0, "end")
            row = tk.Frame(d, bg=T["bg"])
            row.pack(fill="x", padx=24, pady=20)

            def go(_e=None):
                result["v"] = var.get()
                d.destroy()
            ttk.Button(row, text=ok, style="Accent.TButton", command=go).pack(side="right")
            ttk.Button(row, text="Cancel", command=d.destroy).pack(side="right", padx=8)
            e.bind("<Return>", go)
            d.bind("<Escape>", lambda _e: d.destroy())
            self.wait_window(d)
            return result["v"]

        def merge(self):
            mods = self.selected()
            if len(mods) < 2:
                messagebox.showinfo(APP_NAME, "Select two or more mods to merge them into one.")
                return
            name = self.ask_text("Merge", "Name for the merged mod:", mods[0].name, "Merge")
            if name and name.strip():
                self.mgr.merge(mods, name.strip())
                self.refresh()
                self.select_name(name.strip())

        def rename(self):
            mods = self.selected()
            if len(mods) != 1:
                messagebox.showinfo(APP_NAME, "Select one mod to rename.")
                return
            name = self.ask_text("Rename", "New name:", mods[0].name, "Rename")
            if name and name.strip():
                self.mgr.merge(mods, name.strip())
                self.refresh()
                self.select_name(name.strip())

        def split(self):
            mods = self.selected()
            if len(mods) != 1 or len(mods[0].units) < 2:
                messagebox.showinfo(APP_NAME, "Select one mod that has several parts to split it up.")
                return
            self.mgr.split(mods[0])
            self.refresh()

        def suggestions_dialog(self):
            if not self.mgr:
                return
            sugg = suggest_merges(self.mods)
            if not sugg:
                messagebox.showinfo(APP_NAME, "No suggestions. Nothing looks like it belongs together "
                                    "that isn't grouped already.")
                return
            d = self.dialog("Suggested merges", 900, 520, resizable=True)
            tk.Label(d, text="These look like parts of the same mod (similar names, installed at about the same time).\n"
                             "Untick any that are wrong, then merge the rest.", fg=T["muted"], bg=T["bg"],
                     font=font(10), justify="left", anchor="w").pack(fill="x", padx=24, pady=(20, 10))
            frame = tk.Frame(d, bg=T["panel"])
            frame.pack(fill="both", expand=True, padx=24)
            tv = ttk.Treeview(frame, columns=("use", "a", "b", "why"), show="headings", selectmode="browse")
            for c, t, w in (("use", "MERGE", 70), ("a", "MOD", 230), ("b", "WITH", 230), ("why", "WHY", 330)):
                tv.heading(c, text=t)
                tv.column(c, width=w, anchor="w", stretch=(c == "why"))
            sb = ttk.Scrollbar(frame, orient="vertical", command=tv.yview)
            tv.configure(yscrollcommand=sb.set)
            tv.pack(side="left", fill="both", expand=True)
            sb.pack(side="right", fill="y")
            checked = {}
            for i, s in enumerate(sugg):
                checked[str(i)] = True
                tv.insert("", "end", iid=str(i), values=("☑", s["a"].name, s["b"].name, s["why"]))

            def flip(iid):
                checked[iid] = not checked[iid]
                tv.set(iid, "use", "☑" if checked[iid] else "☐")

            def click(ev):
                if tv.identify_region(ev.x, ev.y) == "cell" and tv.identify_column(ev.x) == "#1":
                    iid = tv.identify_row(ev.y)
                    if iid:
                        flip(iid)
            tv.bind("<ButtonRelease-1>", click)
            tv.bind("<space>", lambda _e: [flip(i) for i in tv.selection()] and "break")
            row = tk.Frame(d, bg=T["bg"])
            row.pack(fill="x", padx=24, pady=18)

            def do_merge():
                parent = {}

                def find(x):
                    parent.setdefault(x, x)
                    while parent[x] != x:
                        parent[x] = parent[parent[x]]
                        x = parent[x]
                    return x
                by_key = {}
                for i, s in enumerate(sugg):
                    if checked[str(i)]:
                        by_key[s["a"].key] = s["a"]
                        by_key[s["b"].key] = s["b"]
                        parent[find(s["a"].key)] = find(s["b"].key)
                groups = defaultdict(list)
                for k, m in by_key.items():
                    groups[find(k)].append(m)
                n = 0
                for comp in groups.values():
                    if len(comp) > 1:
                        self.mgr.merge(comp, max(comp, key=lambda m: len(m.units)).name)
                        n += 1
                d.destroy()
                self.refresh()
                self.status.set(f"Merged {n} group(s).")
            ttk.Button(row, text="Merge ticked", style="Accent.TButton", command=do_merge).pack(side="right")
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right", padx=8)

        # ---- first start: the Nexus key -----------------------------------------------------
        def first_run_key(self):
            """With no key yet, ask for it as soon as the app is up (CP2077_NO_WELCOME=1 switches this off, for tests)."""
            if (os.environ.get("CP2077_NO_WELCOME") or self.cfg.get("api_key", "").strip()
                    or self.cfg.get("api_prompt_off") or getattr(self, "_welcome", None)):
                return
            self.welcome_dialog()

        def welcome_dialog(self):
            d = self.dialog("Welcome to ModScout 2077", 660, 540)
            self._welcome = d
            d.bind("<Destroy>", lambda e: setattr(self, "_welcome", None) if e.widget is d else None)
            pad = dict(padx=30)
            tk.Label(d, text="Welcome to ModScout 2077", fg=T["accent"], bg=T["bg"], font=font(17, True),
                     anchor="w").pack(fill="x", pady=(26, 2), **pad)
            tk.Label(d, text="One quick step: connect your Nexus Mods account.", fg=T["fg"], bg=T["bg"],
                     font=font(11, True), anchor="w").pack(fill="x", **pad)
            tk.Label(d, text="ModScout uses your personal Nexus API key to recognise your mods, find their pages and "
                             "tell you when an update is out. The key is free, takes about a minute, stays on this PC "
                             "and is only ever sent to nexusmods.com.", fg=T["muted"], bg=T["bg"], font=font(10),
                     anchor="w", justify="left", wraplength=600).pack(fill="x", pady=(6, 0), **pad)
            tk.Label(d, text="1   Get your key", fg=T["fg"], bg=T["bg"], font=font(11, True), anchor="w").pack(
                fill="x", pady=(22, 2), **pad)
            tk.Label(d, text="Open this page and log in to Nexus. Scroll down to “Personal API Key”, press "
                             "“Request an API Key” and copy the key.", fg=T["muted"], bg=T["bg"], font=font(10),
                     anchor="w", justify="left", wraplength=600).pack(fill="x", **pad)
            lrow = tk.Frame(d, bg=T["bg"])
            lrow.pack(fill="x", pady=(8, 0), **pad)
            d._url_var = tk.StringVar(value=API_KEYS_URL)         # kept on the window so Tk doesn't drop it
            ttk.Entry(lrow, textvariable=d._url_var, state="readonly").pack(side="left", fill="x", expand=True)
            ttk.Button(lrow, text="Open the page", style="Accent.TButton",
                       command=lambda: webbrowser.open(API_KEYS_URL)).pack(side="left", padx=(8, 0))

            def copy_link():
                self.clipboard_clear()
                self.clipboard_append(API_KEYS_URL)
                msg.configure(text="Link copied.", fg=T["muted"])
            ttk.Button(lrow, text="Copy link", command=copy_link).pack(side="left", padx=(8, 0))
            tk.Label(d, text="2   Paste it here", fg=T["fg"], bg=T["bg"], font=font(11, True), anchor="w").pack(
                fill="x", pady=(22, 2), **pad)
            krow = tk.Frame(d, bg=T["bg"])
            krow.pack(fill="x", pady=(2, 0), **pad)
            key = tk.StringVar()
            ke = ttk.Entry(krow, textvariable=key, show="•")
            ke.pack(side="left", fill="x", expand=True)
            shown = {"v": False}

            def toggle():
                shown["v"] = not shown["v"]
                ke.configure(show="" if shown["v"] else "•")
                show_btn.configure(text="Hide" if shown["v"] else "Show")
            show_btn = ttk.Button(krow, text="Show", command=toggle)
            show_btn.pack(side="left", padx=(8, 0))
            msg = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(10), anchor="w", justify="left",
                           wraplength=600)
            msg.pack(fill="x", pady=(8, 0), **pad)
            dont = tk.BooleanVar(value=False)
            ttk.Checkbutton(d, text="Don't ask me again (I can add it later in Settings)", variable=dont).pack(
                anchor="w", pady=(10, 0), **pad)
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=30, pady=22)

            def skip():
                if dont.get():
                    self.cfg["api_prompt_off"] = True
                    save_config(api_prompt_off=True)
                d.destroy()

            def connect(_e=None):
                k = key.get().strip()
                if not k:
                    msg.configure(text="Paste your key first.", fg=T["amber"])
                    return
                msg.configure(text="Checking the key with Nexus…", fg=T["muted"])
                self.configure(cursor="watch")
                d.update_idletasks()
                try:
                    me = Nexus(k, timeout=15).validate() or {}
                except NexusError as e:
                    msg.configure(text=("Nexus didn't accept that key. Copy it again from the page above - the whole "
                                        "key, with no spaces." if e.status == 401 else "✗ " + str(e)), fg=T["amber"])
                    return
                finally:
                    self.configure(cursor="")
                self.cfg["api_key"] = k
                save_config(api_key=k)
                self._nx = None
                d.destroy()
                who = str(me.get("name") or "")
                self.status.set("Connected to Nexus" + (f" as {who}" if who else "") + ".")
                if self.mgr and messagebox.askyesno(
                        APP_NAME, "Connected" + (f" as {who}" if who else "") + ".\n\nMatch your installed mods with "
                        "Nexus now? It finds their pages and checks for updates."):
                    self.match_nexus()
                elif not self.mgr:
                    self.status.set(self.status.get() + "  Pick your Cyberpunk 2077 folder with Tools → “Game folder…”.")
            ttk.Button(row, text="Connect", style="Accent.TButton", command=connect).pack(side="right")
            ttk.Button(row, text="Skip for now", command=skip).pack(side="right", padx=8)
            ke.bind("<Return>", connect)
            d.protocol("WM_DELETE_WINDOW", skip)
            ke.focus_set()

        # ---- Nexus ------------------------------------------------------------------
        def nexus_client(self, ask=True):
            key = self.cfg.get("api_key", "").strip()
            if not key:
                if ask:
                    messagebox.showinfo(APP_NAME, "Add your Nexus API key first.\n\nSettings → Nexus API key.")
                    self.open_settings()
                return None
            if getattr(self, "_nx", None) is None or self._nx.key != key:
                self._nx = Nexus(key)                    # kept, so it remembers what Nexus accepted
            return self._nx

        def open_nexus(self):
            mods = self.selected()
            if len(mods) != 1:
                return
            m = mods[0]
            webbrowser.open(m.url if m.nexus_id else search_url(m.local_name or m.name))

        def link_dialog(self):
            mods = self.selected()
            if not mods:
                messagebox.showinfo(APP_NAME, "Select the mod (or mods) you want to link first.")
                return
            m = mods[0]
            d = self.dialog("Link to Nexus", 600, 500)
            tk.Label(d, text=f"Link “{m.name}” to its Nexus page" + (f" (+{len(mods) - 1} more)" if len(mods) > 1 else ""),
                     fg=T["fg"], bg=T["bg"], font=font(11, True), anchor="w").pack(fill="x", padx=24, pady=(22, 4))
            tk.Label(d, text="Paste the Nexus page link (or just the mod number):", fg=T["muted"], bg=T["bg"],
                     font=font(9), anchor="w").pack(fill="x", padx=24, pady=(6, 4))
            url = tk.StringVar()
            e = ttk.Entry(d, textvariable=url)
            e.pack(fill="x", padx=24)
            e.focus_set()
            tk.Label(d, text="Version you have installed (optional):", fg=T["muted"], bg=T["bg"],
                     font=font(9), anchor="w").pack(fill="x", padx=24, pady=(14, 4))
            ver = tk.StringVar(value=m.installed_version)
            ttk.Entry(d, textvariable=ver).pack(fill="x", padx=24)
            tk.Label(d, text="Or look it up here (click a result to use it):", fg=T["muted"], bg=T["bg"],
                     font=font(9), anchor="w").pack(fill="x", padx=24, pady=(14, 4))
            res = tk.Listbox(d, height=6, bg=T["panel2"], fg=T["fg"], relief="flat", bd=0,
                             highlightthickness=1, highlightbackground=T["line"], highlightcolor=T["accent"],
                             selectbackground=T["sel"], selectforeground=T["fg"], font=font(9),
                             activestyle="none", exportselection=False)
            res.pack(fill="x", padx=24)
            found = []

            def find():
                nx = self.nexus_client(ask=True)
                if not nx:
                    return
                self.configure(cursor="watch")
                d.update_idletasks()
                try:
                    words = spaced_words(m.local_name or m.name) or [m.name]
                    nodes = nx.search(" ".join(words))
                    if not nodes and len(words) > 1:
                        nodes = nx.search(max(words, key=len))
                except NexusError as e:
                    messagebox.showwarning(APP_NAME, str(e), parent=d)
                    return
                finally:
                    self.configure(cursor="")
                keys, toks = {norm_key(m.name)}, set(name_tokens(m.name))
                nodes.sort(key=lambda n: -score_match(keys, toks, n["name"])[0])
                found[:] = nodes[:12]
                res.delete(0, "end")
                for n in found:
                    res.insert("end", f"{n['name']}   ·   v{n['version'] or '?'}   ·   #{n['id']}")
                if not found:
                    res.insert("end", "Nothing found. Try “Search on Nexus” to look in your browser.")

            def pick(_e=None):
                s = res.curselection()
                if s and s[0] < len(found):
                    url.set(str(found[s[0]]["id"]))
            res.bind("<<ListboxSelect>>", pick)
            row = tk.Frame(d, bg=T["bg"])
            row.pack(fill="x", padx=24, pady=22)
            ttk.Button(row, text="Look up here", command=find).pack(side="right", padx=(8, 0))

            def go(_e=None):
                mid, err = parse_mod_ref(url.get())
                if mid is None:
                    messagebox.showwarning(APP_NAME, err, parent=d)
                    return
                self.mgr.link(mods, mid, ver.get())
                d.destroy()
                nx = self.nexus_client(ask=False)
                self.refresh()
                if nx:
                    self.start_job("Reading the Nexus page…",
                                   lambda p: refresh_nexus(self.mgr, nx, ids=[mid], force=True, progress=p),
                                   lambda errs: (self.mgr.save(), self.refresh(), self.select_name_for(mid)))
            ttk.Button(row, text="Link", style="Accent.TButton", command=go).pack(side="right")
            ttk.Button(row, text="Search on Nexus", command=lambda: webbrowser.open(
                search_url(m.local_name or m.name))).pack(side="right", padx=8)
            e.bind("<Return>", go)

        def select_name_for(self, mid):
            for m in self.mods:
                if m.nexus_id == mid and self.tree.exists(m.key):
                    self.tree.selection_set([m.key])
                    self.tree.see(m.key)
                    self.show_details()
                    return

        def unlink(self):
            mods = [m for m in self.selected() if m.nexus_id]
            if mods:
                self.mgr.unlink(mods)
                self.refresh()

        def match_nexus(self):
            if not self.mgr:
                return
            nx = self.nexus_client(ask=False)
            dirs = self.cfg.get("download_dirs") or default_download_dirs()
            if not nx and not dirs:
                messagebox.showinfo(APP_NAME, "To match mods I need either your Nexus API key or the folder "
                                    "where you keep your downloaded mod archives.\n\nOpening Settings.")
                self.open_settings()
                return
            cfg = dict(self.cfg)
            self.start_job("Matching with Nexus…", lambda p: run_match(self.mgr, nx, cfg, p), self._match_done)

        def _match_done(self, rep):
            self.mgr.save()
            self.refresh()
            self.proposals = list(rep["proposals"])
            self._sync_props_button()
            bits = [f"Linked {rep.get('linked', 0)} of {rep.get('total', 0)} mods"]
            if rep["archive_mods"]:
                bits.append(f"{rep['archive_mods']} from your downloads")
            if rep["name_mods"] + rep["search_mods"]:
                bits.append(f"{rep['name_mods'] + rep['search_mods']} by name")
            cm = rep.get("contents") or {}
            if cm.get("auto", 0) + cm.get("unify", 0):
                bits.append(f"{cm['auto'] + cm['unify']} by their files")
            if rep["proposals"]:
                bits.append(f"{len(rep['proposals'])} waiting for your OK")
            self.status.set("  ·  ".join(bits) + ".")
            self.match_report(rep)

        def match_report(self, rep):
            notes = rep["notes"]
            props = rep["proposals"]
            d = self.dialog("Matching results", 780, min(640, 150 + 48 * len(notes)))
            tk.Label(d, text="What happened", fg=T["accent"], bg=T["bg"], font=font(13, True),
                     anchor="w").pack(fill="x", padx=26, pady=(22, 10))
            for line in notes:
                col = (T["green"] if line.startswith("✓") else T["red"] if line.startswith("✗")
                       else T["accent"] if line.startswith("→") else T["fg"])
                tk.Label(d, text=line, fg=col, bg=T["bg"], font=font(10), anchor="w", justify="left",
                         wraplength=720).pack(fill="x", padx=26, pady=3)
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=20)
            if props:
                ttk.Button(row, text=f"Review {len(props)} suggested match(es)", style="Accent.TButton",
                           command=lambda: (d.destroy(), self.proposals_dialog())).pack(side="right")
                ttk.Button(row, text="Later", command=d.destroy).pack(side="right", padx=8)
            else:
                ttk.Button(row, text="OK", style="Accent.TButton", command=d.destroy).pack(side="right")

        def _sync_props_button(self):
            n = len(self.proposals)
            self.btn_props.pack_forget()
            if n:
                self.btn_props.configure(text=f"Review matches ({n})")
                self.btn_props.pack(side="right")

        def proposals_dialog(self):
            """Per mod: the Nexus pages it could be, side by side, to choose from."""
            if not self.mgr:
                return
            links = self.mgr.state["links"]
            self.proposals = [p for p in self.proposals if not any(r in links for r in p["rels"])]
            self._sync_props_button()
            props = list(self.proposals)
            if not props:
                messagebox.showinfo(APP_NAME, "No Nexus matches are waiting for your OK.\n\n"
                                    "Press “Match with Nexus” to search again.")
                return
            d = self.dialog("Review Nexus matches", 1260, 740, resizable=True)
            tk.Label(d, text="Which Nexus page is each mod?", fg=T["accent"], bg=T["bg"], font=font(14, True),
                     anchor="w").pack(fill="x", padx=24, pady=(18, 0))
            tk.Label(d, text="Translations, add-ons and patches share a name with the original, so only a page with "
                             "exactly your mod's name is linked automatically. For these I wasn't sure - the best "
                             "guess is already selected where I'm fairly confident. A ✓ means the page's own file list "
                             "(“Preview file contents” on Nexus) shows the files you have installed. “Verify in "
                             "browser” compares the date Nexus shows you with the date your files were installed.",
                     fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left", wraplength=1200).pack(
                fill="x", padx=24, pady=(2, 10))
            bottom = tk.Frame(d, bg=T["bg"])
            bottom.pack(side="bottom", fill="x", padx=24, pady=14)
            main = tk.Frame(d, bg=T["bg"])
            main.pack(fill="both", expand=True, padx=24)
            left = tk.Frame(main, bg=T["bg"], width=390)
            left.pack(side="left", fill="y")
            left.pack_propagate(False)
            lf, lt = self._table(left, [("st", "", 34, "center", False), ("mod", "YOUR MOD", 190, "w", True),
                                        ("best", "BEST GUESS", 150, "w", True)], select="browse")
            lf.pack(fill="both", expand=True)
            lt.tag_configure("ok", foreground=T["green"])
            lt.tag_configure("no", foreground=T["muted"])
            lt.tag_configure("ask", foreground=T["amber"])
            right = tk.Frame(main, bg=T["bg"])
            right.pack(side="left", fill="both", expand=True, padx=(16, 0))
            title = tk.Label(right, text="", fg=T["fg"], bg=T["bg"], font=font(13, True), anchor="w")
            title.pack(fill="x")
            info = tk.Label(right, text="", fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left",
                            wraplength=780)
            info.pack(fill="x", pady=(2, 8))
            cf, ct = self._table(right, [("pick", "", 34, "center", False), ("page", "NEXUS PAGE", 330, "w", True),
                                         ("author", "AUTHOR", 110, "w", False), ("ver", "VER", 64, "w", False),
                                         ("dl", "DOWNLOADS", 86, "e", False), ("upd", "UPDATED", 86, "w", False),
                                         ("fit", "MATCH", 70, "e", False)], select="browse")
            cf.pack(fill="x")
            ct.configure(height=7)
            ct.tag_configure("deriv", foreground=T["muted"])
            ct.tag_configure("picked", foreground=T["green"])
            detail = tk.Label(right, text="", fg=T["fg"], bg=T["panel"], font=font(10), anchor="nw", justify="left",
                              wraplength=770, padx=16, pady=12)
            brow = tk.Frame(right, bg=T["bg"])
            brow.pack(side="bottom", fill="x", pady=(10, 0))
            detail.pack(fill="both", expand=True, pady=(10, 0))
            choice = {i: (p["cands"][p["pick"]]["id"] if p["pick"] is not None else None) for i, p in enumerate(props)}
            rejected, checked_no = set(), set()
            cur = {"i": 0}

            def st_of(i):
                return ("✓", "ok") if choice[i] else (("✗", "no") if i in rejected else ("?", "ask"))

            def best_name(i):
                c = next((x for x in props[i]["cands"] if x["id"] == choice[i]), None) if choice[i] else None
                return (c or props[i]["cands"][0])["name"] if (c or props[i]["cands"]) else ""

            def refresh_left(i):
                s, tag = st_of(i)
                lt.item(str(i), values=(s, props[i]["mod"], best_name(i)), tags=(tag,))
                undecided = sum(1 for k in choice if not choice[k] and k not in rejected)
                n_ok = sum(1 for k in choice if choice[k])
                count.configure(text=f"{n_ok} chosen  ·  {undecided} still to decide")
                link_btn.configure(text=f"Link chosen ({n_ok})")

            def fill_cands(i):
                p = props[i]
                ct.delete(*ct.get_children())
                for c in p["cands"]:
                    tags = []
                    if c.get("deriv"):
                        tags.append("deriv")
                    if choice[i] == c["id"]:
                        tags.append("picked")
                    fit = f"{int(c['score'] * 100)}%"
                    name = (("✓ " if c.get("contents") in ("verified", "likely") else "") + c["name"]
                            + ("  ✗ checked: not it" if (i, c["id"]) in checked_no else ""))
                    ct.insert("", "end", iid=str(c["id"]), tags=tags, values=(
                        "◉" if choice[i] == c["id"] else "○", name, c.get("author", ""), c.get("version", ""),
                        human_count(c.get("downloads")) if c.get("downloads") else "—",
                        fmt_date(c.get("updated")) or "—", fit))

            def show_mod(i):
                cur["i"] = i
                p = props[i]
                title.configure(text=f"“{p['mod']}”")
                files = ", ".join(r.rsplit("/", 1)[-1] for r in p["rels"][:3]) + (" …" if len(p["rels"]) > 3 else "")
                info.configure(text=f"Files: {files}\nInstalled on this PC: "
                                    f"{fmt_dt(p['install_ts']) if p['install_ts'] else 'unknown'}")
                fill_cands(i)
                if choice[i] and ct.exists(str(choice[i])):
                    ct.selection_set(str(choice[i]))
                elif p["cands"]:
                    ct.selection_set(str(p["cands"][0]["id"]))
                show_cand()

            def sel_cand():
                s = ct.selection()
                return next((c for c in props[cur["i"]]["cands"] if s and str(c["id"]) == s[0]), None)

            def show_cand(*_):
                c = sel_cand()
                if not c:
                    detail.configure(text="")
                    return
                lines = [c["name"] + (f"   by {c['author']}" if c.get("author") else "")]
                bits = []
                if c.get("downloads"):
                    bits.append(f"{human_count(c['downloads'])} downloads")
                if c.get("endorsements"):
                    bits.append(f"{human_count(c['endorsements'])} endorsements")
                if c.get("created"):
                    bits.append(f"created {fmt_date(c['created'])}")
                if bits:
                    lines.append("  ·  ".join(bits))
                lines.append(f"Why: {c['why']}")
                for f in c.get("flags", []):
                    lines.append("⚠ " + f)
                if c.get("summary"):
                    lines += ["", c["summary"]]
                detail.configure(text="\n".join(lines))

            def go_next(i):
                for k in list(range(i + 1, len(props))) + list(range(0, i)):
                    if not choice[k] and k not in rejected:
                        lt.selection_set(str(k))
                        lt.see(str(k))
                        return
                lt.selection_set(str(i))

            def choose(_e=None):
                c = sel_cand()
                if not c:
                    return
                i = cur["i"]
                choice[i] = c["id"]
                rejected.discard(i)
                refresh_left(i)
                fill_cands(i)
                ct.selection_set(str(c["id"]))
                go_next(i)

            def reject():
                i = cur["i"]
                choice[i] = None
                rejected.add(i)
                refresh_left(i)
                fill_cands(i)
                go_next(i)

            def open_page():
                c = sel_cand()
                if c:
                    webbrowser.open(f"{NEXUS_SITE}/{DOMAIN}/mods/{c['id']}")

            def verify():
                c = sel_cand()
                if not c:
                    return
                r = self.verify_dialog(props[cur["i"]], c)
                try:
                    d.grab_set()
                except tk.TclError:
                    pass
                if r == "match":
                    choose()
                elif r == "no":
                    checked_no.add((cur["i"], c["id"]))
                    fill_cands(cur["i"])
                    ids = [str(x["id"]) for x in props[cur["i"]]["cands"]]
                    j = ids.index(str(c["id"])) + 1
                    if j < len(ids):
                        ct.selection_set(ids[j])
                    show_cand()
                return r

            def verify_all():
                todo = [i for i in range(len(props)) if not choice[i] and i not in rejected]
                if not todo:
                    messagebox.showinfo(APP_NAME, "Everything is decided already.", parent=d)
                    return
                if not messagebox.askyesno(
                        APP_NAME, f"Check {len(todo)} mod(s) one at a time?\n\nFor each, the best candidates open on "
                        "Nexus (use the browser you're logged in with) and you tell me the date it shows. "
                        "It takes a minute or two per mod - stop any time with Close.", parent=d):
                    return
                for i in todo:
                    lt.selection_set(str(i))
                    lt.see(str(i))
                    d.update_idletasks()
                    for c in props[i]["cands"][:3]:
                        if c.get("deriv") and len(props[i]["cands"]) > 1:
                            continue
                        ct.selection_set(str(c["id"]))
                        show_cand()
                        r = verify()
                        if r == "match":
                            break
                        if r is None:
                            return

            def paste_link():
                txt = self.ask_text("Paste a Nexus link", "Paste the Nexus page link (or just the mod number):",
                                    ok="Use it", width=520)
                if not txt:
                    return
                mid, err = parse_mod_ref(txt)
                if mid is None:
                    messagebox.showwarning(APP_NAME, err, parent=d)
                    return
                p = props[cur["i"]]
                if not any(c["id"] == mid for c in p["cands"]):
                    p["cands"].append({"id": mid, "name": f"Nexus page #{mid} (the link you pasted)", "version": "",
                                       "score": 1.0, "why": "you pasted this link", "kind": "manual", "deriv": False,
                                       "flags": [], "downloads": 0, "author": "", "updated": 0})
                fill_cands(cur["i"])
                ct.selection_set(str(mid))
                choose()

            ttk.Button(brow, text="Open page", command=open_page).pack(side="left")
            ttk.Button(brow, text="Verify in browser…", command=verify).pack(side="left", padx=8)
            ttk.Button(brow, text="Paste a link…", command=paste_link).pack(side="left")
            ttk.Button(brow, text="None of these", command=reject).pack(side="right")
            ttk.Button(brow, text="This is it", style="Accent.TButton", command=choose).pack(side="right", padx=8)
            count = tk.Label(bottom, text="", fg=T["muted"], bg=T["bg"], font=font(10))
            count.pack(side="left")
            link_btn = ttk.Button(bottom, text="Link chosen (0)", style="Accent.TButton")
            link_btn.pack(side="right")
            ttk.Button(bottom, text="Close", command=d.destroy).pack(side="right", padx=8)
            ttk.Button(bottom, text="Verify the unsure ones, one by one…", command=verify_all).pack(side="right")

            for i, p in enumerate(props):
                lt.insert("", "end", iid=str(i), values=("", p["mod"], ""))
                refresh_left(i)
            lt.bind("<<TreeviewSelect>>", lambda _e: lt.selection() and show_mod(int(lt.selection()[0])))
            ct.bind("<<TreeviewSelect>>", show_cand)
            ct.bind("<Double-1>", choose)
            lt.selection_set("0")
            show_mod(0)

            def do_link():
                chosen = [(props[i], choice[i]) for i in choice if choice[i]]
                if not chosen:
                    messagebox.showinfo(APP_NAME, "Choose a page for at least one mod first.", parent=d)
                    return
                for p, cid in chosen:
                    for rel in p["rels"]:
                        links[rel] = {"id": cid, "src": "manual"}
                self.mgr.save()
                done_keys = {id(p) for p, _c in chosen}
                self.proposals = [p for p in props if id(p) not in done_keys]
                self._sync_props_button()
                d.destroy()
                self.refresh()
                self.status.set(f"Linked {len(chosen)} mod(s) to Nexus.")
                nx = self.nexus_client(ask=False)
                ids = sorted({c for _p, c in chosen})
                if nx and ids:
                    self.start_job("Reading the Nexus pages…",
                                   lambda pr: refresh_nexus(self.mgr, nx, ids=ids, progress=pr),
                                   lambda errs: (self.mgr.save(), self.refresh()))
            link_btn.configure(command=do_link)

        def verify_dialog(self, p, cand):
            """Guided check: open the Nexus page, read the 'You last downloaded…' line, compare the date."""
            d = self.dialog("Check on Nexus", 720, 690)
            res = {"v": None}
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            url = f"{NEXUS_SITE}/{DOMAIN}/mods/{cand['id']}"
            tk.Label(d, text="Is this the page your files came from?", fg=T["accent"], bg=T["bg"],
                     font=font(14, True), anchor="w").pack(fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text=f"{cand['name']}" + (f"  ·  by {cand['author']}" if cand.get("author") else ""),
                     fg=T["fg"], bg=T["bg"], font=font(11, True), anchor="w", wraplength=660).pack(fill="x", padx=26)
            card = tk.Frame(d, bg=T["panel"])
            card.pack(fill="x", padx=26, pady=(14, 8))
            tk.Label(card, text=f"Your files for “{p['mod']}” appeared on this PC on", fg=T["muted"], bg=T["panel"],
                     font=font(9), anchor="w").pack(fill="x", padx=16, pady=(12, 0))
            tk.Label(card, text=fmt_dt(p["install_ts"]) if p["install_ts"] else "an unknown date", fg=T["fg"],
                     bg=T["panel"], font=font(15, True), anchor="w").pack(fill="x", padx=16, pady=(0, 12))
            steps = ("1.  Press “Open the page”. Use the browser where you're logged in to Nexus.\n"
                     "2.  Near the top of the mod page, find the line\n"
                     "      “You last downloaded a file from this mod on …”\n"
                     "3.  Type or paste that date (or the whole line) below - I'll compare it.\n"
                     "      No such line? You've never downloaded from this page, so it isn't it.")
            tk.Label(d, text=steps, fg=T["fg"], bg=T["bg"], font=font(10), anchor="w", justify="left").pack(
                fill="x", padx=26, pady=(8, 10))
            ttk.Button(d, text="Open the page in my browser", command=lambda: webbrowser.open(url)).pack(
                anchor="w", padx=26)
            tk.Label(d, text="Date or line from the page:", fg=T["muted"], bg=T["bg"], font=font(9),
                     anchor="w").pack(fill="x", padx=26, pady=(16, 4))
            var = tk.StringVar()
            e = ttk.Entry(d, textvariable=var)
            e.pack(fill="x", padx=26)
            e.focus_set()
            out = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(10, True), anchor="w", justify="left",
                           wraplength=660)
            out.pack(fill="x", padx=26, pady=(10, 0))

            def judge(*_):
                txt = var.get().strip()
                if not txt:
                    out.configure(text="", fg=T["muted"])
                    return
                ts = parse_page_date(txt)
                if ts is None:
                    out.configure(text="I can't find a date in that. Try “26 Oct 2026”.", fg=T["amber"])
                    return
                verdict, sentence = date_fit(p["install_ts"], ts)
                out.configure(text=f"Nexus date: {fmt_date(ts)}.  {sentence}",
                              fg={"same": T["green"], "close": T["green"], "later": T["amber"], "far": T["red"]}[verdict])
            var.trace_add("write", judge)
            tk.Label(d, text="I can't read your browser or your Nexus login - and don't want to - so you read the "
                             "date and I do the comparing. Nexus doesn't offer your download history to apps.",
                     fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left", wraplength=660).pack(
                fill="x", padx=26, pady=(14, 0))

            def fin(v):
                res["v"] = v
                d.destroy()
            ttk.Button(row, text="Yes, use this page", style="Accent.TButton", command=lambda: fin("match")).pack(side="right")
            ttk.Button(row, text="Not this one", command=lambda: fin("no")).pack(side="right", padx=8)
            ttk.Button(row, text="Stop", command=d.destroy).pack(side="right")
            d.bind("<Escape>", lambda _e: d.destroy())
            self.wait_window(d)
            return res["v"]

        # ---- playing ---------------------------------------------------------------------------------------
        PLAY_FIRST_MS, PLAY_POLL_MS = 4000, 5000
        PLAY_GIVE_UP_S = 90 if os.name == "nt" else 6

        def _fill_play_menu(self):
            m = self.play_menu
            m.delete(0, "end")
            if not self.mgr:
                m.add_command(label="Pick your game folder first", state="disabled")
                return
            self.mgr.ensure_instances()
            m.add_command(label="Play with this set of mods:", state="disabled")
            for name in sorted(self.mgr.state["instances"], key=str.lower):
                on = len(self.mgr.state["instances"][name].get("on", []))
                m.add_command(label=("●  " if name == self.mgr.state["active"] else "○  ") + f"{name}   ({on} on)",
                              command=lambda n=name: self.play(n))
            m.add_separator()
            m.add_command(label="Play without any mods (vanilla)", command=lambda: self.play(vanilla=True))
            m.add_command(label="Launch options…", command=self.open_settings)

        def play(self, instance=None, vanilla=False, confirm=True):
            """Switch to `instance` (if one is chosen) and start the game."""
            if not self.mgr:
                messagebox.showinfo(APP_NAME, "Pick your game folder first.")
                return
            if game_running():
                messagebox.showinfo(APP_NAME, "Cyberpunk 2077 is already running.")
                return
            if vanilla:
                self.mgr.remember_return()
                instance = self.mgr.all_off_instance(keep_frameworks=False)
                if not self.switch_to(instance, ok_text="Switch and play", force=True):
                    return
            elif instance and not self.switch_to(instance, ok_text="Switch and play", confirm=confirm):
                return
            if self.mgr_lock.locked() or any(j["status"] in ("downloading", "installing") for j in self.jobs):
                messagebox.showinfo(APP_NAME, "A download or install is still running. Press Play again when it has "
                                              "finished (see the Downloads tab).")
                return
            try:
                self.mgr.saves_sync()                    # no-op unless "saves per instance" is switched on
            except ValueError as e:
                messagebox.showerror(APP_NAME, f"Your saves couldn't be set up for this instance, so the game was not "
                                               f"started:\n\n{e}")
                return
            try:
                msg = launch_game(self.mgr.game, self.cfg.get("launch_method", "auto"), self.cfg.get("launch_args", ""))
            except LaunchError as e:
                messagebox.showerror(APP_NAME, str(e))
                return
            self.status.set(f"{msg}  Instance: {self.mgr.state['active']}.")
            self._play_watch()

        def _play_watch(self):
            """While the game starts and runs, the Play button says so; it comes back when the game has closed."""
            self.play_btn.configure(text="Starting…", state="disabled")
            self.play_menu_btn.configure(state="disabled")
            started, seen = time.time(), {"v": False}

            def release():
                self.play_btn.configure(text="Play", state="normal")
                self.play_menu_btn.configure(state="normal")
                self.refresh()

            def poll():
                def done(running):
                    if running:
                        seen["v"] = True
                        self.play_btn.configure(text="Running…")
                    elif seen["v"] or time.time() - started > self.PLAY_GIVE_UP_S:
                        release()
                        return
                    self.after(self.PLAY_POLL_MS, poll)
                self.bg(game_running, done, lambda _e: release())
            self.after(self.PLAY_FIRST_MS, poll)

        # ---- instances -------------------------------------------------------------------------------------
        def _sync_instance_btn(self):
            name = self.mgr.state["active"] if self.mgr else ""
            self.inst_btn.configure(text=f"◈  {name or 'No instance'}  ▾")

        def _fill_instance_menu(self):
            m = self.inst_menu
            m.delete(0, "end")
            if not self.mgr:
                m.add_command(label="Pick your game folder first", state="disabled")
                return
            self.mgr.ensure_instances()
            for name in sorted(self.mgr.state["instances"], key=str.lower):
                on = len(self.mgr.state["instances"][name].get("on", []))
                m.add_command(label=("●  " if name == self.mgr.state["active"] else "○  ") + f"{name}   ({on} on)",
                              command=lambda n=name: self.switch_to(n))
            m.add_separator()
            m.add_command(label="New instance…", command=self.new_instance_dialog)
            m.add_command(label="Manage instances…", command=self.instances_dialog)
            m.add_separator()
            g = self.mgr.good_get()
            m.add_command(label="✓  This setup works", command=self.mark_good)
            m.add_command(label=("Go back to the setup that worked  (" + self._when(g["ts"]).strip() + ")") if g else
                          "Go back to the setup that worked", command=lambda: self.restore_good(None),
                          state="normal" if g else "disabled")
            sc = self.shortcut_menu
            sc.delete(0, "end")
            for name in sorted(self.mgr.state["instances"], key=str.lower):
                sc.add_command(label=name, command=lambda n=name: self.make_instance_shortcut(n))
            m.add_cascade(label="Desktop shortcut for ▸", menu=sc)

        def switch_to(self, name, ok_text="Switch", confirm=True, force=False):
            """Make `name` the active instance. -> True if it is the active one afterwards."""
            if not self._ready():
                return False
            if name == self.mgr.state["active"] and not force:
                return True
            self.mgr.sync_active()
            plan = self.mgr.instance_plan(name)
            if confirm and (plan["enable"] or plan["disable"]):
                if not self.plan_dialog(plan, ok_text):
                    return False
            if not self.mgr_lock.acquire(blocking=False):
                messagebox.showinfo(APP_NAME, "An install is running. Try again when it has finished.")
                return False
            try:
                self.configure(cursor="watch")
                self.update_idletasks()
                self.mgr.merged = []
                moved, errors = self.mgr.switch_instance(name)
            finally:
                self.configure(cursor="")
                self.mgr_lock.release()
            self.refresh()
            if errors:
                self.status.set(f"Couldn't finish switching to “{name}”.")
                messagebox.showerror(APP_NAME, f"{len(errors)} problem(s):\n\n" + "\n".join(errors[:10]))
            else:
                self.status.set(f"Switched to “{name}”: {len(plan['enable_mods'])} mod(s) turned on, "
                                f"{len(plan['disable_mods'])} turned off.")
            self._merge_report()
            return not errors

        def _merge_report(self):
            """Tell the person about copies that were found in both places and merged (nothing is lost)."""
            got, self.mgr.merged = list(self.mgr.merged), []
            if got:
                messagebox.showinfo(APP_NAME, f"{len(got)} item(s) were found both in the game folder and in "
                                              f"{STASH_NAME}, so I merged them. Nothing was lost: if two files "
                                              f"differed, the newer one is used and the older is kept in "
                                              f"{STASH_NAME}\\{BACKUP_NAME}.\n\n" + "\n".join(got[:8]))

        def plan_dialog(self, plan, ok_text="Switch"):
            d = self.dialog(f"Switch to “{plan['name']}”", 640, 560, resizable=True)
            tk.Label(d, text=f"Switch to “{plan['name']}”?", fg=T["accent"], bg=T["bg"], font=font(14, True),
                     anchor="w").pack(fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="Only the difference is moved. Nothing is deleted - mods you turn off wait in "
                             "_disabled_mods and come back when you switch again.", fg=T["muted"], bg=T["bg"],
                     font=font(9), anchor="w", justify="left", wraplength=580).pack(fill="x", padx=26, pady=(0, 10))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            txt = tk.Text(d, wrap="word", relief="flat", bd=0, bg=T["panel"], fg=T["fg"], font=font(10), padx=14,
                          pady=10, highlightthickness=0)
            txt.pack(fill="both", expand=True, padx=26)
            txt.tag_configure("on", foreground=T["green"], font=font(10, True))
            txt.tag_configure("off", foreground=T["amber"], font=font(10, True))
            for key, tag, head in (("enable_mods", "on", "Turned ON"), ("disable_mods", "off", "Turned OFF")):
                names = plan[key]
                txt.insert("end", f"{head} ({len(names)})\n", tag)
                txt.insert("end", (", ".join(names[:60]) + (f" … and {len(names) - 60} more" if len(names) > 60 else ""))
                           if names else "nothing", "")
                txt.insert("end", "\n\n")
            txt.configure(state="disabled")
            out = {"v": False}

            def go():
                out["v"] = True
                d.destroy()
            ttk.Button(row, text=ok_text, style="Accent.TButton", command=go).pack(side="right")
            ttk.Button(row, text="Cancel", command=d.destroy).pack(side="right", padx=8)
            self.wait_window(d)
            return out["v"]

        def new_instance_dialog(self):
            if not self.mgr:
                return
            self.mgr.ensure_instances()
            d = self.dialog("New instance", 600, 430)
            tk.Label(d, text="New instance", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="An instance is a saved set of switched-on mods - for example “Story run”, "
                             "“Vanilla+” or “Testing”. Switching moves only what differs.", fg=T["muted"], bg=T["bg"],
                     font=font(9), anchor="w", justify="left", wraplength=540).pack(fill="x", padx=26, pady=(0, 12))
            name = tk.StringVar()
            e = ttk.Entry(d, textvariable=name)
            e.pack(fill="x", padx=26)
            e.focus_set()
            mode = tk.StringVar(value="current")
            names = sorted(self.mgr.state["instances"], key=str.lower)
            src = tk.StringVar(value=self.mgr.state["active"] or names[0])
            for val, text in (("current", "Start from what is switched on right now"),
                              ("frameworks", "Clean slate - only the shared frameworks (CET, RED4ext, ArchiveXL…)"),
                              ("copy", "Copy another instance:")):
                tk.Radiobutton(d, text=text, variable=mode, value=val, bg=T["bg"], fg=T["fg"], selectcolor=T["panel2"],
                               activebackground=T["bg"], activeforeground=T["fg"], font=font(10), anchor="w",
                               highlightthickness=0, bd=0).pack(fill="x", padx=26, pady=(10 if val == "current" else 2, 0))
            ttk.Combobox(d, textvariable=src, values=names, state="readonly").pack(fill="x", padx=50, pady=(2, 0))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=20)

            def go(_e=None):
                try:
                    new = self.mgr.create_instance(name.get(), mode.get(), src.get())
                except ValueError as err:
                    messagebox.showwarning(APP_NAME, str(err), parent=d)
                    return
                d.destroy()
                self._sync_instance_btn()
                if messagebox.askyesno(APP_NAME, f"“{new}” was created. Switch to it now?"):
                    self.switch_to(new)
            ttk.Button(row, text="Create", style="Accent.TButton", command=go).pack(side="right")
            ttk.Button(row, text="Cancel", command=d.destroy).pack(side="right", padx=8)
            e.bind("<Return>", go)

        def instances_dialog(self):
            if not self.mgr:
                return
            self.mgr.ensure_instances()
            self.mgr.sync_active()
            d = self.dialog("Instances", 680, 500)
            tk.Label(d, text="Instances", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="All your mods stay in the game folder (on) or in _disabled_mods (off). An instance "
                             "remembers which are on; switching puts the rest away and brings the right ones back. "
                             "Saved games and mod settings are shared between instances, unless you give one saves of its own "
                             "(Tools → Saves per instance).",
                     fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left", wraplength=620).pack(
                fill="x", padx=26, pady=(0, 10))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            fr, tv = self._table(d, [("name", "INSTANCE", 280, "w", True), ("on", "MODS ON", 100, "e", False),
                                     ("act", "", 120, "w", False)], select="browse")
            fr.pack(fill="both", expand=True, padx=26)

            def fill():
                tv.delete(*tv.get_children())
                for n in sorted(self.mgr.state["instances"], key=str.lower):
                    tv.insert("", "end", iid=n, values=(n, len(self.mgr.state["instances"][n].get("on", [])),
                                                        "running now" if n == self.mgr.state["active"] else ""))
            fill()

            def sel():
                s = tv.selection()
                return s[0] if s else None

            def do_switch():
                n = sel()
                if n:
                    d.destroy()
                    self.switch_to(n)

            def do_rename():
                n = sel()
                if not n:
                    return
                new = self.ask_text("Rename", "New name:", n, "Rename")
                if new:
                    try:
                        self.mgr.rename_instance(n, new)
                    except ValueError as err:
                        messagebox.showwarning(APP_NAME, str(err), parent=d)
                    fill()
                    self._sync_instance_btn()

            def do_delete():
                n = sel()
                if n and messagebox.askyesno(APP_NAME, f"Delete the instance “{n}”?\n\nYour mods are not touched.",
                                             parent=d):
                    try:
                        self.mgr.delete_instance(n)
                    except ValueError as err:
                        messagebox.showwarning(APP_NAME, str(err), parent=d)
                    fill()
            ttk.Button(row, text="Switch to", style="Accent.TButton", command=do_switch).pack(side="left")
            ttk.Button(row, text="New…", command=lambda: (d.destroy(), self.new_instance_dialog())).pack(side="left", padx=8)
            ttk.Button(row, text="Rename…", command=do_rename).pack(side="left")
            ttk.Button(row, text="Delete", command=do_delete).pack(side="left", padx=8)
            ttk.Button(row, text="Shortcut…", command=lambda: self.shortcut_dialog(sel())).pack(side="left")
            ttk.Button(row, text="Compare…", command=lambda: (d.destroy(), self.compare_dialog(sel()))
                       ).pack(side="left", padx=8)
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")
            tv.bind("<Double-1>", lambda _e: do_switch())

        # ---- Tools menu: last known good, History and undo, compare, disk space, notes, shortcuts ------------
        def _fill_tools_menu(self):
            m = self.tools_menu
            m.delete(0, "end")
            st = "normal" if self.mgr else "disabled"
            m.add_command(label="✓  This setup works", command=self.mark_good, state=st)
            m.add_command(label="Go back to a setup that worked…", command=self.good_dialog, state=st)
            m.add_separator()
            m.add_command(label="History and undo…", command=self.history_dialog, state=st)
            m.add_command(label="Compare two instances…", command=self.compare_dialog, state=st)
            m.add_command(label="Disk space…", command=self.disk_dialog, state=st)
            m.add_separator()
            m.add_command(label="Desktop shortcut for an instance…", command=self.shortcut_dialog, state=st)
            self._fill_tools_extra(m, st)
            m.add_separator()
            m.add_command(label="Game folder…", command=self.pick_game)

        @staticmethod
        def _when(ts) -> str:
            try:
                return time.strftime("%d %b  %H:%M", time.localtime(float(ts)))
            except (OverflowError, OSError, ValueError, TypeError):
                return ""

        # ---- last known good --------------------------------------------------------------------------
        def mark_good(self):
            if not self.mgr:
                messagebox.showinfo(APP_NAME, "Pick your game folder first.")
                return None
            rec = self.mgr.good_save()
            self.status.set(f"Saved: this setup works ({rec['mods_on']} mod{'s' if rec['mods_on'] != 1 else ''} on). "
                            "Tools → “Go back to a setup that worked” brings it back after something breaks.")
            return rec

        def good_dialog(self):
            if not self.mgr:
                return
            d = self.dialog("Setups that worked", 720, 520, resizable=True)
            tk.Label(d, text="Setups that worked", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="Press “This setup works” when the game runs well. If a later update or a new mod breaks "
                             "something, pick that setup here: the same mods are switched on and off again, and updates "
                             "made since can be undone too. Nothing is deleted.", fg=T["muted"], bg=T["bg"], font=font(9),
                     anchor="w", justify="left", wraplength=660).pack(fill="x", padx=26, pady=(0, 10))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            fr, tv = self._table(d, [("when", "SAVED", 150, "w", False), ("mods", "MODS ON", 90, "e", False),
                                     ("inst", "INSTANCE", 150, "w", False), ("note", "NOTE", 260, "w", True)],
                                 select="browse")
            fr.pack(fill="both", expand=True, padx=26)

            def fill():
                tv.delete(*tv.get_children())
                for g in self.mgr.state["good"]:
                    tv.insert("", "end", iid=g["id"], values=(self._when(g["ts"]), g.get("mods_on", ""),
                                                              g.get("active", ""), g.get("note", "")))
                kids = tv.get_children()
                if kids:
                    tv.selection_set(kids[0])

            def sel():
                s = tv.selection()
                return s[0] if s else None

            def add():
                self.mark_good()
                fill()

            def back():
                g = sel()
                if g:
                    d.destroy()
                    self.restore_good(g)

            def edit_note():
                g = sel()
                rec = self.mgr.good_get(g) if g else None
                if rec:
                    t = self.ask_text("Note", "A note to remember this setup by:", rec.get("note", ""), "Save")
                    if t is not None:
                        rec["note"] = t.strip()[:80]
                        self.mgr.save()
                        fill()

            def delete():
                g = sel()
                if g and messagebox.askyesno(APP_NAME, "Forget this saved setup?\n\nYour mods are not touched.", parent=d):
                    self.mgr.good_delete(g)
                    fill()
            fill()
            ttk.Button(row, text="Go back to this one…", style="Accent.TButton", command=back).pack(side="left")
            ttk.Button(row, text="✓  This setup works", command=add).pack(side="left", padx=8)
            ttk.Button(row, text="Note…", command=edit_note).pack(side="left")
            ttk.Button(row, text="Forget", command=delete).pack(side="left", padx=8)
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")
            tv.bind("<Double-1>", lambda _e: back())

        def restore_good(self, good_id=None):
            """Ask what going back would do, then do it."""
            if not self._ready():
                return
            rec = self.mgr.good_get(good_id)
            if not rec:
                messagebox.showinfo(APP_NAME, "Nothing is marked as working yet.\n\nPress “This setup works” "
                                              "(Tools menu) while the game runs well.")
                return
            ch = self.mgr.good_changes(rec)
            d = self.dialog("Go back to a setup that worked", 660, 600, resizable=True)
            tk.Label(d, text=f"Go back to the setup from {self._when(rec['ts'])}?", fg=T["accent"], bg=T["bg"],
                     font=font(14, True), anchor="w").pack(fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text=(rec.get("note") + "  ·  " if rec.get("note") else "") +
                             f"{rec.get('mods_on', '?')} mods were on.", fg=T["muted"], bg=T["bg"], font=font(9),
                     anchor="w").pack(fill="x", padx=26, pady=(0, 8))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            undo_var = tk.BooleanVar(value=bool(ch["updates"]))
            if ch["updates"]:
                ttk.Checkbutton(d, text=f"Also undo the {len(ch['updates'])} update(s) made since (recommended)",
                                variable=undo_var).pack(side="bottom", anchor="w", padx=26, pady=(6, 0))
            txt = tk.Text(d, wrap="word", relief="flat", bd=0, bg=T["panel"], fg=T["fg"], font=font(10), padx=14,
                          pady=10, highlightthickness=0)
            txt.pack(fill="both", expand=True, padx=26)
            txt.tag_configure("on", foreground=T["green"], font=font(10, True))
            txt.tag_configure("off", foreground=T["amber"], font=font(10, True))
            txt.tag_configure("up", foreground=T["cyan"], font=font(10, True))

            def block(head, tag, names):
                txt.insert("end", f"{head} ({len(names)})\n", tag)
                txt.insert("end", (", ".join(names[:60]) + (f" … and {len(names) - 60} more" if len(names) > 60 else ""))
                           if names else "nothing", "")
                txt.insert("end", "\n\n")
            block("Turned ON", "on", ch["enable_mods"])
            block("Turned OFF", "off", ch["disable_mods"])
            block("Updates undone", "up", [e["text"].replace("Updated ", "") for e in ch["updates"]])
            if ch["versions"] and not ch["updates"]:
                txt.insert("end", "Versions that changed since (no undo available):\n", "up")
                txt.insert("end", "\n".join(f"{v['name']}: {v['then'] or '?'} → {v['now'] or '?'}" for v in ch["versions"][:20]))
            txt.configure(state="disabled")
            out = {"v": False}

            def go():
                out["v"] = True
                d.destroy()
            ttk.Button(row, text="Go back", style="Accent.TButton", command=go).pack(side="right")
            ttk.Button(row, text="Cancel", command=d.destroy).pack(side="right", padx=8)
            self.wait_window(d)
            if not out["v"]:
                return
            if not self.mgr_lock.acquire(blocking=False):
                messagebox.showinfo(APP_NAME, "An install is running. Try again when it has finished.")
                return
            try:
                self.configure(cursor="watch")
                self.update_idletasks()
                self.mgr.merged = []
                res = self.mgr.good_restore(rec["id"], undo_updates=bool(undo_var.get()))
            finally:
                self.configure(cursor="")
                self.mgr_lock.release()
            self.refresh()
            n_on, n_off = len(res["plan"]["enable_mods"]), len(res["plan"]["disable_mods"])
            self.status.set(f"Back to the setup from {self._when(rec['ts'])}: {n_on} mod(s) turned on, {n_off} off"
                            + (f", {len(res['undone'])} update(s) undone." if res["undone"] else "."))
            if res["errors"]:
                messagebox.showerror(APP_NAME, f"{len(res['errors'])} problem(s):\n\n" + "\n".join(res["errors"][:10]))
            if res["skipped"]:
                messagebox.showinfo(APP_NAME, "These updates could not be undone:\n\n• " + "\n• ".join(res["skipped"][:8]))
            self._merge_report()

        # ---- History and undo -----------------------------------------------------------------------------
        def history_dialog(self):
            if not self.mgr:
                return
            d = self.dialog("History", 780, 560, resizable=True)
            tk.Label(d, text="History", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="Every install, update, switch and on/off change. Pick one and press Undo to go back to how "
                             "things were before it. Updates and installs keep a backup of what they replaced "
                             "(in _disabled_mods\\_backup), so nothing is lost.", fg=T["muted"], bg=T["bg"], font=font(9),
                     anchor="w", justify="left", wraplength=720).pack(fill="x", padx=26, pady=(0, 10))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            why = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left", wraplength=720)
            why.pack(side="bottom", fill="x", padx=26, pady=(8, 0))
            fr, tv = self._table(d, [("when", "WHEN", 130, "w", False), ("what", "WHAT HAPPENED", 460, "w", True),
                                     ("st", "", 110, "w", False)], select="browse")
            fr.pack(fill="both", expand=True, padx=26)
            tv.tag_configure("note", foreground=T["muted"])
            tv.tag_configure("undone", foreground=T["muted"])
            undo_btn = ttk.Button(row, text="Undo this", style="Accent.TButton")
            undo_btn.pack(side="left")

            def sel():
                s = tv.selection()
                return self.mgr.journal_get(s[0]) if s else None

            def status_pick(*_):
                e = sel()
                if not e:
                    why.configure(text="Nothing has been recorded yet.")
                    undo_btn.state(["disabled"])
                    return
                reason = self.mgr.undo_check(e)
                undo_btn.state(["disabled"] if reason else ["!disabled"])
                why.configure(text=reason or {"install": "This install can be undone: the new files are put aside and "
                                                          "the old ones come back.",
                                              "update": "This update can be undone: the new files are put aside and the "
                                                        "old version comes back.",
                                              }.get(e["kind"], "This change can be undone."))

            def fill():
                tv.delete(*tv.get_children())
                for e in self.mgr.journal():
                    tag = "undone" if e.get("undone") else ("" if e["kind"] in self.mgr.UNDOABLE else "note")
                    tv.insert("", "end", iid=e["id"], tags=(tag,) if tag else (), values=(
                        self._when(e["ts"]), e["text"], "undone" if e.get("undone") else ""))
                status_pick()

            def do_undo():
                e = sel()
                if not e or not self._ready():
                    return
                if not messagebox.askyesno(APP_NAME, f"Undo this?\n\n{e['text']}", parent=d):
                    return
                if not self.mgr_lock.acquire(blocking=False):
                    messagebox.showinfo(APP_NAME, "An install is running. Try again when it has finished.", parent=d)
                    return
                try:
                    self.configure(cursor="watch")
                    self.update_idletasks()
                    r = self.mgr.undo(e["id"])
                finally:
                    self.configure(cursor="")
                    self.mgr_lock.release()
                self.refresh()
                fill()
                if r["ok"]:
                    self.status.set(r["text"])
                else:
                    messagebox.showwarning(APP_NAME, r["text"] + ("\n\n" + "\n".join(r["errors"][:8]) if r["errors"] else ""),
                                           parent=d)
            undo_btn.configure(command=do_undo)
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")
            tv.bind("<<TreeviewSelect>>", status_pick)
            fill()
            kids = tv.get_children()
            if kids:
                tv.selection_set(kids[0])

        # ======================================================================
        # Round 2: check-up, crash finder, log reader, requirement prompts, banner
        # ======================================================================
        def _fill_tools_extra(self, m, st):
            m.add_separator()
            n = self._warn_total()
            m.add_command(label="Check-up…" + (f"   ({n})" if n else ""), command=self.checkup_dialog, state=st)
            m.add_command(label="Find the mod that crashes my game…", command=self.crash_dialog, state=st)
            m.add_command(label="Read the game's logs…", command=self.logs_dialog, state=st)
            m.add_separator()
            m.add_command(label="Back up my settings…", command=self.settings_backup_dialog, state=st)
            m.add_command(label="Restore settings from a backup…", command=self.settings_restore_dialog, state=st)
            m.add_command(label="Export my mod list…", command=self.export_list_dialog, state=st)
            m.add_command(label="Import a mod list…", command=self.import_list_dialog, state=st)
            m.add_command(label="Saves per instance…", command=self.saves_dialog, state=st)
            m.add_command(label="Endorse the mods I use…", command=self.endorse_dialog, state=st)

        def _warn_total(self) -> int:
            return sum(1 for f in self.findings if f["sev"] in ("problem", "warn"))

        # ---- running the check-up in the background -------------------------------------------------------
        def run_checkup(self, done=None):
            """Check-up off the screen thread; `done(findings or None)` runs on it afterwards."""
            if not self.mgr:
                return
            if done:
                self._checkup_waiters.append(done)
            if self._checking:
                return
            self._checking = True
            mgr = self.mgr

            def work():
                try:
                    return mgr.check_up()
                except RuntimeError:                              # a list changed while it was being read
                    time.sleep(0.3)
                    return mgr.check_up()

            def finish(fs):
                self._checking = False
                waiters, self._checkup_waiters = self._checkup_waiters, []
                if mgr is self.mgr and fs is not None:
                    self.findings = fs
                    warn = defaultdict(list)
                    for f in fs:
                        if f["sev"] in ("problem", "warn"):
                            for name in f.get("mods") or ([f["mod"]] if f["mod"] else []):
                                warn[name].append(f)
                    self._warn_mods = dict(warn)
                    self.populate()
                for cb in waiters:
                    try:
                        cb(fs)
                    except tk.TclError:
                        pass
            self.bg(work, finish, lambda e: finish(None))

        # ---- banner under the header --------------------------------------------------------------------------
        def show_banner(self, text, buttons):
            self.hide_banner()
            b = tk.Frame(self, bg=T["panel"], highlightthickness=1, highlightbackground=T["line"])
            for lab, cmd in reversed(buttons):
                ttk.Button(b, text=lab, command=lambda c=cmd: (self.hide_banner(), c() if c else None)
                           ).pack(side="right", padx=(0, 8), pady=6)
            tk.Label(b, text=text, fg=T["fg"], bg=T["panel"], font=font(10), anchor="w", justify="left",
                     wraplength=760).pack(side="left", fill="x", expand=True, padx=12, pady=8)
            b.pack(fill="x", padx=26, pady=(8, 0), before=self.host)
            self.banner = b

        def hide_banner(self):
            if self.banner is not None:
                try:
                    self.banner.destroy()
                except tk.TclError:
                    pass
                self.banner = None

        def _startup_checks(self, force=False):
            """After the game folder is loaded: look for a game update, a crash search that was left open, problems."""
            if not self.mgr or (os.environ.get("CP2077_NO_WELCOME") and not force):
                return
            mgr = self.mgr
            patch = mgr.check_game_patch()

            def after(fs):
                if mgr is not self.mgr or fs is None:
                    return
                if CrashFinder(mgr).active():
                    self.show_banner("A crash search is still open - your mods are set up for its current test.",
                                     [("Continue the search", self.crash_dialog)])
                    return
                if patch["changed"]:
                    stale = mgr.stale_after_patch(self.mods)
                    names = ", ".join(m.name for m in stale[:6]) + (" …" if len(stale) > 6 else "")
                    text = ("Cyberpunk 2077 was updated since this app last looked."
                            + (f" {len(stale)} mod{'s' if len(stale) != 1 else ''} that reach{'es' if len(stale) == 1 else ''} "
                               f"into the game {'has' if len(stale) == 1 else 'have'} no update on Nexus since: {names}. "
                               "Check their pages before you play." if stale else
                               " Nothing you have installed looks out of date for it."))
                    self.show_banner(text, [("Open check-up", self.checkup_dialog), ("Got it", mgr.ack_game_patch)])
                    return
                n = sum(1 for f in fs if f["sev"] == "problem")
                if n:
                    self.show_banner(f"The check-up found {n} problem{'s' if n != 1 else ''} "
                                     "(for example a mod in the wrong folder, or a framework that is switched off).",
                                     [("Open check-up", self.checkup_dialog), ("Later", None)])
            self.run_checkup(after)

        # ---- the check-up window ----------------------------------------------------------------------------------
        SEV_LABEL = {"problem": "PROBLEM", "warn": "CHECK", "info": "FYI"}

        def checkup_dialog(self):
            if not self.mgr:
                return
            d = self.dialog("Check-up", 960, 700, resizable=True)
            tk.Label(d, text="Check-up", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="Looks for mods in the wrong folder, leftovers of removed mods, mods that need a framework "
                             "that is off or missing, mods that change the same game files, and mods whose Nexus page "
                             "looks abandoned or is gone. Nothing changes until you press a fix button, and fixes can be "
                             "undone in Tools → History and undo.", fg=T["muted"], bg=T["bg"], font=font(9), anchor="w",
                     justify="left", wraplength=880).pack(fill="x", padx=26, pady=(0, 8))
            top = tk.Frame(d, bg=T["bg"])
            top.pack(fill="x", padx=26, pady=(0, 6))
            head = tk.Label(top, text="Checking…", fg=T["fg"], bg=T["bg"], font=font(10, True), anchor="w")
            head.pack(side="left")
            show_fyi = tk.BooleanVar(value=True)
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            detail = tk.Label(d, text="", fg=T["fg"], bg=T["bg"], font=font(10), anchor="nw", justify="left",
                              wraplength=880, height=5)
            detail.pack(side="bottom", fill="x", padx=26, pady=(8, 0))
            fr, tv = self._table(d, [("sev", "", 90, "w", False), ("what", "WHAT", 560, "w", True),
                                     ("mod", "MOD", 230, "w", False)], select="browse")
            fr.pack(fill="both", expand=True, padx=26)
            tv.tag_configure("problem", foreground=T["red"])
            tv.tag_configure("warn", foreground=T["amber"])
            tv.tag_configure("info", foreground=T["muted"])
            fix_btn = ttk.Button(row, text="Fix", style="Accent.TButton")
            nx_btn = ttk.Button(row, text="Open on Nexus")
            lib_btn = ttk.Button(row, text="Show in library")
            fix_btn.pack(side="left")
            nx_btn.pack(side="left", padx=8)
            lib_btn.pack(side="left")
            again_btn = ttk.Button(row, text="Check again")
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")
            again_btn.pack(side="right", padx=8)
            ttk.Checkbutton(top, text="Show “for information” items", variable=show_fyi,
                            command=lambda: fill(self.findings)).pack(side="right")
            by_id = {}

            def cur():
                s = tv.selection()
                return by_id.get(s[0]) if s else None

            def pick(*_):
                f = cur()
                if not f:
                    detail.configure(text="Select a line to read more." if by_id else "")
                    for b in (fix_btn, nx_btn, lib_btn):
                        b.state(["disabled"])
                    return
                detail.configure(text=f["detail"] or f["title"])
                fx = f.get("fix")
                fix_btn.configure(text=fx["label"] if fx else "Fix")
                fix_btn.state(["!disabled"] if fx else ["disabled"])
                if f.get("nexus_id"):
                    nx_btn.configure(text="Open on Nexus")
                    nx_btn.state(["!disabled"])
                elif f.get("search"):
                    nx_btn.configure(text="Search on Nexus")
                    nx_btn.state(["!disabled"])
                else:
                    nx_btn.state(["disabled"])
                has = any(m.name in (f.get("mods") or [f["mod"]]) for m in self.mods)
                lib_btn.state(["!disabled"] if has else ["disabled"])

            def fill(fs):
                if not d.winfo_exists():
                    return
                by_id.clear()
                tv.delete(*tv.get_children())
                if fs is None:
                    head.configure(text="The check-up couldn't finish.")
                    pick()
                    return
                for f in fs:
                    if f["sev"] == "info" and not show_fyi.get():
                        continue
                    by_id[f["id"]] = f
                    tv.insert("", "end", iid=f["id"], tags=(f["sev"],), values=(self.SEV_LABEL[f["sev"]], f["title"], f["mod"]))
                c = Counter(f["sev"] for f in fs)
                head.configure(text=("Nothing found. All good." if not fs else
                                     f"{c['problem']} problem{'s' if c['problem'] != 1 else ''},  {c['warn']} to check,  "
                                     f"{c['info']} for information."))
                kids = tv.get_children()
                if kids:
                    tv.selection_set(kids[0])
                pick()

            def again():
                head.configure(text="Checking…")
                self.run_checkup(fill)

            def do_fix():
                f = cur()
                fx = f.get("fix") if f else None
                if not fx or not self._ready():
                    return
                undo = "" if fx["action"] == "forget" else "\n\nYou can undo this in Tools → History and undo."
                if not messagebox.askyesno(APP_NAME, f"{fx['label']}?\n\n{f['title']}{undo}", parent=d):
                    return
                if not self.mgr_lock.acquire(blocking=False):
                    messagebox.showinfo(APP_NAME, "An install is running. Try again when it has finished.", parent=d)
                    return
                try:
                    self.configure(cursor="watch")
                    self.update_idletasks()
                    r = self.mgr.fix(f)
                finally:
                    self.configure(cursor="")
                    self.mgr_lock.release()
                self.refresh()
                self.status.set(r["text"])
                if r["errors"]:
                    messagebox.showwarning(APP_NAME, r["text"] + "\n\n" + "\n".join(r["errors"][:8]), parent=d)
                again()

            def nexus():
                f = cur()
                if f:
                    webbrowser.open(f"{NEXUS_SITE}/{DOMAIN}/mods/{f['nexus_id']}" if f.get("nexus_id") else search_url(f["search"]))

            def to_library():
                f = cur()
                if not f:
                    return
                for name in (f.get("mods") or [f["mod"]]):
                    if any(m.name == name for m in self.mods):
                        d.destroy()
                        self.show_page("lib")
                        self.filter.set("All")
                        self.search.set("")
                        self.select_name(name)
                        return
            fix_btn.configure(command=do_fix)
            nx_btn.configure(command=nexus)
            lib_btn.configure(command=to_library)
            again_btn.configure(command=again)
            tv.bind("<<TreeviewSelect>>", pick)
            tv.bind("<Double-1>", lambda _e: do_fix() if (cur() or {}).get("fix") else None)
            d._checkup = {"fill": fill, "cur": cur, "tv": tv, "fix": do_fix, "again": again}
            again()

        # ---- before switching mods on / off: what do they need? -------------------------------------------
        def _ask_requirements(self, mods, plan):
            """-> list of mods to switch on (the chosen ones, plus the frameworks they need if the person agrees), or None."""
            lines = []
            for who, labels in sorted(plan["why"].items(), key=lambda kv: kv[0].lower()):
                lines.append(f"•  {who} needs {', '.join(labels)}")
            text = "\n".join(lines[:8]) + ("\n…" if len(lines) > 8 else "")
            if plan["also"]:
                names = ", ".join(m.name for m in plan["also"])
                body = f"{text}\n\nThey are switched off right now: {names}."
                if plan["missing"]:
                    body += f"\n\nNot installed at all: {', '.join(plan['missing'])} (get them from Nexus)."
                pick = self.choose("These mods need something that is off", body,
                                   ["Switch them on too", "Only the ones I picked", "Cancel"], width=700)
                if pick is None or pick == 2:
                    return None
                return mods + plan["also"] if pick == 0 else mods
            body = f"{text}\n\nNot installed: {', '.join(plan['missing'])}. Without it the mod will not work. " \
                   "Get it from Nexus Mods first, or continue anyway."
            pick = self.choose("A framework is missing", body, ["Continue anyway", "Cancel"], width=700)
            return mods if pick == 0 else None

        # ---- find the mod that crashes my game ------------------------------------------------------------------
        def crash_dialog(self):
            if not self.mgr:
                return
            cf = CrashFinder(self.mgr)
            d = self.dialog("Find the mod that crashes my game", 800, 680, resizable=True)
            tk.Label(d, text="Find the mod that crashes my game", fg=T["accent"], bg=T["bg"], font=font(14, True),
                     anchor="w").pack(fill="x", padx=26, pady=(22, 4))
            msg = tk.Label(d, text="", fg=T["fg"], bg=T["bg"], font=font(10), anchor="nw", justify="left", wraplength=740)
            msg.pack(fill="x", padx=26, pady=(0, 6))
            sub = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(9), anchor="nw", justify="left", wraplength=740)
            sub.pack(fill="x", padx=26, pady=(0, 6))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            fr, tv = self._table(d, [("mod", "SUSPECT", 440, "w", True), ("st", "", 240, "w", False)], select="browse")
            fr.pack(fill="both", expand=True, padx=26)
            tv.tag_configure("in", foreground=T["accent"])
            tv.tag_configure("cleared", foreground=T["muted"])
            btns = {}
            ui = {"after": None}

            def clear_buttons():
                for b in btns.values():
                    b.destroy()
                btns.clear()
                tip = ui.pop("tip", None)
                if tip is not None:
                    tip.destroy()

            def add(key, text, cmd, accent=False, side="left"):
                b = ttk.Button(row, text=text, command=cmd, style="Accent.TButton" if accent else "TButton")
                b.pack(side=side, padx=(0, 8) if side == "left" else (8, 0))
                btns[key] = b
                return b

            def locked(fn):
                if not self.mgr_lock.acquire(blocking=False):
                    messagebox.showinfo(APP_NAME, "An install is running. Try again when it has finished.", parent=d)
                    return None
                try:
                    self.configure(cursor="watch")
                    self.update_idletasks()
                    return fn()
                finally:
                    self.configure(cursor="")
                    self.mgr_lock.release()

            def start():
                if not self._ready():
                    return
                try:
                    if not messagebox.askyesno(
                            APP_NAME, "Start the search?\n\nThe app will switch your mods on and off in turns (the frameworks "
                                      "stay on). At the end everything is put back the way it is now - a copy of the current "
                                      "setup is also saved as the instance “" + BISECT_INSTANCE + "”.", parent=d):
                        return
                    locked(cf.start)
                except ValueError as e:
                    messagebox.showinfo(APP_NAME, str(e), parent=d)
                    return
                self.refresh()
                render()

            def answer(crashed):
                if not self._ready():
                    return
                try:
                    locked(lambda: cf.answer(crashed))
                except ValueError as e:
                    messagebox.showinfo(APP_NAME, str(e), parent=d)
                self.refresh()
                if cf.st.get("errors"):
                    messagebox.showwarning(APP_NAME, "Some mods couldn't be moved:\n\n" + "\n".join(cf.st["errors"][:8]),
                                           parent=d)
                render()

            def finish(keep_off):
                if not self._ready():
                    return
                r = locked(lambda: cf.finish(keep_off))
                self.refresh()
                if r and r["errors"]:
                    messagebox.showwarning(APP_NAME, "Some mods couldn't be put back:\n\n" + "\n".join(r["errors"][:8]) +
                                           "\n\nThe search is still open; fix the problem and try again.", parent=d)
                    render()
                    return
                self.status.set("Crash search finished - your mods are back" + (", with the culprit off." if keep_off else "."))
                d.destroy()

            def stop():
                if messagebox.askyesno(APP_NAME, "Stop the search and put every mod back the way it was before it?", parent=d):
                    finish(False)

            def game_state():
                if not d.winfo_exists():
                    return
                running = game_running()
                for k in ("crashed", "fine"):
                    if k in btns:
                        btns[k].state(["disabled"] if running else ["!disabled"])
                if "tip" in ui:
                    ui["tip"].configure(text="The game is running - close it, then tell me what happened." if running else "")
                ui["after"] = d.after(1500, game_state)

            def render():
                if not d.winfo_exists():
                    return
                clear_buttons()
                tv.delete(*tv.get_children())
                st = cf.st
                if not cf.active():
                    n = len(cf.suspects_now())
                    msg.configure(text=f"Your game crashes (or misbehaves) and you do not know which mod does it? The app can "
                                       f"narrow it down for you: it switches half of your {n} switched-on mods off, you start "
                                       "the game and tell it what happened, and it repeats - 10 mods take about 6 tries, "
                                       "100 about 9. The frameworks (Cyber Engine Tweaks, RED4ext, Codeware, …) always stay on.")
                    sub.configure(text="Good to know: this finds ONE mod that makes the problem happen. Mods that need each other "
                                       "can fool it, and it only works for a problem you can make happen on purpose (a crash at "
                                       "the main menu or when you load a save, say). The last step always checks the result. "
                                       "Mods that are already off stay off. Nothing is deleted.")
                    add("start", "Start the search", start, accent=True)
                    add("close", "Close", d.destroy, side="right")
                    return
                if st["phase"] == "testing":
                    step = st["step"]
                    left = len(st["cand"])
                    more = cf.remaining()
                    head = {"baseline": "Test 1: only the frameworks are on.",
                            "halve": f"Test {st['tests']}: {len(st['half'])} of the {left} suspects are on.",
                            "confirm": f"Final check: everything is on except “{st['cand'][0]['name']}”."}[step]
                    todo = {"baseline": "Start the game and do whatever made it crash. If it still goes wrong with no mods on, "
                                        "the problem is not one of your mods.",
                            "halve": "Start the game and do whatever made it crash.",
                            "confirm": "Start the game one last time. If it runs fine without this mod, we have our culprit."}[step]
                    msg.configure(text=f"{head}\n\n{todo}\n\nThen close the game and tell me what happened.")
                    sub.configure(text=f"Suspects left: {left}.   About {more} more test{'s' if more != 1 else ''}.   "
                                       "You can close this window and come back through Tools - the search is kept.")
                    inn = set(st["half"]) if step == "halve" else set()
                    for c in st["cand"]:
                        tv.insert("", "end", values=(c["name"], "on in this test" if c["name"] in inn else "off in this test"),
                                  tags=("in",) if c["name"] in inn else ())
                    for c in st["good"]:
                        tv.insert("", "end", values=(c["name"], "cleared - on in this test"), tags=("cleared",))
                    add("crashed", "It crashed / the problem is there", lambda: answer(True), accent=True)
                    add("fine", "It ran fine", lambda: answer(False))
                    add("play", "Start the game", self.play)
                    add("stop", "Stop and put everything back", stop, side="right")
                    ui["tip"] = tk.Label(d, text="", fg=T["amber"], bg=T["bg"], font=font(9), anchor="w")
                    ui["tip"].pack(side="bottom", fill="x", padx=26)
                    if ui["after"]:
                        d.after_cancel(ui["after"])
                    game_state()
                    return
                outcome = st.get("outcome")
                if outcome == "confirmed":
                    name = st["culprit"]
                    msg.configure(text=f"The culprit is “{name}”.\n\nThe game runs without it, and goes wrong with it on.")
                    sub.configure(text="Look for a newer version on its Nexus page, check its comments, or leave it off. "
                                       "Everything else can go back on now.")
                    tv.insert("", "end", values=(name, "found"), tags=("in",))
                    add("keep", f"Put everything back, keep “{name}” off", lambda: finish(True), accent=True)
                    add("all", "Put everything back (including it)", lambda: finish(False))
                elif outcome == "frameworks":
                    msg.configure(text="The game goes wrong even with none of your ordinary mods on.")
                    sub.configure(text="So it is not one of them. Look at a framework (update Cyber Engine Tweaks, RED4ext, "
                                       "redscript, Codeware …), at the game files (verify them in Steam/GOG), or at your "
                                       "save. Tools → Read the game's logs may help.")
                    add("all", "Put everything back", lambda: finish(False), accent=True)
                else:
                    msg.configure(text="No single mod explains it.")
                    sub.configure(text="The game still goes wrong without the last suspect, so more than one mod is involved "
                                       "(or two mods work against each other), or something else is wrong. Run the search "
                                       "again after putting everything back and leave out the mod you most suspect, or read "
                                       "the logs (Tools → Read the game's logs).")
                    add("all", "Put everything back", lambda: finish(False), accent=True)

            def stop_poll(e):
                if e.widget is d and ui["after"]:
                    try:
                        d.after_cancel(ui["after"])
                    except tk.TclError:
                        pass
            d.bind("<Destroy>", stop_poll)
            d._crash = {"render": render, "cf": cf, "start": start, "answer": answer, "finish": finish}
            render()

        # ---- the game's logs -------------------------------------------------------------------------------------
        def logs_dialog(self):
            if not self.mgr:
                return
            d = self.dialog("The game's logs", 940, 700, resizable=True)
            tk.Label(d, text="The game's logs", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="Reads the end of the logs that RED4ext, redscript and Cyber Engine Tweaks write, picks out the "
                             "error lines and points at the mods they mention. A mod named here is a lead, not proof: it "
                             "may only be the one that reported someone else's mistake.", fg=T["muted"], bg=T["bg"],
                     font=font(9), anchor="w", justify="left", wraplength=880).pack(fill="x", padx=26, pady=(0, 8))
            head = tk.Label(d, text="Reading…", fg=T["fg"], bg=T["bg"], font=font(10), anchor="w", justify="left",
                            wraplength=880)
            head.pack(fill="x", padx=26)
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            fr1, sus = self._table(d, [("mod", "MODS NAMED IN ERROR LINES", 600, "w", True), ("n", "LINES", 90, "e", False)],
                                   height=5, select="browse")
            fr1.pack(fill="x", padx=26, pady=(8, 6))
            fr2, lines = self._table(d, [("log", "LOG", 190, "w", False), ("text", "ERROR LINE", 540, "w", True),
                                         ("mods", "MOD", 150, "w", False)], select="browse")
            fr2.pack(fill="both", expand=True, padx=26)
            full = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(9), anchor="nw", justify="left",
                            wraplength=880, height=3)
            full.pack(side="bottom", fill="x", padx=26, pady=(6, 0))
            only = tk.BooleanVar(value=False)
            st = {"lg": None, "mod": ""}
            ttk.Checkbutton(row, text="Only lines that name a mod", variable=only, command=lambda: fill_lines()).pack(side="left")
            lib_btn = ttk.Button(row, text="Show mod in library")
            lib_btn.pack(side="left", padx=12)
            ttk.Button(row, text="Open the game folder", command=lambda: open_folder(self.mgr.game)).pack(side="left")
            again_btn = ttk.Button(row, text="Read again")
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")
            again_btn.pack(side="right", padx=8)

            def fill_lines():
                lines.delete(*lines.get_children())
                lg = st["lg"]
                if not lg:
                    return
                for i, l in enumerate(lg["lines"]):
                    if only.get() and not l["mods"]:
                        continue
                    if st["mod"] and st["mod"] not in l["mods"]:
                        continue
                    lines.insert("", "end", iid=str(i), values=(l["log"], l["text"], ", ".join(l["mods"])))

            def pick_line(*_):
                s = lines.selection()
                full.configure(text=(st["lg"]["lines"][int(s[0])]["text"] if s and st["lg"] else ""))

            def pick_mod(*_):
                s = sus.selection()
                st["mod"] = sus.item(s[0], "values")[0] if s else ""
                lib_btn.state(["!disabled"] if st["mod"] else ["disabled"])
                fill_lines()

            def fill(lg):
                if not d.winfo_exists():
                    return
                st["lg"] = lg
                sus.delete(*sus.get_children())
                for name, n in lg["suspects"]:
                    sus.insert("", "end", values=(name, n))
                if not lg["files"]:
                    head.configure(text="No recent log files were found. They appear in the game folder after you have played "
                                        "with RED4ext, redscript or Cyber Engine Tweaks installed:\n"
                                        "red4ext\\logs, r6\\logs and bin\\x64\\plugins\\cyber_engine_tweaks. "
                                        "(Logs older than 30 days are ignored.)")
                else:
                    head.configure(text=f"Read {len(lg['files'])} log file{'s' if len(lg['files']) != 1 else ''} "
                                        f"(newest {self._when(lg['files'][0]['mtime'])}).  "
                                        f"{len(lg['lines'])} error line{'s' if len(lg['lines']) != 1 else ''}, "
                                        f"{lg['unknown']} that name no mod.")
                st["mod"] = ""
                lib_btn.state(["disabled"])
                fill_lines()

            def to_library():
                if st["mod"] and any(m.name == st["mod"] for m in self.mods):
                    d.destroy()
                    self.show_page("lib")
                    self.filter.set("All")
                    self.search.set("")
                    self.select_name(st["mod"])

            def read():
                head.configure(text="Reading…")
                mgr = self.mgr
                self.bg(lambda: mgr.read_logs(), fill, lambda e: head.winfo_exists() and head.configure(text=f"Couldn't read the logs: {e}"))
            lib_btn.configure(command=to_library)
            again_btn.configure(command=read)
            sus.bind("<<TreeviewSelect>>", pick_mod)
            lines.bind("<<TreeviewSelect>>", pick_line)
            d._logs = {"fill": fill, "state": st}
            read()

        # ======================================================================
        # Round 3: settings backup and restore, mod lists, saves per instance, endorsing
        # ======================================================================
        def _backup_dir_default(self) -> str:
            saved = load_config().get("settings_backup_dir") or ""
            return saved or str(Path.home() / "Documents" / "ModScout backups")

        def _head(self, d, title, text, wrap=700):
            tk.Label(d, text=title, fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text=text, fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left",
                     wraplength=wrap).pack(fill="x", padx=26, pady=(0, 10))

        # ---- back up the settings of my mods ---------------------------------------------------------------
        def settings_backup_dialog(self):
            if not self.mgr:
                return
            mgr = self.mgr
            d = self.dialog("Back up my settings", 760, 600, resizable=True)
            self._head(d, "Back up my settings",
                       "Packs the settings of your mods into one zip file: Cyber Engine Tweaks and its mods' hotkeys and options, "
                       "RED4ext plugin settings, and the game's own graphics and controls. Only settings files go in - no mods, "
                       "no logs, no program files - so it stays small. Settings of mods that are switched off are included. "
                       "Save it outside the game folder (another drive, or a cloud folder), so it survives a reinstall.", 700)
            box = tk.Frame(d, bg=T["bg"])
            box.pack(fill="x", padx=26)
            vars_ = {}
            for g in mgr.settings_inventory():
                v = tk.BooleanVar(value=bool(g["default"] and g["files"]))
                vars_[g["key"]] = v
                cb = ttk.Checkbutton(box, text=g["label"], variable=v)
                cb.pack(fill="x", anchor="w", pady=(8, 0))
                if not g["files"]:
                    cb.state(["disabled"])
                    v.set(False)
                info = (f"{g['files']} file{'s' if g['files'] != 1 else ''}, {human_size(g['size'])}   ·   {g['where']}"
                        if g["files"] else f"none found   ·   {g['where']}")
                if g["key"] == "r6cfg":
                    info += "   ·   hand-edited game files; usually not needed"
                tk.Label(box, text=info, fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left",
                         wraplength=680).pack(fill="x", padx=(26, 0))
            tk.Label(d, text="Save the backup in this folder:", fg=T["fg"], bg=T["bg"], font=font(10), anchor="w").pack(
                fill="x", padx=26, pady=(18, 4))
            drow = tk.Frame(d, bg=T["bg"])
            drow.pack(fill="x", padx=26)
            dest = tk.StringVar(value=self._backup_dir_default())
            ttk.Entry(drow, textvariable=dest).pack(side="left", fill="x", expand=True)

            def browse():
                p = filedialog.askdirectory(title="Where should the backup go?", parent=d,
                                            initialdir=dest.get() if Path(dest.get()).is_dir() else str(Path.home()))
                if p:
                    dest.set(p)
            ttk.Button(drow, text="Browse…", command=browse).pack(side="left", padx=(8, 0))
            result = tk.Label(d, text="", fg=T["fg"], bg=T["bg"], font=font(10), anchor="nw", justify="left", wraplength=700,
                              height=4)
            result.pack(fill="x", padx=26, pady=(14, 0))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            go_btn = ttk.Button(row, text="Back up now", style="Accent.TButton")
            go_btn.pack(side="left")
            open_btn = ttk.Button(row, text="Open that folder", command=lambda: open_folder(dest.get()))
            open_btn.pack(side="left", padx=8)
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")

            def go():
                keys = [k for k, v in vars_.items() if v.get()]
                if not keys:
                    result.configure(text="Tick at least one group.", fg=T["amber"])
                    return
                where = dest.get().strip()
                if not where:
                    result.configure(text="Choose a folder for the backup.", fg=T["amber"])
                    return
                save_config(settings_backup_dir=where)
                go_btn.state(["disabled"])
                result.configure(text="Backing up…", fg=T["muted"])

                def done(r):
                    if not d.winfo_exists():
                        return
                    go_btn.state(["!disabled"])
                    text = f"Saved {r['files']} settings file{'s' if r['files'] != 1 else ''} ({human_size(r['size'])}) to\n{r['path']}"
                    if r["skipped"]:
                        text += f"\n{len(r['skipped'])} could not be read and were left out: " + "; ".join(r["skipped"][:3])
                    result.configure(text=text, fg=T["green"])
                    self.status.set(f"Settings backed up: {Path(r['path']).name}")

                def fail(e):
                    if d.winfo_exists():
                        go_btn.state(["!disabled"])
                        result.configure(text=str(e), fg=T["red"])
                self.bg(lambda: mgr.settings_backup(where, keys), done, fail)
            go_btn.configure(command=go)
            d._backup = {"go": go, "dest": dest, "vars": vars_, "result": result}

        # ---- restore them --------------------------------------------------------------------------------------
        STATUS_WORD = {"new": "NEW", "changed": "CHANGED", "same": "same"}

        def settings_restore_dialog(self, path=None):
            if not self.mgr:
                return
            mgr = self.mgr
            if path is None:
                start = self._backup_dir_default()
                path = filedialog.askopenfilename(
                    title="Pick a settings backup", initialdir=start if Path(start).is_dir() else str(Path.home()),
                    filetypes=[("ModScout settings backup", "*.zip"), ("All files", "*.*")])
            if not path:
                return
            try:
                self.configure(cursor="watch")
                self.update_idletasks()
                insp = mgr.settings_inspect(path)
            except ValueError as e:
                messagebox.showwarning(APP_NAME, str(e))
                return
            finally:
                self.configure(cursor="")
            d = self.dialog("Restore settings", 860, 660, resizable=True)
            made = f"made {self._when(insp['created'])}" if insp["created"] else "made at an unknown time"
            self._head(d, "Restore settings",
                       f"{Path(path).name}  -  {made}. Nothing has changed yet. Every file that would be replaced is first "
                       "moved to _disabled_mods\\_backup, and the restore can be undone in Tools → History and undo. "
                       "The game must be closed.", 800)
            labels = {g[0]: g[1] for g in SETTINGS_GROUPS}
            gvars, gcount = {}, {}
            for e in insp["entries"]:
                if e["status"] != "same":
                    gcount[e["group"]] = gcount.get(e["group"], 0) + 1
            box = tk.Frame(d, bg=T["bg"])
            box.pack(fill="x", padx=26)
            for key in [g[0] for g in SETTINGS_GROUPS if insp["groups"].get(g[0])]:
                n = gcount.get(key, 0)
                v = tk.BooleanVar(value=bool(n) and key != "r6cfg")
                gvars[key] = v
                cb = ttk.Checkbutton(box, text=f"{labels[key]}   -   {insp['groups'][key]} in the backup, "
                                               f"{n} would change", variable=v, command=lambda: refresh_count())
                cb.pack(fill="x", anchor="w", pady=(4, 0))
                if not n:
                    cb.state(["disabled"])
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            note = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left", wraplength=800)
            note.pack(side="bottom", fill="x", padx=26)
            fr, tv = self._table(d, [("st", "", 90, "w", False), ("file", "FILE", 560, "w", True), ("grp", "FROM", 130, "w", False)],
                                 select="browse")
            fr.pack(fill="both", expand=True, padx=26, pady=(10, 6))
            tv.tag_configure("new", foreground=T["green"])
            tv.tag_configure("changed", foreground=T["amber"])
            tv.tag_configure("same", foreground=T["muted"])
            show_same = tk.BooleanVar(value=False)
            for i, e in enumerate(insp["entries"]):
                nm = e["name"].split("/", 1)[1] if "/" in e["name"] else e["name"]
                src = {"game": "game folder", "off": "switched-off mod", "user": "your user folder"}.get(e["name"].split("/")[0], "")
                e["_iid"], e["_row"] = str(i), (self.STATUS_WORD[e["status"]], nm, src)
            go_btn = ttk.Button(row, text="Restore", style="Accent.TButton")
            go_btn.pack(side="left")

            def wanted():
                keys = [k for k, v in gvars.items() if v.get()]
                return keys, [e for e in insp["entries"] if e["status"] != "same" and e["group"] in keys]

            def refresh_count():
                keys, todo = wanted()
                go_btn.configure(text=f"Restore {len(todo)} file{'s' if len(todo) != 1 else ''}")
                go_btn.state(["!disabled"] if todo else ["disabled"])

            def fill():
                tv.delete(*tv.get_children())
                for e in insp["entries"]:
                    if e["status"] == "same" and not show_same.get():
                        continue
                    tv.insert("", "end", iid=e["_iid"], tags=(e["status"],), values=e["_row"])
                c = insp["counts"]
                note.configure(text=f"{c.get('new', 0)} new, {c.get('changed', 0)} changed, {c.get('same', 0)} already the same."
                                    + (f"  {len(insp['skipped'])} item{'s' if len(insp['skipped']) != 1 else ''} in the zip "
                                       "will not be restored (they are not settings files, or would land in a place I do not "
                                       "write to)." if insp["skipped"] else ""))
            ttk.Checkbutton(row, text="Show files that are already the same", variable=show_same, command=fill).pack(
                side="left", padx=12)
            if insp["skipped"]:
                ttk.Button(row, text="What is skipped?", command=lambda: messagebox.showinfo(
                    APP_NAME, "Not restored:\n\n• " + "\n• ".join(insp["skipped"][:14])
                    + ("\n…" if len(insp["skipped"]) > 14 else ""), parent=d)).pack(side="left")
            ttk.Button(row, text="Cancel", command=d.destroy).pack(side="right")

            def go():
                keys, todo = wanted()
                if not todo or not self._ready():
                    return
                if not messagebox.askyesno(APP_NAME, f"Restore {len(todo)} settings file(s)?\n\nThe files they replace are kept, "
                                                     "and you can undo this in Tools → History and undo.", parent=d):
                    return
                d.destroy()

                def work(p):
                    with self.mgr_lock:
                        return mgr.settings_restore(path, keys, p)

                def done(r):
                    self.refresh()
                    self.status.set(f"Restored {r['restored']} settings file(s).")
                    text = f"Restored {r['restored']} settings file(s)."
                    if r["backup"]:
                        text += "\n\nThe files they replaced were kept, and Tools → History and undo can put them back."
                    if r["errors"]:
                        text += "\n\nCould not restore:\n• " + "\n• ".join(r["errors"][:8])
                    (messagebox.showwarning if r["errors"] else messagebox.showinfo)(APP_NAME, text)
                self.start_job("Restoring settings…", work, done)
            go_btn.configure(command=go)
            fill()
            refresh_count()
            d._restore = {"go": go, "gvars": gvars, "tv": tv, "insp": insp, "refresh": refresh_count}

        # ---- my mods as a list ---------------------------------------------------------------------------------
        def export_list_dialog(self):
            if not self.mgr:
                return
            mgr = self.mgr
            d = self.dialog("Export my mod list", 680, 560)
            self._head(d, "Export my mod list",
                       "Writes the mods you have as a list - their names, Nexus numbers, versions and whether each is switched on. "
                       "No folder names and nothing personal goes in. Send it to a friend, post it on a forum, or keep it as a "
                       "record of your setup.", 620)
            tk.Label(d, text="Title:", fg=T["fg"], bg=T["bg"], font=font(10), anchor="w").pack(fill="x", padx=26)
            title = tk.StringVar(value="My Cyberpunk 2077 mods")
            ttk.Entry(d, textvariable=title).pack(fill="x", padx=26, pady=(2, 10))
            fmt = tk.StringVar(value="json")
            for val, text in (("json", "A file for ModScout  -  your friend can open it with “Import a mod list” and compare, "
                                       "download what is missing and make an instance from it"),
                              ("text", "A text list for a forum post or chat  -  one line per mod, linked to its Nexus page")):
                tk.Radiobutton(d, text=text, variable=fmt, value=val, bg=T["bg"], fg=T["fg"], selectcolor=T["panel2"],
                               activebackground=T["bg"], activeforeground=T["fg"], font=font(10), anchor="w", justify="left",
                               wraplength=600, highlightthickness=0, bd=0).pack(fill="x", padx=26, pady=2)
            notes = tk.BooleanVar(value=False)
            ttk.Checkbutton(d, text="Include my notes and tags (they are private otherwise)", variable=notes).pack(
                anchor="w", padx=26, pady=(10, 0))
            msg = tk.Label(d, text="", fg=T["green"], bg=T["bg"], font=font(10), anchor="nw", justify="left", wraplength=620,
                           height=3)
            msg.pack(fill="x", padx=26, pady=(12, 0))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)

            def save():
                js = fmt.get() == "json"
                p = filedialog.asksaveasfilename(
                    parent=d, title="Save the mod list", defaultextension=".json" if js else ".md",
                    initialfile="my-cyberpunk-mods" + (".json" if js else ".md"),
                    filetypes=[("ModScout mod list", "*.json")] if js else [("Text (Markdown)", "*.md"), ("Text", "*.txt")])
                if not p:
                    return
                try:
                    r = mgr.export_list(p, fmt.get(), title.get(), notes.get())
                except OSError as e:
                    msg.configure(text=f"Couldn't save it: {e}", fg=T["red"])
                    return
                msg.configure(text=f"Saved {r['mods']} mods to\n{r['path']}", fg=T["green"])
                self.status.set(f"Mod list saved: {Path(r['path']).name}")

            def copy():
                text, n = mgr.list_text("text", title.get(), notes.get())
                self.clipboard_clear()
                self.clipboard_append(text)
                msg.configure(text=f"Copied {n} mods as text. Paste it into your post.", fg=T["green"])
            ttk.Button(row, text="Save as…", style="Accent.TButton", command=save).pack(side="left")
            ttk.Button(row, text="Copy as text", command=copy).pack(side="left", padx=8)
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")
            d._export = {"save": save, "copy": copy, "fmt": fmt, "notes": notes, "title": title, "msg": msg}

        LIST_STATE = {
            "same": ("You have it", "muted"),
            "older": ("You have an older version", "orange"),
            "newer": ("You have a newer version", "muted"),
            "name": ("You have a mod with this name (not linked to Nexus)", "muted"),
            "missing": ("Not installed  -  it is on Nexus", "amber"),
            "absent": ("Not installed  -  not on Nexus, so find it yourself", "amber"),
        }

        def import_list_dialog(self, path=None):
            if not self.mgr:
                return
            mgr = self.mgr
            if path is None:
                path = filedialog.askopenfilename(title="Open a mod list",
                                                  filetypes=[("ModScout mod list", "*.json"), ("All files", "*.*")])
            if not path:
                return
            try:
                lst = mgr.read_list(path)
            except ValueError as e:
                messagebox.showwarning(APP_NAME, str(e))
                return
            rows = mgr.compare_list(lst)
            d = self.dialog("Import a mod list", 980, 700, resizable=True)
            self._head(d, f"Mod list: {lst['name']}",
                       "Nothing is installed or changed by opening a list. Compare it with what you have, then download what is "
                       "missing (you will see each download in the Downloads tab) or make a new instance that switches the "
                       "same mods on and off. Mods download in their newest version, which can be newer than the list's.", 920)
            c = Counter(r["state"] for r in rows)
            head = tk.Label(d, text=f"{len(rows)} mods in the list.  {c['same'] + c['newer'] + c['name']} you have,  "
                                    f"{c['older']} older here,  {c['missing']} to download from Nexus,  "
                                    f"{c['absent']} not on Nexus.", fg=T["fg"], bg=T["bg"], font=font(10, True), anchor="w")
            head.pack(fill="x", padx=26)
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            detail = tk.Label(d, text="", fg=T["fg"], bg=T["bg"], font=font(10), anchor="nw", justify="left", wraplength=920,
                              height=3)
            detail.pack(side="bottom", fill="x", padx=26)
            fr, tv = self._table(d, [("mod", "MOD", 330, "w", True), ("theirs", "IN THE LIST", 110, "w", False),
                                     ("yours", "YOU HAVE", 110, "w", False), ("state", "", 360, "w", True)], select="extended")
            fr.pack(fill="both", expand=True, padx=26, pady=(8, 6))
            for k, col in (("muted", "muted"), ("orange", "orange"), ("amber", "amber"), ("red", "red")):
                tv.tag_configure(k, foreground=T[col])
            for i, r in enumerate(rows):
                text, tag = self.LIST_STATE[r["state"]]
                tv.insert("", "end", iid=str(i), tags=(tag,), values=(
                    r["name"] + ("" if r["enabled"] else "   (off in the list)"), r["version"], r["local_version"], text))

            def chosen():
                sel = [rows[int(i)] for i in tv.selection()]
                return sel

            def pick(*_):
                s = chosen()
                if len(s) == 1 and (s[0]["note"] or s[0]["tags"]):
                    detail.configure(text=("Note: " + s[0]["note"] if s[0]["note"] else "")
                                          + ("\nTags: " + ", ".join(s[0]["tags"]) if s[0]["tags"] else ""))
                else:
                    detail.configure(text="")
            tv.bind("<<TreeviewSelect>>", pick)

            def download():
                sel = chosen()
                todo = [r for r in (sel or rows) if r["state"] == "missing"]
                if not todo:
                    messagebox.showinfo(APP_NAME, "Nothing to download: every mod in the list that is on Nexus is already "
                                                  "installed." if not sel else "None of the selected mods is missing.", parent=d)
                    return
                nx = self.nexus_client()
                if not nx or not self._ready():
                    return
                if len(todo) > 3 and not messagebox.askyesno(
                        APP_NAME, f"Queue {len(todo)} downloads?\n\nWith Nexus Premium they download by themselves. Without "
                                  "it, each one opens its Nexus page and waits until you press “Slow download”.", parent=d):
                    return
                d.destroy()

                def work(p):
                    out = []
                    for i, r in enumerate(todo):
                        p(i, len(todo), f"Looking up files for {r['name']}…")
                        try:
                            out.append((r, plan_update(nx.files(r["nexus_id"]), None, ""), ""))
                        except NexusError as e:
                            out.append((r, None, str(e)))
                    return out

                def done(plans):
                    started, skipped = 0, []
                    for r, plan, why in plans:
                        if plan is None:
                            skipped.append(f"{r['name']} ({why})")
                            continue
                        f = plan["target"]
                        if f is None and len(plan["options"]) > 1 and len(plans) == 1:
                            f = self.choose_file(type("M", (), {"name": r["name"]})(), plan)
                        elif f is None and len(plan["options"]) > 1:
                            skipped.append(f"{r['name']} (several main files - download it yourself and choose)")
                            continue
                        if f is None:
                            if not plan["options"]:
                                skipped.append(f"{r['name']} (no downloadable file)")
                            continue
                        self.add_job("install", r["nexus_id"], r["name"], f)
                        started += 1
                    if skipped:
                        messagebox.showinfo(APP_NAME, "Not queued:\n\n• " + "\n• ".join(skipped[:12]))
                    if started:
                        self.status.set(f"{started} download(s) queued - see Downloads.")
                        self.show_page("dl")
                self.start_job("Looking up the files…", work, done)

            def to_instance():
                name = self.ask_text("New instance from the list", "Name for the new instance:", lst["name"][:40], "Create")
                if not name or not name.strip():
                    return
                try:
                    new = mgr.list_to_instance(rows, name.strip())
                except ValueError as e:
                    messagebox.showwarning(APP_NAME, str(e), parent=d)
                    return
                gone = sum(1 for r in rows if not r.get("local"))
                d.destroy()
                self._sync_instance_btn()
                if messagebox.askyesno(APP_NAME, f"“{new}” was created. It switches on the mods of the list that you have"
                                                 + (f" ({gone} of the list are not installed here)" if gone else "")
                                                 + ", and puts the others away.\n\nSwitch to it now?"):
                    self.switch_to(new)

            def nexus():
                s = chosen()
                if s and s[0]["nexus_id"]:
                    webbrowser.open(f"{NEXUS_SITE}/{DOMAIN}/mods/{s[0]['nexus_id']}")
                elif s:
                    webbrowser.open(search_url(s[0]["name"]))
            ttk.Button(row, text="Download the missing ones", style="Accent.TButton", command=download).pack(side="left")
            ttk.Button(row, text="Make an instance from this list…", command=to_instance).pack(side="left", padx=8)
            ttk.Button(row, text="Open on Nexus", command=nexus).pack(side="left")
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")
            d._import = {"rows": rows, "tv": tv, "download": download, "to_instance": to_instance, "lst": lst}

        # ---- one set of saved games per instance ------------------------------------------------------------------
        def saves_dialog(self):
            if not self.mgr:
                return
            mgr = self.mgr
            d = self.dialog("Saves per instance", 820, 700, resizable=True)
            self._head(d, "Saves per instance",
                       "Normally every instance plays the same saved games. Here an instance can get saves of its own, so a story "
                       "run and a testing setup never touch each other's saves.\n\nHow: the game keeps its saves in one folder. "
                       "When you switch instance (or press Play), that folder is renamed to rest next to it and the other "
                       "instance's folder takes its place. Nothing is copied unless you ask for a copy, and nothing is ever "
                       "deleted. The game must be closed. If a cloud-sync program watches your Saved Games folder, pause it "
                       "first - it can block the rename (nothing is lost if it does).\n\nSteam or GOG cloud saves: the launcher "
                       "may notice a folder that is empty or different and fill it from the cloud. If you use cloud saves, "
                       "give an instance its own saves with “start with a copy”, and check the first launch.", 760)
            top = tk.Frame(d, bg=T["bg"])
            top.pack(fill="x", padx=26)
            where = tk.Label(top, text="", fg=T["fg"], bg=T["bg"], font=font(10), anchor="w", justify="left", wraplength=640)
            where.pack(side="left", fill="x", expand=True)
            change_btn = ttk.Button(top, text="Change…")
            change_btn.pack(side="right")
            on = tk.BooleanVar(value=False)
            chk = ttk.Checkbutton(d, text="Give instances their own saves", variable=on)
            chk.pack(anchor="w", padx=26, pady=(10, 4))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            msg = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(10), anchor="nw", justify="left", wraplength=760,
                           height=3)
            msg.pack(side="bottom", fill="x", padx=26)
            fr, tv = self._table(d, [("name", "INSTANCE", 250, "w", True), ("which", "SAVES", 250, "w", False),
                                     ("n", "SAVED GAMES", 100, "e", False), ("now", "", 110, "w", False)], select="browse")
            fr.pack(fill="both", expand=True, padx=26, pady=(4, 6))
            tv.tag_configure("kept", foreground=T["muted"])
            ownbtn = ttk.Button(row, text="Own saves, empty")
            copybtn = ttk.Button(row, text="Own saves, start with a copy")
            backbtn = ttk.Button(row, text="Use the shared saves")
            for b in (ownbtn, copybtn, backbtn):
                b.pack(side="left", padx=(0, 8))
            ttk.Button(row, text="Open the saves folder", command=lambda: self._open_saves()).pack(side="left")
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")

            def sel():
                s = tv.selection()
                return s[0] if s and not s[0].startswith("kept:") else None

            def fill():
                if not d.winfo_exists():
                    return
                st = mgr.saves_status()
                where.configure(text=("Saves folder:  " + st["dir"] + ("" if st["exists"] else "   (not found)"))
                                if st["dir"] else "Saves folder:  not found - use “Change…” to point me at it.")
                on.set(st["on"])
                counts = {s["set"]: s["saves"] for s in st["sets"]}
                tv.delete(*tv.get_children())
                for n in sorted(mgr.state["instances"], key=str.lower):
                    own = n in st["owners"]
                    tv.insert("", "end", iid=n, values=(n, "its own set" if own else "the shared set",
                                                        counts.get(n if own else "shared", "?"),
                                                        "    in use now" if n == mgr.state["active"] and st["on"] else ""))
                for s in st["sets"]:
                    if s["kept"]:
                        tv.insert("", "end", iid="kept:" + s["set"], tags=("kept",),
                                  values=(f"(was {s['set']}'s)", "kept, belongs to no instance", s["saves"], ""))
                pick()

            def pick(*_):
                n = sel()
                st = mgr.saves_status()
                can = bool(n) and st["on"]
                own = n in st["owners"] if n else False
                ownbtn.state(["!disabled"] if can and not own else ["disabled"])
                copybtn.state(["!disabled"] if can and not own else ["disabled"])
                backbtn.state(["!disabled"] if can and own else ["disabled"])

            def toggle():
                want = on.get()
                st = mgr.saves_status()
                if want and not st["exists"]:
                    on.set(False)
                    messagebox.showinfo(APP_NAME, "I can't find the folder where the game keeps its saves "
                                                  "(normally Saved Games\\CD Projekt Red\\Cyberpunk 2077). Use “Change…” to "
                                                  "point me at it first.", parent=d)
                    return
                if want and not messagebox.askyesno(
                        APP_NAME, "Switch this on?\n\nFrom now on switching instance renames your saves folder. Nothing is "
                                  "deleted, but it is sensible to copy your Saved Games folder somewhere safe first.\n\n"
                                  "Every instance keeps using the shared saves you have now until you give one its own.",
                        parent=d):
                    on.set(False)
                    return
                try:
                    mgr.saves_turn(want)
                except ValueError as e:
                    messagebox.showwarning(APP_NAME, str(e), parent=d)
                msg.configure(text="Each instance with its own saves now gets them when you switch to it or press Play."
                              if want else "Back to one shared set of saves for every instance. Their own sets stay next to "
                                           "your saves folder, untouched.")
                fill()
            chk.configure(command=toggle)

            def give(copy):
                n = sel()
                if not n:
                    return
                if copy and not self._ready():
                    return
                try:
                    mgr.saves_give(n, copy=copy)
                    if n == mgr.state["active"] and not game_running():
                        mgr.saves_sync()
                except ValueError as e:
                    messagebox.showwarning(APP_NAME, str(e), parent=d)
                    fill()
                    return
                msg.configure(text=f"“{n}” now has saves of its own" + (", starting as a copy of the ones in use." if copy
                                                                        else ", starting empty.") +
                              (" They are in place now." if n == mgr.state["active"] else
                               " They are put in place when you switch to it or press Play."))
                fill()

            def back():
                n = sel()
                if not n:
                    return
                where_ = mgr.saves_release(n)
                msg.configure(text=f"“{n}” uses the shared saves again. Its own saves were not touched - they stay in "
                                   f"{where_}.")
                fill()
                self._sync_instance_btn()

            def change():
                st = mgr.saves_status()
                if st["on"]:
                    messagebox.showinfo(APP_NAME, "Switch “Give instances their own saves” off first, so every set is back "
                                                  "where it belongs.", parent=d)
                    return
                p = filedialog.askdirectory(parent=d, title="Pick the folder where Cyberpunk 2077 keeps its saves "
                                                           "(it contains AutoSave-…, ManualSave-… folders)")
                if p:
                    save_config(saves_dir=p)
                    fill()
            ownbtn.configure(command=lambda: give(False))
            copybtn.configure(command=lambda: give(True))
            backbtn.configure(command=back)
            change_btn.configure(command=change)
            tv.bind("<<TreeviewSelect>>", pick)
            d._saves = {"fill": fill, "give": give, "back": back, "toggle": toggle, "on": on, "tv": tv, "msg": msg}
            fill()

        def _open_saves(self):
            st = self.mgr.saves_status() if self.mgr else {}
            if st.get("exists"):
                open_folder(st["dir"])
            else:
                messagebox.showinfo(APP_NAME, "I can't find the saves folder. Use “Change…” to point me at it.")

        # ---- endorse -----------------------------------------------------------------------------------------------
        def endorse_selected(self):
            """Endorse the selected mod on Nexus - or take the endorsement back if it already is endorsed."""
            mods = [m for m in self.selected() if m.nexus_id]
            if len(mods) != 1:
                messagebox.showinfo(APP_NAME, "Select one mod that is linked to Nexus.")
                return
            m, mgr = mods[0], self.mgr
            nx = self.nexus_client()
            if not nx:
                return
            abstain = mgr.endorse_status(m.nexus_id) == "Endorsed"
            if abstain and not messagebox.askyesno(APP_NAME, f"Take back your endorsement of “{m.name}” on Nexus?"):
                return
            self.d_endorse.state(["disabled"])
            self.status.set("Telling Nexus…")

            def done(status):
                self.status.set(f"“{m.name}”: {'endorsement taken back' if status == 'Abstained' else 'endorsed - thank you from the author'}.")
                self.show_details()

            def fail(e):
                self.status.set("Nexus didn't accept that.")
                self.show_details()
                messagebox.showwarning(APP_NAME, str(e))
            self.bg(lambda: mgr.endorse_do(nx, m.nexus_id, m.installed_version or m.latest_version, abstain), done, fail)

        def endorse_dialog(self):
            """Endorse the mods I use: the linked mods that are not endorsed yet, picked from a list."""
            if not self.mgr:
                return
            nx = self.nexus_client()
            if not nx:
                return
            mgr = self.mgr
            d = self.dialog("Endorse the mods I use", 860, 680, resizable=True)
            self._head(d, "Endorse the mods I use",
                       "Endorsing tells an author you like their mod. It is public: it adds one to the mod's counter under your "
                       "Nexus name. Nexus only lets you endorse a mod you have downloaded with your own account, and not "
                       "right after downloading it - any it refuses are listed afterwards. Mods you have already endorsed "
                       "are not shown.", 800)
            head = tk.Label(d, text="Reading your endorsements from Nexus…", fg=T["fg"], bg=T["bg"], font=font(10, True),
                            anchor="w")
            head.pack(fill="x", padx=26)
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            result = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(9), anchor="nw", justify="left", wraplength=800,
                              height=4)
            result.pack(side="bottom", fill="x", padx=26)
            fr, tv = self._table(d, [("mod", "MOD", 420, "w", True), ("ver", "YOUR VERSION", 130, "w", False),
                                     ("st", "ON NEXUS", 150, "w", False)], select="extended")
            fr.pack(fill="both", expand=True, padx=26, pady=(8, 6))
            by_id = {}
            go_btn = ttk.Button(row, text="Endorse the selected", style="Accent.TButton")
            go_btn.pack(side="left")
            all_btn = ttk.Button(row, text="Select all")
            all_btn.pack(side="left", padx=8)
            ttk.Button(row, text="Open on Nexus", command=lambda: [webbrowser.open(by_id[i].url) for i in tv.selection()[:1]
                                                                  if i in by_id]).pack(side="left")
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")
            busy = {"v": False}

            def fill():
                if not d.winfo_exists():
                    return
                by_id.clear()
                tv.delete(*tv.get_children())
                cands = mgr.endorse_candidates(self.mods)
                for m in cands:
                    by_id[str(m.nexus_id)] = m
                    tv.insert("", "end", iid=str(m.nexus_id), values=(m.name, m.installed_version or m.latest_version or "",
                                                                      mgr.endorse_status(m.nexus_id) or "?"))
                done_n = sum(1 for v in mgr.state["endorse"].values() if v.get("status") == "Endorsed")
                head.configure(text=(f"You have endorsed {done_n} Cyberpunk 2077 mod{'s' if done_n != 1 else ''} on Nexus.  "
                                     if done_n else "") +
                                    (f"{len(cands)} of the mods you have {'is' if len(cands) == 1 else 'are'} not endorsed yet."
                                     if cands else
                                     "Every mod you have that is on Nexus is endorsed. Nice."))
                go_btn.state(["!disabled"] if cands and not busy["v"] else ["disabled"])

            def got(_n):
                busy["v"] = False
                fill()

            def failed_read(e):
                busy["v"] = False
                if d.winfo_exists():
                    head.configure(text=f"Couldn't read your endorsements: {e}")

            def failed_go(e):
                busy["v"] = False
                if d.winfo_exists():
                    result.configure(text=f"That didn't work: {e}", fg=T["red"])
                    fill()
            busy["v"] = True
            go_btn.state(["disabled"])
            self.bg(lambda: mgr.endorse_refresh(nx), got, failed_read)

            def pick_all():
                tv.selection_set(tv.get_children())

            def go():
                mods = [by_id[i] for i in tv.selection() if i in by_id]
                if not mods or busy["v"]:
                    return
                if not messagebox.askyesno(APP_NAME, f"Endorse {len(mods)} mod{'s' if len(mods) != 1 else ''} on Nexus?\n\n"
                                                     "This is public, under your Nexus name.", parent=d):
                    return
                busy["v"] = True
                go_btn.state(["disabled"])
                result.configure(text="Endorsing…", fg=T["muted"])

                def finished(res):
                    busy["v"] = False
                    if not d.winfo_exists():
                        return
                    fill()
                    text = f"Endorsed {len(res['done'])}."
                    if res["failed"]:
                        text += f"  Nexus refused {len(res['failed'])}:\n• " + "\n• ".join(f"{n}: {w}" for n, w in res["failed"][:4])
                    if res["stopped"]:
                        text += f"\nStopped early: {res['stopped']}"
                    result.configure(text=text, fg=T["amber"] if (res["failed"] or res["stopped"]) else T["green"])
                    self.status.set(f"Endorsed {len(res['done'])} mod(s).")
                    self.show_details()
                self.bg(lambda: mgr.endorse_many(nx, mods), finished, failed_go)
            go_btn.configure(command=go)
            all_btn.configure(command=pick_all)
            d._endorse = {"fill": fill, "go": go, "tv": tv, "by_id": by_id, "result": result, "head": head, "all": pick_all}

        # ---- compare two instances -----------------------------------------------------------------------
        def compare_dialog(self, a=None, b=None):
            if not self.mgr:
                return
            self.mgr.ensure_instances()
            names = sorted(self.mgr.state["instances"], key=str.lower)
            if len(names) < 2:
                messagebox.showinfo(APP_NAME, "You need two instances to compare. Make another one with "
                                              "“New instance…” in the ◈ menu at the top.")
                return
            d = self.dialog("Compare instances", 760, 600, resizable=True)
            tk.Label(d, text="Compare two instances", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 8))
            top = tk.Frame(d, bg=T["bg"])
            top.pack(fill="x", padx=26)
            va = tk.StringVar(value=a or self.mgr.state["active"] or names[0])
            vb = tk.StringVar(value=b or next((n for n in names if n != va.get()), names[0]))
            ca = ttk.Combobox(top, textvariable=va, values=names, state="readonly", width=24)
            ca.pack(side="left")
            tk.Label(top, text="   against   ", fg=T["muted"], bg=T["bg"], font=font(10)).pack(side="left")
            cb = ttk.Combobox(top, textvariable=vb, values=names, state="readonly", width=24)
            cb.pack(side="left")
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            txt = tk.Text(d, wrap="word", relief="flat", bd=0, bg=T["panel"], fg=T["fg"], font=font(10), padx=14,
                          pady=10, highlightthickness=0)
            txt.pack(fill="both", expand=True, padx=26, pady=(12, 0))
            txt.tag_configure("a", foreground=T["green"], font=font(10, True))
            txt.tag_configure("b", foreground=T["amber"], font=font(10, True))
            txt.tag_configure("m", foreground=T["cyan"], font=font(10, True))
            self._cmp_text = txt

            def show(*_):
                txt.configure(state="normal")
                txt.delete("1.0", "end")
                try:
                    c = self.mgr.compare_instances(va.get(), vb.get())
                except ValueError as err:
                    txt.insert("end", str(err))
                    txt.configure(state="disabled")
                    return
                self._cmp = c

                def block(head, tag, items):
                    txt.insert("end", f"{head} ({len(items)})\n", tag)
                    txt.insert("end", ", ".join(items) if items else "nothing", "")
                    txt.insert("end", "\n\n")
                if va.get() == vb.get():
                    txt.insert("end", "Pick two different instances.")
                else:
                    block(f"Only in “{c['a']}”", "a", c["only_a"])
                    block(f"Only in “{c['b']}”", "b", c["only_b"])
                    if c["differ"]:
                        block("Partly on in one of them", "m", c["differ"])
                    txt.insert("end", f"On in both: {c['same_on']}   ·   off in both: {c['same_off']}")
                txt.configure(state="disabled")
            ca.bind("<<ComboboxSelected>>", show)
            cb.bind("<<ComboboxSelected>>", show)
            show()
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")

        # ---- disk space and moving the switched-off mods ----------------------------------------------------
        def disk_dialog(self):
            if not self.mgr:
                return
            d = self.dialog("Disk space", 800, 640, resizable=True)
            tk.Label(d, text="Disk space", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            head = tk.Label(d, text="Measuring…", fg=T["fg"], bg=T["bg"], font=font(10), anchor="w", justify="left",
                            wraplength=740)
            head.pack(fill="x", padx=26, pady=(0, 8))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            fr, tv = self._table(d, [("mod", "MOD (biggest first)", 380, "w", True), ("on", "SWITCHED ON", 120, "e", False),
                                     ("off", "SWITCHED OFF", 120, "e", False), ("total", "TOTAL", 110, "e", False)])
            fr.pack(fill="both", expand=True, padx=26)
            tv.tag_configure("off", foreground=T["muted"])
            state = {"du": None}
            btn_move = ttk.Button(row, text="Move switched-off mods to another drive…")
            btn_back = ttk.Button(row, text="Move them back")
            btn_prune = ttk.Button(row, text="Delete old backups…")
            btn_move.pack(side="left")
            btn_prune.pack(side="left", padx=8)
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right")

            def fill(du):
                if not d.winfo_exists():
                    return
                state["du"] = du
                tv.delete(*tv.get_children())
                for r in du["rows"]:
                    tv.insert("", "end", values=(r["name"], human_size(r["on"]) if r["on"] else "—",
                                                 human_size(r["off"]) if r["off"] else "—", human_size(r["total"])),
                              tags=("off",) if r["status"] == "off" else ())
                where = (f"The switched-off mods are kept on another drive: {du['stash_link']}"
                         if du["stash_link"] else f"The switched-off mods are kept in the game folder ({STASH_NAME}).")
                head.configure(text=(f"Your mods use {human_size(du['mods_total'])} in total.\n"
                                     f"Old copies kept for Undo (backups): {human_size(du['backups'])}.   "
                                     f"Free space on the game's drive: {human_size(du['free'])}.\n{where}"))
                if du["stash_link"]:
                    btn_move.pack_forget()
                    btn_back.pack(side="left", before=btn_prune)
                else:
                    btn_back.pack_forget()
                    btn_move.pack(side="left", before=btn_prune)

            def measure():
                head.configure(text="Measuring…")
                self.bg(self.mgr.disk_usage, fill, lambda e: head.winfo_exists() and head.configure(text=f"Couldn't measure: {e}"))

            def move():
                if not self._ready():
                    return
                dest = filedialog.askdirectory(parent=d, title="Where should the switched-off mods be kept? (pick a folder on "
                                                               "the other drive)")
                if not dest:
                    return
                if not messagebox.askyesno(APP_NAME, "Move the switched-off mods to:\n\n" + dest + "\n\nThey are copied, "
                                           "checked, and then a link is left in the game folder so everything works as "
                                           "before. Switching mods on from that drive is a little slower (the files are "
                                           "copied between drives). The game must be closed.\n\nContinue?", parent=d):
                    return

                def work(pr):
                    with self.mgr_lock:
                        return self.mgr.move_stash(dest, pr)
                d.destroy()
                self.start_job("Moving the switched-off mods…", work,
                               lambda loc: (self.refresh(), self.status.set(f"The switched-off mods now live in {loc}."),
                                            messagebox.showinfo(APP_NAME, f"Done. They are in:\n{loc}")))

            def move_back():
                if not self._ready():
                    return
                if not messagebox.askyesno(APP_NAME, "Move the switched-off mods back into the game folder?", parent=d):
                    return

                def work(pr):
                    with self.mgr_lock:
                        return self.mgr.unmove_stash(pr)
                d.destroy()
                self.start_job("Moving the switched-off mods back…", work,
                               lambda loc: (self.refresh(), self.status.set("The switched-off mods are back in the game folder.")))

            def prune():
                bs = self.mgr.backup_folders()
                old = [b for b in bs if b["ts"] < time.time() - 30 * 86400]
                if not old:
                    messagebox.showinfo(APP_NAME, f"There are {len(bs)} backup folder(s), none older than 30 days.", parent=d)
                    return
                if messagebox.askyesno(APP_NAME, f"Delete {len(old)} backup folder(s) older than 30 days "
                                       f"({human_size(sum(b['size'] for b in old))})?\n\nThose installs and updates can then "
                                       "no longer be undone.", parent=d):
                    n, freed = self.mgr.prune_backups(30)
                    self.status.set(f"Deleted {n} old backup folder(s), freed {human_size(freed)}.")
                    measure()
            btn_move.configure(command=move)
            btn_back.configure(command=move_back)
            btn_prune.configure(command=prune)
            measure()

        # ---- notes, tags and colours ------------------------------------------------------------------------------
        def notes_dialog(self):
            mods = self.selected()
            if len(mods) != 1:
                messagebox.showinfo(APP_NAME, "Select one mod to write a note about it.")
                return
            m = mods[0]
            d = self.dialog(f"Notes - {m.name}", 580, 540)
            tk.Label(d, text=m.name, fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w", wraplength=520,
                     justify="left").pack(fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="Only you see this. Search finds words in notes and tags.", fg=T["muted"], bg=T["bg"],
                     font=font(9), anchor="w").pack(fill="x", padx=26, pady=(0, 10))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            tk.Label(d, text="Note", fg=T["fg"], bg=T["bg"], font=font(10, True), anchor="w").pack(fill="x", padx=26)
            note = tk.Text(d, height=7, wrap="word", relief="flat", bd=0, bg=T["panel2"], fg=T["fg"], font=font(10),
                           padx=10, pady=8, highlightthickness=1, highlightbackground=T["line"],
                           highlightcolor=T["accent"], insertbackground=T["fg"])
            note.pack(fill="x", padx=26, pady=(4, 12))
            note.insert("1.0", m.note)
            tk.Label(d, text="Tags (separated by commas)", fg=T["fg"], bg=T["bg"], font=font(10, True), anchor="w").pack(
                fill="x", padx=26)
            tags = tk.StringVar(value=", ".join(m.tags))
            ttk.Entry(d, textvariable=tags).pack(fill="x", padx=26, pady=(4, 12))
            tk.Label(d, text="Colour", fg=T["fg"], bg=T["bg"], font=font(10, True), anchor="w").pack(fill="x", padx=26)
            chips = tk.Frame(d, bg=T["bg"])
            chips.pack(fill="x", padx=26, pady=(6, 0))
            color = tk.StringVar(value=m.color)
            cells = {}

            def paint():
                for c, w in cells.items():
                    w.configure(highlightbackground=T["accent"] if color.get() == c else T["line"])
            for c in ("",) + NOTE_COLORS:
                w = tk.Label(chips, text="none" if not c else "", width=5 if not c else 3, height=1,
                             bg=NOTE_DOT.get(c, T["panel2"]), fg=T["muted"], font=font(8), cursor="hand2",
                             highlightthickness=2, highlightbackground=T["line"])
                w.pack(side="left", padx=(0, 6))
                w.bind("<Button-1>", lambda _e, c=c: (color.set(c), paint()))
                cells[c] = w
            paint()

            def save():
                self.mgr.set_note(m, note=note.get("1.0", "end").strip(), tags=[t for t in tags.get().split(",")],
                                  color=color.get())
                d.destroy()
                self.refresh()
            ttk.Button(row, text="Save", style="Accent.TButton", command=save).pack(side="right")
            ttk.Button(row, text="Cancel", command=d.destroy).pack(side="right", padx=8)

        def set_color(self, color):
            mods = self.selected()
            if mods and self.mgr:
                self.mgr.set_note(mods, color=color)
                self.refresh()

        # ---- pin / skip an update -------------------------------------------------------------------------------
        def pin_selected(self, mode):
            mods = self.upd_selected() if self.page == "upd" else self.selected()
            mods = [m for m in mods if m.nexus_id]
            if not mods:
                messagebox.showinfo(APP_NAME, "Select a mod that is linked to Nexus.")
                return
            for m in mods:
                self.mgr.pin(m, mode)
            self.refresh()
            self.status.set((f"Staying on the current version of {len(mods)} mod(s)." if mode == "stay" else
                             f"Skipped this update for {len(mods)} mod(s) - it shows again when a newer version comes out.")
                            + "  (Pinned mods stay at the bottom of the Updates list.)")

        def unpin_selected(self):
            mods = self.upd_selected() if self.page == "upd" else self.selected()
            mods = [m for m in mods if m.nexus_id and m.pinned]
            if not mods:
                messagebox.showinfo(APP_NAME, "Select a pinned mod to unpin it.")
                return
            for m in mods:
                self.mgr.unpin(m)
            self.refresh()
            self.status.set(f"Unpinned {len(mods)} mod(s).")

        # ---- desktop shortcuts ----------------------------------------------------------------------------------------
        def shortcut_dialog(self, preselect=None):
            if not self.mgr:
                return
            self.mgr.ensure_instances()
            d = self.dialog("Desktop shortcut", 600, 520)
            tk.Label(d, text="Desktop shortcut", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text="Pick an instance. The shortcut switches to it and starts the game - without opening "
                             "this window. (If you rename the instance later, make the shortcut again.)",
                     fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left", wraplength=540).pack(
                fill="x", padx=26, pady=(0, 10))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=18)
            lb = tk.Listbox(d, height=10, bg=T["panel2"], fg=T["fg"], relief="flat", bd=0, highlightthickness=1,
                            highlightbackground=T["line"], highlightcolor=T["accent"], selectbackground=T["accent"],
                            selectforeground=T["accent_fg"], font=font(10), activestyle="none", exportselection=False)
            lb.pack(fill="both", expand=True, padx=26)
            names = sorted(self.mgr.state["instances"], key=str.lower)
            lb.insert("end", "(the game as it is now - no switching)")
            for n in names:
                lb.insert("end", n)
            lb.selection_set(names.index(preselect) + 1 if preselect in names else 1 if names else 0)

            def go():
                s = lb.curselection()
                if not s:
                    return
                name = "" if s[0] == 0 else names[s[0] - 1]
                self.make_instance_shortcut(name, d)
            ttk.Button(row, text="Create shortcut", style="Accent.TButton", command=go).pack(side="right")
            ttk.Button(row, text="Close", command=d.destroy).pack(side="right", padx=8)
            lb.bind("<Double-1>", lambda _e: go())

        def make_instance_shortcut(self, name, parent=None):
            try:
                path = make_shortcut(self.mgr.game, name)
            except OSError as e:
                messagebox.showerror(APP_NAME, f"Couldn't create the shortcut:\n\n{e}", parent=parent)
                return None
            messagebox.showinfo(APP_NAME, f"Created “{path.name}”.\n\nDouble-click it to " +
                                (f"switch to “{name}” and start the game" if name else "start the game") +
                                ", without opening ModScout.", parent=parent)
            self.status.set(f"Shortcut created: {path}")
            return path

        # ---- adding a mod by hand ------------------------------------------------------------------------------
        def add_mod(self):
            if not self._ready():
                return
            paths = filedialog.askopenfilenames(title="Pick the mod archive(s) to install",
                                                filetypes=[("Mod archives", "*.zip *.7z *.rar"), ("All files", "*.*")])
            if paths:
                self._add_next([Path(p) for p in paths], self.nexus_client(ask=False))

        def _add_next(self, paths, nx):
            if not paths:
                return
            p = paths.pop(0)
            sz = find_7zip(self.cfg.get("seven_zip", ""))

            def work(pr):
                ident = identify_archive(self.mgr, nx, p)
                try:
                    pv = preview_archive(self.mgr, p, sz, ident["name"])
                    err = ""
                except InstallError as e:
                    pv, err = None, str(e)
                return ident, pv, err
            self.start_job(f"Identifying {p.name}…", work, lambda r: self._add_confirm(p, r, paths, nx))

        def _add_confirm(self, p, r, paths, nx):
            ident, pv, err = r
            d = self.dialog("Add mod", 700, 640)
            tk.Label(d, text="Add a mod", fg=T["accent"], bg=T["bg"], font=font(14, True), anchor="w").pack(
                fill="x", padx=26, pady=(22, 2))
            tk.Label(d, text=p.name, fg=T["muted"], bg=T["bg"], font=font(9), anchor="w").pack(fill="x", padx=26)
            chosen = {"id": ident["mod_id"], "name": ident["name"], "version": ident["version"]}
            how = {"fingerprint": "recognised by its file fingerprint (exact)", "file name": "taken from its file name",
                   "name": "matched by its exact name"}.get(ident["how"], "")
            head = tk.Label(d, text="", fg=T["fg"], bg=T["bg"], font=font(12, True), anchor="w", justify="left",
                            wraplength=640)
            head.pack(fill="x", padx=26, pady=(14, 2))
            sub = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(10), anchor="w", justify="left",
                           wraplength=640)
            sub.pack(fill="x", padx=26)
            lb = None
            if ident["cands"] and not ident["mod_id"]:
                tk.Label(d, text="I'm not sure which Nexus mod this is. Pick one (or none):", fg=T["fg"], bg=T["bg"],
                         font=font(10), anchor="w").pack(fill="x", padx=26, pady=(12, 4))
                lb = tk.Listbox(d, height=6, bg=T["panel2"], fg=T["fg"], relief="flat", bd=0, highlightthickness=1,
                                highlightbackground=T["line"], highlightcolor=T["accent"], selectbackground=T["accent"],
                                selectforeground=T["accent_fg"], font=font(10), activestyle="none", exportselection=False)
                lb.pack(fill="x", padx=26)
                for c in ident["cands"]:
                    lb.insert("end", f"{c['name']}   ·   v{c['version'] or '?'}   ·   #{c['id']}"
                              + ("   (translation / add-on?)" if c["deriv"] else ""))
                lb.insert("end", "None of these - install it without linking")
                lb.selection_set("end")

            def current():
                if lb is not None:
                    s = lb.curselection()
                    if s and s[0] < len(ident["cands"]):
                        c = ident["cands"][s[0]]
                        return {"id": c["id"], "name": c["name"], "version": c["version"]}
                    return {"id": None, "name": ident["name"], "version": ""}
                return chosen

            def describe(*_):
                c = current()
                if c["id"]:
                    mine = next((m for m in self.mods if m.nexus_id == c["id"]), None)
                    head.configure(text=f"{c['name']}" + (f"  ·  v{c['version']}" if c["version"] else ""))
                    sub.configure(text=(how.capitalize() + ". " if how and lb is None else "")
                                  + (f"It's already in your library (v{mine.installed_version or '?'}) - installing "
                                     "replaces its files; the old ones are backed up." if mine else
                                     "It will be linked to its Nexus page so updates can be found."))
                else:
                    head.configure(text=ident["name"] or p.stem)
                    sub.configure(text="Not linked to Nexus. You can link it later (More → Link to a Nexus page).")
            describe()
            if lb is not None:
                lb.bind("<<ListboxSelect>>", describe)
            if err:
                tk.Label(d, text="✗ " + err, fg=T["red"], bg=T["bg"], font=font(10), anchor="w", justify="left",
                         wraplength=640).pack(fill="x", padx=26, pady=(14, 0))
            elif pv:
                tk.Label(d, text=f"Will install {pv['files']} file(s) into: " + ", ".join(
                    sorted({x.split('/')[0] + '/' + x.split('/')[1] if x.count('/') > 1 else x.split('/')[0]
                            for x in pv['dests']})[:5]) + (f"\n{pv['overwrites']} existing file(s) will be replaced "
                                                           "(a backup is kept)." if pv["overwrites"] else ""),
                         fg=T["muted"], bg=T["bg"], font=font(10), anchor="w", justify="left", wraplength=640).pack(
                    fill="x", padx=26, pady=(14, 0))
            row = tk.Frame(d, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=20)

            def go():
                c = current()
                d.destroy()
                f = {"file_id": ident["file_id"] if c["id"] == ident["mod_id"] else None, "version": c["version"],
                     "file_name": p.name}
                self.add_job("file", c["id"], c["name"] or pretty_name(p.stem), f, path=p, version=c["version"])
                self.show_page("dl")
                self._add_next(paths, nx)

            def skip():
                d.destroy()
                self._add_next(paths, nx)
            b = ttk.Button(row, text="Install", style="Accent.TButton", command=go)
            b.pack(side="right")
            if err:
                b.state(["disabled"])
            ttk.Button(row, text="Skip", command=skip).pack(side="right", padx=8)

        def check_updates(self, silent=False, force=False):
            if not self.mgr:
                return
            nx = self.nexus_client(ask=not silent)
            if not nx:
                return
            if not self.mgr.state["links"]:
                if not silent:
                    messagebox.showinfo(APP_NAME, "Nothing is linked to Nexus yet. Press “Match with Nexus” first.")
                return

            def done(errors):
                self.mgr.save()
                self.refresh()
                ups = sum(1 for m in self.mods if m.update == "update")
                left = nx.limits.get("daily-remaining")
                if errors:
                    self.status.set("Couldn't finish the check: " + errors[0])
                else:
                    self.status.set(f"{ups} update(s) available." +
                                    (f"  ({left} Nexus requests left today.)" if left is not None else ""))
                if errors and not silent:
                    messagebox.showwarning(APP_NAME, "\n".join(errors[:6]))
            self.start_job("Checking for updates…",
                           lambda p: refresh_nexus(self.mgr, nx, force=force, progress=p), done, silent=silent)

        # ---- background jobs ----------------------------------------------------------
        def start_job(self, text, fn, done, silent=False):
            if self.busy:
                self.status.set("Busy - wait for the current task to finish.")
                return
            self.busy = True
            self.status.set(text)
            self.pbar.configure(value=0, maximum=1)
            self.pbar.pack(side="right")
            q = queue.Queue()

            def work():
                try:
                    res = fn(lambda i, n, t="": q.put(("p", i, n, t)))
                except Exception as e:  # shown to the user, never silently lost
                    q.put(("e", e))
                else:
                    q.put(("d", res))
            threading.Thread(target=work, daemon=True).start()
            self.after(120, lambda: self._poll(q, done, silent))

        def _poll(self, q, done, silent):
            finished = None
            try:
                while True:
                    msg = q.get_nowait()
                    if msg[0] == "p":
                        self.pbar.configure(maximum=max(msg[2], 1), value=msg[1])
                        if msg[3]:
                            self.status.set(msg[3])
                    else:
                        finished = msg
                        break
            except queue.Empty:
                pass
            if finished is None:
                self.after(120, lambda: self._poll(q, done, silent))
                return
            self.busy = False
            self.pbar.pack_forget()
            if finished[0] == "e":
                self.status.set("That didn't work.")
                if not silent:
                    messagebox.showerror(APP_NAME, str(finished[1]))
                return
            done(finished[1])

        def on_close(self):
            busy = [j for j in self.jobs if j["status"] in ("downloading", "installing")]
            if busy and not messagebox.askyesno(
                    APP_NAME, "A download or install is still running. Closing now cancels it (the game folder is "
                    "left as it was). Close anyway?"):
                return
            for j in self.jobs:
                j["cancel"].set()
            if self.ipc:
                self.ipc.close()
            self.destroy()

        # ---- dialogs ----------------------------------------------------------------------
        def dialog(self, title, w, h, resizable=False):
            d = tk.Toplevel(self)
            d.title(title)
            d.configure(bg=T["bg"])
            d.transient(self)
            self.update_idletasks()
            w = min(w, max(self.winfo_screenwidth() - 40, 400))
            h = min(h, max(self.winfo_screenheight() - 120, 400))
            d.resizable(resizable, resizable)
            x = max(self.winfo_rootx() + max((self.winfo_width() - w) // 2, 0), 0)
            y = max(min(self.winfo_rooty() + 70, self.winfo_screenheight() - h - 70), 0)
            d.geometry(f"{w}x{h}+{x}+{y}")
            dark_titlebar(d)
            try:
                d.wait_visibility()
                d.grab_set()
            except tk.TclError:
                pass
            return d

        def open_settings(self):
            win = self.dialog("Settings", 680, 800, resizable=True)
            row = tk.Frame(win, bg=T["bg"])
            row.pack(side="bottom", fill="x", padx=26, pady=16)
            cv = tk.Canvas(win, bg=T["bg"], highlightthickness=0)
            vsb = ttk.Scrollbar(win, orient="vertical", command=cv.yview)
            cv.configure(yscrollcommand=vsb.set)
            vsb.pack(side="right", fill="y")
            cv.pack(side="left", fill="both", expand=True)
            d = tk.Frame(cv, bg=T["bg"])
            wid = cv.create_window((0, 0), window=d, anchor="nw")
            d.bind("<Configure>", lambda _e: cv.configure(scrollregion=cv.bbox("all")))
            cv.bind("<Configure>", lambda e: cv.itemconfigure(wid, width=e.width))
            win.bind("<MouseWheel>", lambda e: cv.yview_scroll(int(-e.delta / 120), "units"))
            win.bind("<Button-4>", lambda _e: cv.yview_scroll(-3, "units"))
            win.bind("<Button-5>", lambda _e: cv.yview_scroll(3, "units"))
            pad = dict(padx=26)
            tk.Label(d, text="Nexus Mods", fg=T["accent"], bg=T["bg"], font=font(13, True), anchor="w").pack(
                fill="x", pady=(22, 2), **pad)
            tk.Label(d, text="Your personal API key from nexusmods.com. It is stored only on this PC "
                             "and only sent to api.nexusmods.com.", fg=T["muted"], bg=T["bg"], font=font(9),
                     anchor="w", wraplength=600, justify="left").pack(fill="x", **pad)
            krow = tk.Frame(d, bg=T["bg"])
            krow.pack(fill="x", pady=(10, 0), **pad)
            key = tk.StringVar(value=self.cfg.get("api_key", ""))
            ke = ttk.Entry(krow, textvariable=key, show="•")
            ke.pack(side="left", fill="x", expand=True)
            showing = {"v": False}

            def toggle_show():
                showing["v"] = not showing["v"]
                ke.configure(show="" if showing["v"] else "•")
                show_btn.configure(text="Hide" if showing["v"] else "Show")
            show_btn = ttk.Button(krow, text="Show", command=toggle_show)
            show_btn.pack(side="left", padx=(8, 0))
            vstatus = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(9), anchor="w",
                               wraplength=600, justify="left")

            def validate():
                k = key.get().strip()
                if not k:
                    vstatus.configure(text="Paste your key first.", fg=T["amber"])
                    return
                nx = Nexus(k, timeout=15)
                self.configure(cursor="watch")
                d.update_idletasks()
                lines, ok = [], True
                try:
                    me = nx.validate() or {}
                    left = nx.limits.get("daily-remaining")
                    lines.append("✓ Connected as " + str(me.get("name", "?")) +
                                 ("  ·  Premium" if me.get("is_premium") else "") +
                                 (f"  ·  {left} requests left today" if left is not None else ""))
                    try:
                        t, en = nx.tracked(), nx.endorsed()
                        lines.append(f"Your Cyberpunk 2077 mods on Nexus: {len(en)} endorsed, {len(t)} tracked.")
                    except NexusError as e:
                        ok = False
                        lines.append("✗ Couldn't read your endorsed/tracked mods: " + str(e))
                    try:
                        nx.probe_search()
                        lines.append("✓ Searching Nexus by name works.")
                    except NexusError as e:
                        ok = False
                        lines.append("✗ " + str(e))
                except NexusError as e:
                    ok = False
                    lines.append("✗ " + str(e))
                finally:
                    self.configure(cursor="")
                vstatus.configure(text="\n".join(lines), fg=T["green"] if ok else T["amber"])
            ttk.Button(krow, text="Check key", command=validate).pack(side="left", padx=(8, 0))
            ttk.Button(krow, text="Get a key…", command=lambda: webbrowser.open(API_KEYS_URL)).pack(
                side="left", padx=(8, 0))
            vstatus.pack(fill="x", pady=(6, 0), **pad)

            tk.Label(d, text="Where you keep your downloaded mod archives", fg=T["fg"], bg=T["bg"],
                     font=font(10, True), anchor="w").pack(fill="x", pady=(20, 2), **pad)
            tk.Label(d, text="The zips you downloaded from Nexus. The tool reads them to find the exact mod "
                             "and version of every installed file, and to group files that belong together. "
                             "If you add nothing, your Downloads folder is used.",
                     fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", wraplength=600,
                     justify="left").pack(fill="x", **pad)
            lrow = tk.Frame(d, bg=T["bg"])
            lrow.pack(fill="x", pady=(8, 0), **pad)
            lb = tk.Listbox(lrow, height=4, bg=T["panel2"], fg=T["fg"], relief="flat", bd=0,
                            highlightthickness=1, highlightbackground=T["line"], highlightcolor=T["accent"],
                            selectbackground=T["sel"], selectforeground=T["fg"], font=font(9),
                            activestyle="none")
            lb.pack(side="left", fill="x", expand=True)
            for p in self.cfg.get("download_dirs", []):
                lb.insert("end", p)
            bcol = tk.Frame(lrow, bg=T["bg"])
            bcol.pack(side="left", padx=(8, 0))

            def add_dir():
                p = filedialog.askdirectory(title="Folder with your downloaded mod archives", parent=d)
                if p and p not in lb.get(0, "end"):
                    lb.insert("end", p)

            def del_dir():
                for i in reversed(lb.curselection()):
                    lb.delete(i)
            ttk.Button(bcol, text="Add folder…", command=add_dir).pack(fill="x")
            ttk.Button(bcol, text="Remove", command=del_dir).pack(fill="x", pady=(6, 0))
            sz = find_7zip(self.cfg.get("seven_zip", ""))
            tk.Label(d, text=("7-Zip found: .zip, .7z and .rar downloads can all be read." if sz else
                              "7-Zip not found: only .zip downloads can be read. Install 7-Zip to include .7z and .rar."),
                     fg=T["green"] if sz else T["amber"], bg=T["bg"], font=font(9), anchor="w",
                     wraplength=600, justify="left").pack(fill="x", pady=(8, 0), **pad)
            auto = tk.BooleanVar(value=self.cfg.get("auto_check", True))
            ttk.Checkbutton(d, text="Check for updates when the app starts", variable=auto).pack(
                anchor="w", pady=(18, 0), **pad)
            content = tk.BooleanVar(value=self.cfg.get("content_match", True))
            ttk.Checkbutton(d, text="Match by file lists too (reads up to 45 Nexus pages per run)",
                            variable=content).pack(anchor="w", pady=(8, 0), **pad)
            tk.Label(d, text="For mods the name can't settle, the “Preview file contents” list of the Nexus pages "
                             "found by its keywords is compared with your installed files.", fg=T["muted"],
                     bg=T["bg"], font=font(9), anchor="w", justify="left", wraplength=600).pack(fill="x", **pad)
            tk.Label(d, text="Save mods I download from Nexus to", fg=T["fg"], bg=T["bg"], font=font(10, True),
                     anchor="w").pack(fill="x", pady=(18, 2), **pad)
            srow = tk.Frame(d, bg=T["bg"])
            srow.pack(fill="x", **pad)
            save_dir = tk.StringVar(value=self.cfg.get("save_dir", ""))
            ttk.Entry(srow, textvariable=save_dir).pack(side="left", fill="x", expand=True)
            ttk.Button(srow, text="Browse…", command=lambda: save_dir.set(
                filedialog.askdirectory(title="Where should downloads be saved?", parent=d) or save_dir.get())
                       ).pack(side="left", padx=(8, 0))
            tk.Label(d, text="Empty = your first archive folder above, or your Downloads folder.", fg=T["muted"],
                     bg=T["bg"], font=font(9), anchor="w").pack(fill="x", **pad)
            tk.Label(d, text="Starting the game (the Play button)", fg=T["fg"], bg=T["bg"], font=font(10, True),
                     anchor="w").pack(fill="x", pady=(18, 2), **pad)
            lm = tk.StringVar(value=dict(LAUNCH_METHODS).get(self.cfg.get("launch_method", "auto"), LAUNCH_METHODS[0][1]))
            ttk.Combobox(d, textvariable=lm, state="readonly", values=[t for _k, t in LAUNCH_METHODS]).pack(
                fill="x", **pad)
            largs = tk.StringVar(value=self.cfg.get("launch_args", ""))
            ttk.Entry(d, textvariable=largs).pack(fill="x", pady=(6, 0), **pad)
            tk.Label(d, text="Extra launch options, if you use any (for example -modded for REDmod mods, or "
                             "-skipStartScreen). Leave it empty if you don't know.", fg=T["muted"], bg=T["bg"],
                     font=font(9), anchor="w", justify="left", wraplength=600).pack(fill="x", **pad)
            if os.name == "nt":
                tk.Label(d, text="Nexus “Mod Manager Download” buttons", fg=T["fg"], bg=T["bg"], font=font(10, True),
                         anchor="w").pack(fill="x", pady=(18, 2), **pad)
                nstat = tk.Label(d, text="", fg=T["muted"], bg=T["bg"], font=font(9), anchor="w", justify="left",
                                 wraplength=600)

                def show_nxm():
                    cur_cmd = nxm_current()
                    mine = bool(cur_cmd) and Path(sys.argv[0]).name.lower() in cur_cmd.lower()
                    nstat.configure(text=("This app handles Nexus download buttons." if mine else
                                          ("Currently handled by: " + cur_cmd[:80]) if cur_cmd else
                                          "No program handles Nexus download buttons yet."))

                def use_me():
                    prev = nxm_current()
                    if prev and Path(sys.argv[0]).name.lower() not in prev.lower():
                        save_config(nxm_previous=prev)
                    err = nxm_register()
                    show_nxm()
                    if err:
                        messagebox.showwarning(APP_NAME, err, parent=d)

                def restore():
                    err = nxm_restore(load_config().get("nxm_previous", ""))
                    show_nxm()
                    if err:
                        messagebox.showwarning(APP_NAME, err, parent=d)
                nrow = tk.Frame(d, bg=T["bg"])
                nrow.pack(fill="x", **pad)
                ttk.Button(nrow, text="Use this app for Nexus downloads", command=use_me).pack(side="left")
                ttk.Button(nrow, text="Give it back", command=restore).pack(side="left", padx=8)
                nstat.pack(fill="x", pady=(6, 0), **pad)
                tk.Label(d, text="With a free account, Nexus's “Slow download” button then hands the file to this app. "
                                 "This replaces Vortex / Mod Organizer as the handler (for your Windows user only) "
                                 "until you press “Give it back”.", fg=T["muted"], bg=T["bg"], font=font(9), anchor="w",
                         justify="left", wraplength=600).pack(fill="x", **pad)
                show_nxm()

            def save():
                method = next((k for k, t in LAUNCH_METHODS if t == lm.get()), "auto")
                self.cfg.update(api_key=key.get().strip(), download_dirs=list(lb.get(0, "end")),
                                auto_check=bool(auto.get()), save_dir=save_dir.get().strip(),
                                launch_method=method, launch_args=largs.get().strip(),
                                content_match=bool(content.get()))
                save_config(api_key=self.cfg["api_key"], download_dirs=self.cfg["download_dirs"],
                            auto_check=self.cfg["auto_check"], save_dir=self.cfg["save_dir"],
                            launch_method=method, launch_args=self.cfg["launch_args"],
                            content_match=self.cfg["content_match"])
                win.destroy()
                self.status.set("Settings saved.")
            ttk.Button(row, text="Save", style="Accent.TButton", command=save).pack(side="right")
            ttk.Button(row, text="Cancel", command=win.destroy).pack(side="right", padx=8)

    return App()


def run_gui(game_arg=None, nxm_arg=None):
    make_app(game_arg, nxm_arg).mainloop()


# --------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description=APP_NAME)
    ap.add_argument("nxm", nargs="?", help="an nxm:// link (Windows starts the app with it from the Nexus button)")
    ap.add_argument("--game", help="path to the Cyberpunk 2077 folder")
    ap.add_argument("--list", action="store_true", help="print all detected mods")
    ap.add_argument("--enable", nargs="+", metavar="NAME", help="enable mods whose name contains NAME ('*' = all)")
    ap.add_argument("--disable", nargs="+", metavar="NAME", help="disable mods whose name contains NAME ('*' = all)")
    ap.add_argument("--no-fuzzy", action="store_true", help="only group files with identical names")
    ap.add_argument("--match", action="store_true", help="match installed mods with Nexus (downloads + names)")
    ap.add_argument("--check-updates", action="store_true", help="refresh Nexus info for linked mods")
    ap.add_argument("--force", action="store_true", help="with --check-updates: re-read every linked mod")
    ap.add_argument("--suggest", action="store_true", help="print suggested merges")
    ap.add_argument("--downloads", nargs="+", metavar="DIR", help="folder(s) with your downloaded mod archives")
    ap.add_argument("--api-key", help="Nexus API key (or set NEXUS_API_KEY, or use the Settings window)")
    ap.add_argument("--instances", action="store_true", help="list your instances")
    ap.add_argument("--switch", metavar="NAME", help="switch to an instance")
    ap.add_argument("--play", nargs="?", const="", metavar="INSTANCE",
                    help="switch to the instance (if given) and start the game, without opening the window")
    ap.add_argument("--make-shortcut", metavar="INSTANCE", help="put a “Play - INSTANCE” shortcut on the desktop")
    args = ap.parse_args()
    if args.play is not None:
        return play_cli(args)
    if any((args.list, args.enable, args.disable, args.match, args.check_updates, args.suggest,
            args.instances, args.switch, args.make_shortcut)):
        return cli(args)
    if getattr(sys, "frozen", False):
        scrub_frozen_env()                   # see PYI_VARS
    nxm = args.nxm if args.nxm and args.nxm.lower().startswith("nxm://") else None
    if nxm and hand_over_nxm(nxm):           # the window that is already open takes it: no second window
        return 0
    if not nxm and not args.game and show_running():
        return 0                             # started the icon again: just bring the open window forward
    try:
        run_gui(args.game, nxm)
    except ImportError:
        print("tkinter is not available in this Python install. Reinstall Python from "
              "python.org (keep 'tcl/tk' ticked) or use the command-line options (--help).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
