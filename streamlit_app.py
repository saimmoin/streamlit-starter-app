import streamlit as st
import PyPDF2
import google.generativeai as genai

def read_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = ""
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        return text

def configure_genai(api_key):
    genai.configure(api_key=api_key)

def generate_questions(cv_text, job_title, job_description, difficulty, experience_level, api_key):
    if not cv_text or not job_title or not job_description or not difficulty or not experience_level:
        return ["Please provide all necessary input fields: CV text, job title, job description, difficulty, and experience level."]

    configure_genai(api_key)
    defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.7,
        'candidate_count': 5,
        'top_k': 40,
        'top_p': 0.95,
        'max_output_tokens': 1024,
    }
    prompt = f"""
    Generate a set of technical and relevant interview questions based on the following information:
    
    1. CV content
    2. Job title
    3. Job description
    4. Difficulty level
    5. Experience level

    Ensure the questions are aligned with the candidate's experience, technical skills, and the specific requirements of the job. The questions should be designed to assess the candidate's knowledge and abilities in relation to the job description, with varying levels of difficulty based on the provided difficulty level.

    CV: {cv_text}
    Job Title: {job_title}
    Job Description: {job_description}
    Difficulty: {difficulty}
    Experience Level: {experience_level}
    """
    response = genai.generate_text(
        **defaults,
        prompt=prompt
    )
    questions = response.result.split('\n')
    filtered_questions = list(set(question.strip() for question in questions if question.strip()))
    return filtered_questions

def score_responses(cv_text, job_title, job_description, difficulty, experience_level, questions_and_responses, api_key):
    if not questions_and_responses:
        return "No user responses provided to score."

    configure_genai(api_key)
    defaults = {
        'model': 'models/text-bison-001',
        'temperature': 0.1,
        'candidate_count': 1,
        'top_k': 40,
        'top_p': 0.95,
        'max_output_tokens': 1024,
    }
    prompt = f"""
    Based on the following CV text, job title, job description, difficulty, experience level, and user responses, provide a detailed score and constructive feedback for the user's performance. Ensure the feedback is specific and actionable.

    CV: {cv_text}
    Job Title: {job_title}
    Job Description: {job_description}
    Difficulty: {difficulty}
    Experience Level: {experience_level}
    Questions and User Responses: {questions_and_responses}
    """
    response = genai.generate_text(
        **defaults,
        prompt=prompt
    )
    return response.result

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Barriecito&family=Dancing+Script&display=swap');

    html, body, [class*="css"]  {
        font-family: monospace;
    }
    h1, p, span, strong {
        font-family: monospace;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('Welcome to Interprep AI🎈')

st.info('**Interprep: Your Gateway to Real-World Job Success – Empowering Fresh Graduates to Ace Their Career Journey.**')

# with st.expander('Accordian'):
#   st.write('This is a text which is inside accordian.')

# with st.sidebar:
#     gender = st.radio("Select your gender:", ['Male', 'Female', 'Custom'])
#     age = st.slider("Select your age:", 18, 45)
#     profession = st.selectbox("Select your profession:", ('Data Scientist', 'Blockchain Developer', 'React Developer (Frontend)'))

# st.write('**Gender**:', gender)
# st.write('**Age**:', age)
# st.write('**Profession**:', profession)

# api_key = 'AIzaSyBn6ErvYhOqnKlx26WhcEtNt5jTQDD2DCE'
# cv_path = 'cv.pdf'
# job_title = 'Data Scientist'
# job_description = "This is a full-time on-site role for a Machine Learning Engineer at CenturionVR in Lahore. As a Machine Learning Engineer, you will be responsible for developing, implementing, and maintaining machine learning models and algorithms. You will collaborate with cross-functional teams to gather deployment information and deploy your models. You will need to train lightweight human body pose tracking models that are capable of running on mobile phones. The models will be primarily used in video game experiences made with Unity3D so while it is not required, experience with that is a plus."
# difficulty = "MEDIUM"
# experience_level = "5 years of experience"

cv_path = st.file_uploader("Upload your CV (PDF format)", type=["pdf"])
job_title = st.text_input("Job Title: ")
job_description = st.text_area("Job Description: ")
difficulty = st.selectbox("Difficulty Level", ["EASY", "MEDIUM", "HARD"], index=1)
experience_level = st.text_input("Experience Level: ")
api_key = st.text_input("API Key", type="password")


if st.button("Generate Interview Questions"):
    if cv_path:
        cv_text = read_pdf(cv_path)
        questions = generate_questions(cv_text, job_title, job_description, difficulty, experience_level, api_key)
        if not questions or "Please provide" in questions[0]:
            st.error("Error generating questions:" + questions)
        else:
            # print("Generated Questions:")
            user_responses = []
            for question in questions:
                if question.strip():
                    answer = st.text_input(question + ": ")
                    if answer:
                        user_responses.append(f"{question} {answer}")
                    else:
                        st.warning("No answer provided for this question.")

            if not user_responses:
                st.error("No valid answers were provided. Please provide answers to score.")
            else:
                questions_and_responses = "\n".join(user_responses)
                score = score_responses(cv_text, job_title, job_description, difficulty, experience_level, questions_and_responses, api_key)
                st.subheader("Score and Feedback:")
                st.write(score)
    else:
        st.error("Please upload your CV file.")
