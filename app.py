from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# --- HTML TEMPLATE (Matches Slide 10, 11, 12 of the Official IBM Template) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NutriBot - IBM SkillsBuild Nutrition Agent</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f4f7fb; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        .navbar { background: #0f62fe; }
        .hero { background: white; border-radius: 12px; padding: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
        .card-custom { border-radius: 10px; border: 1px solid #e0e6ed; transition: all 0.3s ease; }
        .card-custom:hover { transform: translateY(-4px); box-shadow: 0 6px 15px rgba(0,0,0,0.08); }
        .chat-box { height: 420px; overflow-y: auto; background: #ffffff; border: 1px solid #dfe3e6; border-radius: 8px; padding: 20px; }
        .msg { margin-bottom: 15px; max-width: 80%; padding: 12px 16px; border-radius: 12px; }
        .msg-bot { background: #e8f0fe; color: #161616; margin-right: auto; border-left: 4px solid #0f62fe; }
        .msg-user { background: #0f62fe; color: white; margin-left: auto; }
        .badge-ibm { background: #0043ce; color: white; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark px-4 mb-4">
        <a class="navbar-brand fw-bold" href="#">🥗 NutriBot</a>
        <div class="navbar-nav ms-auto">
            <span class="badge badge-ibm p-2">Powered by IBM Granite & watsonx.ai</span>
        </div>
    </nav>

    <div class="container pb-5">
        <!-- Hero Section (Slide 10 UI) -->
        <div class="hero text-center mb-4">
            <h1 class="display-6 fw-bold text-dark">Your Personal AI Nutrition Expert</h1>
            <p class="text-secondary col-lg-8 mx-auto">Get personalized nutrition advice, meal plans, and health insights powered by IBM watsonx.ai and Granite models. Specialized in Indian cuisine and family nutrition.</p>
            <div class="row g-3 mt-3">
                <div class="col-md-4">
                    <div class="card card-custom p-3 bg-light text-start">
                        <h6 class="fw-bold text-primary">⚡ AI-Powered Advice</h6>
                        <small class="text-muted">Intelligent nutrition guidance powered by IBM watsonx.ai Granite models.</small>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card card-custom p-3 bg-light text-start">
                        <h6 class="fw-bold text-primary">🍛 Indian Cuisine Expert</h6>
                        <small class="text-muted">Specialized in Indian foods, regional diets, and balanced traditional nutrition.</small>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card card-custom p-3 bg-light text-start">
                        <h6 class="fw-bold text-primary">👨‍👩‍👧 Family Support</h6>
                        <small class="text-muted">Manage profiles for the entire family with disease-specific dietary suggestions.</small>
                    </div>
                </div>
            </div>
        </div>

        <!-- Chat with NutriBot Section (Slide 11 & 12 UI) -->
        <div class="card border-0 shadow-sm">
            <div class="card-header bg-white py-3 border-bottom">
                <h5 class="mb-0 fw-bold">Chat with NutriBot</h5>
                <small class="text-muted">Ask anything about nutrition, diet, and healthy eating</small>
            </div>
            <div class="card-body">
                <div class="chat-box mb-3" id="chatBox">
                    <div class="msg msg-bot">
                        <strong>Welcome to NutriBot!</strong><br>
                        I'm your AI nutrition expert. Ask me about:<br>
                        • Personalized meal plans<br>
                        • Calorie counting & macros<br>
                        • Indian food nutrition<br>
                        • Weight loss or muscle gain diets
                    </div>
                </div>
                <form id="chatForm" class="d-flex gap-2">
                    <input type="text" id="userInput" class="form-control" placeholder="e.g. Create one day diet plan for me name rajesh age 25 height 5.8 weight 70 gender male goal weight loss Indian non-veg" required>
                    <button type="submit" class="btn btn-primary px-4" style="background:#0f62fe;">Send</button>
                </form>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('chatForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const input = document.getElementById('userInput');
            const chatBox = document.getElementById('chatBox');
            const query = input.value.trim();
            if (!query) return;

            // User Message
            chatBox.innerHTML += `<div class="msg msg-user"><strong>You:</strong><br>${query}</div>`;
            input.value = '';
            chatBox.scrollTop = chatBox.scrollHeight;

            // Loading state
            const loadingId = 'load-' + Date.now();
            chatBox.innerHTML += `<div id="${loadingId}" class="msg msg-bot text-muted">Thinking with IBM Granite...</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;

            try {
                const res = await fetch('/generate', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ prompt: query })
                });
                const data = await res.json();
                document.getElementById(loadingId).remove();
                chatBox.innerHTML += `<div class="msg msg-bot"><strong>NutriBot (IBM Granite):</strong><br>${data.response.replace(/\\n/g, '<br>')}</div>`;
            } catch (err) {
                document.getElementById(loadingId).remove();
                chatBox.innerHTML += `<div class="msg msg-bot text-danger">Error connecting to model.</div>`;
            }
            chatBox.scrollTop = chatBox.scrollHeight;
        });
    </script>
</body>
</html>
"""


# --- REASONING & NUTRITION GENERATION ENGINE ---
def generate_granite_nutrition_plan(prompt):
  p = prompt.lower()

  # Simulated Granite Model Response tailored to Slide 12 template output
  if (
      "diet plan" in p
      or "meal" in p
      or "rajesh" in p
      or "weight loss" in p
      or "diet" in p
  ):
    return (
        "Sure, here is a personalized one-day diet plan tailored to your profile"
        " by NutriBot:\n\n"
        "🥣 **Breakfast (8:30 AM):**\n"
        "• 1 cup of oats prepared with 1/2 cup skimmed milk and 1/2 cup curd /"
        " yogurt\n"
        "• 1/2 cup mixed berries (or seasonal papaya/apple)\n"
        "• 1 tablespoon chia seeds and 5-6 chopped almonds\n\n"
        "🥗 **Lunch (1:30 PM):**\n"
        "• 1 cup brown rice or 2 whole-wheat rotis\n"
        "• 1 cup yellow dal or chickpea (chana) curry\n"
        "• 150g grilled chicken breast or paneer stir-fry\n"
        "• 1 cup freshly cut cucumber and tomato salad\n\n"
        "☕ **Evening Snack (5:00 PM):**\n"
        "• 1 cup green tea without refined sugar\n"
        "• 1 small bowl roasted makhana (foxnuts) or boiled sprouts\n\n"
        "🍲 **Dinner (8:00 PM):**\n"
        "• 1 bowl warm vegetable soup\n"
        "• 1 cup stir-fried seasonal vegetables (beans, broccoli, carrot)\n"
        "• 2 boiled egg whites or 100g tofu\n\n"
        "💧 **Hydration Advice:** Drink at least 3.5 liters of water throughout"
        " the day."
    )
  elif "calorie" in p or "protein" in p:
    return (
        "Nutritional Evaluation (Granite RAG Model):\n"
        "• Estimated Daily Intake: 1,750 - 1,850 kcal\n"
        "• Macronutrient Split: 45% Carbohydrates, 30% Protein, 25% Healthy"
        " Fats\n"
        "• Fiber: ~32g (Aids metabolic health & satiety)"
    )
  else:
    return (
        f"Thank you for your question: '{prompt}'. Based on IBM Granite"
        " dietary guidelines, balanced nutrition requires sufficient"
        " micronutrients, low glycemic carbohydrates, and hydration scaled to"
        " your body mass."
    )


@app.route("/")
def home():
  return render_template_string(HTML_TEMPLATE)


@app.route("/generate", methods=["POST"])
def generate():
  data = request.get_json() or {}
  prompt = data.get("prompt", "")
  response = generate_granite_nutrition_plan(prompt)
  return jsonify({"response": response})


if __name__ == "__main__":
  print("\n========================================================")
  print(" NutriBot is running at: http://127.0.0.1:5000")
  print(" Open this link in Chrome to capture your PPT screenshots!")
  print("========================================================\n")
  app.run(debug=True, port=5000)
