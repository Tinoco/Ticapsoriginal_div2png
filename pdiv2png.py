# IMPORT BEAUTIFULSOUP TO READ WEB CONTENT
from bs4 import BeautifulSoup

# IMPORT REQUESTS TO RECEIVE RESPONSES
import requests

# IMPORT URLIB TO PARSE URL DATA
from urllib.parse import quote

# IMPORT html2image TO CONVERT HTML TO IMAGE
from html2image import Html2Image


# FUNCRION TO MAKE REQUEST
def get_code(url) -> requests.Response:
    return requests.get(url)


# INPUT YOUR URL TO EXTRACT DIVS
url = 'https://ticapsoriginal.com'

urlg = (get_code(url))
soup = BeautifulSoup(urlg.text, 'html.parser')

div2png = Html2Image()

counter = 0
for divlink in soup.find_all('div'):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<link rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
<link rel="stylesheet"
href="https://hidedomain.info/css/ticapsoriginal.css">
</head>
<body style="background:#a5ce89" >
<script type="module"
src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
<script nomodule
src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js">
</script>
<section class="section">
<div class="box" style="background:#a5ce89" >
<div class="tile has-text-centered">
{divlink}
</div>
</div>
</section>
<script src="https://hidedomain.info/js/ticapsoriginal.min.js"></script>
</body>
</html>"""
    counter += 1
    div2png.screenshot(
                       html_str=html,
                       save_as=("div"+str(counter)+'.png')
                      )
