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
                <button class="submenu-back" type="button" aria-label="Go back to main menu">
                  <i class="fa-solid fa-arrow-left" aria-hidden="true"></i>
                  <span>Back to Menu</span>
                </button>
                <a href="harun-venkatesan.html">
                  <i class="fa-solid fa-user-tie" aria-hidden="true"></i>
                  <span>Harun Venkatesan</span>
                </a>
                <a href="alumni-postdoc.html">
                  <i class="fa-solid fa-user-gear" aria-hidden="true"></i>
                  <span>Staff</span>
                </a>
                <a href="alumni-phd.html">
                  <i class="fa-solid fa-graduation-cap" aria-hidden="true"></i>
                  <span>Ph.D. Graduates</span>
                </a>
                <a href="alumni-masters-ug.html">
                   <i class="fa-solid fa-user-group" aria-hidden="true"></i>
                   <span>Masters & Undergraduates</span>
                </a>
              </div>
            </div>

            <div class="nav-item has-dropdown">
              <button class="nav-trigger" type="button" aria-expanded="false">
                <i class="fa-solid fa-flask-vial" aria-hidden="true"></i>
                <span>Current Research</span>
              </button>
              <div class="dropdown">
                <button class="submenu-back" type="button" aria-label="Go back to main menu">
                  <i class="fa-solid fa-arrow-left" aria-hidden="true"></i>
                  <span>Back to Menu</span>
                </button>
                <a href="funding-collaboration.html">
                  <i class="fa-solid fa-handshake" aria-hidden="true"></i>
                  <span>Funding & Collaboration</span>
                </a>
                <a href="research-domains.html">
                  <i class="fa-solid fa-microscope" aria-hidden="true"></i>
                  <span>Domain of Research</span>
                </a>
              </div>
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
                <button class="submenu-back" type="button" aria-label="Go back to main menu">
                  <i class="fa-solid fa-arrow-left" aria-hidden="true"></i>
                  <span>Back to Menu</span>
                </button>
                <div class="dropdown-subgroup">
                  <button class="dropdown-subtrigger" type="button" aria-expanded="false">
                    <i class="fa-solid fa-journal-whills" aria-hidden="true"></i>
                    <span>Publications</span>
                  </button>
                  <div class="dropdown-submenu" aria-label="Publication years">
                    <button class="submenu-back" type="button" aria-label="Go back to publication options">
                      <i class="fa-solid fa-arrow-left" aria-hidden="true"></i>
                      <span>Back</span>
                    </button>
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
                    <button class="submenu-back" type="button" aria-label="Go back to publication options">
                      <i class="fa-solid fa-arrow-left" aria-hidden="true"></i>
                      <span>Back</span>
                    </button>
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
              <a class="nav-link" href="photos.html">
                <i class="fa-solid fa-camera-retro" aria-hidden="true"></i>
                <span>Gallery</span>
              </a>
            </div>

            <div class="nav-item">
              <a class="nav-link" href="awards-honours.html">
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
