[app]

# Náza aplikácie v lište
title = KivyMD Navigation Drawer Example

# Package name (musí byť unikátny na Google Play)
package.name = kivymdexample
package.domain = org.test

# Hlavný súbor
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,ttf,otf
source.entrypoint = main.py

# === TU JE TO DÔLEŽITÉ – fungujúca kombinácia december 2025 ===
requirements = python3, \
    https://github.com/kivy/kivy/archive/master.zip, \
    kivymd==2.0.1.dev0

# Ak chceš úplne najnovšie KivyMD (ešte lepšie, odporúčam):
# requirements = python3, \
#     https://github.com/kivy/kivy/archive/master.zip, \
#     https://github.com/kivymd/KivyMD/archive/master.zip

version = 0.1
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# Ak chceš len na moderné telefóny → rýchlejší build (voliteľné):
# android.archs = arm64-v8a

# Povolenia (pridaj podľa potreby)
android.permissions = INTERNET,VIBRATE

# Toto je kľúčové – sdl2 už dávno nemá ten xsel bug
android.bootstrap = sdl2

# Rýchlejší a čistejší výstup
log_level = 2

# Voliteľné, ale veľmi pomáha pri opakovaných builoch
p4a.branch = master

[buildozer]
warn_on_root = 1
