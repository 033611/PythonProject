import streamlit as st
import time

# Page configuration
st.set_page_config("Study-Route-Map", page_icon="✍")

# Custom CSS for animations, styling, and transitions
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

body {
    font-family: 'Poppins', sans-serif;
    background-color: #f0f2f6;
}

.stButton>button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    background-color: #45a049;
    transform: scale(1.05);
}

.stTextInput>div>div>input, .stTextArea>div>div>textarea {
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 10px;
    transition: all 0.3s ease;
}

.stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
    border-color: #4CAF50;
    box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
}

.stSuccess {
    background-color: #d4edda;
    color: #155724;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #c3e6cb;
    transition: all 0.3s ease;
    animation: slideUp 0.5s ease-out;
}

.stWarning {
    background-color: #fff3cd;
    color: #856404;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ffeeba;
    transition: all 0.3s ease;
    animation: slideDown 0.5s ease-out;
}

.stInfo {
    background-color: #d1ecf1;
    color: #0c5460;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #bee5eb;
    transition: all 0.3s ease;
    animation: slideUp 0.5s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fadeIn {
    animation: fadeIn 1s ease-in;
}

@keyframes slideUp {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

@keyframes slideDown {
    from { transform: translateY(-20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.emoji {
    font-size: 24px;
    margin-right: 10px;
}
</style>
""", unsafe_allow_html=True)

# Header with animation
st.markdown("<h1 class='fadeIn'>Your Path to Success 🏆</h1>", unsafe_allow_html=True)
st.write("**A Study Route Map is a structured plan that outlines the steps and resources needed to achieve academic goals efficiently 🗺️📚✏️**")
st.markdown("<h2 class='fadeIn'>Study without desire spoils the memory, and it retains nothing that it takes in. Leonardo da Vinci</h2>", unsafe_allow_html=True)

# Section for difficulties
st.markdown("<h2 class='fadeIn'>What is Your Difficulties face in Your Study Route Map? ❓🤔😕</h2>", unsafe_allow_html=True)
user_input = st.text_input("Please Explain Your Problems or Difficulties You are Facing During Your Study Route Map? ❓🤔😕")

if user_input:
    time.sleep(1)  # Delay for 1 second
    st.success(f"""A well-planned study timetable is your secret weapon—stick to it, stay disciplined, and watch yourself achieve greatness! ⏳📚✨

Success follows those who respect their time—create a study route map, set your timetable, and make every second count!🕰️🎯

Your timetable is your roadmap to success—follow it with dedication, and no goal will be too far to reach!🏆🛤️

A perfect study timetable is not about studying all day; its about studying smart—balance your time, stay consistent, and keep moving forward! 📖⚖️""")
else:
    st.warning(f"Ignoring your study difficulties can lead to bigger challenges—address them now before they become roadblocks to success! ⚠️🚧")

# Section for recent problems
st.markdown("<h2 class='fadeIn'>What is Your Recently Facing Problem in Study? ❓🤔😕</h2>", unsafe_allow_html=True)
reflection = st.text_area("Please Tell me In Depth What is Your Current Problem Facing in Study? ❓🤔😕")

if reflection:
    time.sleep(1)  # Delay for 1 second
    st.success(f"""2️ Procrastination ⏳😴
Problem: Delaying study sessions and cramming at the last moment.
Solution: Set small, achievable goals, create a realistic timetable, reward yourself for completing tasks, and remind yourself of the bigger picture—your future success!

3️ Difficulty in Understanding Concepts 🤯📖
Problem: Struggling with tough subjects or topics.
Solution: Break concepts into smaller parts, use visual aids (diagrams, mind maps), watch educational videos, and seek help from teachers or friends.

4️ Time Management Issues 🕰️📚
Problem: Not having enough time to cover all subjects properly.
Solution: Plan a daily study schedule, prioritize important topics, avoid multitasking, and track your progress to stay on schedule.""")
else:
    time.sleep(1)  # Delay for 1 second
    st.info(f"Demotivation: You feel frustrated because you waste time and achieve nothing. 🙇‍♂️")

# Section for achievements
st.markdown("<h2 class='fadeIn'>What is achievements when you read the following lines or sentences related to study? ❓</h2>", unsafe_allow_html=True)
user_input_achievements = st.text_input("Enter your thoughts here")

if user_input_achievements:
    time.sleep(1)  # Delay for 1 second
    st.success(f"""1️⃣ "Knowledge is power.📚⚡
✅ Achievement: You become confident, well-informed, and capable of making smart decisions in life.

2️⃣ "Success is the sum of small efforts repeated daily. 🔄🎯
✅ Achievement: Consistency in studying helps you master difficult subjects and improve your grades.

3️⃣ "Your future is created by what you do today, not tomorrow. ⏳🏆
✅ Achievement: You develop time management skills, avoid procrastination, and stay ahead in studies.

4️⃣ "The expert in anything was once a beginner. 🌱🎓
✅ Achievement: You gain patience and resilience, understanding that hard work and practice lead to mastery.

5️⃣ "There are no secrets to success. It is the result of preparation, hard work, and learning from failure. 💪📖
✅ Achievement: You develop a growth mindset, learning from mistakes instead of fearing failure.

6️⃣ "Study while others are sleeping, work while others are loafing, prepare while others are playing, and dream while others are wishing. 🌙📚
✅ Achievement: You build discipline and achieve academic excellence, standing out from the rest.

7️⃣ "Don’t stop until you’re proud. 🏅🔥
✅ Achievement: You push yourself beyond limits and reach your true potential in studies and beyond.

8️⃣ "Difficult roads often lead to beautiful destinations. 🛤️🌄
✅ Achievement: Overcoming study challenges gives you the confidence and skills needed for real-life success.

9️⃣ "Live as if you were to die tomorrow. Learn as if you were to live forever. 💡🔁
✅ Achievement: You develop a lifelong love for learning, making you more adaptable and wise in every situation.

🔟 "Hard work beats talent when talent doesn’t work hard. 🏋️‍♂️📖
✅ Achievement: You realize that dedication and persistence are more important than natural ability.""")
else:
    st.warning(f"Nothing")

# Footer
st.write("- - -")
st.write("""**⚠︎ Created By Muhammad-Saad-Khan**""")