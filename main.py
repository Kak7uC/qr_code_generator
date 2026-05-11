@'
import qrcode
img = qrcode.make('Other data here')
img.save("other_file.png")
'@ | Set-Content -Encoding UTF8 main.py