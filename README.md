# Image Analysis and Description Generator

This script processes a collection of images, generating descriptive captions and answering a specific question for each image using the Salesforce Blip model. The results are saved in a CSV file.

## Features

This Image Analysis and Description Generator script offers the following features:

1. Batch processing: Analyze a collection of images in a single run, saving time and effort.
2. Dual tasks: Generate both descriptive captions and answers to specific questions for each image.
3. Salesforce Blip model integration: Utilize the powerful Salesforce Blip model for high-quality image captioning and visual question answering.
4. CSV output: Export the generated captions and answers to a CSV file for easy review and further analysis.
5. Customizable input and output: Easily define input and output folders and sample questions to suit your specific needs.

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

## Disclaimer

Please note that the output generated by the Salesforce Blip model and other AI tools may not always be entirely accurate, complete, or free from biases. Users should exercise critical thinking when reviewing the generated output and consider it as a starting point for further research, discussion, or refinement.

It is the user's responsibility to verify the accuracy and relevance of the AI-generated content and adapt it to their specific needs and context. Additionally, users should be aware that the AI tool might sometimes generate content that is inappropriate, offensive, or unrelated to the given input. Always review and revise the generated content before using it in any professional or educational setting.
