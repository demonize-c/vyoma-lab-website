import os

file_path = '/home/sourab/Documents/vyoma_lab_website/facilities.html'
with open(file_path, 'r') as f:
    content = f.read()

# Hitachi SEM - Add missing info
content = content.replace(
    '<span class="data-label">EDS</span>\n                  <span class="data-value">Xplore SDD (<129 eV resolution)</span>',
    '<span class="data-label">EDS</span>\n                  <span class="data-value">Xplore SDD (<129 eV resolution)</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Sample Size</span>\n                  <span class="data-value">Max 15 x 15 x 15 mm</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Coater</span>\n                  <span class="data-value">MC1000 Sputter Coater</span>'
)

# GeoPyc - Add missing info
content = content.replace(
    '<span class="data-label">Chambers</span>\n                  <span class="data-value">12.7 to 50.8 mm Diameter</span>',
    '<span class="data-label">Chambers</span>\n                  <span class="data-value">12.7 to 50.8 mm Diameter</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Temp Range</span>\n                  <span class="data-value">10°C to 35°C</span>'
)

with open(file_path, 'w') as f:
    f.write(content)

print("Successfully refined facilities.html")
