# pelican-blog

Clone and install `brutalist` theme (don't clone theme into this dir):
https://github.com/mc-buckets/brutalist
- `git clone https://github.com/mc-buckets/brutalist.git`
- `pelican-themes -i ../brutalist`

Create environment:
- `python3 -m venv env`
- `source env/bin/activate`

Restore packages:
- `pip install -r requirements.txt`

To build:
- `pelican content` from project root

To start a dev server:
- `pelican --listen`

View preview site at http://localhost:8000