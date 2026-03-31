import streamlit as st

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ankit Kumar | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;700;800&display=swap');
/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [data-testid="stAppViewContainer"] {
    background: #080810 !important;
    color: #e8e8f0 !important;
    font-family: 'Syne', sans-serif !important;
}
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(ellipse 80% 50% at 20% -10%, rgba(99,60,255,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 80% 100%, rgba(0,200,180,0.10) 0%, transparent 60%),
        #080810 !important;
}
[data-testid="stHeader"],
[data-testid="stToolbar"],
footer,
#MainMenu { display: none !important; }
[data-testid="stVerticalBlock"] { gap: 0 !important; }
section.main > div { padding: 0 !important; }
/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #080810; }
::-webkit-scrollbar-thumb { background: #633cff; border-radius: 2px; }
/* ── Typography ── */
h1, h2, h3, h4 { font-family: 'Syne', sans-serif !important; }
code, pre { font-family: 'Space Mono', monospace !important; }
/* ── Divider ── */
hr { border: none; border-top: 1px solid rgba(255,255,255,0.07) !important; margin: 0 !important; }
/* ── Nav ── */
.nav-wrap {
    position: sticky; top: 0; z-index: 100;
    background: rgba(8,8,16,0.85);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(99,60,255,0.2);
    padding: 0 3rem;
    display: flex; align-items: center; justify-content: space-between;
    height: 64px;
}
.nav-logo {
    font-family: 'Space Mono', monospace;
    font-size: 1rem; font-weight: 700;
    color: #633cff; letter-spacing: 0.1em;
}
.nav-links { display: flex; gap: 2rem; }
.nav-links a {
    font-size: 0.78rem; font-weight: 600; letter-spacing: 0.12em;
    text-transform: uppercase; color: rgba(232,232,240,0.6);
    text-decoration: none; transition: color 0.2s;
}
.nav-links a:hover { color: #00c8b4; }
/* ── Hero ── */
.hero-wrap {
    min-height: 92vh;
    display: flex; align-items: center;
    padding: 6rem 3rem 4rem;
    position: relative; overflow: hidden;
}
.hero-grid-bg {
    position: absolute; inset: 0; z-index: 0;
    background-image:
        linear-gradient(rgba(99,60,255,0.06) 1px, transparent 1px),
        linear-gradient(90deg, rgba(99,60,255,0.06) 1px, transparent 1px);
    background-size: 60px 60px;
    mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 0%, transparent 100%);
}
.hero-inner {
    position: relative; z-index: 1;
    display: flex; align-items: center; justify-content: space-between;
    gap: 4rem; width: 100%;
}
.hero-content { flex: 1; max-width: 680px; }
.hero-image-col {
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
}
.hero-image-col img {
    width: 320px; height: 320px;
    object-fit: cover;
    border-radius: 50%;
    border: 3px solid rgba(99,60,255,0.5);
    box-shadow: 0 0 0 8px rgba(99,60,255,0.08), 0 0 60px rgba(99,60,255,0.2);
}
@media (max-width: 768px) {
    .hero-inner { flex-direction: column-reverse; gap: 2rem; }
    .hero-image-col img { width: 200px; height: 200px; }
}
.hero-tag {
    display: inline-flex; align-items: center; gap: 0.5rem;
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem; letter-spacing: 0.2em; text-transform: uppercase;
    color: #00c8b4;
    background: rgba(0,200,180,0.08);
    border: 1px solid rgba(0,200,180,0.25);
    border-radius: 100px; padding: 0.35rem 1rem;
    margin-bottom: 2rem;
}
.hero-tag::before { content: '●'; font-size: 0.5rem; animation: pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }
.hero-name {
    font-size: clamp(3.5rem, 8vw, 6.5rem);
    font-weight: 800; line-height: 0.95;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #ffffff 0%, rgba(255,255,255,0.6) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.hero-role {
    font-size: clamp(1.5rem, 3.5vw, 2.5rem);
    font-weight: 700; letter-spacing: -0.02em;
    background: linear-gradient(135deg, #633cff 0%, #00c8b4 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 1.5rem;
}
.hero-desc {
    font-size: 1.05rem; line-height: 1.75;
    color: rgba(232,232,240,0.65); max-width: 560px;
    margin-bottom: 2.5rem;
}
.hero-cta-row { display: flex; gap: 1rem; flex-wrap: wrap; }
.btn-primary {
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: #633cff; color: #fff;
    padding: 0.75rem 1.75rem;
    border-radius: 8px; font-weight: 700;
    font-size: 0.88rem; letter-spacing: 0.05em;
    text-decoration: none; transition: all 0.2s;
    border: 1px solid #633cff;
}
.btn-primary:hover { background: #7a58ff; transform: translateY(-2px); box-shadow: 0 8px 30px rgba(99,60,255,0.4); }
.btn-ghost {
    display: inline-flex; align-items: center; gap: 0.5rem;
    background: transparent; color: rgba(232,232,240,0.8);
    padding: 0.75rem 1.75rem;
    border-radius: 8px; font-weight: 700;
    font-size: 0.88rem; letter-spacing: 0.05em;
    text-decoration: none; transition: all 0.2s;
    border: 1px solid rgba(232,232,240,0.2);
}
.btn-ghost:hover { border-color: #00c8b4; color: #00c8b4; transform: translateY(-2px); }
/* ── Section Wrappers ── */
.section-wrap { padding: 5rem 3rem; }
.section-wrap-alt { padding: 5rem 3rem; background: rgba(255,255,255,0.018); }
.section-label {
    font-family: 'Space Mono', monospace;
    font-size: 0.7rem; letter-spacing: 0.25em; text-transform: uppercase;
    color: #633cff; margin-bottom: 0.75rem;
}
.section-title {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800; letter-spacing: -0.03em;
    color: #fff; margin-bottom: 1rem;
}
.section-sub {
    font-size: 1rem; color: rgba(232,232,240,0.55);
    max-width: 520px; line-height: 1.7; margin-bottom: 3rem;
}
/* ── Stats Row ── */
.stats-row {
    display: flex; gap: 2rem; flex-wrap: wrap;
    margin-top: 3rem; padding-top: 3rem;
    border-top: 1px solid rgba(255,255,255,0.07);
}
.stat-item { }
.stat-num {
    font-family: 'Space Mono', monospace;
    font-size: 2.5rem; font-weight: 700;
    background: linear-gradient(135deg, #633cff, #00c8b4);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    line-height: 1;
}
.stat-label {
    font-size: 0.8rem; color: rgba(232,232,240,0.5);
    letter-spacing: 0.1em; text-transform: uppercase;
    margin-top: 0.25rem;
}
/* ── Project Cards ── */
.projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 1.5rem;
}
.project-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px; padding: 2rem;
    transition: all 0.3s; cursor: default;
    position: relative; overflow: hidden;
    display: flex; flex-direction: column;
}
.project-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, transparent, var(--accent, #633cff), transparent);
    opacity: 0; transition: opacity 0.3s;
}
.project-card:hover {
    border-color: rgba(99,60,255,0.3);
    background: rgba(99,60,255,0.05);
    transform: translateY(-4px);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
}
.project-card:hover::before { opacity: 1; }
.project-icon {
    font-size: 2rem; margin-bottom: 1.25rem;
    display: block;
}
.project-title {
    font-size: 1.2rem; font-weight: 700;
    color: #fff; margin-bottom: 0.5rem;
}
.project-desc {
    font-size: 0.88rem; line-height: 1.7;
    color: rgba(232,232,240,0.55);
    margin-bottom: 1.25rem;
}
.tag-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1.25rem; }
.tag {
    font-family: 'Space Mono', monospace;
    font-size: 0.65rem; letter-spacing: 0.08em;
    padding: 0.2rem 0.6rem; border-radius: 4px;
    background: rgba(99,60,255,0.12);
    border: 1px solid rgba(99,60,255,0.25);
    color: rgba(200,190,255,0.85);
}
.feature-list { list-style: none; padding: 0; flex-grow: 1; }
.feature-list li {
    font-size: 0.82rem; color: rgba(232,232,240,0.5);
    padding: 0.2rem 0; padding-left: 1rem;
    position: relative;
}
.feature-list li::before {
    content: '→'; position: absolute; left: 0;
    color: #00c8b4; font-size: 0.7rem;
}
.card-link {
    display: inline-flex; align-items: center; gap: 0.4rem;
    margin-top: 1.25rem;
    font-size: 0.78rem; font-weight: 700; letter-spacing: 0.05em;
    color: #633cff; text-decoration: none;
    border: 1px solid rgba(99,60,255,0.3);
    border-radius: 6px; padding: 0.35rem 0.85rem;
    background: rgba(99,60,255,0.08);
    transition: all 0.2s; align-self: flex-start;
}
.card-link:hover { background: rgba(99,60,255,0.2); color: #fff; border-color: #633cff; }
/* ── Skills ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 1rem;
}
.skill-category {
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px; padding: 1.5rem;
}
.skill-cat-title {
    font-size: 0.75rem; font-weight: 700;
    letter-spacing: 0.15em; text-transform: uppercase;
    color: #00c8b4; margin-bottom: 1rem;
}
.skill-pills { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.skill-pill {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem; padding: 0.3rem 0.75rem;
    border-radius: 6px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    color: rgba(232,232,240,0.75);
}
/* ── Contact ── */
.contact-card {
    max-width: 640px; margin: 0 auto; text-align: center;
}
.contact-links { display: flex; gap: 1.5rem; justify-content: center; flex-wrap: wrap; margin-top: 2rem; }
.contact-link {
    display: inline-flex; align-items: center; gap: 0.5rem;
    font-size: 1rem; font-weight: 600;
    text-decoration: none; color: rgba(232,232,240,0.7);
    transition: color 0.2s;
}
.contact-link:hover { color: #00c8b4; }
/* ── Footer ── */
.footer {
    padding: 2rem 3rem;
    border-top: 1px solid rgba(255,255,255,0.07);
    display: flex; align-items: center; justify-content: space-between;
    flex-wrap: wrap; gap: 1rem;
}
.footer-copy {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem; color: rgba(232,232,240,0.3);
}
.footer-made {
    font-family: 'Space Mono', monospace;
    font-size: 0.72rem; color: rgba(232,232,240,0.3);
}
.footer-made span { color: #633cff; }
/* ── Streamlit overrides ── */
.stMarkdown p { margin: 0 !important; }
div[data-testid="column"] { padding: 0 !important; }
a:link {
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# NAV
# ══════════════════════════════════════════════════════════════

# ── Set your logo image path here ────────────────────────────
LOGO_IMAGE = "logo.png"  # place logo.png next to portfolio.py

import base64, os
def get_img_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        ext = path.rsplit(".", 1)[-1].lower().replace("jpg", "jpeg")
        return f"data:image/{ext};base64,{data}"
    return None

logo_src = get_img_base64(LOGO_IMAGE)
logo_html = f'<img src="{logo_src}" alt="Logo" style="height:38px;object-fit:contain;border-radius:50%;">' if logo_src else '<span class="nav-logo">AK.dev</span>'

st.markdown(f"""
<div class="nav-wrap">
    <div class="nav-logo">{logo_html}</div>
    <div class="nav-links">
        <a href="#about">About</a>
        <a href="#projects">Projects</a>
        <a href="#skills">Skills</a>
        <a href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════
# ── Image uploader (hidden in sidebar) ───────────────────────
PROFILE_IMAGE = "profile.jpg"  # put your image in the same folder as portfolio.py

def get_img_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        ext = path.rsplit(".", 1)[-1].lower().replace("jpg", "jpeg")
        return f"data:image/{ext};base64,{data}"
    return None
 
img_src = get_img_base64(PROFILE_IMAGE)
 
if img_src:
    img_html = f'<div class="hero-image-col"><img src="{img_src}" alt="Ankit Kumar"></div>'
else:
    img_html = '''<div class="hero-image-col">
        <div style="width:320px;height:320px;border-radius:50%;
            border:3px dashed rgba(99,60,255,0.4);
            background:rgba(99,60,255,0.07);
            display:flex;flex-direction:column;align-items:center;justify-content:center;
            box-shadow:0 0 0 8px rgba(99,60,255,0.06),0 0 60px rgba(99,60,255,0.15);">
            <span style="font-size:3rem;">👤</span>
            <span style="font-size:0.72rem;color:rgba(232,232,240,0.35);margin-top:0.75rem;
                font-family:Space Mono,monospace;letter-spacing:0.08em;text-align:center;">
                Place your image as<br><b style="color:rgba(99,60,255,0.8);">profile.jpg</b><br>next to portfolio.py
            </span>
        </div>
    </div>'''
 
st.markdown(f"""
<div class="hero-wrap">
    <div class="hero-grid-bg"></div>
    <div class="hero-inner">
        <div class="hero-content">
            <div class="hero-tag">Available for projects</div>
            <div class="hero-name">Ankit<br>Kumar</div>
            <div class="hero-role">Developer &amp; Builder</div>
            <p class="hero-desc">
                I build things that are genuinely useful &mdash; from AI-powered tools and
                computer vision systems to games and custom browser experiences.
                I turn ideas into working software.
            </p>
            <div class="hero-cta-row">
                <a class="btn-primary" href="https://github.com/Kenk26">View GitHUB</a>
                <a class="btn-ghost" href="#contact">Get in Touch</a>
            </div>
        </div>
        {img_html}
    </div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("<hr>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="about"></div><div class="section-wrap"><div class="section-label">// About Me</div><div class="section-title">Who I Am</div><p class="section-sub">I&#39;m a self-driven developer passionate about building creative, real-world projects. I love combining machine learning, computer vision, and clean UI to create software that actually works and feels great to use.</p><p style="font-size:1rem;line-height:1.8;color:rgba(232,232,240,0.6);max-width:640px;">My projects span multiple domains &mdash; desktop GUI apps in C and Python, AI-powered document tools, real-time gesture controllers, face recognition security systems, and polished web games. I&#39;m always learning, always building.<br><br>When I&#39;m not coding, I&#39;m diving into Games, Anime, Manga, and anything that inspires creative thinking.</p><div class="stats-row"><div class="stat-item"><div class="stat-num">7+</div><div class="stat-label">Projects Built</div></div><div class="stat-item"><div class="stat-num">5+</div><div class="stat-label">Languages Used</div></div><div class="stat-item"><div class="stat-num">3</div><div class="stat-label">AI/ML Projects</div></div><div class="stat-item"><div class="stat-num">&#8734;</div><div class="stat-label">Ideas in Progress</div></div></div></div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PROJECTS
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap-alt">
    <div class="section-label">// Projects</div>
    <div class="section-title">What I&#39;ve Built</div>
    <p class="section-sub">A collection of projects across AI, computer vision, games, and web.</p>
    <div class="projects-grid">
        <div class="project-card" style="--accent:#633cff">
            <span class="project-icon">🖐️</span>
            <div class="project-title">Hand Gesture Mouse Controller</div>
            <p class="project-desc">Control your entire computer with hand gestures via webcam. No hardware required &mdash; just your hand.</p>
            <div class="tag-row">
                <span class="tag">Python</span>
                <span class="tag">MediaPipe</span>
                <span class="tag">TensorFlow</span>
                <span class="tag">PyAutoGUI</span>
            </div>
            <ul class="feature-list">
                <li>6 gesture classes with 63-feature landmark detection</li>
                <li>Custom TF classifier with gesture smoothing</li>
                <li>Move, click, scroll, drag &mdash; all hands-free</li>
                <li>Full data collection + training pipeline</li>
            </ul>
            <a href="https://github.com/Kenk26/HandGestureSystemControl.git" target="_blank" class="card-link">&#128279; View on GitHub</a>
        </div>
        <div class="project-card" style="--accent:#00c8b4">
            <span class="project-icon">📄</span>
            <div class="project-title">DocMind AI &mdash; RAG Q&amp;A</div>
            <p class="project-desc">Upload any document and ask questions about it. Fully local, privacy-first RAG pipeline.</p>
            <div class="tag-row">
                <span class="tag">Python</span>
                <span class="tag">LangChain</span>
                <span class="tag">ChromaDB</span>
                <span class="tag">Ollama</span>
                <span class="tag">Tkinter</span>
            </div>
            <ul class="feature-list">
                <li>Supports PDF, DOCX, TXT, CSV, Markdown</li>
                <li>Hot-swappable LLM models (llama3, mistral...)</li>
                <li>Source attribution on every answer</li>
                <li>Adjustable chunking &amp; retrieval settings</li>
            </ul>
            <a href="https://github.com/Kenk26/DocuMind_AI" target="_blank" class="card-link">&#128279; View on GitHub</a>
        </div>
        <div class="project-card" style="--accent:#ff5470">
            <span class="project-icon">🛡️</span>
            <div class="project-title">Face Recognition Security</div>
            <p class="project-desc">Real-time face recognition security system with live webcam feed and full access logging.</p>
            <div class="tag-row">
                <span class="tag">Python</span>
                <span class="tag">OpenCV</span>
                <span class="tag">LBPH</span>
                <span class="tag">Tkinter</span>
            </div>
            <ul class="feature-list">
                <li>Register multiple users with live face capture</li>
                <li>Confidence-scored GRANTED / DENIED access</li>
                <li>Timestamped access log viewer</li>
                <li>Dark-themed professional GUI</li>
            </ul>
            <a href="https://github.com/Kenk26/FaceRecognitionSystem" target="_blank" class="card-link">&#128279; View on GitHub</a>
        </div>
        <div class="project-card" style="--accent:#f5a623">
            <span class="project-icon">🧩</span>
            <div class="project-title">Crossword Puzzle Game</div>
            <p class="project-desc">A feature-rich desktop crossword game with a custom word engine, built entirely in C with GTK4.</p>
            <div class="tag-row">
                <span class="tag">C</span>
                <span class="tag">GTK4</span>
                <span class="tag">Trie</span>
                <span class="tag">Data Structures</span>
            </div>
            <ul class="feature-list">
                <li>Trie data structure for fast word lookup</li>
                <li>Teacher / Student role-based UI</li>
                <li>Dynamic crossword grid generation</li>
                <li>Persistent word &amp; hint database</li>
            </ul>
            <a href="https://github.com/Kenk26/CrossWord" target="_blank" class="card-link">&#128279; View on GitHub</a>
        </div>
        <div class="project-card" style="--accent:#633cff">
            <span class="project-icon">🎙️</span>
            <div class="project-title">Voice Assistant</div>
            <p class="project-desc">A desktop voice assistant that listens to commands and responds with natural synthesized speech.</p>
            <div class="tag-row">
                <span class="tag">Python</span>
                <span class="tag">SpeechRecognition</span>
                <span class="tag">pyttsx3</span>
                <span class="tag">Tkinter</span>
            </div>
            <ul class="feature-list">
                <li>Google STT + offline pyttsx3 TTS</li>
                <li>Continuous &amp; single-shot listening modes</li>
                <li>Ambient noise calibration</li>
                <li>Female voice preference selection</li>
            </ul>
            <a href="https://github.com/Kenk26/VoiceAssistant" target="_blank" class="card-link">&#128279; View on GitHub</a>
        </div>
        <div class="project-card" style="--accent:#00c8b4">
            <span class="project-icon">🔢</span>
            <div class="project-title">Sudoku Game</div>
            <p class="project-desc">A polished browser-based Sudoku with dark mode, save/continue, and animated error feedback.</p>
            <div class="tag-row">
                <span class="tag">JavaScript</span>
                <span class="tag">HTML</span>
                <span class="tag">CSS</span>
            </div>
            <ul class="feature-list">
                <li>3 difficulty levels with backtracking generator</li>
                <li>Dark / light mode toggle</li>
                <li>Save &amp; continue via localStorage</li>
                <li>Animated cell error highlighting</li>
            </ul>
            <a href="https://github.com/Kenk26/Sudoku" target="_blank" class="card-link">&#128279; View on GitHub</a>
        </div>
        <div class="project-card" style="--accent:#ff5470">
            <span class="project-icon">🌐</span>
            <div class="project-title">Custom New Tab Page</div>
            <p class="project-desc">A personal browser dashboard with a video background, live clock, and animated sidebar.</p>
            <div class="tag-row">
                <span class="tag">HTML</span>
                <span class="tag">CSS</span>
                <span class="tag">JavaScript</span>
            </div>
            <ul class="feature-list">
                <li>Animated video background</li>
                <li>Live digital clock with date</li>
                <li>Quick-access shortcut tile grid</li>
                <li>Slide-out sidebar with Google apps</li>
            </ul>
            <a href="https://github.com/Kenk26/HomePage" target="_blank" class="card-link">&#128279; View on GitHub</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
    <div class="section-label">// Skills & Stack</div>
    <div class="section-title">Tools I Work With</div>
    <p class="section-sub">Technologies I use to build things from scratch.</p>
    <div class="skills-grid">
        <div class="skill-category">
            <div class="skill-cat-title">Languages</div>
            <div class="skill-pills">
                <span class="skill-pill">Python</span>
                <span class="skill-pill">C</span>
                <span class="skill-pill">JavaScript</span>
                <span class="skill-pill">HTML</span>
                <span class="skill-pill">CSS</span>
            </div>
        </div>
        <div class="skill-category">
            <div class="skill-cat-title">AI / ML</div>
            <div class="skill-pills">
                <span class="skill-pill">TensorFlow</span>
                <span class="skill-pill">MediaPipe</span>
                <span class="skill-pill">OpenCV</span>
                <span class="skill-pill">LangChain</span>
                <span class="skill-pill">ChromaDB</span>
                <span class="skill-pill">Ollama</span>
            </div>
        </div>
        <div class="skill-category">
            <div class="skill-cat-title">GUI / Frontend</div>
            <div class="skill-pills">
                <span class="skill-pill">Tkinter</span>
                <span class="skill-pill">GTK4</span>
                <span class="skill-pill">Streamlit</span>
                <span class="skill-pill">Vanilla JS</span>
            </div>
        </div>
        <div class="skill-category">
            <div class="skill-cat-title">Libraries & Tools</div>
            <div class="skill-pills">
                <span class="skill-pill">PyAutoGUI</span>
                <span class="skill-pill">pyttsx3</span>
                <span class="skill-pill">SpeechRecognition</span>
                <span class="skill-pill">NumPy</span>
                <span class="skill-pill">Pickle</span>
                <span class="skill-pill">Git</span>
            </div>
        </div>
        <div class="skill-category">
            <div class="skill-cat-title">Concepts</div>
            <div class="skill-pills">
                <span class="skill-pill">RAG Pipelines</span>
                <span class="skill-pill">Computer Vision</span>
                <span class="skill-pill">Trie / DSA</span>
                <span class="skill-pill">Multithreading</span>
                <span class="skill-pill">Vector DBs</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap-alt">
    <div class="contact-card">
        <div class="section-label" style="text-align:center">// Contact</div>
        <div class="section-title" style="text-align:center">Let&#39;s Connect</div>
        <p style="font-size:1rem;line-height:1.75;color:rgba(232,232,240,0.55);text-align:center;">
            Have a project in mind or just want to say hi? 
            Reach out on any of the platforms below.
        </p>
        <div class="contact-links">
            <a class="contact-link" href="https://www.instagram.com/_.ken_k_/" target="_blank">
                📸 Instagram
            </a>
            <a class="contact-link" href="https://discord.com/invite/QzeZ3haT" target="_blank">
                💬 Discord
            </a>
            <a class="contact-link" href="https://www.linkedin.com/in/ankit-kumar-10o26/" target="_blank">
                👤 LinkedIn
            </a>
            <a class="contact-link" href="mailto:ankitmukesh2003@gmail.com" target="_blank">
                ✉️ Main Me
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    <div class="footer-copy">😉Ankit Kumar.</div>
    <div class="footer-made">Built with <span>♥</span> using Streamlit & Python</div>
</div>
""", unsafe_allow_html=True)