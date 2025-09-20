import gradio as gr
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from skimage.measure import regionprops
from skimage.segmentation import clear_border
from cellpose import models

# Load Cellpose model - updated for v4.0.6
try:
    # Try the new API first
    model = models.CellposeModel(gpu=False, model_type="cyto")
except AttributeError:
    # Fall back to older API if needed
    model = models.Cellpose(gpu=False, model_type="cyto")

def process_image(image):
    # Convert to numpy array and make grayscale
    image_np = np.array(image.convert("L"))
    
    try:
        # Try new API call format
        masks, flows, styles = model.eval(image_np, diameter=None, channels=[0,0])
    except TypeError:
        # Fall back to older API format
        masks, flows, styles, diams = model.eval([image_np], diameter=None, channels=[0,0])
        masks = masks[0]
    
    # Clean up borders and small artifacts
    masks_cleaned = clear_border(masks)
    masks_cleaned = masks_cleaned.astype(np.uint32)
    
    # Get region properties
    props = regionprops(masks_cleaned, intensity_image=image_np)
    
    # Extract metrics
    metrics = []
    for idx, prop in enumerate(props):
        if prop.area > 10:  # Filter out tiny regions
            metrics.append({
                "Cell_ID": idx + 1,
                "Area": prop.area,
                "Perimeter": prop.perimeter,
                "Eccentricity": prop.eccentricity,
                "Mean_Intensity": prop.mean_intensity
            })
    
    df = pd.DataFrame(metrics)
    
    # Create visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    
    ax1.imshow(image_np, cmap="gray")
    ax1.set_title("Original Image")
    ax1.axis("off")
    
    ax2.imshow(masks_cleaned, cmap="nipy_spectral")
    ax2.set_title("Cellpose Segmentation")
    ax2.axis("off")
    
    plt.tight_layout()
    plt.close(fig)
    
    return fig, df

# Create Gradio interface
demo = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="pil", label="Upload Microscopy Image"),
    outputs=[
        gr.Plot(label="Segmentation Result"),
        gr.Dataframe(label="Cell Metrics")
    ],
    title="Cell Image AI (Microscopy Assistant)",
    description="Upload a microscopy image (.jpg/.png/.tif) to segment cells and extract metrics."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
