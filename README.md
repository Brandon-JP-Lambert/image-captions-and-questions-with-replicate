# Image Captions and Questions to CSV with Replicate

This Python script generates informative image descriptions and answers a user-defined question for a collection of images using the Replicate API with the Salesforce BLIP model. The output is conveniently saved to a CSV file.

## Features

- Automatically generate captions for images using the Salesforce BLIP AI model powered by Replicate.
- Answer a pre-defined question about each image using the same AI model.
- Save the image filenames, generated captions, and answers to a CSV file.

## Requirements

The following Python libraries are required to run the script:

- `os`
- `shutil`
- `csv`
- `replicate`

## Setup and Configuration

1. Install the required Python libraries.
2. Set the `input_folder` variable to the path of the folder containing your image files.
3. Set the `output_folder` variable to the path of the folder where you'd like to save the output CSV file.
4. Replace the value of `REPLICATE_API_TOKEN` with your actual Replicate API token.
5. Define a sample question for the visual question answering task by updating the `sample_question` variable.

## Usage

Run the script after completing the setup and configuration steps. The script will process the images in the input folder, generate captions and answers to the pre-defined question using the Salesforce BLIP model, and save the results to a CSV file in the output folder.

Ensure that the `input_folder`, `output_folder`, and `REPLICATE_API_TOKEN` values are updated with your desired paths and token before running the script.

## Troubleshooting

If you encounter any issues while running the script, please ensure that:

- The input folder contains only image files.
- Your Replicate API token is valid.
- The required Python libraries are installed.

If issues persist, refer to the error messages for more information on the problem.

## Model Information

The script uses the Salesforce BLIP model, which is a powerful AI model capable of performing tasks such as image captioning and visual question answering. The model is accessed via the Replicate API, which provides a convenient way to integrate the model's capabilities into the script.

You can find more information about the Salesforce BLIP model and the Replicate API on the [Replicate website](https://replicate.com/salesforce/blip/api) and on the [Salesforce Research blog](https://blog.salesforceairesearch.com/blip-2/)²¹.
