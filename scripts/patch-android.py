#!/usr/bin/env python3
"""Conecta AdMob con el proyecto de Android que genera Capacitor.

Agrega el ID de tu app de AdMob en AndroidManifest.xml y strings.xml.
Por defecto usa el ID real de la app en AdMob (Tereré Tycoon). Para usar otro:
    ADMOB_APP_ID="ca-app-pub-XXXXXXXXXXXXXXXX~YYYYYYYYYY" python3 scripts/patch-android.py
"""
import os
import pathlib
import re

# ID de prueba de Google (por si hace falta volver a anuncios de prueba): ca-app-pub-3940256099942544~3347511713
APP_ID = "ca-app-pub-4029429267067973~9509309371"
app_id = os.environ.get("ADMOB_APP_ID", "").strip() or APP_ID

root = pathlib.Path("android/app/src/main")

# 1) AndroidManifest.xml: referencia al ID de la app de AdMob
manifest = root / "AndroidManifest.xml"
text = manifest.read_text(encoding="utf-8")
meta = (
    '<meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" '
    'android:value="@string/admob_app_id" />'
)
if "com.google.android.gms.ads.APPLICATION_ID" not in text:
    text, n = re.subn(r"(<application\b[^>]*>)", r"\1\n        " + meta, text, count=1)
    if n != 1:
        raise SystemExit("No encontré la etiqueta <application> en AndroidManifest.xml")
    manifest.write_text(text, encoding="utf-8")

# 2) strings.xml: el ID de la app de AdMob
strings = root / "res" / "values" / "strings.xml"
s = strings.read_text(encoding="utf-8")
if 'name="admob_app_id"' in s:
    s = re.sub(r'(<string name="admob_app_id">)[^<]*(</string>)', r"\g<1>" + app_id + r"\g<2>", s)
else:
    s = s.replace("</resources>", '    <string name="admob_app_id">' + app_id + "</string>\n</resources>")
strings.write_text(s, encoding="utf-8")

print("AdMob conectado con el ID de app:", app_id)
