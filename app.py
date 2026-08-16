import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Web Generator", page_icon="🎨", layout="wide")

st.title("🎨 Web Generator")
st.caption("Pilih rekomendasi komponen HTML/CSS/JS, sesuaikan kodenya, dan lihat hasil *Live Preview* secara instan.")

# Sidebar untuk Pemilihan Komponen
st.sidebar.header("⚙️ Pilih Komponen")
category = st.sidebar.selectbox("Kategori Syntax:", [
    "Buttons & Links",
    "Cards & Containers",
    "Forms & Inputs",
    "CSS Animations",
    "JS Interactivity"
])

# Library Template Komponen
templates = {
    "Buttons & Links": {
        "Modern Gradient Button": {
            "html": '<button class="btn-gradient">Klik Saya</button>',
            "css": """.btn-gradient {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  padding: 12px 28px;
  font-size: 16px;
  font-weight: bold;
  border-radius: 8px;
  cursor: pointer;
  box-shadow: 0 4px 15px rgba(118, 75, 162, 0.4);
  transition: all 0.3s ease;
}

.btn-gradient:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(118, 75, 162, 0.6);
}""",
            "js": "// Tidak ada JavaScript tambahan untuk komponen ini"
        },
        "Outline Ripple Button": {
            "html": '<button class="btn-outline">Hover Effect</button>',
            "css": """.btn-outline {
  background: transparent;
  color: #0070f3;
  border: 2px solid #0070f3;
  padding: 10px 24px;
  font-size: 16px;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s ease, color 0.2s ease;
}

.btn-outline:hover {
  background-color: #0070f3;
  color: white;
}""",
            "js": ""
        }
    },
    "Cards & Containers": {
        "Glassmorphism Card": {
            "html": """<div class="glass-card">
  <h3>Glassmorphism Card</h3>
  <p>Komponen modern dengan efek latar belakang buram transparan.</p>
</div>""",
            "css": """body {
  background: linear-gradient(45deg, #ff9a9e 0%, #fad0c4 99%);
  font-family: sans-serif;
}

.glass-card {
  background: rgba(255, 255, 255, 0.25);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.18);
  padding: 24px;
  max-width: 300px;
  color: #333;
}""",
            "js": ""
        }
    },
    "Forms & Inputs": {
        "Floating Label Input": {
            "html": """<div class="input-group">
  <input type="text" id="username" placeholder=" " required />
  <label for="username">Nama Pengguna</label>
</div>""",
            "css": """.input-group {
  position: relative;
  width: 280px;
  margin-top: 20px;
}

.input-group input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 6px;
  outline: none;
  font-size: 16px;
}

.input-group label {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: white;
  padding: 0 4px;
  color: #999;
  transition: 0.2s ease all;
  pointer-events: none;
}

.input-group input:focus ~ label,
.input-group input:not(:placeholder-shown) ~ label {
  top: 0;
  font-size: 12px;
  color: #0070f3;
}""",
            "js": ""
        }
    },
    "CSS Animations": {
        "Pulse Loading Spinner": {
            "html": '<div class="spinner"></div>',
            "css": """.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid #f3f3f3;
  border-top: 5px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}""",
            "js": ""
        }
    },
    "JS Interactivity": {
        "Character Counter Input": {
            "html": """<div style="font-family: sans-serif;">
  <textarea id="my-text" rows="4" cols="35" placeholder="Ketik pesan Anda..."></textarea>
  <p><span id="char-count">0</span> / 100 Karakter</p>
</div>""",
            "css": """textarea {
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-family: inherit;
}
p {
  font-size: 14px;
  color: #555;
}""",
            "js": """const textArea = document.getElementById('my-text');
const charCount = document.getElementById('char-count');

textArea.addEventListener('input', () => {
  const currentLength = textArea.value.length;
  charCount.textContent = currentLength;
  if(currentLength > 100) {
    charCount.style.color = 'red';
  } else {
    charCount.style.color = '#555';
  }
});"""
        }
    }
}

# Pilih Nama Komponen berdasarkan Kategori
snippet_name = st.sidebar.selectbox("Pilih Template Komponen:", list(templates[category].keys()))
selected_data = templates[category][snippet_name]

# Kolom Kiri: Editor Kode & Rekomendasi | Kolom Kanan: Live Preview
col_code, col_preview = st.columns([1, 1])

with col_code:
    st.subheader("📝 Syntax Editor")
    
    html_code = st.text_area("HTML Syntax:", value=selected_data["html"], height=120)
    css_code = st.text_area("CSS Syntax:", value=selected_data["css"], height=180)
    js_code = st.text_area("JavaScript Syntax:", value=selected_data["js"], height=120)

with col_preview:
    st.subheader("👁️ Live Preview")
    
    # Menggabungkan HTML, CSS, dan JS ke dalam iframe terisolasi
    full_preview_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body {{
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
          display: flex;
          justify-content: center;
          align-items: center;
          min-height: 250px;
          margin: 0;
        }}
        {css_code}
      </style>
    </head>
    <body>
      {html_code}
      <script>
        {js_code}
      </script>
    </body>
    </html>
    """
    
    # Render iframe menggunakan komponen Streamlit
    components.html(full_preview_html, height=350, scrolling=True)

st.divider()

# Tab Penyorot Kode Siap Salin
st.markdown("### 📋 Salin Kode Siap Pakai")
tab_html, tab_css, tab_js = st.tabs(["HTML", "CSS", "JavaScript"])

with tab_html:
    st.code(html_code, language="html")
with tab_css:
    st.code(css_code, language="css")
with tab_js:
    st.code(js_code, language="javascript")
