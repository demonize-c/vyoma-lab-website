import os
import re

HEAD_BLOCK_MASTER = '''    <link
      rel="apple-touch-icon"
      sizes="180x180"
      href="./images/favicon_io/apple-touch-icon.png?v=2"
    />
    <link rel="icon" type="image/png" sizes="32x32" href="./images/favicon_io/favicon-32x32.png?v=2" />
    <link rel="icon" type="image/png" sizes="16x16" href="./images/favicon_io/favicon-16x16.png?v=2" />
    <link rel="icon" type="image/x-icon" sizes="any" href="./images/favicon_io/favicon.ico?v=2" />
    <link rel="shortcut icon" href="./images/favicon_io/favicon.ico?v=2" />
    <link rel="manifest" href="./images/favicon_io/site.webmanifest?v=2" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css"
    />
    <link rel="stylesheet" href="styles.css" />'''

NAV_BLOCK_MASTER = '''<nav id="nav-menu" class="nav-menu" aria-label="Primary">
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
                <a href="index.html#current-research">
                  <i class="fa-solid fa-microscope" aria-hidden="true"></i>
                  <span>Domain of Research</span>
                </a>
                <a href="#">
                  <i class="fa-solid fa-link" aria-hidden="true"></i>
                  <span>Link 1</span>
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
              <a class="nav-link" href="index.html#honours">
                <i class="fa-solid fa-award" aria-hidden="true"></i>
                <span>Honours</span>
              </a>
            </div>
          </nav>'''

FOOTER_BLOCK_MASTER = '''<footer class="site-footer">
        <div class="container">
          <div class="footer-grid">
            <div class="footer-brand">
              <a class="brand" href="index.html#home" style="margin-bottom: 2rem; display: flex;">
                <img class="brand-mark" src="images/logo-transparent.svg" alt="Vyoma Lab" style="filter: brightness(0) invert(1); width: 42px;">
                <span style="color: white; margin-left: 0.75rem; font-weight: 700; font-size: 1.25rem;">Vyoma Lab</span>
              </a>
              <p>
                Leading research in advanced textiles, biomaterials, and energy-efficient cooling solutions. 
                Pushing boundaries in multifunctional sensors and sustainable technology.
              </p>
            </div>

            <div class="footer-col">
              <h4>Navigation</h4>
              <ul class="footer-links-list">
                <li><a href="index.html#home">Home</a></li>
                <li><a href="harun-venkatesan.html">Dr. Harun Venkatesan</a></li>
                <li><a href="index.html#current-research">Current Research</a></li>
                <li><a href="photos.html">Gallery</a></li>
                <li><a href="index.html#honours">Honours</a></li>
              </ul>
            </div>

            <div class="footer-col">
              <h4>Research</h4>
              <ul class="footer-links-list">
                <li><a href="publications.html">All Publications</a></li>
                <li><a href="book-chapters.html">Book Chapters</a></li>
                <li><a href="publications-2025.html">2025 Archive</a></li>
                <li><a href="publications-2024.html">2024 Archive</a></li>
                <li><a href="book-chapters-2026.html">2026 Book Chapters</a></li>
              </ul>
            </div>

            <div class="footer-col">
              <h4>People</h4>
              <ul class="footer-links-list">
                <li><a href="alumni-postdoc.html">Staff</a></li>
                <li><a href="alumni-phd.html">Ph.D. Graduates</a></li>
                <li><a href="alumni-masters-ug.html">Masters & Undergraduates</a></li>
              </ul>
            </div>
          </div>

          <div class="footer-bottom">
            <div class="footer-contact">
              <strong>Department of Textile and Fibre Engineering</strong><br>
              IIT Campus, Hauz Khas, New Delhi-110016
            </div>
            <div class="footer-copyright">
              Copyright © 2026 Vyoma Lab. All rights reserved.
            </div>
          </div>
        </div>
      </footer>'''

# (JS SCRIPT included)
SCRIPT_BLOCK_MASTER = '''<script>
      // Navigation functionality
      const menuToggle = document.querySelector(".menu-toggle");
      const navMenu = document.querySelector(".nav-menu");
      const dropdownItems = Array.from(document.querySelectorAll(".has-dropdown"));
      const dropdownSubgroups = Array.from(document.querySelectorAll(".dropdown-subgroup"));

      const setTriggerState = (trigger, isOpen) => {
        if (!trigger) return;
        trigger.setAttribute("aria-expanded", String(isOpen));
      };

      const closeDropdownSubgroups = () => {
        dropdownSubgroups.forEach((group) => {
          group.classList.remove("open");
          setTriggerState(group.querySelector(".dropdown-subtrigger"), false);
        });
      };

      const closeDropdownItems = () => {
        dropdownItems.forEach((item) => {
          item.classList.remove("open");
          setTriggerState(item.querySelector(".nav-trigger"), false);
        });
        closeDropdownSubgroups();
      };

      const closeNavMenu = () => {
        if (!navMenu || !menuToggle) return;
        navMenu.classList.remove("open");
        document.body.classList.remove("menu-open");
        setTriggerState(menuToggle, false);
      };

      if (menuToggle && navMenu) {
        menuToggle.addEventListener("click", (event) => {
          event.stopPropagation();
          const isOpen = navMenu.classList.toggle("open");
          document.body.classList.toggle("menu-open", isOpen);
          setTriggerState(menuToggle, isOpen);

          if (!isOpen) {
            closeDropdownItems();
          }
        });

        navMenu.querySelectorAll("a").forEach((link) => {
          link.addEventListener("click", () => {
            closeDropdownItems();
            closeNavMenu();
          });
        });
      }

      dropdownItems.forEach((item) => {
        const trigger = item.querySelector(".nav-trigger");

        if (!trigger) return;

        trigger.addEventListener("click", (event) => {
          event.stopPropagation();
          const isOpen = item.classList.contains("open");

          closeDropdownItems();

          if (!isOpen) {
            item.classList.add("open");
            setTriggerState(trigger, true);
          }
        });
      });

      dropdownSubgroups.forEach((group) => {
        const trigger = group.querySelector(".dropdown-subtrigger");

        if (!trigger) return;

        trigger.addEventListener("click", (event) => {
          event.stopPropagation();
          const isOpen = group.classList.contains("open");

          closeDropdownSubgroups();

          if (!isOpen) {
            group.classList.add("open");
            setTriggerState(trigger, true);
          }
        });
      });

      document.addEventListener("click", (event) => {
        const clickedInsideMenu = navMenu && navMenu.contains(event.target);
        const clickedMenuToggle = menuToggle && menuToggle.contains(event.target);

        if (clickedInsideMenu || clickedMenuToggle) return;
        closeDropdownItems();
        closeNavMenu();
      });

      document.addEventListener("keydown", (event) => {
        if (event.key !== "Escape") return;
        closeDropdownItems();
        closeNavMenu();
      });
    </script>'''

def transform_archive_heading(content, filename):
    # Surgical replacement of everything from <main> until the publications-list-layout
    # This is the safest way to reset the hero section
    
    # Identify the title
    match = re.search(r'<h1>(.*?)</h1>', content)
    if not match: return content
    title = match.group(1)
    
    # Identify year
    year_match = re.search(r'\d{4}', title)
    year = year_match.group(0) if year_match else "Selected"
    type_str = "Archive" if "Publications" in title else "Edition"

    hero_section = f'''        <section class="section publication-hero-section">
          <div class="container">
            <div class="content-card publication-hero-card">
              <span class="eyebrow">{title} {type_str}</span>
              <h1>{title}</h1>
              <p>Explore Vyoma Lab's high-impact research contributions and scholarly breakthroughs from the {year} academic cycle.</p>
            </div>
          </div>
        </section>

        <section class="section" style="padding-top: 0;">
          <div class="container">
'''

    # Find <main>
    main_start = content.find('<main>')
    if main_start == -1: return content
    
    # Find the start of the list layout
    list_start = content.find('<div class="publication-list-layout"')
    if list_start == -1: 
        # Fallback if list layout is missing (shouldn't happen)
        return content

    # Replace everything between <main> and the list start
    new_content = content[:main_start + 6] + "\n" + hero_section + content[list_start:]
    
    return new_content

files = [f for f in os.listdir('/home/sourab/Documents/vyoma_lab_website') if f.endswith('.html')]

for filename in files:
    path = os.path.join('/home/sourab/Documents/vyoma_lab_website', filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Sync core elements
    if 'styles.css' in content:
        start_idx = content.find('<link')
        end_idx = content.find('styles.css')
        if start_idx != -1 and end_idx != -1:
            end_idx = content.find('>', end_idx) + 1
            content = content[:start_idx] + HEAD_BLOCK_MASTER + content[end_idx:]

    content = re.sub(r'<nav id="nav-menu".*?>.*?</nav>', NAV_BLOCK_MASTER, content, flags=re.DOTALL)
    content = re.sub(r'<footer\s+class=["\'](?:footer|site-footer)["\'].*?>.*?</footer>', FOOTER_BLOCK_MASTER, content, flags=re.DOTALL)
    
    if 'menuToggle' in content:
        script_regex = r'<script>.*?menuToggle.*?<\/script>'
        if not re.search(script_regex, content, flags=re.DOTALL):
            script_regex = r'<script>.*?</script>'
        content = re.sub(script_regex, SCRIPT_BLOCK_MASTER, content, flags=re.DOTALL)
    
    # Archive Transformation (Surgically reset header)
    is_archive = ('publications-' in filename or 'book-chapters-' in filename or filename == 'book-chapters.html' or filename == 'publications.html')
    if is_archive and 'index.html' not in filename:
        content = transform_archive_heading(content, filename)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Robust Sync: {filename}")
