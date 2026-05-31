import re

with open('alumni-postdoc.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the grid content
grid_start_idx = content.find('<div class="alumni-grid">') + len('<div class="alumni-grid">')
grid_end_idx = content.find('</div>\n          </div>\n        </section>')

grid_content = content[grid_start_idx:grid_end_idx]

# Split articles by looking for <article
articles_raw = re.split(r'(<article class="content-card alumni-card">)', grid_content)
# articles_raw[0] is whitespace before first article
# articles_raw[1] is the tag itself
# articles_raw[2] is the inner content

articles = []
for i in range(1, len(articles_raw), 2):
    article_html = articles_raw[i] + articles_raw[i+1]
    articles.append(article_html)

# Map names to articles
article_dict = {}
for a in articles:
    if "Shama Parveen" in a:
        article_dict['shama'] = a
    elif "Srikrishna" in a:
        article_dict['srikrishna'] = a
    elif "Pankaj" in a:
        article_dict['pankaj'] = a
    elif "Neha Abbasi" in a:
        article_dict['neha'] = a
    elif "Ankita Sharma" in a:
        article_dict['ankita'] = a
    elif "Lacksaya Nagarajan" in a:
        article_dict['lakshay'] = a
    elif "Sureshwar Thakur" in a:
        article_dict['sureshwar'] = a
    else:
        article_dict['unknown'] = a

# Requested order: Shama, Srikrishna, Pankaj, Neha, Ankita, Lakshay, Kumaresan(Sureshwar)
ordered_keys = ['shama', 'srikrishna', 'pankaj', 'neha', 'ankita', 'lakshay', 'sureshwar']

ordered_articles_html = "\n".join([article_dict[k] for k in ordered_keys])

new_content = content[:grid_start_idx] + "\n" + ordered_articles_html + content[grid_end_idx:]

with open('alumni-postdoc.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Reordered successfully!")
