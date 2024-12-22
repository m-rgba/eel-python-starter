# -*- mode: python ; coding: utf-8 -*-
a = Analysis(
    ["src/app.py"],
    pathex=[],
    binaries=[],
    datas=[("src/web", "web")],
    hiddenimports=[
        "eel",
        "routes",
        "utils",
        "functions",
        "window_manager"
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Eel",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon="icon.png",
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="Eel",
)

app = BUNDLE(
    coll,
    name="Eel.app",
    icon="icon.png",
)
