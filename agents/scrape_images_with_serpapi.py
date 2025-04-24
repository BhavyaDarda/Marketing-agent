import logging
import pathlib
from urllib.parse import urlparse, unquote
import urllib.request
from serpapi.google_search import GoogleSearch

def scrape_images_with_serpapi(self, product_name, product_features, description, audience, platform):
    """
    Scrape images related to the product using SerpAPI and download them locally.
    
    This method constructs a search query from the product details,
    including description, audience, and platform to provide more targeted results.
    It then uses SerpAPI to fetch image results and downloads the first three valid images
    into a local folder.
    
    Parameters:
        product_name (str): Name of the product.
        product_features (str): Features of the product.
        description (str): Description of the product.
        audience (str): Target audience.
        platform (str): Platform detail.
    
    Returns:
        list: A list containing paths to the downloaded images, or a fallback message.
    """
    logging.info(f"Attempting to scrape images for {product_name}")
    try:
        # Compose the search query using all provided parameters for better targeting
        search_query = f"{product_name} {product_features} {description} for {audience} on {platform} image"
        search_params = {
            "engine": "google_images",
            "q": search_query,
            "api_key": self.SERP_API_KEY
        }
        
        # Initialize and execute the search
        search = GoogleSearch(search_params)
        results = search.get_dict()
        logging.debug(f"SerpAPI results: {results}")
        
        image_files = []
        if "images_results" in results and results["images_results"]:
            # Create a local directory for downloads if it does not exist
            download_dir = pathlib.Path("downloaded_images")
            download_dir.mkdir(exist_ok=True)
            
            # Process the first 3 image results
            for idx, item in enumerate(results["images_results"][:3]):
                # Unquote the image URL to decode any % escapes
                img_url = unquote(item.get("original", ""))
                parsed = urlparse(img_url)
                
                # Validate URL scheme
                if parsed.scheme not in ('http', 'https'):
                    logging.warning(f"Skipping invalid image URL: {img_url}")
                    continue
                
                local_filename = download_dir / f"{product_name.replace(' ', '_')}_{idx}.jpg"
                try:
                    # Download the image and save locally
                    urllib.request.urlretrieve(img_url, local_filename)
                    logging.info(f"Downloaded image from {img_url} to {local_filename}")
                    image_files.append(str(local_filename.resolve()))
                except Exception as download_error:
                    logging.error(f"Error downloading image {img_url}: {download_error}")
            if image_files:
                return image_files
        
        logging.info("No valid images found, returning fallback message.")
        return ["Could not scrape any relevant images."]
    except Exception as e:
        logging.error(f"Error scraping images with SerpAPI: {str(e)}")
        return ["Could not scrape images. Falling back to image generation."]
