# -*- mode: python -*-
a = Analysis(['yifyyy.py'],
             pathex=['/home/melvin/development/RandomMovieDownloader/RandomMovieDownloaderLinux'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='yifyyy',
          debug=False,
          strip=None,
          upx=True,
          console=False )
