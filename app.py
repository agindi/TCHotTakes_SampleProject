import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def main():
    df = load_data()
    #print(df)

    #question: which types of developer are more generally dissatisfied?
    df2 = pd.DataFrame()
    
    df2['end'] = df['end']
    df2['moving_image'] = df['moving_image']

    df2['end'] = df2.apply(lambda x: 0 if x['end'] == 'back' else 1, axis=1)
    df2['moving_image'] = df2.apply(lambda x: 0 if x['moving_image'] == 'Gif' else 1, axis=1)

    print(df2)
    print(df2.corr()) 

    # adapted from example from https://matplotlib.org/
    labels = ['"Gif"', '"Jif"']
    front_vals = [len(df[(df['end'] == 'front') & (df['moving_image'] == 'Gif')]), len(df[(df['end'] == 'front') & (df['moving_image'] == 'Jif')])]
    back_vals = [len(df[(df['end'] == 'back') & (df['moving_image'] == 'Gif')]), len(df[(df['end'] == 'back') & (df['moving_image'] == 'Jif')])]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, front_vals, width, label='Frontend')
    rects2 = ax.bar(x + width/2, back_vals, width, label='Backend')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of Responses')
    ax.set_title('Are backend developers right about GIFs?')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()

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