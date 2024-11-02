import streamlit as st
import datetime  # Import the datetime module

def data_entry_form():
    st.title("COVID-19 Social Media Usage Survey")
    st.write("Thank you for your willingness to participate in our survey. Your answers will help us understand more about social media and information. Please answer the questions based on your experiences during the height of the COVID-13 pandemic, in 2020-2021. Note that some of the later questions are populated by your early answers so please do the questions in order, thank you!")

    # Consent statement
    st.write("**Informed Consent** I am a doctoral student at the School of Information Studies at Syracuse University enrolled in IST 776: Research Methods in Information Science and Technology. I am inviting you to participate in a survey I am running for learning purposes only. Involvement in the survey is voluntary, so you may choose to participate or not. The survey will ask you about your use of social media for COVID-related information. I expect this survey to take a few minutes to complete. This survey is an opportunity to give students experience in developing and administering a survey and is not part of a formal research project. The results of the survey will not be shared in any public venue. No personally identifiable information will be collected and the information you provide will be kept strictly confidential. Only the course instructor and I will have access to the information you provide. I will delete your responses at the end of the semester. Please feel free to ask questions about the survey and this activity. I will be happy to explain anything in detail. There are no known risks to your participation in this study. You may refuse to participate, refuse to answer any question, and withdraw at any time with no negative effect. Please note that if you decide not to participate or to withdraw from the survey, my grade in the course will not be affected. If you have any questions, concerns, or complaints about this activity, please contact the course instructor, Dr. Kevin Crowston (crowston@syr.edu). **By continuing to fill out the survey, you are indicating your consent to participate.**")
        
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
        "": 0,
        "Never": 1,
        "Rarely / Less than once a month": 2,
        "Sometimes / 1 time per month": 3,
        "Somewhat Often / 2-3 times a month": 4,
        "Often / once a week": 5,
        "Very Often / 2-3 times per week": 6,
        "Always / Daily": 7
    }

    frequency_ratings = {}
    for network in social_networks:
        frequency_ratings[network] = st.selectbox(f"{network}", list(frequency_options.keys()), index=0)

    # Question 2
    st.subheader("For those you reported using, how satisfied were you with the COVID-related information you received?")

    satisfaction_options = {
        "": 0,
        "Very Dissatisfied": 1,
        "Dissatisfied": 2,
        "Neutral": 3,
        "Satisfied": 4,
        "Very Satisfied": 5
    }

    satisfaction_ratings = {}
    for network, frequency_str in frequency_ratings.items():
        frequency = frequency_options[frequency_str]  # Convert frequency to integer
        if frequency > 1:
            satisfaction_ratings[network] = st.selectbox(f"{network}", list(satisfaction_options.keys()), index=0)

    # Question 3
    st.subheader("For the social media that you reported using, rate the following statements:")

    quality_options = {
        "": 0,
        "Never": 1,
        "Not often": 2,
        "Sometimes": 3,
        "Often": 4,
        "Always": 5
    }

    quality_ratings = {}
    for network, frequency_str in frequency_ratings.items():
        frequency = frequency_options[frequency_str]  # Convert frequency to integer
        if frequency > 1:
            quality_ratings[network] = {}
            for quality in ["The information I received was accurate", "The information I received was up-to-date", "The information I received was relevant to me", "The information helped me", "I trusted the information"]:
                quality_ratings[network][quality] = st.selectbox(f"{network}: {quality}.", list(quality_options.keys()), index=0)

    # Question 4
    st.subheader("Which of the following challenges did you encounter with the information about COVID-19 that you received via social media?")

    challenge_options = {
         "": 0,
         "Never": 1,
         "Not often": 2,
         "Sometimes": 3,
         "Often": 4,
         "Always": 5
    }

    challenges = ["Media access problems", "Unreliable information", "Fake news spreading", "Information overload", "Contradictions in information", "Science denial groups/movements", "Inconsistent information", "Fear mongering", "Famous people such as politicians, celebrities or influencers who deny science", "Confusing medical terms", "Information that was unusable to me"]
    challenge_ratings = {}
    for challenge in challenges:
        challenge_ratings[challenge] = st.selectbox(f"{challenge}", list(challenge_options.keys()), index=0)

    challenge_ratings["Other"] = st.text_input("Please specify any other challenges you encountered:")

    # Question 5
    st.subheader("Please provide any explanation for or commentary on your answers above.")
    commentary = st.text_area("Your comments:")
    
    # Demographic Questions
    st.subheader("Demographic Information")
    gender_options = ["", "Male", "Female", "Non-binary"]
    gender = st.selectbox("What is your gender?", gender_options, index=0)

    race_options = ["", "American Indian or Alaskan Native", "Asian / Pacific Islander", "Black or African American", "Hispanic", "White / Caucasian", "Multiple ethnicity / Other"] 

    race = st.selectbox("Which race or ethnicity best describes you?", race_options, index=0)
    if race == "Multiple ethnicity / Other":
        race_other = st.text_input("Please specify:")

    age_options = ["", "Under 18", "18-22", "23-30", "31-40", "41-50", "51-60", "61-70", "Over 70"]
    age = st.selectbox("What is your age?", age_options, index=0)

    education_options = ["", "Less than high school", "High school graduate or equivalent (GED)", "Some college credit, no degree, currently a student", "Some college credit, no degree, not currently a student", "Bachelor's degree", "Master's degree", "PhD or higher", "Trade/technical/vocational school", "Prefer not to say"]
    education = st.selectbox("What is the highest degree or school level you have completed?", education_options, index=0)

    # Submit button
    if st.button("Submit"):
        # Generate a unique filename based on timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"survey_response_{timestamp}.txt"

        with open(filename, "w") as f:
            f.write("New Survey Response\n")
            f.write("Social Media Usage:\n")
            for network, frequency in frequency_ratings.items():
                f.write(f"- {network}: {frequency}\n")

            f.write("\nSatisfaction with Information:\n")
            for network, satisfaction in satisfaction_ratings.items():
                f.write(f"- {network}: {satisfaction}\n")

            f.write("\nInformation Quality Ratings:\n")
            for network, ratings in quality_ratings.items():
                for quality, rating in ratings.items():
                    f.write(f"- {network}: {quality} - {rating}\n")

            f.write("\nChallenges Encountered:\n")
            for challenge, rating in challenge_ratings.items():
                f.write(f"- {challenge}: {rating}\n")

            f.write("\nAdditional Comments:\n")
            f.write(commentary + "\n")

            f.write("\nDemographic Information:\n")
            f.write(f"- Gender: {gender}\n")
            f.write(f"- Race/Ethnicity: {race}\n")
            if race == "Multiple ethnicity / Other":
                f.write(f"  - Other: {race_other}\n")
            f.write(f"- Age: {age}\n")
            f.write(f"- Education: {education}\n\n")

        st.success("Thank you for your participation!")

if __name__ == "__main__":
        data_entry_form()
