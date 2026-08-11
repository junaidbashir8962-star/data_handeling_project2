import streamlit as st
import os

def load_css(css_path="assets/styles.css"):
    """Injects CSS file contents into Streamlit."""
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render_header(title, subtitle):
    """Renders a styled header banner."""
    html = f"""
    <div class="main-header">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)