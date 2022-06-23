import numpy as np
import pandas as pd

def main():
    print(load_data())

def load_data():
    df = pd.read_excel("./data.xlsx")

    # remove unused columns
    for label in ['#' , 'Start Date (UTC)', 'Submit Date (UTC)', 'Network ID']:
        df = df.drop(label, axis=1)

    # replace questions with more convenient, one word keys
    column_names = {'What\'s your office location': 'location', 
                    'Are you an Intern or a TDP?': 'cohort', 
                    'What year are you in school?': 'school_year', 
                    'Is the grass really greener on the other side?': 'greener', 
                    'Is a hotdog really a sandwich?': 'hotdog', 
                    'Backend or Frontend?': 'end', 
                    'Is water wet?': 'water', 
                    'Do straws have two holes or one?': 'straw', 
                    'Is it Gif or Jif?': 'moving_image', 
                    'Is cereal soup?': 'soup', 
                    'If you are at a restaurant and your waiter doesn\'t come back, are you the waiter?': 'self_service',
                    'Since tomatoes are technically fruits, does that make ketchup jam?': 'ketchup', 
                    'Does pineapple belong on pizza?': 'pineapple', 
                    'If you put one lasagna on top of another lasagna is it two lasagnas or just one big one?': 'lasagna', 
                    'Does Mike Wazowski wink or blink?': 'monsters_inc', 
                    'If you fold pizza and eat it, are you eating a sandwich?': 'pizza_fold'}
    df.rename(columns = column_names, inplace=True)

    # replace some of the data values with more convenient ones
    df['end'] = df.apply(lambda x: 'front' if x['end'] == '&lt;title&gt;Frontend&lt;/title&gt;' else 'back', axis=1)
    df['straw'] = df.apply(lambda x: 1 if x['straw'] == 'One Hole' else 2, axis=1)
    df['lasagna'] = df.apply(lambda x: 1 if x['lasagna'] == 'One Lasagna' else 2, axis=1)
    
    return df


if __name__ == '__main__':
    main()