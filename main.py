import requests
import argparse
import os
from dotenv import load_dotenv
import fal
from PIL import Image
from io import BytesIO

load_dotenv()

def save_image(image_data, filename="flower.png"):
    try:
        image = Image.open(BytesIO(image_data))
        image.save(filename, format="PNG")
        print(f"Image saved as {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")


def generate_image(plant_name, api_key):
    api_url = "https://fal.run/fal-ai/illusion-diffusion"

    illusion_diffusion_input = {
        "prompt": f"(masterpiece:1.4), (best quality), (detailed), {plant_name}",
        "guidance_scale": 7.5,
        "controlnet_conditioning_scale": 1,
        "control_guidance_end": 1,
        "scheduler": "Euler",
        "num_inference_steps": 40,
        "image_size": "square_hd",
    }

    response = requests.post(api_url, json=illusion_diffusion_input, headers={"Authorization": f"Bearer {api_key}"})
    print(f"response.status_code:{response.status_code}")
    
    if response.status_code == 200:
        illusion_diffusion_output = response.json()
        if "image" in illusion_diffusion_output:
            image_url = illusion_diffusion_output["image"]["url"]
            image_data = requests.get(image_url).content
            save_image(image_data, "generated_image.png")
            return image_data
        else:
            print("No 'image' key in the API response.")
    else:
        print(f"API request failed with status code: {response.status_code}")
        print(response.text)
    
    return None


def recognize_plant(image_data, api_key):
    url = "https://my.plantnet.org/api/identify"
    headers = {"Api-Key": api_key}
    files = {"images": ("image.jpg", image_data, "image/jpeg")}
    
    try:
        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()
        return response.json()["results"][0]["species"]["scientificNameWithoutAuthor"]
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")


def main():
    parser = argparse.ArgumentParser(description="Generate and recognize plant images.")
    parser.add_argument("plant_name", type=str, nargs="?", default="Sunflower", help="Name of the flower or plant")
    args = parser.parse_args()
    illusion_diffusion_api_key = os.getenv("ILLUSION_DIFFUSION_API_KEY")
    plantnet_api_key = os.getenv("PLANTNET_API_KEY")
    if not illusion_diffusion_api_key or not plantnet_api_key:
        print("Please provide API keys in the .env file.")
        return

    image_data = generate_image(args.plant_name, illusion_diffusion_api_key)

    if image_data:

        plant_name = recognize_plant(image_data, plantnet_api_key)

        if plant_name:
            print(f"The recognized plant is: {plant_name}")
        else:
            print("Plant recognition failed.")
    else:
        print("Image generation failed.")

if __name__ == "__main__":
    main()
