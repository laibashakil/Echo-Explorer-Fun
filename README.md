# VisioFun

VisioFun is an interactive application designed to provide entertainment and assistance to visually impaired individuals. This project leverages various technologies to offer a range of features aimed at enhancing user experience and engagement.

## Features

### 1. Describe Image
- Upload an image and receive a descriptive text generated using a combination of machine learning and natural language processing.
- The application uses a pre-trained MobileNet model for image recognition and the Cohere API for generating textual descriptions.
- Additionally, the generated description can be converted into speech for auditory feedback.

### 2. Imagine the World
- Enter the name of an object or place you want to visualize, and the application generates a descriptive text.
- The user provides input, prompting the application to produce descriptive text using the Cohere API.
- The generated text is converted into speech for auditory output.

### 3. Guess the Animal Sound
- Listen to various animal sounds and guess the corresponding animals.
- The application provides a set of animal sounds for users to identify, enhancing auditory recognition skills.

### 4. Riddles
- Listen to audio riddles and type your answers.
- Users engage in a riddle-solving activity, enhancing cognitive abilities and critical thinking.

### 5. Quiz
- Participate in a quiz featuring multiple-choice questions.
- Users answer questions across various topics, providing an interactive learning experience.

## Usage

To use VisioFun:
1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit application by executing `streamlit run main.py`.
4. Alternatively, you can access the application through the following link: [VisioFun Web App](https://visiofun.streamlit.app/).

## Tech Stack and Technologies Used

- **Streamlit**: Framework for building interactive web applications with Python.
- **TensorFlow**: Open-source machine learning framework for image recognition tasks.
- **Cohere API**: Natural language processing API for generating descriptive text based on input prompts.
- **PIL (Python Imaging Library)**: Library for image processing tasks.
- **gTTS (Google Text-to-Speech)**: Library for converting text descriptions into speech.
- **NumPy**: Fundamental package for scientific computing in Python.
- **IPython.display**: Module for playing audio files within the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
