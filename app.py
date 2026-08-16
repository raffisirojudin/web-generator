import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Web Generator", page_icon="🌐", layout="wide")

st.title("🌐 Web Generator")
st.caption("Pilih template komponen UI modern di bawah ini, kustomisasi kodenya, dan lihat hasil *Live Preview* secara instan.")

# ==============================================================================
# DATABASE TEMPLATE KOMPONEN (MUDAH DITAMBAH VARIANT BARU)
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
.navbar { display: flex; justify-content: space-between; align-items: center; background: #0f172a; padding: 16px 32px; color: white; }
.logo { font-size: 20px; font-weight: bold; color: #38bdf8; }
.nav-links { display: flex; list-style: none; gap: 24px; align-items: center; }
.nav-links a { color: #94a3b8; text-decoration: none; transition: 0.2s; }
.nav-links a:hover { color: white; }
.btn-nav { background: #0284c7; color: white !important; padding: 8px 16px; border-radius: 6px; }
.menu-btn { display: none; background: none; border: none; color: white; font-size: 24px; cursor: pointer; }

@media (max-width: 640px) {
  .menu-btn { display: block; }
  .nav-links { display: none; flex-direction: column; position: absolute; top: 60px; right: 0; left: 0; background: #0f172a; padding: 20px; text-align: center; }
  .nav-links.active { display: flex; }
}""",
            "js": """const menuBtn = document.getElementById('menuBtn');
const navLinks = document.getElementById('navLinks');
if(menuBtn) { menuBtn.addEventListener('click', () => navLinks.classList.toggle('active')); }"""
        },
        "Vertical Dashboard Sidebar": {
            "html": """<aside class="sidebar">
  <div class="brand">⚡ AdminDash</div>
  <ul class="menu-list">
    <li class="active">📊 Overview</li>
    <li>📦 Produk</li>
    <li>👥 Pelanggan</li>
    <li>⚙️ Pengaturan</li>
  </ul>
</aside>""",
            "css": """body { font-family: sans-serif; margin: 0; background: #f8fafc; }
.sidebar { width: 220px; height: 100vh; background: #1e293b; color: white; padding: 20px; box-sizing: border-box; }
.brand { font-weight: bold; font-size: 18px; margin-bottom: 30px; color: #38bdf8; }
.menu-list { list-style: none; padding: 0; margin: 0; }
.menu-list li { padding: 12px 16px; border-radius: 8px; margin-bottom: 6px; color: #94a3b8; cursor: pointer; transition: 0.2s; font-size: 14px; }
.menu-list li:hover, .menu-list li.active { background: #334155; color: white; font-weight: 600; }""",
            "js": ""
        },
        "Footer dengan Kolom Multi-Link": {
            "html": """<footer class="footer">
  <div class="footer-col">
    <h4>Perusahaan</h4>
    <a href="#">Tentang Kami</a>
    <a href="#">Karir</a>
  </div>
  <div class="footer-col">
    <h4>Dukungan</h4>
    <a href="#">Pusat Bantuan</a>
    <a href="#">Kontak</a>
  </div>
  <div class="footer-bottom">
    <p>© 2026 WebGenerator. All rights reserved.</p>
  </div>
</footer>""",
            "css": """body { font-family: sans-serif; margin: 0; background: #f1f5f9; display: flex; align-items: flex-end; min-height: 100vh; }
.footer { background: #0f172a; color: #94a3b8; padding: 32px; width: 100%; box-sizing: border-box; display: flex; flex-wrap: wrap; gap: 40px; }
.footer-col h4 { color: white; margin-bottom: 12px; font-size: 15px; }
.footer-col a { display: block; color: #94a3b8; text-decoration: none; margin-bottom: 8px; font-size: 13px; }
.footer-col a:hover { color: white; }
.footer-bottom { border-top: 1px solid #1e293b; padding-top: 16px; width: 100%; text-align: center; font-size: 12px; }""",
            "js": ""
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
.badge { display: inline-block; background: rgba(56, 189, 248, 0.1); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 20px; }
.hero h1 { font-size: 32px; font-weight: 800; line-height: 1.2; margin-bottom: 16px; color: #ffffff; }
.hero p { color: #94a3b8; font-size: 15px; margin-bottom: 24px; line-height: 1.6; }
.cta-group { display: flex; gap: 12px; justify-content: center; }
.btn-primary { background: #2563eb; color: white; border: none; padding: 10px 20px; font-size: 14px; font-weight: 600; border-radius: 8px; cursor: pointer; }
.btn-secondary { background: #1e293b; color: #e2e8f0; border: 1px solid #334155; padding: 10px 20px; font-size: 14px; border-radius: 8px; cursor: pointer; }""",
            "js": ""
        },
        "Feature Grid (3 Kolom)": {
            "html": """<div class="grid-container">
  <div class="feature-card">
    <div class="icon">🚀</div>
    <h3>Performa Cepat</h3>
    <p>Dioptimalkan untuk kecepatan dan efisiensi memori tinggi.</p>
  </div>
  <div class="feature-card">
    <div class="icon">🔒</div>
    <h3>Aman Terjamin</h3>
    <p>Dilengkapi proteksi keamanan sesuai standar industri.</p>
  </div>
  <div class="feature-card">
    <div class="icon">🎨</div>
    <h3>Mudah Dikustom</h3>
    <p>Komponen fleksibel yang mudah disesuaikan dengan brand.</p>
  </div>
</div>""",
            "css": """body { font-family: sans-serif; background: #f8fafc; padding: 40px 20px; margin: 0; }
.grid-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; max-width: 900px; margin: 0 auto; }
.feature-card { background: white; padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; transition: 0.3s; }
.feature-card:hover { transform: translateY(-4px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
.icon { font-size: 28px; margin-bottom: 12px; }
.feature-card h3 { font-size: 18px; margin-bottom: 8px; color: #0f172a; }
.feature-card p { font-size: 13px; color: #64748b; line-height: 1.5; margin: 0; }""",
            "js": ""
        },
        "Stat Counter Banner": {
            "html": """<div class="stats-banner">
  <div class="stat-item"><h2>10M+</h2><p>Pengguna Aktif</p></div>
  <div class="stat-item"><h2>99.9%</h2><p>Uptime Server</p></div>
  <div class="stat-item"><h2>24/7</h2><p>Dukungan Tim</p></div>
</div>""",
            "css": """body { font-family: sans-serif; background: #0f172a; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
.stats-banner { display: flex; gap: 40px; text-align: center; background: #1e293b; padding: 24px 40px; border-radius: 16px; border: 1px solid #334155; }
.stat-item h2 { color: #38bdf8; font-size: 28px; margin: 0; font-weight: 800; }
.stat-item p { color: #94a3b8; font-size: 13px; margin: 4px 0 0; }""",
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
.card-pricing { background: white; border-radius: 16px; padding: 28px; width: 280px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1); border: 2px solid #2563eb; position: relative; }
.popular-tag { position: absolute; top: -12px; right: 20px; background: #2563eb; color: white; font-size: 11px; font-weight: bold; padding: 4px 10px; border-radius: 12px; }
.card-pricing h3 { font-size: 20px; margin-bottom: 8px; color: #0f172a; margin-top: 0; }
.price { font-size: 28px; font-weight: 800; color: #0f172a; margin-bottom: 16px; }
.price span { font-size: 13px; color: #64748b; font-weight: normal; }
.features { list-style: none; padding: 0; margin-bottom: 20px; color: #334155; line-height: 1.8; font-size: 14px; }
.btn-card { width: 100%; background: #2563eb; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; }""",
            "js": ""
        },
        "E-Commerce Product Card": {
            "html": """<div class="product-card">
  <div class="img-placeholder">🎧 Product Image</div>
  <div class="product-info">
    <span class="category">Electronics</span>
    <h4>Wireless Headphones</h4>
    <div class="price-row">
      <span class="price">Rp 850.000</span>
      <button class="add-btn">+</button>
    </div>
  </div>
</div>""",
            "css": """body { font-family: sans-serif; background: #f8fafc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
.product-card { background: white; border-radius: 12px; width: 240px; overflow: hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; }
.img-placeholder { background: #e2e8f0; height: 140px; display: flex; justify-content: center; align-items: center; color: #64748b; font-weight: bold; font-size: 14px; }
.product-info { padding: 16px; }
.category { font-size: 11px; color: #2563eb; font-weight: bold; text-transform: uppercase; }
.product-info h4 { margin: 4px 0 12px; font-size: 16px; color: #0f172a; }
.price-row { display: flex; justify-content: space-between; align-items: center; }
.price { font-weight: 800; color: #0f172a; font-size: 15px; }
.add-btn { background: #0f172a; color: white; border: none; width: 32px; height: 32px; border-radius: 6px; cursor: pointer; font-size: 18px; font-weight: bold; }""",
            "js": ""
        },
        "User Profile Card": {
            "html": """<div class="profile-card">
  <div class="avatar">👨‍💻</div>
  <h3>Alex Rivera</h3>
  <p class="title">Senior Web Developer</p>
  <div class="stats">
    <div><b>124</b><span>Proyek</span></div>
    <div><b>12.5k</b><span>Followers</span></div>
  </div>
  <button class="btn-follow">Ikuti</button>
</div>""",
            "css": """body { font-family: sans-serif; background: #e2e8f0; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
.profile-card { background: white; padding: 24px; border-radius: 16px; text-align: center; width: 220px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
.avatar { font-size: 40px; background: #f1f5f9; width: 70px; height: 70px; line-height: 70px; border-radius: 50%; margin: 0 auto 12px; }
.profile-card h3 { margin: 0; font-size: 18px; color: #0f172a; }
.title { color: #64748b; font-size: 12px; margin: 4px 0 16px; }
.stats { display: flex; justify-content: space-around; margin-bottom: 20px; border-top: 1px solid #f1f5f9; padding-top: 12px; }
.stats b { display: block; font-size: 14px; color: #0f172a; }
.stats span { font-size: 11px; color: #94a3b8; }
.btn-follow { background: #0284c7; color: white; border: none; width: 100%; padding: 8px; border-radius: 8px; font-weight: bold; cursor: pointer; }""",
            "js": ""
        },
        "Testimonial Review Card": {
            "html": """<div class="testimonial-card">
  <div class="stars">⭐⭐⭐⭐⭐</div>
  <p>"Template ini sangat membantu mempercepat pembuatan landing page kami!"</p>
  <div class="user-info">
    <strong>Budi Pratama</strong>
    <span>Product Designer</span>
  </div>
</div>""",
            "css": """body { font-family: sans-serif; background: #f8fafc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
.testimonial-card { background: white; padding: 24px; border-radius: 12px; width: 280px; box-shadow: 0 4px 12px rgba(0,0,0,0.06); border: 1px solid #e2e8f0; }
.stars { font-size: 14px; margin-bottom: 12px; }
.testimonial-card p { font-size: 13px; color: #334155; line-height: 1.6; font-style: italic; margin-bottom: 16px; }
.user-info strong { display: block; font-size: 14px; color: #0f172a; }
.user-info span { font-size: 12px; color: #94a3b8; }""",
            "js": ""
        }
    },

    "📝 Form & Input": {
        "Clean Sign-In Form": {
            "html": """<form class="login-form">
  <h2>Masuk Akun</h2>
  <div class="input-group">
    <label>Email</label>
    <input type="email" placeholder="nama@email.com" required>
  </div>
  <div class="input-group">
    <label>Kata Sandi</label>
    <input type="password" placeholder="••••••••" required>
  </div>
  <button type="button" class="btn-submit">Masuk Sekarang</button>
</form>""",
            "css": """body { font-family: sans-serif; background: #f1f5f9; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
.login-form { background: white; padding: 32px; border-radius: 16px; width: 280px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.08); }
.login-form h2 { margin-top: 0; font-size: 20px; color: #0f172a; margin-bottom: 20px; text-align: center; }
.input-group { margin-bottom: 16px; }
.input-group label { display: block; font-size: 12px; font-weight: 600; color: #475569; margin-bottom: 6px; }
.input-group input { width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 14px; box-sizing: border-box; outline: none; }
.input-group input:focus { border-color: #2563eb; }
.btn-submit { width: 100%; background: #2563eb; color: white; border: none; padding: 10px; border-radius: 8px; font-weight: bold; cursor: pointer; }""",
            "js": ""
        },
        "Modern Search Bar with Icon": {
            "html": """<div class="search-box">
  <span class="search-icon">🔍</span>
  <input type="text" placeholder="Cari dokumen atau komponen...">
</div>""",
            "css": """body { font-family: sans-serif; background: #f8fafc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
.search-box { display: flex; align-items: center; background: white; border: 1px solid #cbd5e1; padding: 8px 16px; border-radius: 24px; width: 300px; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.search-icon { margin-right: 10px; opacity: 0.6; }
.search-box input { border: none; outline: none; width: 100%; font-size: 14px; }""",
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
.modal-overlay { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0, 0, 0, 0.5); backdrop-filter: blur(4px); justify-content: center; align-items: center; }
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
}"""
        },
        "Slide-Over Drawer (Off-Canvas)": {
            "html": """<button id="openDrawer" class="btn-open">Buka Slide Drawer</button>
<div class="drawer" id="drawer">
  <div class="drawer-header">
    <h3>Pengaturan Panel</h3>
    <button id="closeDrawer" class="close-btn">✕</button>
  </div>
  <p style="margin-top: 16px; font-size: 14px; color: #64748b;">Area drawer slide-in dari sebelah kanan.</p>
</div>""",
            "css": """body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background: #f8fafc; }
.btn-open { background: #2563eb; color: white; border: none; padding: 12px 20px; border-radius: 8px; cursor: pointer; }
.drawer { position: fixed; top: 0; right: -300px; width: 260px; height: 100%; background: white; box-shadow: -5px 0 25px rgba(0,0,0,0.15); padding: 20px; transition: 0.3s ease; }
.drawer.open { right: 0; }
.drawer-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #e2e8f0; padding-bottom: 12px; }
.drawer-header h3 { margin: 0; font-size: 16px; }
.close-btn { background: none; border: none; font-size: 18px; cursor: pointer; }""",
            "js": """const openDrawer = document.getElementById('openDrawer');
const closeDrawer = document.getElementById('closeDrawer');
const drawer = document.getElementById('drawer');
if(openDrawer && closeDrawer && drawer) {
  openDrawer.addEventListener('click', () => drawer.classList.add('open'));
  closeDrawer.addEventListener('click', () => drawer.classList.remove('open'));
}"""
        }
    },

    "🔔 Badge & Feedback": {
        "Toast Alert System": {
            "html": """<button id="showToastBtn" class="btn-toast">Tampilkan Notifikasi Toast</button>
<div id="toastContainer" class="toast-container"></div>""",
            "css": """body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; background: #f8fafc; }
.btn-toast { background: #16a34a; color: white; border: none; padding: 12px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; }
.toast-container { position: fixed; bottom: 20px; right: 20px; display: flex; flex-direction: column; gap: 10px; }
.toast { background: #0f172a; color: white; padding: 12px 20px; border-left: 4px solid #38bdf8; border-radius: 6px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); font-size: 14px; animation: slideIn 0.3s ease; }
@keyframes slideIn { from { transform: translateX(100%); } to { transform: translateX(0); } }""",
            "js": """const btn = document.getElementById('showToastBtn');
const container = document.getElementById('toastContainer');
if(btn && container) {
  btn.addEventListener('click', () => {
    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.innerText = '✅ Perubahan berhasil disimpan!';
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
  });
}"""
        },
        "Accordion / FAQ Dropdown": {
            "html": """<div class="accordion">
  <div class="acc-item">
    <button class="acc-btn">Apa itu Web Generator? <span>+</span></button>
    <div class="acc-content"><p>Web Generator adalah utilitas untuk melihat dan membuat contoh sintaks UI dengan cepat.</p></div>
  </div>
  <div class="acc-item">
    <button class="acc-btn">Apakah kode ini gratis dipakai? <span>+</span></button>
    <div class="acc-content"><p>Ya, semua komponen siap pakai dan bisa disalin langsung untuk proyek Anda.</p></div>
  </div>
</div>""",
            "css": """body { font-family: sans-serif; background: #f1f5f9; padding: 40px 20px; margin: 0; }
.accordion { max-width: 400px; margin: 0 auto; display: flex; flex-direction: column; gap: 8px; }
.acc-item { background: white; border-radius: 8px; overflow: hidden; border: 1px solid #e2e8f0; }
.acc-btn { width: 100%; padding: 14px; text-align: left; background: none; border: none; font-weight: bold; cursor: pointer; display: flex; justify-content: space-between; color: #0f172a; }
.acc-content { display: none; padding: 0 14px 14px; color: #64748b; font-size: 13px; line-height: 1.5; }
.acc-item.active .acc-content { display: block; }""",
            "js": """const btns = document.querySelectorAll('.acc-btn');
btns.forEach(btn => {
  btn.addEventListener('click', () => {
    btn.parentElement.classList.toggle('active');
  });
});"""
        },
        "Status Badges & Pills": {
            "html": """<div class="badge-group">
  <span class="badge success">Active</span>
  <span class="badge warning">Pending</span>
  <span class="badge danger">Error</span>
  <span class="badge info">Beta</span>
</div>""",
            "css": """body { font-family: sans-serif; background: #ffffff; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
.badge-group { display: flex; gap: 10px; }
.badge { padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: bold; }
.success { background: #dcfce7; color: #15803d; }
.warning { background: #fef9c3; color: #a16207; }
.danger { background: #fee2e2; color: #b91c1c; }
.info { background: #e0f2fe; color: #0369a1; }""",
            "js": ""
        },
        "Animated Skeleton Loader": {
            "html": """<div class="skeleton-card">
  <div class="skeleton skeleton-avatar"></div>
  <div class="skeleton-body">
    <div class="skeleton skeleton-title"></div>
    <div class="skeleton skeleton-text"></div>
  </div>
</div>""",
            "css": """body { font-family: sans-serif; background: #f8fafc; display: flex; justify-content: center; align-items: center; min-height: 100vh; margin: 0; }
.skeleton-card { background: white; padding: 20px; border-radius: 12px; width: 260px; display: flex; gap: 16px; align-items: center; border: 1px solid #e2e8f0; }
.skeleton { background: #e2e8f0; background: linear-gradient(90deg, #e2e8f0 25%, #f1f5f9 50%, #e2e8f0 75%); background-size: 200% 100%; animation: loading 1.5s infinite; border-radius: 4px; }
.skeleton-avatar { width: 48px; height: 48px; border-radius: 50%; flex-shrink: 0; }
.skeleton-body { width: 100%; }
.skeleton-title { height: 16px; width: 70%; margin-bottom: 8px; }
.skeleton-text { height: 12px; width: 100%; }
@keyframes loading { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }""",
            "js": ""
        }
    }
}

# ==============================================================================
# SELEKSI INTERAKTIF HALAMAN UTAMA
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
