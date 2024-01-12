# Intrusion Warning

## Table of Contents
- [Pipeline](#Pipeline)
- [Installation](#Installation)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](#License)


## Pipeline 
1. Read from camera and display frame
2. Draw polygon to define restricted area
3. Define detect object
4. Detect using Yolo and find centroid
5. Check if centroids in restricted area
6. Display alert and send Telegram message

## Installation

1. Clone the repository or download the source code

        git clone https://github.com/BachNg311/Intrusion-Warning

2. Install the dependencies

        pip install -r setup.txt

3. Download file cfg, weight from https://github.com/AlexeyAB/darknet at Pre-trained models 

3. Perform any additional setup steps required, such as creating telegram bot and obtaining telegram bot tokens


## Usage 
 To run IntrusionWarning server, follow thse steps:
 1. Make sure all dependencies are downloaded
 2. Run the app

        python main.py


## Contributing
- Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. For major changes, please discuss them first in the project's issue tracker.

## License
- This project is licensed under the MIT License. You can find the full license text in the LICENSE file.