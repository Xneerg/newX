[app]
​(str) Názov tvojej aplikácie
​title = KivyMD Navigation Drawer Example
​(str) ID balíčka (package name) musí byť v tvare doména.projekt
​package.name = kivymdexample
package.domain = org.test
​(list) Požiadavky (dependencies)
​requirements = python3, kivy==2.3.0, kivymd==2.0.1.dev0
​(str) Adresár so zdrojovým kódom (aktuálny adresár)
​source.dir = .
​(str) Hlavný súbor aplikácie
​source.entrypoint = main.py
​(int) Android API, na ktorý sa kompiluje (musí byť >= 33 pre Google Play)
​android.api = 33
​(int) Minimálne API pre kompatibilitu (pre Kivy sa odporúča 21 alebo vyššie)
​android.minapi = 21
​(list) Architektúry (arm64-v8a pre moderné telefóny, armeabi-v7a pre staršie)
​android.archs = arm64-v8a, armeabi-v7a
​(str) Režim balíčka (debug pre testovanie, release pre produkciu)
​android.release = 0
