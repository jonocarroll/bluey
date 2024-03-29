import fandom
import os

fandom.set_wiki("bluey")
pages = fandom.search("/Script", results = 1000)
len(pages)
scripts = [x for x in pages if x[0].endswith('Script')]
len(scripts)
script_titles = [x[0] for x in scripts]

dir = "episodes"
for ep in range(len(script_titles)):
  t = script_titles[ep]
  try:
    text = fandom.page(t).content
    with open(os.path.join(dir, t.replace("/Script", '').replace("/Main", '')), 'w') as f:
        f.write(text['content'])
  except:
    pass

## episode listings
episode_list = fandom.page("Episode_List").content
# episode_list = episode_list['sections'][0]['content']
episode_list = episode_list['content']
with open('listing', 'w') as eplist:
    eplist.write(episode_list)

