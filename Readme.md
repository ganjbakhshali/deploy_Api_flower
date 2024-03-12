# Plant Image Recognition using Illusion Diffusion and PlantNet

This Python script allows you to generate and recognize plant images using Illusion Diffusion and PlantNet APIs. The script takes a flower or plant name as input, generates an image using Illusion Diffusion, and then uses PlantNet for plant recognition.

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3.x
- Required Python libraries: `requests`, `Pillow`, `argparse`, `dotenv`

## Setup

1. **Clone this repository to your local machine:**

    ```bash
    git clone https://github.com/ganjbakhshali/deploy_Api_flower.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd deploy_Api_flower
    ```

3. **Install the required Python libraries:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the project directory and add the following:**

    ```env
    ILLUSION_DIFFUSION_API_KEY=your_illusion_diffusion_api_key
    PLANTNET_API_KEY=your_plantnet_api_key
    ```

    Replace `your_illusion_diffusion_api_key` and `your_plantnet_api_key` with your actual API keys.

## Usage

Run the script with the desired flower or plant name:

```bash
python script_name.py "Sunflower"
```

image generated:

![image info](91758cec-a911-492d-8179-20608da17942.png)
and recognised name:

```
The recognized plant is: Helianthus annuus
```

## Colab
you can also run API.ipynb in colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/ganjbakhshali/deploy_Api_flower/blob/main/API.ipynb)
