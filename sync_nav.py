import os
import re

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
                <div class="dropdown-subgroup">
                  <button class="dropdown-subtrigger" type="button" aria-expanded="false">
                    Publications
                  </button>
                  <div class="dropdown-submenu" aria-label="Publication years">
                    <a class="dropdown-subitem" href="publications.html">All Publications</a>
                    <a class="dropdown-subitem" href="publications-2025.html">2025 Publications</a>
                    <a class="dropdown-subitem" href="publications-2024.html">2024 Publications</a>
                    <a class="dropdown-subitem" href="publications-2023.html">2023 Publications</a>
                    <a class="dropdown-subitem" href="publications-2022.html">2022 Publications</a>
                    <a class="dropdown-subitem" href="publications-2021.html">2021 Publications</a>
                  </div>
                </div>
                <div class="dropdown-subgroup">
                  <button class="dropdown-subtrigger" type="button" aria-expanded="false">
                    Book Chapters
                  </button>
                  <div class="dropdown-submenu" aria-label="Book Chapter years">
                    <a class="dropdown-subitem" href="book-chapters.html">All Chapters</a>
                    <a class="dropdown-subitem" href="book-chapters-2026.html">2026 Book Chapters</a>
                    <a class="dropdown-subitem" href="book-chapters-2025.html">2025 Book Chapters</a>
                    <a class="dropdown-subitem" href="book-chapters-2020.html">2020 Book Chapters</a>
                    <a class="dropdown-subitem" href="book-chapters-2019.html">2019 Book Chapters</a>
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

files = [f for f in os.listdir('/home/sourab/Documents/vyoma_lab_website') if f.endswith('.html')]

for filename in files:
    path = os.path.join('/home/sourab/Documents/vyoma_lab_website', filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = re.sub(NAV_PATTERN, NAV_BLOCK_NEW, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {filename}")
