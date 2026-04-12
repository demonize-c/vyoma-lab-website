import os
import re

nav_block_old_pattern = r'<nav id="nav-menu" class="nav-menu" aria-label="Primary">.*?</nav>'
nav_block_new = '''<nav id="nav-menu" class="nav-menu" aria-label="Primary">
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
                Publications & Books
              </button>
              <div class="dropdown">
                <a href="publications.html">All Publications</a>
                <div class="dropdown-subgroup">
                  <button class="dropdown-subtrigger" type="button" aria-expanded="false">
                    Book Chapters
                  </button>
                  <div class="dropdown-submenu" aria-label="Book Chapters years">
                    <a class="dropdown-subitem" href="book-chapters.html">All Chapters</a>
                    <a class="dropdown-subitem" href="book-chapters-2025.html">2025</a>
                    <a class="dropdown-subitem" href="book-chapters-2020.html">2020</a>
                    <a class="dropdown-subitem" href="book-chapters-2019.html">2019</a>
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

files = [
    'index.html', 'harun-venkatesan.html', 
    'alumni-postdoc.html', 'alumni-phd.html', 'alumni-masters-ug.html',
    'publications.html', 'publications-2025.html', 'publications-2023.html', 'publications-2022.html',
    'book-chapters.html', 'book-chapters-2025.html', 'book-chapters-2020.html', 'book-chapters-2019.html'
]

for filename in files:
    path = os.path.join('/home/sourab/Documents/vyoma_lab_website', filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace nav block
        new_content = re.sub(nav_block_old_pattern, nav_block_new, content, flags=re.DOTALL)
        
        # Also clean up 2026 footer links if present
        new_content = new_content.replace('publications-2026.html', 'publications.html')
        new_content = new_content.replace('2026 Publications', 'All Publications')
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
