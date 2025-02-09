from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session tracking

# Choices for Rock Paper Scissors
CHOICES = ["Rock", "Paper", "Scissors"]

# Home route to serve HTML file
@app.route("/")
def home():
    session.clear()  # Reset session data on new visit
    return render_template("index.html")

# Start the game by setting the total rounds
@app.route("/start_game", methods=["POST"])
def start_game():
    data = request.json
    session["total_rounds"] = int(data.get("rounds"))
    session["current_round"] = 0
    session["player_score"] = 0
    session["computer_score"] = 0
    return jsonify({"message": "Game started!", "total_rounds": session["total_rounds"]})

# API route to handle game logic
@app.route("/play", methods=["POST"])
def play():
    if "total_rounds" not in session:
        return jsonify({"error": "Game not started"}), 400

    data = request.json
    player_choice = data.get("choice")
    computer_choice = random.choice(CHOICES)

    # Determine the round winner
    if player_choice == computer_choice:
        result = "Draw"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "Player Wins"
        session["player_score"] += 1
    else:
        result = "Computer Wins"
        session["computer_score"] += 1

    session["current_round"] += 1
    is_game_over = session["current_round"] >= session["total_rounds"]

    # Determine final winner if game is over
    final_winner = None
    if is_game_over:
        if session["player_score"] > session["computer_score"]:
            final_winner = "Player"
        elif session["computer_score"] > session["player_score"]:
            final_winner = "Computer"
        else:
            final_winner = "Draw"

    return jsonify({
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "result": result,
        "current_round": session["current_round"],
        "total_rounds": session["total_rounds"],
        "player_score": session["player_score"],
        "computer_score": session["computer_score"],
        "is_game_over": is_game_over,
        "final_winner": final_winner
    })

if __name__ == "__main__":
    app.run(debug=True)