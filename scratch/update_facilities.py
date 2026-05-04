import os

file_path = '/home/sourab/Documents/vyoma_lab_website/facilities.html'
with open(file_path, 'r') as f:
    content = f.read()

# C-Therm
content = content.replace(
    'A high-precision system using the MTPS sensor for rapid, single-sided thermal conductivity measurement. Ideal for solids, liquids, and powders with minimal sample preparation.',
    'A high-precision system using the MTPS sensor for rapid, single-sided thermal conductivity measurement of solids, liquids, and powders.'
)
content = content.replace(
    '<span class="data-label">Range</span>\n                  <span class="data-value">0.01 – 500 W/m·K</span>\n                </div>',
    '<span class="data-label">Range</span>\n                  <span class="data-value">0.01 – 500 W/m·K</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Setup</span>\n                  <span class="data-value">Single-sided, rapid analysis</span>\n                </div>'
)

# AccuPyc
content = content.replace(
    'Critical for calculating true density and porosity with sub-0.03% accuracy.',
    'Critical for calculating true density and porosity with automatic pressure and temperature control.'
)
content = content.replace(
    '<span class="data-label">Repeatability</span>\n                  <span class="data-value">±0.01%</span>',
    '<span class="data-label">Range</span>\n                  <span class="data-value">0.01 to >100 g/cm³</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Chambers</span>\n                  <span class="data-value">1, 10, and 100 cm³</span>'
)

# GeoPyc
content = content.replace(
    'A specialized instrument for determining the envelope density of porous materials, using a unique dry displacement technique that is both rapid and non-destructive.',
    'Precise determination of envelope volume and density of solid samples using DryFlo displacement technology. Features automated, non-destructive analysis and T.A.P. mode.'
)
content = content.replace(
    '<span class="data-label">Capability</span>\n                  <span class="data-value">Bulk & Envelope Density</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Process</span>\n                  <span class="data-value">Dry Displacement (DryFlo)</span>',
    '<span class="data-label">Technology</span>\n                  <span class="data-value">DryFlo Displacement</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Reproducibility</span>\n                  <span class="data-value">≈±1.1% (≥25% chamber volume)</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Chambers</span>\n                  <span class="data-value">12.7 to 50.8 mm Diameter</span>'
)

# Liquid Density
content = content.replace(
    '<h2>Anton Paar Liquid Density Meter</h2>',
    '<h2>Anton Paar Liquid Density Meter (DMA)</h2>'
)
content = content.replace(
    'A highly accurate digital density meter for liquid samples, utilizing the oscillating U-tube principle to provide rapid and reliable results.',
    'High-precision instrument for measuring liquid density based on the oscillating U-tube principle, providing rapid and accurate analysis.'
)
content = content.replace(
    '<span class="data-label">Accuracy</span>\n                  <span class="data-value">Up to 0.0001 g/cm³</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Technology</span>\n                  <span class="data-value">Digital Oscillating U-tube</span>',
    '<span class="data-label">Principle</span>\n                  <span class="data-value">Oscillating U-tube</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Application</span>\n                  <span class="data-value">High-precision liquid analysis</span>'
)

# Impedance Tube
content = content.replace(
    'A professional-grade acoustic measurement system designed for determining the sound absorption coefficient and transmission loss of small material samples.',
    'Precision acoustic characterization system for measuring sound absorption, reflection, and acoustic impedance using the transfer function method.'
)
content = content.replace(
    '<span class="data-label">Standards</span>\n                  <span class="data-value">ASTM E1050 & ISO 10534-2</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Frequency Range</span>\n                  <span class="data-value">50 Hz – 6.4 kHz</span>',
    '<span class="data-label">Standards</span>\n                  <span class="data-value">ASTM E1050 / ISO 10534-2</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Frequency Range</span>\n                  <span class="data-value">100 Hz to 6,400 Hz</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Capability</span>\n                  <span class="data-value">Circular samples (29mm & 100mm)</span>'
)

# Thermal Imager
content = content.replace(
    '<h2>Thermal Imaging Camera</h2>',
    '<h2>Fluke TiX580 Thermal Imager</h2>'
)
content = content.replace(
    'High-resolution thermal analysis system for monitoring heat distribution, thermal insulation efficiency, and detecting thermal anomalies in real-time.',
    'High-performance infrared camera with 640 x 480 resolution (SuperResolution up to 1280 x 960) and MultiSharp™ focus for precise heat distribution monitoring.'
)
content = content.replace(
    '<span class="data-label">Sensor</span>\n                  <span class="data-value">Uncooled Focal Plane Array</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Accuracy</span>\n                  <span class="data-value">±2°C or ±2%</span>',
    '<span class="data-label">Resolution</span>\n                  <span class="data-value">Up to 1280 × 960 (SuperRes)</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Sensitivity</span>\n                  <span class="data-value">≤0.05 °C (50 mK)</span>\n                </div>\n                <div class="data-row">\n                  <span class="data-label">Range</span>\n                  <span class="data-value">−20 °C to 1000 °C</span>'
)

with open(file_path, 'w') as f:
    f.write(content)

print("Successfully updated facilities.html")
