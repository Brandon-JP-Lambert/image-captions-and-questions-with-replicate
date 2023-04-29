import os
import shutil
import csv
import replicate

# Define input and output folders
input_folder = 'C:\\Users\\brand\\OneDrive\\Midjourney Galleries'
output_folder = 'C:\\Users\\brand\\OneDrive\\Midjourney Galleries\\Description and Analysis'
output_csv = os.path.join(output_folder, 'Midjourney Gallery Image Descriptions 4.28.23.csv')

# Set your Replicate API token as an environment variable
os.environ['REPLICATE_API_TOKEN'] = 'r8_J1bZVoYIgHO0IoBOgILmyBHh3uPzqEF1PNBcL'

# Define a sample question for the visual question answering task
sample_question = "Is there a person or persons in the image?"

# Create the CSV file and write the header
with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Image Filename', 'Caption', 'Answer'])

    # Iterate through the input folder and process each image file
    for dirpath, dirnames, filenames in os.walk(input_folder):
        for filename in filenames:
            # Construct the full path to the image file
            image_path = os.path.join(dirpath, filename)

            try:
                print(f"Processing image: {image_path}")  # Debugging: Print the image being processed

                # Run the model for image captioning
                with open(image_path, "rb") as image_file:
                    # Image Captioning Task
                    caption_output = replicate.run(
                        "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
                        input={"image": image_file, "task": "image_captioning"}
                    )
                    # Visual Question Answering Task
                    vqa_output = replicate.run(
                        "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
                        input={"image": image_file, "task": "visual_question_answering", "question": sample_question}
                    )

                # Extract the caption and answer from the output
                caption = caption_output[0]
                answer = vqa_output[0]

                # Write the image filename, caption, and answer to the CSV file
                csv_writer.writerow([filename, caption, answer])

                print(f"Processing complete for image: {image_path}")  # Debugging: Print when processing is complete
            except Exception as e:
                print(f"Error processing file '{image_path}': {e}")

print("CSV file has been created successfully.")
