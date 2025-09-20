Cell Image AI (Microscopy Assistant)

**Cell Image AI** is an interactive web application that uses **Cellpose**, a deep learning model, to segment cells in microscopy images and extract quantitative metrics such as area, perimeter, eccentricity, and mean intensity. This tool allows researchers, students, and lab technicians to analyze microscopy images quickly and efficiently without writing any code.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ezzaa44/Microscopy-Assistant.git
cd Microscopy-Assistant
```

### 2. Install Dependencies

Make sure you have Python ==3.10 installed. Then install the required Python packages:

```bash
pip install -r requirements.txt
```

> Note: The `numpy<2` constraint is required for compatibility with Cellpose v4.

## Usage

Run the application locally:

```bash
python app.py
```

- The Gradio app will start at `http://0.0.0.0:7860` or `http://localhost:7860`.
- Open the URL in your web browser.
- Upload a microscopy image and wait for the segmentation results.

## Dependencies

- **Python 3.10**
- **Gradio**: For building the interactive web interface.
- **NumPy**: Numerical operations on images.
- **Pandas**: Organize and display cell metrics in a table.
- **Matplotlib**: Visualization of original and segmented images.
- **Scikit-Image**: Image processing (region properties, clearing border artifacts).
- **Cellpose (v4.0.6+)**: Deep learning-based cell segmentation.

## Project Structure

```
Cell_Image_AI/
│
├── app.py                  # Main Gradio app
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── sample_images/          # Optional folder for example microscopy images
```

## How it Works

1. **Image Upload**: Users upload a microscopy image through the Gradio interface.
2. **Preprocessing**: Image is converted to grayscale for segmentation.
3. **Cellpose Segmentation**:
   - Uses Cellpose's pre-trained `cyto` model for cell detection.
   - Supports both new and older API formats for compatibility.
4. **Postprocessing**:
   - Removes artifacts and cells touching the border using `clear_border`.
   - Filters out tiny regions to avoid noise.
5. **Metric Extraction**:
   - Calculates area, perimeter, eccentricity, and mean intensity for each detected cell.
6. **Visualization**:
   - Plots the original image alongside the segmentation mask.
   - Displays metrics in an interactive table.

## Metrics Extracted

| Metric Name     | Description                                   |
|-----------------|-----------------------------------------------|
| **Cell_ID**      | Unique identifier for each detected cell     |
| **Area**         | Pixel area of the cell                        |
| **Perimeter**    | Cell perimeter length                         |
| **Eccentricity** | Ratio of the distance between the foci to the major axis (shape measure) |
| **Mean_Intensity** | Average grayscale intensity of the cell      |

## Visualization

- **Left Panel**: Original microscopy image.
- **Right Panel**: Segmented cells with unique colors (using `nipy_spectral` colormap).
- Allows users to easily identify segmented cells and visually confirm accuracy.

## License

This project is open-source and available under the MIT License.

---

**Developed with ❤️ using Python, Gradio, and Cellpose.**

