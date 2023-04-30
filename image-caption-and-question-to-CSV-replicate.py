import os
import csv
import replicate

def process_image(image_path, csv_writer):
    # Print the image being processed
    print(f"\nProcessing image: {image_path}")

    try:
        # Run the model for image captioning
        with open(image_path, "rb") as image_file:
            print("Running image captioning task...")  # Debugging
            # Image Captioning Task
            caption_response = replicate.run(
                "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
                input={"image": image_file, "task": "image_captioning"}
            )
            print("Caption response:", caption_response)  # Debugging
            print("Running visual question answering task...")  # Debugging
            # Visual Question Answering Task
            answer_response = replicate.run(
                "salesforce/blip:2e1dddc8621f72155f24cf2e0adbde548458d3cab9f00c0139eea840d0ac4746",
                input={"image": image_file, "task": "visual_question_answering", "question": sample_question}
            )
            print("Answer response:", answer_response)  # Debugging
            # Extract the text after the "Caption: " prefix
            caption = caption_response.split("Caption: ")[1]
            # Extract the text after the "Answer: " prefix
            answer = answer_response.split("Answer: ")[1]

    except Exception as e:
        print(f"Error processing file '{image_path}': {e}")
        print("Caption output:", caption if 'caption' in locals() else "Caption not generated")
        print("VQA output:", answer if 'answer' in locals() else "Answer not generated")
        return

    # The rest of your code remains the same

# Define input and output folders
input_folder = 'C:\\Users\\brand\\OneDrive\\Midjourney Galleries\Art'
output_folder = 'C:\\Users\\brand\\OneDrive\\Midjourney Galleries\\Description and Analysis'
output_csv = os.path.join(output_folder, 'Midjourney Gallery Image Descriptions 4.28.23.csv')

# Set your Replicate API token as an environment variable
os.environ['REPLICATE_API_TOKEN'] = 'r8_J1bZVoYIgHO0IoBOgILmyBHh3uPzqEF1PNBcL'

# Define a sample question for the visual question answering task
sample_question = "Is there a person or persons in the image?"

# Create the CSV file and write the header
with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['Image Filename', 'Caption', 'Answer']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    # Iterate through the input folder and process each image file
    for dirpath, dirnames, filenames in os.walk(input_folder):
        for filename in filenames:
            # Construct the full path to the image file
            image_path = os.path.join(dirpath, filename)
            # Process the image and print the results
            process_image(image_path, csv_writer)

print("\nCSV file has been created successfully.")
