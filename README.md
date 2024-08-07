# Trakteer Hotkeys

---
Trakteer Hotkeys aplikasi untuk berinteraksi dengan *Keyboard Shortcut / Hotkeys* saat mendapat donasi dari trakteer.

** Ini adalah aplikasi *Unofficial* **

---
## Prerequisites
- Python 3.12.4 (latest version)
- Websocket

  Setelah menginstall Python, buka CMD atau Powershell lalu ketik command berikut :

  `pip install websockets`
- Browser

## Installation
- Buka https://trakteer.id/manage/webhook/websocket untuk mendapatkan Channel ID
- Clone Repo

  ` Git Clone https://github.com/anandac16/trakteer-hotkeys.git`

  Setelah clone repo / download files, buka config.js. Lalu isi channelID dengan Channel ID dari trakteer

  ` const channelID = ''; `
---
### Setting & Command
Kalian dapat mengubah setting untuk *min qty* dan *allowed command* di file **Settings.json**
```
{
   "settings": [
      {
         "min_qty": 1,
         "allowedCommand": ["!AltTab"]
      },
      ...
    ]
}
```
Ini adalah list Command yang tersedia saat ini. Jika ingin request untuk menambah command atau lainnya bisa [diskusi di sini](https://github.com/anandac16/trakteer-hotkeys/discussions/1) atau DM [twitter/X](https://x.com/achandesu_)
| Command | Description |
| ----------- | ----------- |
| !AltTab | Fungsi Alt + Tab |
| !throwGun | Fungsi tombol "G" (Untuk melempar senjata di Valorant / CS2) |
| !throwGun5Sec | Fungsi tombol "G" (Untuk melempar senjata di Valorant / CS2) selama 5 detik |
| !knifeOnly | Fungsi tombol "3" (Untuk memegang knife di Valorant / CS2) |
| !knifeOnly5Sec | Fungsi tombol "3" (Untuk memegang knife di Valorant / CS2) selama 5 detik |
| !AltF4 | Fungsi Alt + F4 |

Kalian bisa membuat fungsi sendiri di file main.py


## Start the Program!

Untuk menjalankan program, buka / double click file **start.bat**. Pastikan kalian sudah mengisi channelID di file config.js.

Untuk menjalankan command, ketik command di pesan donasi. Command akan berjalan jika Qty >= min_qty yang ada di Settings.json dan ada di list allowedCommand.


---
## Referensi
[rmdwirizki/trws-js.example.html](https://gist.github.com/rmdwirizki/1d4cd9c8daadf74d2cdf72af2b97d8e5#file-trws-js-example-html)

[How To Build WebSocket Server And Client in Python](https://piehost.com/websocket/python-websocket)

[How to make Keyboard Event](https://stackoverflow.com/a/13615802)

---

## License

MIT


---

## Me
Ini hanyalah project iseng-iseng dari seorang *Script Kiddies* yang mostly ngoding pake PHP. Jadi, maaf kalau ngeliat kodingannya kurang rapih karena ini literally my first time using Python :3
But any support is appreciated!

[Trakteer](https://trakteer.id/achanch)

[twitter/X](https://x.com/achandesu_)

