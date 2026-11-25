from pathlib import Path

TIP = "Sedang memuat keajaiban kecil... Tarik napas, tersenyum, dan ingat: loading pun punya tujuan. Jika bar bergerak pelan, mungkin ia sedang memilih musik kemenangan terbaik untukmu!"
Path("/output/entry.txt").write_text(TIP, encoding="utf-8")
