import logging

def generate_hashtags(self, product_name, product_features, description, audience, platform):
    """
    Generate trending hashtags related to the product using the Gemini text model.
    
    Constructs a detailed prompt that includes all product details,
    including description and audience, to generate industry-specific, 
    high-engagement hashtags.
    
    Parameters:
        product_name (str): The product's name.
        product_features (str): Features of the product.
        description (str): Detailed description of the product.
        audience (str): Target audience.
        platform (str): Platform detail.
    
    Returns:
        str: Generated hashtags as a text response; returns an empty string on error.
    """
    logging.info(f"Generating hashtags for product '{product_name}' on platform '{platform}'")
    
    # Construct a clean, multi-line prompt without extra whitespace.
    prompt = f"""
Generate a list of trending and relevant hashtags for:
Product: {product_name}
Features: {product_features}
Description: {description}
Audience: {audience}
Platform: {platform}

Include industry-specific, high-engagement hashtags.
    """.strip()
    
    try:
        response = self.gemini_text_model.generate_content(prompt)
        
        if hasattr(response, 'text'):
            logging.debug("Successfully generated hashtags.")
            return response.text
        else:
            logging.error("Response from gemini_text_model.generate_content does not have attribute 'text'.")
            return ""
    except Exception as err:
        logging.error(f"Error generating hashtags: {err}")
        return ""
