
from markdownify import markdownify as mdf
import requests
import html
from pathlib import Path
# url = 'https://www.okex.com/docs/zh/'
# r = requests.get(url, timeout=15)
# f.write_text(html.unescape(r.text))
f = Path('cn.html')
orig = f.read_text()
cn_decode = Path('cn-decode.html')
cn_md = Path('cn.md')
# new = html.unescape(orig)
# BLACK_LIST = ['<br>', '']
# cleaned_decode = '\n'.join(line for line in new.splitlines() if line.strip() not in BLACK_LIST)
r = mdf(orig)
print(r)
cn_md.write_text(r)

# cn_decode.write_text(cleaned_decode)


