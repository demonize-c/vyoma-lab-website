import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Extract top and bottom
match = re.search(r'(.*?)<main>(.*?)</main>(.*)', content, re.DOTALL)
if not match:
    print("Could not find main tag in index.html")
    exit(1)

top = match.group(1) + "<main>\n"
bottom = "\n</main>" + match.group(3)

def create_page(filename, title, image, content_html):
    html = f"""  <section class="section" style="padding-top: 8rem; padding-bottom: 4rem;">
    <div class="container" style="max-width: 800px; margin: 0 auto;">
      <span class="rh-chip" style="margin-bottom: 1rem; display: inline-block;">News Feature</span>
      <h1 style="font-family: var(--font-display, 'Space Grotesk', sans-serif); font-size: clamp(2rem, 5vw, 3rem); font-weight: 700; color: var(--navy-900, #07202f); margin-bottom: 1rem; line-height: 1.2;">{title}</h1>
      <p style="color: var(--slate-500, #64748b); font-size: 1.1rem; margin-bottom: 2rem;">Source: NewsBytes | FITT Forward 2025 Tech Fest</p>
      
      <img src="{image}" alt="{title}" style="width: 100%; border-radius: var(--radius-lg, 24px); margin-bottom: 2.5rem; box-shadow: var(--shadow-md);" />
      
      <div class="article-content" style="font-size: 1.15rem; line-height: 1.8; color: var(--slate-700, #334155);">
         {content_html}
      </div>
      
      <div style="margin-top: 4rem; text-align: center;">
         <a href="index.html#highlights" style="display: inline-flex; align-items: center; gap: 0.5rem; color: var(--sky-600, #1480b0); font-weight: 600; text-decoration: none;">
           <i class="fa-solid fa-arrow-left"></i> Back to News
         </a>
      </div>
    </div>
  </section>"""
    
    with open(filename, "w", encoding="utf-8") as out:
        out.write(top + html + bottom)
    print(f"Created {filename}")

content1 = """
<p>Students from IIT Delhi’s Textile Department impressed with their use of aerogel — the lightest solid on Earth — to create fabrics that withstand temperatures as low as -200°C.</p>
<p>Jackets designed with this technology can protect soldiers in high-altitude regions down to -40°C, while remaining far lighter and less restrictive than traditional cold-weather gear.</p>
"""
create_page("news-aerogel-cold.html", "Extreme cold? No problem", "images/highlights/newsbytes-aerogel.png", content1)


content2 = """
<p>IIT Delhi just wrapped up its FITT Forward 2025 Tech Fest, and it was all about homegrown innovation.</p>
<p>The event brought together investors, policymakers, and young tech fans to check out India's latest breakthroughs—from wind turbines for busses, lorries, and trains to a restored 1920 vintage car and converted Gypsies turned electric for the Army.</p>
<h3>From EV chargers to aerogel fabrics</h3>
<p>Standouts included paper-thin solar panels from P3C Technology (already teamed up with Tata Power), GroKalp's heat-proof composite material, and aerogel fabrics from IIT Delhi that can handle extreme cold.</p>
"""
create_page("news-deep-tech-fest.html", "IIT Delhi's tech fest showcases India's deep-tech breakthroughs", "images/highlights/deep-tech-fest.png", content2)

content3 = """
<p>IIT Delhi's Textile Department students showcased their use of aerogel, the lightest solid on Earth, to create fabrics that can withstand temperatures as low as -200°C.</p>
<p>PhD student Gauri Naik also unveiled a compact laparoscopic camera holder for pediatric surgeries, India's first such device.</p>
<p>These innovations highlight the potential of advanced materials and medical technology in improving our daily lives and health.</p>
"""
create_page("news-medical-aerogel.html", "Aerogel fabrics and laparoscopic camera holder", "images/highlights/medical-aerogel.png", content3)

# Now update index.html
content = content.replace(
    '<a href="https://www.newsbytesapp.com/" target="_blank" rel="noreferrer">Extreme cold? No problem <span class="rh-arrow" aria-hidden="true">&#x2197;</span></a>',
    '<a href="news-aerogel-cold.html">Extreme cold? No problem <span class="rh-arrow" aria-hidden="true">&#x2197;</span></a>'
)

content = content.replace(
    '<a href="https://www.newsbytesapp.com/" target="_blank" rel="noreferrer">Deep-tech Breakthroughs <span class="rh-arrow" aria-hidden="true">&#x2197;</span></a>',
    '<a href="news-deep-tech-fest.html">Deep-tech Breakthroughs <span class="rh-arrow" aria-hidden="true">&#x2197;</span></a>'
)

content = content.replace(
    '<a href="https://www.newsbytesapp.com/" target="_blank" rel="noreferrer">Aerogel in Medical Tech <span class="rh-arrow" aria-hidden="true">&#x2197;</span></a>',
    '<a href="news-medical-aerogel.html">Aerogel in Medical Tech <span class="rh-arrow" aria-hidden="true">&#x2197;</span></a>'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html links")
