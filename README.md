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

*Question:* how do I want to handle unpublished drafts away from the master branch? If I have one "drafts" branch I'll need to do tricks to pull individual files from the drafts branch into master to publish. I could do one branch per article? Akin to a feature branch. Then as a draft is completed just pull the whole thing (one file) into master and rebuild. Then delete the article draft branch.
