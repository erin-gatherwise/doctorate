import streamlit as st

def data_entry_form():
    st.title("COVID-19 Social Media Usage Survey")
    st.write("Thank you for your willingness to participate in our survey. Your answers will help us understand more about social media and information. Please answer the questions based on your experiences during the height of the COVID-13 pandemic, in 2020-2021. Note that some of the later questions are populated by your early answers so please do the questions in order, thank you!")

    # Question 1
    st.subheader("How often did you use the following social media for COVID-related information during the pandemic (e.g. 2020-2021)?")

    social_networks = [
        "Facebook",
	"Instagram",
	"LinkedIn",
        "Pinterest",
        "Reddit",
        "TikTok",
        "Twitch",
        "Twitter",
        "YouTube",
        "WhatsApp",
        "Other",
    ]
    
    frequency_options = {
        "Never": 0,
        "Rarely / Less than once a month": 1,
        "Sometimes / 1 time per month": 2,
        "Somewhat Often / 2-3 times a month": 3,
        "Often / once a week": 4,
        "Very Often / 2-3 times per week": 5,
        "Always / Daily": 6
    }

    frequency_ratings = {}
    for network in social_networks:
        frequency_ratings[network] = st.selectbox(f"{network}", list(frequency_options.keys()))

    # Question 2
    st.subheader("For those you reported using, how satisfied were you with the COVID-related information you received?")

    satisfaction_options = {
        "Very Dissatisfied": 1,
        "Dissatisfied": 2,
        "Neutral": 3,
        "Satisfied": 4,
        "Very Satisfied": 5
    }

    satisfaction_ratings = {}
    for network, frequency_str in frequency_ratings.items():
        frequency = frequency_options[frequency_str]  # Convert frequency to integer
        if frequency > 0:
            satisfaction_ratings[network] = st.selectbox(f"{network}", list(satisfaction_options.keys()))

    # Question 3
    st.subheader("For the social media that you reported using, rate the following statements:")

    quality_options = {
        "Never": 1,
        "Not often": 2,
        "Sometimes": 3,
        "Often": 4,
        "Always": 5
    }

    quality_ratings = {}
    for network, frequency_str in frequency_ratings.items():
        frequency = frequency_options[frequency_str]  # Convert frequency to integer
        if frequency > 0:
            quality_ratings[network] = {}
            for quality in ["The information I received was accurate", "The information I received was up-to-date", "The information I received was relevant to me", "The information helped me", "I trusted the information"]:
                quality_ratings[network][quality] = st.selectbox(f"{network}: {quality}.", list(quality_options.keys()))

    # Question 4
    st.subheader("Which of the following challenges did you encounter with the information about COVID-19 that you received via social media?")

    challenge_options = {
         "Never": 1,
         "Not often": 2,
         "Sometimes": 3,
         "Often": 4,
         "Always": 5
    }

    challenges = ["Media access problems", "Unreliable information", "Fake news spreading", "Information overload", "Contradictions in information", "Science denial groups/movements", "Inconsistent information", "Fear mongering", "Famous people such as politicians, celebrities or influencers who deny science", "Confusing medical terms", "Information that was unusable to me"]
    challenge_ratings = {}
    for challenge in challenges:
        challenge_ratings[challenge] = st.selectbox(f"{challenge}", list(challenge_options.keys()))

    challenge_ratings["Other"] = st.text_input("Please specify any other challenges you encountered:")

    # Question 5
    st.subheader("Please provide any explanation for or commentary on your answers above.")
    commentary = st.text_area("Your comments:")
    
    # Demographic Questions
    st.subheader("Demographic Information")
    gender_options = ["Male", "Female", "Non-binary"]
    gender = st.selectbox("What is your gender?", gender_options)

    race_options = ["American Indian or Alaskan Native", "Asian / Pacific Islander", "Black or African American", "Hispanic", "White / Caucasian", "Multiple ethnicity / Other"] 

    race = st.selectbox("Which race or ethnicity best describes you?", race_options)
    if race == "Multiple ethnicity / Other":
        race_other = st.text_input("Please specify:")

    age_options = ["Under 18", "18-22", "23-30", "31-40", "41-50", "51-60", "61-70", "Over 70"]
    age = st.selectbox("What is your age?", age_options)

    education_options = ["Less than high school", "High school graduate or equivalent (GED)", "Some college credit, no degree, currently a student", "Some college credit, no degree, not currently a student", "Bachelor's degree", "Master's degree", "PhD or higher", "Trade/technical/vocational school", "Prefer not to say"]
    education = st.selectbox("What is the highest degree or school level you have completed?", education_options)

    # Submit button
    if st.button("Submit"):
        # Process the data (e.g., save to a CSV file)
        print(frequency_ratings)
        print(satisfaction_ratings)
        print(quality_ratings)
        print(challenge_ratings)
        print(commentary)
        print(gender)
        print(race)
        if race == "Multiple ethnicity / Other":
            print(race_other)
        print(age)
        print(education)

if __name__ == "__main__":
        data_entry_form()
