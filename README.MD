# Batch Image Resizer

A Python script that batch resizes all images in the script's directory to a specified dimension in inches at a given DPI, saving the resized versions with a `resized_` prefix.

---

## Author

**Nitish Kapur**<br>
GitHub: [github.com/nitish-kapur](https://github.com/nitish-kapur)

---

## Supported File Types

`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`

---

## Requirements
```bash
pip install pillow
```

---

## Usage

Run the script directly:
```bash
python resize-images.py
```

The script will automatically process all supported image files found in the same directory as the script. No file dialog is required.

---

## Output

| File | Description |
|---|---|
| `resized_<original_filename>` | Resized image saved in the same directory |

Example: `resized_plot1.png`

---

## Configuration

The target dimensions and DPI are set at the bottom of the script:
```python
resize_all_images_in_folder(current_directory, 14, 8, dpi=300)
```

| Parameter | Current Value | Description |
|---|---|---|
| `width_inch` | `14` | Target width in inches |
| `height_inch` | `8` | Target height in inches |
| `dpi` | `300` | Dots per inch (resolution) |

Edit these values directly in the script to change the output dimensions.

---

## Notes

- Resizing uses the **Lanczos** resampling filter for high-quality downscaling.
- Original files are not modified; resized copies are saved alongside them with the `resized_` prefix.
- The output pixel dimensions are calculated as: **pixels = inches × DPI**. At the default settings this produces 4200 × 2400 px images.
