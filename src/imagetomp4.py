import cv2
import os
import json


class ImageToVideoConverter:
    def __init__(
        self,
        input_folder,
        output_folder,
        video_filename="output_video.mp4",
        frame_rate=24,
        frame_size=(640, 480),
    ):
        """
        Initializes the converter with parameters for input folder, output folder, video filename, frame rate, and frame size.

        Parameters:
            input_folder (str): Path to the folder containing images.
            output_folder (str): Path to the folder where the video and metadata JSON will be saved.
            video_filename (str): Name of the output video file.
            frame_rate (int): Frame rate of the output video.
            frame_size (tuple): Size of each frame as (width, height).
        """
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.video_filename = video_filename
        self.output_file = os.path.join(output_folder, video_filename)
        self.frame_rate = frame_rate
        self.frame_size = frame_size

        # Ensure output directory exists
        os.makedirs(self.output_folder, exist_ok=True)

    def get_images(self):
        """Retrieves and sorts image files from the input folder."""
        images = [
            img
            for img in os.listdir(self.input_folder)
            if img.endswith((".png", ".jpg", ".jpeg"))
        ]
        images.sort()  # Ensure the images are in correct order
        return images

    def generate_metadata_json(self, images):
        """Generates a JSON file with metadata about each image used in the video."""
        metadata = []
        for img_name in images:
            img_path = os.path.join(self.input_folder, img_name)
            img = cv2.imread(img_path)
            height, width, _ = img.shape
            metadata.append(
                {
                    "filename": img_name,
                    "path": img_path,
                    "width": width,
                    "height": height,
                }
            )

        json_path = os.path.join(self.output_folder, "image_metadata.json")
        with open(json_path, "w") as json_file:
            json.dump(metadata, json_file, indent=4)
        print(f"Metadata JSON saved as {json_path}")

    def convert(self):
        """Converts the images to a video and saves it to the output file, then generates a JSON metadata file."""
        images = self.get_images()

        # Check if there are images to process
        if not images:
            print("No images found in the input folder.")
            return

        # Define video codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # type: ignore
        out = cv2.VideoWriter(
            self.output_file, fourcc, self.frame_rate, self.frame_size
        )

        for image_name in images:
            img_path = os.path.join(self.input_folder, image_name)
            frame = cv2.imread(img_path)

            # Resize frame to match frame size
            frame = cv2.resize(frame, self.frame_size)

            # Write the frame into the video file
            out.write(frame)
            print(f"Added {image_name} to video.")

        # Release the video writer object
        out.release()
        print(f"Video saved as {self.output_file}")

        # Generate metadata JSON
        self.generate_metadata_json(images)


class VideoToImagesConverter:
    def __init__(self, video_file, output_folder, frame_interval=1):
        """
        Initializes the converter with parameters for the video file, output folder, and frame interval.

        Parameters:
            video_file (str): Path to the input MP4 video file.
            output_folder (str): Path to the folder where images will be saved.
            frame_interval (int): Extract every n-th frame (1 means every frame).
        """
        self.video_file = video_file
        self.output_folder = output_folder
        self.frame_interval = frame_interval

    def convert(self):
        """Extracts frames from the video and saves them as images in the output folder."""
        # Ensure the output directory exists
        os.makedirs(self.output_folder, exist_ok=True)

        # Open the video file
        cap = cv2.VideoCapture(self.video_file)
        if not cap.isOpened():
            print(f"Error opening video file {self.video_file}")
            return

        frame_count = 0
        saved_frame_count = 0

        # Loop through each frame in the video
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Save every n-th frame according to the frame interval
            if frame_count % self.frame_interval == 0:
                image_path = os.path.join(
                    self.output_folder, f"frame_{saved_frame_count:04d}.file.png"
                )
                cv2.imwrite(image_path, frame)
                print(f"Saved {image_path}")
                saved_frame_count += 1

            frame_count += 1

        # Release the video capture object
        cap.release()
        print("Finished extracting frames.")
