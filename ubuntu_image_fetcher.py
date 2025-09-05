# Ubuntu Image Fetcher
# This script fetches images from the web in a mindful and respectful way,
# inspired by the Ubuntu philosophy: "I am because we are."

import requests         # For HTTP requests to fetch images
import os               # For directory and file management
from urllib.parse import urlparse  # To extract filenames from URLs

def main():
    # Welcome message to introduce the program
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Ask the user to enter the URL of the image they want to download
    url = input("Please enter the image URL: ")

    try:
        # Step 1: Ensure that the folder 'Fetched_Images' exists
        # If it doesn't exist, it will be created automatically
        os.makedirs("Fetched_Images", exist_ok=True)
        
        # Step 2: Fetch the image from the URL
        # timeout=10 ensures the program doesn't hang indefinitely
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error if the HTTP status is not 200 OK
        
        # Step 3: Extract the filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)  # Get the last part of the URL path
        
        # If the URL does not contain a filename, use a default name
        if not filename:
            filename = "downloaded_image.jpg"
        
        # Step 4: Create the full path to save the image
        filepath = os.path.join("Fetched_Images", filename)
        
        # Step 5: Save the image in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        # Step 6: Success messages to the user
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched. 🌍")
    
    # Handle network-related errors (connection issues, timeout, etc.)
    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    
    # Handle any other unexpected errors gracefully
    except Exception as e:
        print(f"✗ An error occurred: {e}")

# This ensures the program runs only if executed directly
if __name__ == "__main__":
    main()
