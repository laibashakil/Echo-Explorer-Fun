
# Echo Explorer Fun

This project is a Streamlit-based tool designed to enhance interaction and accessibility for the visually impaired community through audio cues and text-to-speech features. Users can engage in various activities such as guessing animal sounds, solving riddles, taking quizzes, and generating visual descriptions using text inputs.

## Features
- **Guess the Animal Sound**: Listen to animal sounds and guess the corresponding animal.
- **Riddles**: Listen to audio riddles and type your answers.
- **Quiz**: Test your knowledge with multiple-choice questions.
- **Visualization Helper**: Generate vivid descriptions of objects or places.

## Prerequisites
Before running the application, ensure you have the following dependencies installed:
- `Streamlit`
- `gTTS` (Google Text-to-Speech)
- `cohere` (Cohere API for text generation)
- Ensure Python 3.6 or higher is installed on your system.

## Setup
1. Clone this repository to your local machine.
2. Install the required dependencies using pip:

   `pip install streamlit gtts cohere`

4.  Run the application using the following command:
        
    `streamlit run app.py` 
    

## Usage

1.  Upon launching the application, navigate through different pages using the sidebar menu.
2.  Follow on-screen instructions for each activity:
    -   Listen to audio cues for guessing animal sounds and solving riddles.
    -   Select options for quiz questions.
    -   Input objects or places for visualization descriptions.
3.  Enjoy the interactive experience!

## Additional Notes

-   The application leverages the Cohere API for generating text descriptions, enhancing accessibility for visually impaired users.
-   Feel free to customize the activities, add new features, or modify the UI to suit your preferences.

## Credits

This project utilizes open-source libraries and APIs to provide a rich and engaging user experience:

-   [Streamlit](https://streamlit.io/) for building interactive web applications with Python.
-   [gTTS (Google Text-to-Speech)](https://gtts.readthedocs.io/en/latest/) for generating audio files from text.
-   [Cohere API](https://cohere.ai/) for text generation capabilities.

## License

This project is licensed under the MIT License.
