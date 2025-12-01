[app]
title = KivyMD Navigation Drawer Example
package.name = kivymdexample
package.domain = org.test

# Toto je kľúč – master Kivy má fix pre xsel/chlipboard v headless
requirements = python3, \
    https://github.com/kivy/kivy/archive/master.zip, \
    kivymd==2.0.1.dev0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,ttf,otf
source.entrypoint = main.py

version = 0.1
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET,VIBRATE
android.bootstrap = sdl2

log_level = 2
p4a.branch = master

# === NOVÉ: Vypni problematické clipboard providers (len pre Linux/headless) ===
# Toto zabije xclip/xsel pokusy – sdl2 sa použije automaticky na Androide
[buildozer]
# Pridaj xclip/xsel do requirements, ale len ak treba (pre testy) – lepšie vypnúť
# requirements.source_kivy = extra

# Kivy config sekcia – deaktivuj xclip/xsel/dbusklipper
# Toto ide do ~/.kivy/config.ini, ale buildozer to zvládne cez prescriptor
prescriptor = |
    [core]
    clipboard = sdl2,dummy
    cutbuffer = dummy

    [input]
    # Vypni mtdev (nie je v GitHub runneri)
    mtdev = disable

# Voliteľne: Ak chceš úplne vypnúť clipboard v appke, pridaj do main.py
# os.environ['KIVY_CLIPBOARD'] = 'dummy'
