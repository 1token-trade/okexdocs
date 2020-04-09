
import requests
import html
from pathlib import Path
# url = 'https://www.okex.com/docs/zh/'
# r = requests.get(url, timeout=15)
# f.write_text(html.unescape(r.text))
f = Path('cn.html')
orig = f.read_text()
cn_decode = Path('cn-decode.html')
cn_decode.write_text(html.unescape(orig))


