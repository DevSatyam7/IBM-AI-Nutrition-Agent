# IBM-AI-Nutrition-Agent
# NutriBot: Agentic AI Nutrition Assistant 🥗🤖
An Intelligent, Multi-Agent Personalized Dietary Guidance System Powered by IBM Granite, watsonx.ai, and IBM Bob.

---

## 📌 Project Overview
- **Program:** IBM SkillsBuild for University Engagements (AICTE 2026)
- **Problem Statement No. 8:** Nutrition Agent
- **Domain:** Healthcare & Preventive Nutrition
- **Student Name:** Satyam Kumar
- **AICTE STU ID:** STU68f7c371dc3df1761067889
- **Institution:** Government Engineering College, Munger

Traditional diet tools rely on generic, static meal plans that fail to consider regional food habits, cultural preferences, and evolving health conditions. **NutriBot** leverages Agentic AI and Retrieval-Augmented Generation (RAG) to deliver dynamic, context-aware nutrition plans, meal logging, and disease-preventive advisories.

---

## 🏗️ Multi-Agent Architecture
Rather than functioning as a standard single-turn chatbot, NutriBot operates via a collaborative multi-agent workflow:
1. **Nutrition Knowledge Agent:** Retrieves verified macronutrient and micronutrient values from trusted food databases using RAG.
2. **Diet Recommendation Agent:** Generates personalized daily and weekly diet plans based on user profiles (age, BMI, fitness goal, cuisine preference).
3. **Health Advisory Agent:** Evaluates disease-specific constraints (e.g., diabetes, hypertension, cardiovascular health) for preventive care.
4. **Food Log & Feedback Agent:** Analyzes user inputs and generates real-time adjustments and calorie tracking.

---

## 🛠️ Technology Stack
- **AI Models:** IBM Granite 3.2 8B / Granite Guardian
- **Agent Orchestration:** IBM Bob & IBM watsonx Orchestrate
- **AI Platform & Inference:** IBM watsonx.ai
- **Retrieval Engine:** RAG Pipeline with Vector DB (FAISS / Chroma)
- **Application Framework:** Python, Flask, HTML5, CSS3, Bootstrap 5

---

## 📊 Sample Execution & Output
- **User Profile:** Rajesh (Age: 25, Height: 5'8", Weight: 70 kg, Goal: Weight Loss, Cuisine: Indian Non-Vegetarian)
- **Generated Plan Output:**
  - **Breakfast:** 1 cup oats + 1/2 cup skimmed milk/yogurt + mixed berries + almonds/chia seeds
  - **Lunch:** 1 cup brown rice / whole wheat roti + yellow dal / chickpea curry + grilled chicken + fresh cucumber-tomato salad
  - **Dinner:** 1 bowl vegetable soup + 2 boiled egg whites with steamed seasonal greens

---

## 📂 Repository Structure
```text
├── app.py                                   # Core Flask application and NutriBot reasoning engine
├── requirements.txt                         # Application environment dependencies
├── README.md                                # Comprehensive project documentation
├── Problem_Statement_Nutrition_Agent.pdf    # Official IBM AICTE problem statement
└── IBM_Major_Project_Presentation.pptx      # Capstone slide deck submission
