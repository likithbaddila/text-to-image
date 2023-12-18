import streamlit as st
import openai,dotenv
import os
from dotenv import load_dotenv



openai.api_key = os.environ.get("api_key")
from openai import OpenAI
client = OpenAI(api_key=os.environ.get("api_key"))

def generate_image(prompt, image_size):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size = image_size,
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url if image_url else None


def main():
    st.title("Text to Image Generator")

    # Text input for the prompt
    prompt = st.text_area("Enter your text prompt:")

    # Checkbox for image size
    image_size = st.selectbox("Select image size:", ["1024x1024", "1024x1792"])

    # Submit button
    if st.button("Generate Image"):
        if not prompt:
            st.warning("Please enter a prompt.")
        else:
            st.info("Generating image. This may take a moment...")
            image_url = generate_image(prompt, image_size)

            if image_url:
                st.image(image_url, caption="Generated Image", use_column_width=True)
            else:
                st.error("Failed to generate image.")

if __name__ == "__main__":
    main()