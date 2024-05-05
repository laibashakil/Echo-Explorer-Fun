import streamlit as st
from gtts import gTTS
import os
import cohere
from PIL import Image
import tensorflow as tf
import numpy as np
from IPython.display import Audio

# Load the pre-trained MobileNet model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Initialize Cohere client with your trial API key
co = cohere.Client('hNTwkgKbaioZwVEbSBqI6wOcy80Dvqp6hELtMqe1')

# Function to preprocess the image and make predictions
def predict_image(image):
    # Preprocess the image
    img_array = np.array(image)
    img_array = tf.image.resize(img_array, (224, 224))
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = tf.expand_dims(img_array, 0)

    # Make predictions
    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]

    return decoded_predictions

# Function to generate description using Cohere API
def generate_description(predictions):
    labels = [label for (_, label, _) in predictions]
    input_text = f"This image contains: {', '.join(labels)}. Describe the scene."
    response = co.generate(
        prompt=input_text,
        max_tokens=100,
        temperature=0.7,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop_sequences=["\n"],
        return_likelihoods='NONE'
    )
    generated_text = response.generations[0].text.strip()
    return generated_text

# Function to convert text to speech
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("generated_description.mp3")

# Function to play the selected sound
def play_sound(audio_path):
    audio_file = open(audio_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/wav")

# Function to generate audio file from text
def generate_audio(text):
    tts = gTTS(text=text, lang='en', slow=False)
    audio_file = "audio.mp3"
    tts.save(audio_file)
    return audio_file

# Function to increase font size
if 'font_size' not in st.session_state:
    st.session_state['font_size'] = 16  # Set a default font size
def increase_font_size():
    current_font_size = st.session_state.get("font_size", 14)
    st.session_state.font_size = current_font_size + 2
    st.write("Font size increased!")
    st.write(f"Current font size: {st.session_state.font_size}px")

# Function to generate text using Cohere API
def generate_text(prompt):
    response = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=150,
        temperature=0.9,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE'
    )
    generated_text = response.generations[0].text
    return generated_text

# Function to generate description using Cohere API
def generate_description(predictions):
    labels = [label for (_, label, _) in predictions]
    input_text = f"This image contains: {', '.join(labels)}. Describe the scene."
    response = co.generate(
        prompt=input_text,
        max_tokens=100,
        temperature=0.7,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop_sequences=["\n"],
        return_likelihoods='NONE'
    )
    generated_text = response.generations[0].text.strip()
    return generated_text

# Streamlit app
def main():
    st.title("VisioFun")

    # Define page options
    pages = {
        "Homepage": homepage,
        "Describe Image": describe_image,
        "Imagine the World": visualization_helper,
        "Guess the Animal Sound": guess_animal_sound,
        "Riddles": riddles,
        "Quiz": quiz
    }

    # Sidebar navigation
    page = st.sidebar.radio("Select Page", list(pages.keys()))

    # Display the selected page
    pages[page]()

def homepage():
    st.header("Welcome to VisioFun!")
    st.write("This app is designed to provide entertainment and assistance to visually impaired individuals.")
    st.write("We understand that they also need fun and games, as well as a chance to visualize their surroundings.")
    st.write("Please use the sidebar to navigate to different sections.")

def describe_image():
    st.title("Describe Image")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Make predictions
        with st.spinner('Predicting...'):
            predictions = predict_image(image)

        # Generate description using Cohere API
        generated_description = generate_description(predictions)

        # Display the generated description
        st.subheader("Generated Description:")
        st.write(generated_description)

        # Convert text to speech
        text_to_speech(generated_description)

        audio_file = "generated_description.mp3"
        st.audio(audio_file, format='audio/mp3')

def visualization_helper():
    st.title("Imagine the World")

    # Input for user to enter the thing or place they want to visualize
    object_to_describe = st.text_input("Enter the thing or place you want to visualize:")

    # Construct the prompt with the user's input
    prompt = f"You are a blind person who needs visionary descriptions. Help me visualize {object_to_describe}. Describe the experience as if I am right there, experiencing it firsthand."

    # Generate description button
    if st.button("Generate Description"):
        if not object_to_describe:
            st.warning("Please enter the thing or place you want to visualize.")
        else:
            # Generate text description
            generated_description = generate_text(prompt)

            # Display the generated description
            st.subheader("Generated Description:")
            st.write(generated_description)

            # Convert text to speech
            text_to_speech(generated_description)

            # Play the audio
            audio_file = "generated_description.mp3"
            st.audio(audio_file, format="audio/mp3")

def guess_animal_sound():
    st.title("Guess the Animal Sound")

    st.write("Listen to each animal sound and guess which animal it is!")

    sound_dir = "animal_sounds"
    animal_sounds = os.listdir(sound_dir)

    correct_guesses = 0

    # Play each animal sound
    for i, sound_name in enumerate(animal_sounds[:4]):
        animal_name = sound_name.split(".")[0]
        st.write(f"Sound {i + 1}:")
        play_sound(os.path.join(sound_dir, sound_name))

        # User input for guessing the animal
        guess = st.text_input(f"Guess for Sound {i + 1}:")

        # Check if the guess is correct
        if guess.lower() == animal_name.lower():
            st.success("Correct!")
            correct_guesses += 1
        elif guess != "":
            st.error("Incorrect! Try again.")
            st.write(f"The correct answer was: {animal_name.capitalize()}")

    st.write(f"You got {correct_guesses} out of 4 correct.")

def riddles():
    st.title("Riddles")
    st.write("Listen to the audio riddles and type your answers below.")

    # Define riddles and quiz questions
    riddles = {
        "What has a head, a tail, is brown, and has no legs?": ["penny", "a penny"],
        "What has keys but can't open locks?": ["piano"],
        "I’m tall when I’m young, and I’m short when I’m old. What am I?": ["candle", "a candle"],
        "What comes once in a minute, twice in a moment, but never in a thousand years?": ["letter m", "the letter m", "m"]
    }

    # Iterate through each riddle
    for idx, (riddle, answers) in enumerate(riddles.items(), start=1):
        st.subheader(f"Riddle {idx}:")
        st.write(riddle)

        # Generate audio for the riddle
        audio_file = generate_audio(riddle)
        st.audio(audio_file, format='audio/mp3')

        # User input for answer with unique key
        user_answer = st.text_input(f"Your Answer for Riddle {idx}:", key=f"answer_{idx}")

        # Check user's answer when the user enters a value
        if user_answer:
            if any(answer.lower() == user_answer.lower() for answer in answers):
                st.success("Correct!")
            else:
                st.error("Incorrect! The correct answer is one of: " + ', '.join(answers))

            # Remove generated audio file
            os.remove(audio_file)

def quiz():
    st.title("Quiz Time!")
    st.write("Select the correct answer for each question.")

    # Display button to increase font size
    if st.button("Increase Font Size"):
        increase_font_size()

    # Define quiz questions
    questions = {
        "What is the capital of France?": {
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        "Which planet is known as the Red Planet?": {
            "options": ["Venus", "Mars", "Jupiter", "Mercury"],
            "correct_answer": "Mars"
        },
        "Who wrote 'To Kill a Mockingbird'?": {
            "options": ["Ernest Hemingway", "J.K. Rowling", "Harper Lee", "Stephen King"],
            "correct_answer": "Harper Lee"
        },
        "What is the chemical symbol for water?": {
            "options": ["O2", "H2O", "CO2", "NaCl"],
            "correct_answer": "H2O"
        },
        "Who is credited with discovering penicillin?": {
            "options": ["Albert Einstein", "Alexander Fleming", "Marie Curie", "Louis Pasteur"],
            "correct_answer": "Alexander Fleming"
        },
        "Which mammal can fly?": {
            "options": ["Elephant", "Bat", "Dolphin", "Giraffe"],
            "correct_answer": "Bat"
        },
        "In which year did the Titanic sink?": {
            "options": ["1918", "1914", "1912", "1916"],
            "correct_answer": "1912"
        },
        "Who painted the Mona Lisa?": {
            "options": ["Vincent van Gogh", "Michelangelo", "Pablo Picasso", "Leonardo da Vinci"],
            "correct_answer": "Leonardo da Vinci"
        },
        "What is the chemical symbol for gold?": {
            "options": ["Cu", "Ag", "Fe", "Au"],
            "correct_answer": "Au"
        },
        "Which is the largest mammal on Earth?": {
            "options": ["Hippopotamus", "Blue Whale", "African Elephant", "Giraffe"],
            "correct_answer": "Blue Whale"
        }
    }

    # Iterate through each question
    for idx, (question, data) in enumerate(questions.items(), start=1):
        st.subheader(f"Question {idx}:")
        st.markdown(f"<span style='font-size:{st.session_state.font_size}px'>{question}</span>", unsafe_allow_html=True)

        # Generate audio for the question
        audio_file = generate_audio(question)
        st.audio(audio_file, format='audio/mp3')

        # Display options
        options = data["options"]
        selected_option = st.radio(f"Options for Question {idx}:", options)

        # Check user's answer
        correct_answer = data["correct_answer"]
        button_key = f"submit_{idx}"
        if st.button("Submit", key=button_key):
            if selected_option == correct_answer:
                st.success("Correct!")
            else:
                st.error(f"Incorrect! The correct answer is: {correct_answer}")

            # Remove generated audio file
            os.remove(audio_file)

if __name__ == "__main__":
    main()
