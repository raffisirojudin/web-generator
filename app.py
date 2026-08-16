import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Web Generator", page_icon="🌐", layout="wide")

st.title("🌐 Web Generator")
st.caption("Pilih template komponen UI modern di bawah ini, kustomisasi kodenya, dan lihat hasil *Live Preview* secara instan.")

# ==============================================================================
# DATABASE TEMPLATE KOMPONEN KEPERLUAN WEB MODERN
# ==============================================================================
templates = {
    "🌐 Navigasi & Header": {
        "Responsive Navbar + Mobile Menu": {
            "html": """<nav class="navbar">
  <div class="logo">BrandName</div>
  <ul class="nav-links" id="navLinks">
    <li><a href="#">Beranda</a></li>
    <li><a href="#">Fitur</a></li>
    <li><a href="#">Harga</a></li>
    <li><a href="#" class="btn-nav">Mulai</a></li>
  </ul>
  <button class="menu-btn" id="menuBtn">☰</button>
</nav>""",
            "css": """* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', sans-serif; background: #ffffff; }

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #0f172a;
  padding: 16px 32px;
  color: white;
}
.logo { font-size: 20px; font-weight: bold; color: #38bdf8; }
.nav-links { display: flex; list-style: none; gap: 24px; align-items: center; }
.nav-links a { color: #94a3b8; text-decoration: none; transition: 0.2s; }
.nav-links a:hover { color: white; }
.btn-nav { background: #0284c7; color: white !important; padding: 8px 16px; border-radius: 6px; }
.menu-btn { display: none; background: none; border: none; color: white; font-size: 24px; cursor: pointer; }

@media (max-width: 640px) {
  .menu-btn { display: block; }
  .nav-links {
    display: none;
    flex-direction: column;
    position: absolute;
    top: 60px; right: 0; left: 0;
    background: #0f172a; padding: 20px; text-align: center;
  }
  .nav-links.active { display: flex; }
}""",
            "js": """const menuBtn = document.getElementById('menuBtn');
const navLinks = document.getElementById('navLinks');

if(menuBtn) {
  menuBtn.addEventListener('click', () => {
    navLinks.classList.toggle('active');
  });
}"""
        }
    },

    "✨ Hero & Banner": {
        "Modern SaaS Hero Section": {
            "html": """<section class="hero">
  <div class="badge">🚀 Versi 2.0 Telah Rilis</div>
  <h1>Bangun Aplikasi Web 10x Lebih Cepat</h1>
  <p>Platform utilitas siap pakai untuk mempercepat workflow pengembangan aplikasi web modern Anda.</p>
  <div class="cta-group">
    <button class="btn-primary">Coba Gratis</button>
    <button class="btn-secondary">Lihat Dokumentasi</button>
  </div>
</section>""",
            "css": """body { font-family: system-ui, sans-serif; background: #090d16; color: white; text-align: center; margin: 0; }

.hero { padding: 40px 20px; max-width: 800px; margin: 0 auto; }
.badge {
  display: inline-block; background: rgba(56, 189, 248, 0.1);
  color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3);
  padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 20px;
}
.hero h1 { font-size: 32px; font-weight: 800; line-height: 1.2; margin-bottom: 16px; color: #ffffff; }
.hero p { color: #94a3b8; font-size: 15px; margin-bottom: 24px; line-height: 1.6; }
.cta-group { display: flex; gap: 12px; justify-content: center; }
.btn-primary { background: #2563eb; color: white; border: none; padding: 10px 20px; font-size: 14px; font-weight: 600; border-radius: 8px; cursor: pointer; transition: 0.2s; }
.btn-primary:hover { background: #1d4ed8; }
.btn-secondary { background: #1e293b; color: #e2e8f0; border: 1px solid #334155; padding: 10px 20px; font-size: 14px; border-radius: 8px; cursor: pointer; transition: 0.2s; }
.btn-secondary:hover { background: #334155; }""",
            "js": ""
        }
    },

    "💳 Card & Layout": {
        "Pricing Plan Card": {
            "html": """<div class="card-pricing">
  <span class="popular-tag">Paling Populer</span>
  <h3>Pro Plan</h3>
  <div class="price">Rp 199k <span>/bulan</span></div>
  <ul class="features">
    <li>✓ Akses Semua Modul</li>
    <li>✓ Unlimited Project</li>
    <li>✓ Support 24/7</li>
  </ul>
  <button class="btn-card">Pilih Paket Pro</button>
</div>""",
            "css": """body { font-family: sans-serif; background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }

.card-pricing {
  background: white; border-radius: 16px; padding: 28px; width: 280px;
  box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1); border: 2px solid #2563eb; position: relative;
}
.popular-tag {
  position: absolute; top: -12px; right: 20px; background: #2563eb;
  color: white; font-size: 11px; font-weight: bold; padding: 4px 10px; border-radius: 12px;
}
.card-pricing h3 { font-size: 20px; margin-bottom: 8px; color: #0f172a; margin-top: 0; }
.price { font-size: 28px; font-weight: 800; color: #0f172a; margin-bottom: 16px; }
.price span { font-size: 13px; color: #64748b; font-weight: normal; }
.features { list-style: none; padding: 0; margin-bottom: 20px; color: #334155; line-height: 1.8; font-size: 14px; }
.btn-card {
  width: 100%; background: #2563eb; color: white; border: none;
  padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.2s;
}
.btn-card:hover { background: #1d4ed8; }""",
            "js": ""
        }
    },

    "⚡ Modal & Popup": {
        "Interactive Modal Dialog": {
            "html": """<button id="openModal" class="btn-open">Buka Modal Window</button>

<div class="modal-overlay" id="modalOverlay">
  <div class="modal-content">
    <h3>Konfirmasi Tindakan</h3>
    <p>Apakah Anda yakin ingin menyimpan perubahan pada konfigurasi ini?</p>
    <div class="modal-actions">
      <button id="closeModal" class="btn-cancel">Batal</button>
      <button class="btn-confirm">Ya, Simpan</button>
    </div>
  </div>
</div>""",
            "css": """body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background: #f8fafc; }

.btn-open { background: #0f172a; color: white; border: none; padding: 12px 20px; border-radius: 8px; cursor: pointer; font-size: 14px; }

.modal-overlay {
  display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(4px);
  justify-content: center; align-items: center;
}
.modal-overlay.active { display: flex; }

.modal-content { background: white; padding: 20px; border-radius: 12px; width: 300px; box-shadow: 0 20px 25px -5px rgba(0,0,0,0.2); }
.modal-content h3 { margin-bottom: 8px; color: #0f172a; margin-top: 0; font-size: 18px; }
.modal-content p { color: #64748b; font-size: 13px; margin-bottom: 16px; line-height: 1.5; }
.modal-actions { display: flex; justify-content: flex-end; gap: 8px; }
.btn-cancel { background: #e2e8f0; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; font-size: 13px; }
.btn-confirm { background: #16a34a; color: white; border: none; padding: 8px 14px; border-radius: 6px; cursor: pointer; font-size: 13px; }""",
            "js": """const openModal = document.getElementById('openModal');
const closeModal = document.getElementById('closeModal');
const modalOverlay = document.getElementById('modalOverlay');

if(openModal && closeModal && modalOverlay) {
  openModal.addEventListener('click', () => modalOverlay.classList.add('active'));
  closeModal.addEventListener('click', () => modalOverlay.classList.remove('active'));
  modalOverlay.addEventListener('click', (e) => {
    if(e.target === modalOverlay) modalOverlay.classList.remove('active');
  });
}"""
        }
    },

    "🔔 Notifikasi & UI Feedback": {
        "Toast Alert System": {
            "html": """<button id="showToastBtn" class="btn-toast">Tampilkan Notifikasi Toast</button>
<div id="toastContainer" class="toast-container"></div>""",
            "css": """body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background: #f8fafc; }

.btn-toast { background: #16a34a; color: white; border: none; padding: 12px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; }

.toast-container { position: fixed; bottom: 20px; right: 20px; display: flex; flex-direction: column; gap: 10px; }
.toast {
  background: #0f172a; color: white; padding: 12px 20px; border-left: 4px solid #38bdf8;
  border-radius: 6px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); font-size: 14px;
  animation: slideIn 0.3s ease;
}

@keyframes slideIn { from { transform: translateX(100%); } to { transform: translateX(0); } }""",
            "js": """const btn = document.getElementById('showToastBtn');
const container = document.getElementById('toastContainer');

if(btn && container) {
  btn.addEventListener('click', () => {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerText = '✅ Perubahan berhasil disimpan!';
    container.appendChild(toast);

    setTimeout(() => {
      toast.remove();
    }, 3000);
  });
}"""
        }
    }
}

# ==============================================================================
# MENU PEMILIHAN TERBUKA DI HALAMAN UTAMA
# ==============================================================================
st.markdown("#### 📌 Step 1: Pilih Kategori UI")
category = st.radio(
    "Kategori",
    options=list(templates.keys()),
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("#### 📌 Step 2: Pilih Komponen")
selected_component_name = st.radio(
    "Komponen",
    options=list(templates[category].keys()),
    horizontal=True,
    label_visibility="collapsed"
)

selected_data = templates[category][selected_component_name]

st.divider()

# ==============================================================================
# WORKSPACE: SYNTAX EDITOR & LIVE PREVIEW
# ==============================================================================
col_code, col_preview = st.columns([1, 1])

with col_code:
    st.subheader("📝 Syntax Editor")
    html_code = st.text_area("HTML Syntax:", value=selected_data["html"], height=140)
    css_code = st.text_area("CSS Syntax:", value=selected_data["css"], height=200)
    js_code = st.text_area("JavaScript Syntax:", value=selected_data["js"], height=120)

with col_preview:
    st.subheader("👁️ Live Preview")
    
    # Menyiapkan dokumen HTML lengkap untuk Iframe
    full_preview_html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    {css_code}
  </style>
</head>
<body>
  {html_code}
  <script>
    {js_code}
  </script>
</body>
</html>"""
    
    # Render menggunakan komponen resmi Streamlit Iframe
    components.html(full_preview_html, height=450, scrolling=True)

st.divider()

# ==============================================================================
# TAB KODE SIAP SALIN (COPY-PASTE)
# ==============================================================================
st.markdown("### 📋 Salin Kode Siap Pakai")
tab_html, tab_css, tab_js = st.tabs(["HTML Code", "CSS Code", "JavaScript Code"])

with tab_html:
    st.code(html_code, language="html")
with tab_css:
    st.code(css_code, language="css")
with tab_js:
    st.code(js_code, language="javascript")
