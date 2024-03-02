#!/path/to/python/interpreter

from joblib import load
import pandas as pd

# Load the model
model = load('fm24_model.joblib')

abbreviations_mapping = {
    'Corners': 'Cor',
    'Crossing': 'Cro',
    'Dribbling': 'Dri',
    'Finishing': 'Fin',
    'First Touch': 'Fir',
    'Free Kick Taking': 'Fre',
    'Heading': 'Hea',
    'Long Shots': 'Lon',
    'Long Throws': 'L Th',
    'Marking': 'Mar',
    'Passing': 'Pas',
    'Penalty Taking': 'Pen',
    'Tackling': 'Tck',
    'Technique': 'Tec',
    'Aggression': 'Agg',
    'Anticipation': 'Ant',
    'Bravery': 'Bra',
    'Composure': 'Com',
    'Concentration': 'Con',
    'Decisions': 'Dec',
    'Determination': 'Det',
    'Flair': 'Fla',
    'Leadership': 'Ldr',
    'Off The Ball': 'OtB',
    'Positioning': 'Pos',
    'Teamwork': 'Tea',
    'Vision': 'Vis',
    'Work Rate': 'Wor',
    'Acceleration': 'Acc',
    'Agility': 'Agi',
    'Balance': 'Bal',
    'Jumping Reach': 'Jum',
    'Natural Fitness': 'Nat',
    'Pace': 'Pac',
    'Stamina': 'Sta',
    'Strength': 'Str'
}

player_attributes = {
    'Corners': 12,
    'Crossing': 12,
    'Dribbling': 12,
    'Finishing': 15,
    'First Touch': 14,
    'Free Kick Taking': 12,
    'Heading': 12,
    'Long Shots': 11,
    'Long Throws': 3,
    'Marking': 8,
    'Passing': 13,
    'Penalty Taking': 12,
    'Tackling': 7,
    'Technique': 14,
    'Aggression': 12,
    'Anticipation': 14,
    'Bravery': 13,
    'Composure': 14,
    'Concentration': 11,
    'Decisions': 11,
    'Determination': 12,
    'Flair': 15,
    'Leadership': 14,
    'Off The Ball': 16,
    'Positioning': 8,
    'Teamwork': 15,
    'Vision': 15,
    'Work Rate': 15,
    'Acceleration': 9,
    'Agility': 11,
    'Balance': 14,
    'Jumping Reach': 10,
    'Natural Fitness': 11,
    'Pace': 8,
    'Stamina': 12,
    'Strength': 12
}

def get_abbreviation(attribute_value):
    for key, value in player_attributes.items():
        if value == attribute_value:
            return abbreviations_mapping[key]
    return None

# Example usage
attribute_value = 12
abbreviation = get_abbreviation(attribute_value)
print("Abbreviation for value", attribute_value, "is", abbreviation)

# Create a DataFrame with your input data
input_df = pd.DataFrame([input_data])

# Make prediction
predicted_ca = model.predict(input_df)


print("Predicted Current Ability (CA):", predicted_ca)