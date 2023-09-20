# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Linear Regression model
filename = 'Batting-score-LassoReg-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

filename2 = 'Winning-model.pkl'
classifier = pickle.load(open(filename2, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
    
	return render_template('about.html')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/win')
def win():
	return render_template('winner.html')

@app.route('/score')
def score():
	return render_template('score.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    
    if request.method == 'POST':
        
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
            
        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
            
        
        Venue = request.form['venue']
        if Venue == 'M Chinnaswamy Stadium':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        elif Venue == 'Eden Gardens':
            temp_array = temp_array + [0,1,0,0,0,0,0,0]
        elif Venue == 'Feroz Shah Kotla':
            temp_array = temp_array + [0,0,1,0,0,0,0,0]
        elif Venue == 'MA Chidambaram Stadium, Chepauk':
            temp_array = temp_array + [0,0,0,1,0,0,0,0]
        elif Venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array = temp_array + [0,0,0,0,1,0,0,0]
        elif Venue == 'Wankhede Stadium':
            temp_array = temp_array + [0,0,0,0,0,1,0,0]
        elif Venue == 'Sawai Mansingh Stadium':
            temp_array = temp_array + [0,0,0,0,0,0,1,0]
        elif Venue == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array = temp_array + [0,0,0,0,0,0,0,1]
        
        
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp_array])
        my_prediction = int(regressor.predict(data)[0])
              
        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)

@app.route('/predict2', methods=['POST'])
def predict2():
    temp_array2 = list()
    
    if request.method == 'POST':
        
        team1 = request.form['team1']
        if team1 == 'Chennai Super Kings':
            temp_array2 = temp_array2 + [5]
        elif team1 == 'Delhi Daredevils':
            temp_array2 = temp_array2 + [7]
        elif team1 == 'Kings XI Punjab':
            temp_array2 = temp_array2 + [9]
        elif team1 == 'Kolkata Knight Riders':
            temp_array2 = temp_array2 + [2]
        elif team1 == 'Mumbai Indians':
            temp_array2 = temp_array2 + [1]
        elif team1 == 'Rajasthan Royals':
            temp_array2 = temp_array2 + [6]
        elif team1 == 'Royal Challengers Bangalore':
            temp_array2 = temp_array2 + [3]
        elif team1 == 'Sunrisers Hyderabad':
            temp_array2 = temp_array2 + [10]
            
            
        team2 = request.form['team2']
        if team2 == 'Chennai Super Kings':
            temp_array2 = temp_array2 + [5]
        elif team2 == 'Delhi Daredevils':
            temp_array2 = temp_array2 + [7]
        elif team2 == 'Kings XI Punjab':
            temp_array2 = temp_array2 + [9]
        elif team2 == 'Kolkata Knight Riders':
            temp_array2 = temp_array2 + [2]
        elif team2 == 'Mumbai Indians':
            temp_array2 = temp_array2 + [1]
        elif team2 == 'Rajasthan Royals':
            temp_array2 = temp_array2 + [6]
        elif team2 == 'Royal Challengers Bangalore':
            temp_array2 = temp_array2 + [3]
        elif team2 == 'Sunrisers Hyderabad':
            temp_array2 = temp_array2 + [10]
            
        
        Venue = request.form['venue']
        if Venue == 'M Chinnaswamy Stadium':
            temp_array2 = temp_array2 + [14]
        elif Venue == 'Eden Gardens':
            temp_array2 = temp_array2 + [7]
        elif Venue == 'Feroz Shah Kotla':
            temp_array2 = temp_array2 + [8]
        elif Venue == 'MA Chidambaram Stadium, Chepauk':
            temp_array2 = temp_array2 + [15]
        elif Venue == 'Punjab Cricket Association Stadium, Mohali':
            temp_array2 = temp_array2 + [22]
        elif Venue == 'Wankhede Stadium':
            temp_array2 = temp_array2 + [34]
        elif Venue == 'Sawai Mansingh Stadium':
            temp_array2 = temp_array2 + [26]
        elif Venue == 'Rajiv Gandhi International Stadium, Uppal':
            temp_array2 = temp_array2 + [23]
        
        Toss_winner = request.form['toss_winner']
        if Toss_winner == 'Chennai Super Kings':
            temp_array2 = temp_array2 + [5]
        elif Toss_winner == 'Delhi Daredevils':
            temp_array2 = temp_array2 + [7]
        elif Toss_winner == 'Kings XI Punjab':
            temp_array2 = temp_array2 + [9]
        elif Toss_winner == 'Kolkata Knight Riders':
            temp_array2 = temp_array2 + [2]
        elif Toss_winner == 'Mumbai Indians':
            temp_array2 = temp_array2 + [1]
        elif Toss_winner == 'Rajasthan Royals':
            temp_array2 = temp_array2 + [6]
        elif Toss_winner == 'Royal Challengers Bangalore':
            temp_array2 = temp_array2 + [3]
        elif Toss_winner == 'Sunrisers Hyderabad':
            temp_array2 = temp_array2 + [10]      

        City = request.form['city']
        if City == 'Kolkata':
            temp_array2 = temp_array2 + [21]
        elif City == 'Delhi':
            temp_array2 = temp_array2 + [9]
        elif City == 'Bangalore':
            temp_array2 = temp_array2 + [2]
        elif City == 'Chennai':
            temp_array2 = temp_array2 + [7]
        elif City == 'Jaipur':
            temp_array2 = temp_array2 + [16]
        elif City == 'Chandigarh':
            temp_array2 = temp_array2 + [6]
        elif City == 'Hyderabad':
            temp_array2 = temp_array2 + [14]
        elif City == 'Mumbai':
            temp_array2 = temp_array2 + [22]
        
        Toss_Decision = request.form['toss_decision']
        if Toss_Decision == 'bat':
            temp_array2 = temp_array2 + [0]
        elif Toss_Decision == 'ball':
            temp_array2 = temp_array2 + [1]

 
        data = np.array([temp_array2])
        my_prediction = int(classifier.predict(data)[0])

        if my_prediction == 1:
            a = "Mumbai Indians"
        elif my_prediction == 2:
            a = "Kolkata Knight Riders"
        elif my_prediction == 3:
            a = "Royal Challengers Bangalore"
        elif my_prediction == 5:
            a = "Chennai Super Kings"
        elif my_prediction == 6:
            a = "Rajasthan Royals"
        elif my_prediction == 7:
            a = "Delhi Daredevils"
        elif my_prediction == 9:
            a = "Kings XI Punjab"
        elif my_prediction == 10:
            a = "Sunrisers Hyderabad"

        return render_template('result2.html', team_name = a)

@app.route('/back')
def back():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)