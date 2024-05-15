import streamlit as st
from gradio_client import Client


st.set_page_config(
        page_title="RealGEN",
        page_icon="https://i.ibb.co/kcfZcsW/new-circle.png"
)

hide_St = """
	<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .viewerBadge_link__qRIco {display:none;}
    </style>
"""

st.markdown(hide_St, unsafe_allow_html=True)

# Initialize the Gradio Client
client = Client("Walmart-the-bag/Juggernaut-X-v10")

# Streamlit app title
st.title("RealGEN")
st.write("Generate UNLIMITED REALISTIC AI images for FREE")

# Input fields for the prompt and negative prompt
prompt = st.text_input("Prompt", "An astronaut riding a robot horse in moon")
negative_prompt = st.text_input("Negative Prompt", value="bad quality, bad anatomy, worst quality, low quality, lowres, extra fingers, blur, blurry, ugly, wrong proportions, watermark, image artifacts, bad eyes")
steps = st.slider("Steps", min_value=1, max_value=100, value=50)
guidance_scale = st.slider("Guidance Scale", min_value=1.0, max_value=20.0, value=7.5)
add_4k_masterpiece = st.checkbox("RECOMENDED: Add 4K Masterpiece", value=True)

# Button to generate the image
if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        result = client.predict(
            prompt=prompt,
            negative_prompt=negative_prompt,
            steps=steps,
            guidance_scale=guidance_scale,
            add_4k_masterpiece=add_4k_masterpiece,
            api_name="/predict"
        )
        st.image(result, caption="Generated Image")
        st.page_link("https://twitter.com/not_gallium", label="🔵Follow me on 𝕏", icon="❎")
        st.page_link("https://youtube.com/@GAllium14", label="🔴Subscribe to my YT channel", icon="📺")
        st.page_link("https://github.com/GokulAnand14/RealGEN", label="🌟Open-Source on GitHub", icon="🔓")
        st.page_link("https://huggingface.co/RunDiffusion/Juggernaut-X-v10", label="🖼Powered By RunDiffusion/Juggernaut-X-v10", icon="⚡")
        st.write("made with ❤ by Gokul Anand")

# Instructions
st.write("""
### Instructions:
1. Enter a prompt describing the image you want to generate.
2. Optionally, enter a negative prompt to exclude certain features.
3. Adjust the steps and guidance scale as needed.
4. Check the box to add 4K masterpiece quality if desired.
5. Click the "Generate Image" button and wait for the result.
""")
