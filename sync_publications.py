import os
import json
import re

# Publication Data from Scholar Crawl
data = [
  {"title": "Dual Layered Janus Nonwovens with Asymmetric Wettability for Efficient Directional Moisture Transport", "authors": "Kumaresan Subramani, Sollazhagan Nataraj, Porika Anirudh Naik, Rengasamy Raju Seenivasan, Harun Venkatesan", "source": "Colloids and Surfaces A: Physicochemical and Engineering Aspects, 138862", "year": 2025, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:L8Ckcad2t8MC"},
  {"title": "Preparation and Characterization of Kombucha-Derived Bacterial Cellulose for Advanced Antimicrobial Biomaterials", "authors": "Ankita Sharma, Harun Venkatesan", "source": "MDPI", "year": 2025, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:-f6ydRqryjwC"},
  {"title": "Surface modification strategies to functionalize biodegradable materials for antimicrobial properties", "authors": "Ankita Sharma, Harun Venkatesan", "source": "Bioresorbable Materials and Bioactive Surface Coatings, 293-321", "year": 2025, "is_book_chapter": True, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:hC7cP41nSMkC"},
  {"title": "Silica/Alginate Hybrid Aerogel‐Coated Sustainable Textile Liners for Cold Weather Insulation", "authors": "Shreya Behera, Lakshmanan Nagarajan, Ankita Sharma, BS Butola, RR Seenivasan, Harun Venkatesan", "source": "Advanced Engineering Materials, e202501458", "year": 2025, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:IWHjjKOFINEC"},
  {"title": "Elastomeric braided textiles", "authors": "Harun Venkatesan, Sollazhagan Natarajan, AL Sockalingam, RS Rengasamy", "source": "Handbook of Stretchable and Elastomeric Textiles, 111-123", "year": 2024, "is_book_chapter": True, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:9ZlFYXVOiuMC"},
  {"title": "Spider-capture-silk mimicking fibers with high-performance fog collection derived from superhydrophilicity and volume-swelling of gelatin knots", "authors": "Y Jiang, H Venkatesan, S Shi, C Wang, M Cui, Q Zhang, L Tan, J Hu", "source": "Collagen and Leather 5 (1), 4", "year": 2023, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:aqlVkmm33-oC"},
  {"title": "Anisotropic thermally superinsulating boron nitride composite aerogel for building thermal management", "authors": "MH Adegun, KY Chan, J Yang, H Venkatesan, E Kim, H Zhang, X Shen, J Jiao, J Kim", "source": "Composites Part A: Applied Science and Manufacturing 169, 107522", "year": 2023, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:Wp0gIr-vW9MC"},
  {"title": "Mechanochromic optical/electrical skin for ultrasensitive dual-signal sensing", "authors": "H Zhang, H Chen, JH Lee, E Kim, KY Chan, H Venkatesan, X Shen, J Kim", "source": "ACS nano 17 (6), 5921-5934", "year": 2023, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:8k81kl-MbHgC"},
  {"title": "Engineering anisotropic structures of thermally insulating aerogels with high solar reflectance for energy-efficient cooling applications", "authors": "E Kim, KY Chan, J Yang, H Venkatesan, MH Adegun, H Zhang, JH Lee, X Shen, J Kim", "source": "Journal of Materials Chemistry A 11 (13), 7105-7114", "year": 2023, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:qxL8FJ1GzNcC"},
  {"title": "Superinsulating BNNS/PVA composite aerogels with high solar reflectance for energy-efficient buildings", "authors": "J Yang, KY Chan, H Venkatesan, E Kim, MH Adegun, JH Lee, X Shen, J Kim", "source": "Nano-micro letters 14 (1), 54", "year": 2022, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:UeHWp8X0CEIC"},
  {"title": "Scalable anisotropic cooling aerogels by additive freeze-casting", "authors": "KY Chan, X Shen, J Yang, KT Lin, H Venkatesan, E Kim, H Zhang, JH Lee, ...", "source": "Nature communications 13 (1), 5553", "year": 2022, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:M3ejUd6NZC8C"},
  {"title": "Rational design of all resistive multifunctional sensors with stimulus discriminability", "authors": "JH Lee, E Kim, H Zhang, H Chen, H Venkatesan, KY Chan, J Yang, J Kim", "source": "Advanced Functional Materials 32 (1), 2107570", "year": 2022, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:Zph67rFs4hoC"},
  {"title": "Bioinspired chromotropic ionic skin with high-pressure sensitivity and optical-signal discriminability", "authors": "H Chen, H Zhang, JH Lee, E Kim, H Venkatesan, KY Chan, J Yang, J Kim", "source": "Advanced Functional Materials 32 (31), 2201812", "year": 2022, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:Y0pCki6q_DkC"},
  {"title": "Make the dream fibre, Artificial Spider Silk, become a reality", "authors": "J Hu, H Venkatesan, L Gu, Y Jiang, J Chen", "source": "12th Advanced Materials World Congress (AMC 2022)", "year": 2022, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:u-x6o8ySG0sC"},
  {"title": "Ultrafast‐Response/Recovery Flexible Piezoresistive Sensors with DNA‐Like Double Helix Yarns for Epidermal Pulse Monitoring", "authors": "J Chen, J Zhang, J Hu, N Luo, F Sun, H Venkatesan, N Zhao, Y Zhang", "source": "Advanced Materials, 2104313", "year": 2021, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:ULOm3_A8WrAC"},
  {"title": "Effect of a peer‐led intervention combining mental health promotion with coping‐strategy‐based workshops on wellbeing among university students", "authors": "DK Ahorsu, DIS Vidaña, D Lipardo, PB Shah, PC González, S Shende, ...", "source": "International journal of mental health systems 15 (1), 1-10", "year": 2021, "is_book_chapter": False, "link": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=_R5JZskAAAAJ&citation_for_view=_R5JZskAAAAJ:3fE2CSJIrl8C"}
]

# Shared Templates
HEADER_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Publications {year} | Vyoma Lab</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css" />
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div class="site-shell">
      <header class="site-header">
        <div class="container nav-wrap">
          <a class="brand" href="index.html#home">
            <img class="brand-mark" src="images/logo-transparent.svg" alt="logo" />
            <span>Vyoma Lab <small>Research & Discovery</small></span>
          </a>
          <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-menu">
            <span class="menu-label">Menu</span>
            <span class="menu-icon" aria-hidden="true">☰</span>
          </button>
          <nav id="nav-menu" class="nav-menu">
            <div class="nav-item"><a class="nav-link" href="index.html#home">Home</a></div>
            <div class="nav-item has-dropdown">
              <button class="nav-trigger" type="button">People</button>
              <div class="dropdown">
                <a href="harun-venkatesan.html">Harun Venkatesan</a>
                <a href="alumni-postdoc.html">Alumni</a>
                <a href="index.html#staff">Staff</a>
              </div>
            </div>
            <div class="nav-item"><a class="nav-link" href="index.html#current-research">Current Research</a></div>
            <div class="nav-item has-dropdown">
              <button class="nav-trigger" type="button" aria-expanded="true">Publications</button>
              <div class="dropdown">
                <a href="publications.html">All Publications</a>
                <div class="dropdown-submenu">
                  <a href="publications-2025.html">2025</a>
                  <a href="publications-2024.html">2024</a>
                  <a href="publications-2023.html">2023</a>
                  <a href="publications-2022.html">2022</a>
                  <a href="publications-2021.html">2021</a>
                </div>
              </div>
            </div>
            <div class="nav-item"><a class="nav-link" href="index.html#news">News</a></div>
          </nav>
        </div>
      </header>
      <main>
        <section class="section">
          <div class="container">
            <h1>Research Publications {year}</h1>
            <div class="publication-list-layout">'''

FOOTER_TEMPLATE = '''            </div>
          </div>
        </section>
      </main>
      <footer class="footer"><div class="container"><p>© Vyoma Lab</p></div></footer>
    </div>
    <script>
      const menuToggle = document.querySelector(".menu-toggle");
      const navMenu = document.querySelector(".nav-menu");
      if(menuToggle) menuToggle.addEventListener("click", () => navMenu.classList.toggle("open"));
    </script>
  </body>
</html>'''

CARD_TEMPLATE = '''              <article class="content-card publication-card">
                <div class="publication-meta-top">
                  <span class="publication-year-tag">{year}</span>
                  <span class="publication-type-tag">{type}</span>
                </div>
                <h3>{title}</h3>
                <p class="publication-authors">{authors}</p>
                <p class="publication-source"><em>{source}</em></p>
                <div class="publication-actions">
                  <a href="{link}" target="_blank" class="button button-sm button-secondary">
                    <i class="fa-solid fa-graduation-cap"></i> View on Scholar
                  </a>
                </div>
              </article>'''

# Generate Pages
years = sorted(list(set(d['year'] for d in data)), reverse=True)
for year in years:
    year_data = [d for d in data if d['year'] == year]
    html = HEADER_TEMPLATE.format(year=year)
    for entry in year_data:
        type_str = "Book Chapter" if entry['is_book_chapter'] else "Journal Article"
        html += CARD_TEMPLATE.format(
            year=entry['year'], type=type_str, title=entry['title'],
            authors=entry['authors'], source=entry['source'], link=entry['link']
        )
    html += FOOTER_TEMPLATE
    with open(f'/home/sourab/Documents/vyoma_lab_website/publications-{year}.html', 'w') as f:
        f.write(html)
    print(f"Generated publications-{year}.html")

# Update Nav Menu in all files
NAV_BLOCK_NEW = '''<nav id="nav-menu" class="nav-menu" aria-label="Primary">
            <div class="nav-item">
              <a class="nav-link" href="index.html#home">Home</a>
            </div>

            <div class="nav-item has-dropdown">
              <button class="nav-trigger" type="button" aria-expanded="false">
                People
              </button>
              <div class="dropdown">
                <a href="harun-venkatesan.html">Harun Venkatesan</a>
                <div class="dropdown-subgroup">
                  <button class="dropdown-subtrigger" type="button" aria-expanded="false">
                    Alumni
                  </button>
                  <div class="dropdown-submenu" aria-label="Alumni groups">
                    <a class="dropdown-subitem" href="alumni-postdoc.html">Postdoctoral Scholars</a>
                    <a class="dropdown-subitem" href="alumni-phd.html">Ph.D. Graduates</a>
                    <a class="dropdown-subitem" href="alumni-masters-ug.html">Masters & Undergraduates</a>
                  </div>
                </div>
                <a href="index.html#staff">Staff</a>
                <a href="index.html#staff-photos">Photos</a>
              </div>
            </div>

            <div class="nav-item">
              <a class="nav-link" href="index.html#current-research">Current Research</a>
            </div>

            <div class="nav-item has-dropdown">
              <button class="nav-trigger" type="button" aria-expanded="false">
                Publications
              </button>
              <div class="dropdown">
                <a href="publications.html">All Publications</a>
                <div class="dropdown-subgroup">
                  <button class="dropdown-subtrigger" type="button" aria-expanded="false">
                    By Year
                  </button>
                  <div class="dropdown-submenu" aria-label="Publication years">
                    <a class="dropdown-subitem" href="publications-2025.html">2025</a>
                    <a class="dropdown-subitem" href="publications-2024.html">2024</a>
                    <a class="dropdown-subitem" href="publications-2023.html">2023</a>
                    <a class="dropdown-subitem" href="publications-2022.html">2022</a>
                    <a class="dropdown-subitem" href="publications-2021.html">2021</a>
                  </div>
                </div>
              </div>
            </div>

            <div class="nav-item">
              <a class="nav-link" href="index.html#news">News</a>
            </div>

            <div class="nav-item">
              <a class="nav-link" href="index.html#honours">Honours</a>
            </div>
          </nav>'''

NAV_PATTERN = r'<nav id="nav-menu" class="nav-menu" aria-label="Primary">.*?</nav>'

all_html_files = [f for f in os.listdir('/home/sourab/Documents/vyoma_lab_website') if f.endswith('.html')]
for filename in all_html_files:
    path = os.path.join('/home/sourab/Documents/vyoma_lab_website', filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(NAV_PATTERN, NAV_BLOCK_NEW, content, flags=re.DOTALL)
    
    # Also clean up footer links if they mention 2026 or book chapters in a weird way
    new_content = new_content.replace('publications-2026.html', 'publications.html')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated nav in {filename}")
