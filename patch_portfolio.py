import re

with open('portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_card = """                        <a href="floodboy.html" class="project-link">เปิดดูโปรเจกต์ 📊</a>
                    </div>
                </div>

                <!-- Project 6 -->
                <div class="project-card" onclick="window.location.href='fruit-ninja.html'">
                    <div class="project-img" style="background: linear-gradient(45deg, #f59e0b, #e11d48);"></div>
                    <div class="project-content">
                        <h3 class="project-title">Fruit Slicer Online 🍉</h3>
                        <p class="project-desc">เกมฟันผลไม้ออนไลน์แบบ Real-time Multiplayer (MQTT)
                            รองรับผู้เล่นหลายคนในห้องเดียวโดยไม่ใช้ Database</p>
                        <div class="project-tags">
                            <span>#GameDev</span><span>#Canvas</span><span>#MQTT</span><span>#WebSockets</span>
                        </div>
                        <a href="fruit-ninja.html" class="project-link">เปิดเล่นเกม ⚔️</a>
                    </div>
                </div>"""

# Replace the last part of floodboy card with the floodboy + new card
html = html.replace('                        <a href="floodboy.html" class="project-link">เปิดดูโปรเจกต์ 📊</a>\n                    </div>\n                </div>', new_card)

with open('portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Patched portfolio.html successfully.")
