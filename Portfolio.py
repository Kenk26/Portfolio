import streamlit as st
import base64, os

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ankit Kumar | Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Load External CSS ─────────────────────────────────────────────────────────
def load_css(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"CSS file not found: {path}")

# Place styles.css next to portfolio.py
load_css("styles.css")

# ── Drag-to-scroll JS for project row ────────────────────────────────────────
st.markdown("""
<script>
(function() {
    function enableDragScroll() {
        const el = document.querySelector('.projects-grid');
        if (!el) { setTimeout(enableDragScroll, 300); return; }
        let isDown = false, startX, scrollLeft;
        el.addEventListener('mousedown', e => {
            isDown = true; el.classList.add('active');
            startX = e.pageX - el.offsetLeft;
            scrollLeft = el.scrollLeft;
        });
        el.addEventListener('mouseleave', () => { isDown = false; el.classList.remove('active'); });
        el.addEventListener('mouseup',    () => { isDown = false; el.classList.remove('active'); });
        el.addEventListener('mousemove',  e => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - el.offsetLeft;
            el.scrollLeft = scrollLeft - (x - startX) * 1.5;
        });
    }
    document.addEventListener('DOMContentLoaded', enableDragScroll);
    setTimeout(enableDragScroll, 800);
})();
</script>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# HELPERS
# ══════════════════════════════════════════════════════════════
def get_img_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        ext = path.rsplit(".", 1)[-1].lower().replace("jpg", "jpeg")
        return f"data:image/{ext};base64,{data}"
    return None


# ══════════════════════════════════════════════════════════════
# NAV
# ══════════════════════════════════════════════════════════════
LOGO_IMAGE = "logo.png"
logo_src   = get_img_base64(LOGO_IMAGE)
logo_html  = (f'<img src="{logo_src}" alt="Logo" style="height:38px;object-fit:contain;border-radius:50%;">'
              if logo_src else '<span class="nav-logo">AK.dev</span>')

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
PROFILE_IMAGE = "profile.jpg"
img_src       = get_img_base64(PROFILE_IMAGE)

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
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
    <div class="section-label">// About Me</div>
    <div class="section-title">Who I Am</div>
    <p class="section-sub">I&#39;m a self-driven developer passionate about building creative, real-world projects. I love combining machine learning, computer vision, and clean UI to create software that actually works and feels great to use.</p>
    <p style="font-size:1.2rem;line-height:1.8;color:rgba(232,232,240,0.6);max-width:640px;">
        My projects span multiple domains &mdash; desktop GUI apps in C and Python, AI-powered document tools,
        real-time gesture controllers, face recognition security systems, and polished web games.
        I&#39;m always learning, always building.<br><br>
        When I&#39;m not coding, I&#39;m diving into Games, Anime, Manga, and anything that inspires creative thinking.
    </p>
    <div class="stats-row">
        <div class="stat-item"><div class="stat-num">7+</div><div class="stat-label">Projects Built</div></div>
        <div class="stat-item"><div class="stat-num">5+</div><div class="stat-label">Languages Used</div></div>
        <div class="stat-item"><div class="stat-num">4</div><div class="stat-label">AI/ML Projects</div></div>
        <div class="stat-item"><div class="stat-num">&#8734;</div><div class="stat-label">Ideas in Progress</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PROJECTS  ← horizontal scroll row
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap-alt">
    <div class="section-label">// Projects</div>
    <div class="section-title">What I&#39;ve Built</div>
    <p class="section-sub">A collection of projects across AI, computer vision, games, and web. Scroll right to explore →</p>
    <div class="projects-scroll-wrapper">
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
            <div class="project-card" style="--accent:#7c3aed">
                <span class="project-icon">🎙️</span>
                <div class="project-title">VoiceFlow — AI Voice Assistant</div>
                <p class="project-desc">A local AI-powered voice assistant with a tool-calling agent loop. Speaks commands aloud, transcribes your voice, and dispatches real system actions — entirely on-device.</p>
                <div class="tag-row">
                    <span class="tag">Python</span>
                    <span class="tag">LangChain</span>
                    <span class="tag">Ollama</span>
                    <span class="tag">Tkinter</span>
                </div>
                <ul class="feature-list">
                    <li>Opens websites, launches apps, searches Google/YouTube via voice</li>
                    <li>Continuous or single-shot listening with noise calibration</li>
                    <li>Offline TTS via pyttsx3 with voice preference selection</li>
                    <li>Hot-swappable Ollama models at runtime</li>
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
                <p class="project-desc">A personal browser dashboard with video background, live clock, animated sidebar, and Trie-powered search autocomplete.</p>
                <div class="tag-row">
                    <span class="tag">HTML</span>
                    <span class="tag">CSS</span>
                    <span class="tag">JavaScript</span>
                    <span class="tag">Trie / DSA</span>
                </div>
                <ul class="feature-list">
                    <li>Trie-based search autocomplete with 400+ seeded queries</li>
                    <li>Animated video background</li>
                    <li>Live digital clock with date</li>
                    <li>Quick-access shortcut tile grid</li>
                    <li>Slide-out sidebar with Google apps</li>
                </ul>
                <a href="https://github.com/Kenk26/HomePage" target="_blank" class="card-link">&#128279; View on GitHub</a>
            </div>
            <div class="project-card" style="--accent:#e94560">
                <span class="project-icon">🛡️</span>
                <div class="project-title">AI SecureVault</div>
                <p class="project-desc">A desktop security app combining face recognition, liveness detection, and AES file encryption. Vault keys are derived via PBKDF2 and never stored on disk.</p>
                <div class="tag-row">
                    <span class="tag">Python</span>
                    <span class="tag">PyQt5</span>
                    <span class="tag">face_recognition</span>
                    <span class="tag">Cryptography</span>
                    <span class="tag">SQLite</span>
                </div>
                <ul class="feature-list">
                    <li>Face recognition with eye-blink liveness detection</li>
                    <li>AES-128 Fernet encryption with session-bound in-memory key</li>
                    <li>Intruder capture — unknown faces photographed and logged</li>
                    <li>bcrypt password fallback with configurable lockout</li>
                    <li>Full SQLite audit trail for auth and encryption events</li>
                </ul>
                <a href="https://github.com/Kenk26/AI-SecureVault" target="_blank" class="card-link">&#128279; View on GitHub</a>
            </div>
            <div class="project-card" style="--accent:#e94560">
                <span class="project-icon">🤟</span>
                <div class="project-title">Sign Language to Speech System</div>
                <p class="project-desc">A real-time sign language recognition pipeline that captures hand gestures via webcam, classifies them using an LSTM model, and converts them into spoken natural English sentences with emotion-aware tone.</p>
                <div class="tag-row">
                    <span class="tag">Python</span>
                    <span class="tag">MediaPipe</span>
                    <span class="tag">TensorFlow</span>
                    <span class="tag">LangChain</span>
                    <span class="tag">Ollama</span>
                    <span class="tag">PyQt5</span>
                    <span class="tag">pyttsx3</span>
                </div>
                <ul class="feature-list">
                    <li>Dual-hand landmark extraction (126-dim vectors) via MediaPipe Tasks API</li>
                    <li>Facial emotion detection integrated into sentence tone</li>
                    <li>LSTM classifier trained on custom-collected 30-frame gesture sequences</li>
                    <li>LLM-powered grammar correction via LangChain + Ollama (Gemma)</li>
                    <li>Full pipeline: data collection → preprocessing → training → live inference</li>
                </ul>
                <a href="https://github.com/Kenk26/Real-Time-Sign-Language-to-Speech-System.git" target="_blank" class="card-link">&#128279; View on GitHub</a>
            </div>
        </div><!-- /.projects-grid -->
    </div><!-- /.projects-scroll-wrapper -->
</div>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════════
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-wrap">
    <div class="section-label">// Skills &amp; Stack</div>
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
                <span class="skill-pill">face_recognition</span>
                <span class="skill-pill">dlib</span>
            </div>
        </div>
        <div class="skill-category">
            <div class="skill-cat-title">GUI / Frontend</div>
            <div class="skill-pills">
                <span class="skill-pill">Tkinter</span>
                <span class="skill-pill">GTK4</span>
                <span class="skill-pill">Streamlit</span>
                <span class="skill-pill">Vanilla JS</span>
                <span class="skill-pill">PyQt5</span>
            </div>
        </div>
        <div class="skill-category">
            <div class="skill-cat-title">Libraries &amp; Tools</div>
            <div class="skill-pills">
                <span class="skill-pill">PyAutoGUI</span>
                <span class="skill-pill">pyttsx3</span>
                <span class="skill-pill">SpeechRecognition</span>
                <span class="skill-pill">NumPy</span>
                <span class="skill-pill">Pickle</span>
                <span class="skill-pill">Git</span>
                <span class="skill-pill">bcrypt</span>
                <span class="skill-pill">cryptography</span>
                <span class="skill-pill">scipy</span>
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
            <a class="contact-link" href="https://www.instagram.com/_.ken_k_/" target="_blank">📸 Instagram</a>
            <a class="contact-link" href="https://discord.com/invite/QzeZ3haT" target="_blank">💬 Discord</a>
            <a class="contact-link" href="https://www.linkedin.com/in/ankit-kumar-10o26/" target="_blank">👤 LinkedIn</a>
            <a class="contact-link" href="mailto:ankitmukesh2003@gmail.com" target="_blank">✉️ Send Mail</a>
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
    <div class="footer-made">Built with <span>♥</span> using Streamlit &amp; Python</div>
</div>
""", unsafe_allow_html=True)