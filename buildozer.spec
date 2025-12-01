[app]
title = KivyMD Navigation Drawer Example
package.name = kivymdexample
package.domain = org.test

# KĽÚČOVÁ ZMENA – KivyMD 2.0.1.dev0 nie je na PyPI → používame git
requirements = python3, \
    https://github.com/kivy/kivy/archive/master.zip, \
    git+https://github.com/kivymd/KivyMD.git@master

# Ak chceš presne ten decembrový commit (2025-12-01), môžeš použiť:
# git+https://github.com/kivymd/KivyMD.git@d668d8b

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,ttf,otf,svg
source.entrypoint = main.py

version = 0.1

# Android nastavenia
android.api = 33
android.minapi = 21
android.archs = arm64-v8a                 # ← rýchly build + menší APK (99,9 % telefónov)
# ak niekedy budeš chcieť podporovať aj veľmi staré 32-bit zariadenia, vráť späť:
# android.archs = arm64-v8a, armeabi-v7a

android.permissions = INTERNET,VIBRATE
android.bootstrap = sdl2

orientation = portrait
fullscreen = 1

log_level = 2
p4a.branch = master

# Vypneme problematické clipboard backendy (už nie je potrebné, lebo Kivy master ich ignoruje, ale pre istotu)
prescriptor = |
    [kivy]
    log_level = info

    [core]
    clipboard = sdl2,dummy
    cutbuffer = dummy

    [input]
    mtdev = disable
