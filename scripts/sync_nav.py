import os
import re

NAV_BLOCK_NEW = '''<nav id="nav-menu" class="nav-menu" aria-label="Primary">
            <div class="nav-item">
              <a class="nav-link" href="index.html#home">
                <i class="fa-solid fa-house" aria-hidden="true"></i>
                <span>Home</span>
              </a>
            </div>

            <div class="nav-item has-dropdown">
              <button class="nav-trigger" type="button" aria-expanded="false">
                <i class="fa-solid fa-users" aria-hidden="true"></i>
                <span>People</span>
              </button>
              <div class="dropdown">
                <a href="harun-venkatesan.html">
                  <i class="fa-solid fa-user-tie" aria-hidden="true"></i>
                  <span>Harun Venkatesan</span>
                </a>
                <a href="alumni-postdoc.html">
                  <i class="fa-solid fa-user-graduate" aria-hidden="true"></i>
                  <span>Postdoctoral Scholars</span>
                </a>
                <a href="alumni-phd.html">
                  <i class="fa-solid fa-graduation-cap" aria-hidden="true"></i>
                  <span>Ph.D. Graduates</span>
                </a>
                <a href="alumni-masters-ug.html">
                  <i class="fa-solid fa-user-group" aria-hidden="true"></i>
                  <span>Masters & Undergraduates</span>
                </a>
                <a href="staff.html">
                  <i class="fa-solid fa-user-gear" aria-hidden="true"></i>
                  <span>Staff</span>
                </a>
                <a href="photos.html">
                  <i class="fa-solid fa-camera-retro" aria-hidden="true"></i>
                  <span>Photos</span>
                </a>
              </div>
            </div>

            <div class="nav-item">
              <a class="nav-link" href="index.html#current-research">
                <i class="fa-solid fa-flask-vial" aria-hidden="true"></i>
                <span>Current Research</span>
              </a>
            </div>

            <div class="nav-item">
              <a class="nav-link" href="facilities.html">
                <i class="fa-solid fa-microscope" aria-hidden="true"></i>
                <span>Facilities</span>
              </a>
            </div>

            <div class="nav-item has-dropdown">
              <button class="nav-trigger" type="button" aria-expanded="false">
                <i class="fa-solid fa-book-open" aria-hidden="true"></i>
                <span>Publications</span>
              </button>
              <div class="dropdown">
                <div class="dropdown-subgroup">
                  <button class="dropdown-subtrigger" type="button" aria-expanded="false">
                    <i class="fa-solid fa-journal-whills" aria-hidden="true"></i>
                    <span>Publications</span>
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
                    <i class="fa-solid fa-book" aria-hidden="true"></i>
                    <span>Book Chapters</span>
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
              <a class="nav-link" href="index.html#news">
                <i class="fa-solid fa-newspaper" aria-hidden="true"></i>
                <span>News</span>
              </a>
            </div>

            <div class="nav-item">
              <a class="nav-link" href="index.html#honours">
                <i class="fa-solid fa-award" aria-hidden="true"></i>
                <span>Honours</span>
              </a>
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
