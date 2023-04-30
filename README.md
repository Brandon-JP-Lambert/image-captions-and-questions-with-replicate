# Image Analysis and Description Generator

This script processes a collection of images, generating descriptive captions and answering a specific question for each image using the Salesforce Blip model. The results are saved in a CSV file.

## Prerequisites

To use this script, you'll need:

- Python 3.7 or later
- The `replicate` Python library: Install it using `pip install replicate`

## Replicate Package

The Replicate package is a Python library that allows you to interact with the Replicate platform's API. Replicate offers various pre-trained machine learning models for tasks such as image captioning, visual question answering, and more.

### Installation

To install the Replicate package, run the following command:

```bash
pip install replicate
```

### Example Replicate Calls

1. Image Captioning:

```python
caption_response = replicate.run(
    "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
    input={"image": image_file, "task": "image_captioning"}
)
```

This call generates a caption describing the contents of an image.

2. Visual Question Answering:

```python
answer_response = replicate.run(
    "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
    input={"image": image_file, "task": "visual_question_answering", "question": sample_question}
)
```

This call answers a specific question about an image.

### Documentation

For more information about the Replicate package and its features, refer to the official documentation:

- [Replicate Website](https://www.replicate.ai/)
- [Replicate Python Library Documentation](https://docs.replicate.ai/)

## Usage

1. Set your input and output folders within the script:
   - `input_folder`: The path to the folder containing your image files.
   - `output_folder`: The path to the folder where the generated CSV file will be saved.
   - `output_csv`: The path and filename for the generated CSV file.

2. Set your Replicate API token as an environment variable:
   - `os.environ['REPLICATE_API_TOKEN'] = 'your_api_token'`
   Replace `'your_api_token'` with your actual Replicate API token.

3. Define a sample question for the visual question answering task:
   - `sample_question`: A string containing the question to be answered for each image.

4. Run the script: `python image_analysis_and_description_generator.py`

## Output

The script will generate a CSV file containing the following columns:

- `Image Filename`: The filename of the processed image.
- `Caption`: The generated caption describing the image (using the Image Captioning task).
- `Answer`: The answer to the sample question provided (using the Visual Question Answering task).

## Troubleshooting

If there is an error during the processing of an image, the script will print the error message, the filename of the image, and any generated output for the caption and/or visual question answering tasks.
