# utils/render.py
#  handles profile card rendering
import os
import streamlit as st
from utils.helpers import highlight_match, encode_image_to_base64


def render_profile_card(row, search_term):
    """Render a single profile card as an HTML block with hover effect."""
    b64_img = encode_image_to_base64(os.path.join("images", row['Avatar']))
    image_html = (
        f'<img src="data:image/png;base64,{b64_img}" '
        'style="width:150px; border-radius:10px;" />'
        if b64_img
        else "<div class='image-not-found'>Image not found</div>"
    )

    # Highlighted fields
    highlighted_name = highlight_match(row['Name'], search_term)
    highlighted_email = highlight_match(row['Email'], search_term)
    job_title = highlight_match(row['Title'], search_term)

    # Format AI Tools
    tools_html_lines = []
    for line in str(row['AI Tools Used']).split('\n'):
        if ':' in line:
            role, tools = line.split(':', 1)
            tools_html_lines.append(
                f"<li><b>{highlight_match(role.strip(), search_term)}</b>: {highlight_match(tools.strip(), search_term)}</li>"
            )
        else:
            tools_html_lines.append(f"<li>{highlight_match(line.strip(), search_term)}</li>")
    tools_html = "<ul>" + "".join(tools_html_lines) + "</ul>"

    card_html = f"""
    <div class="profile-card">
        <div class="profile-image">{image_html}</div>
        <div class="profile-content">
            <h3>{highlighted_name}</h3>
            <div class="title">💼 {job_title}</div>
            <div class="email">📧 {highlighted_email}</div>
            <div><b>🧠 AI Tools Used:</b></div>
            {tools_html}
        </div>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)
