import openai
from django.conf import settings
from django.core.files.base import ContentFile
import requests

def create_image_from_prompt(prompt: str):
    """
    Uses the OpenAI API to generate an image from a text prompt.
    Returns the URL of the generated image.
    """
    if not settings.OPENAI_API_KEY or settings.OPENAI_API_KEY == 'your-openai-api-key-here':
        raise ValueError("OPENAI_API_KEY is not configured in your .env file.")

    openai.api_key = settings.OPENAI_API_KEY

    try:
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="url"
        )
        image_url = response.data[0].url
        return image_url
    except openai.APIError as e:
        print(f"OpenAI API returned an API Error: {e}")
        raise
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise

def download_image_from_url(image_url: str) -> ContentFile:
    """
    Downloads an image from a URL and returns it as a Django ContentFile.
    """
    response = requests.get(image_url)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    return ContentFile(response.content)
