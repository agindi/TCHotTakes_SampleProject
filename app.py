import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

def main():
    df = load_data()
    print(df)

    #question: Does time at the bank make you confused about sandwiches?
    df2 = pd.DataFrame()
    
    df2['cohort'] = df['cohort'] #df[df.cohort.isin(['2021 TDP', '2020 TDP'])]['cohort']
    df2['hotdog_correct'] = 1 - df['hotdog']
    df2['pizza_fold_correct'] = 1 - df['pizza_fold']
    df2['sandwich_confusion_score'] = 2 - df2['hotdog_correct'] - df2['pizza_fold_correct']

    #df2['cohort'] = df2.apply(lambda x: 1 if x['cohort'] == '2021 TDP' el x['cohort'] == '2020 TDP'] 2 else 0, axis=1)
    def time_at_bank(x):
        if x == '2021 TDP':
            return 1
        elif x == '2020 TDP':
            return 2
        else:
            return 0
    
    df2['time_at_bank'] = df2['cohort'].apply(time_at_bank)
    
    print(df2)
    print(df2.corr()) 

    display_visual(df2)

def display_visual(df):
    # look at examples from https://matplotlib.org/
    labels = [ 'New', '1 Year', '2 Years']

    totals_time = [len(df[df['time_at_bank'] == i]) for i in range(0, 3)]

    very_conf_vals = [len(df[(df['sandwich_confusion_score'] == 2) & (df['time_at_bank'] == i)]) for i in range(0, 3)]
    lil_conf_vals =  [len(df[(df['sandwich_confusion_score'] == 1) & (df['time_at_bank'] == i)]) for i in range(0, 3)]
    not_conf_vals =  [len(df[(df['sandwich_confusion_score'] == 0) & (df['time_at_bank'] == i)]) for i in range(0, 3)]

    for i in range(0, 3):
        very_conf_vals[i] = very_conf_vals[i] / totals_time[i]
        lil_conf_vals[i] = lil_conf_vals[i] / totals_time[i]
        not_conf_vals[i] = not_conf_vals[i] / totals_time[i]

    width = 0.35       # the width of the bars: can also be len(x) sequence

    _, ax = plt.subplots()

    ax.bar(labels, very_conf_vals, width, bottom=[lil_conf_vals[i] + not_conf_vals[i] for i in range(0,3)], label='Very Confused')
    ax.bar(labels, lil_conf_vals, width, bottom=not_conf_vals, label='Somewhat Confused')
    ax.bar(labels, not_conf_vals, width, label='Not Confused')

    ax.set_ylabel('Proportion Confused')
    ax.set_title('Sandwich Confusion vs. Time Spent at M&T')
    ax.legend()

    plt.show()

def normalize(a):
    sum_a = sum(a)
    return [i / sum_a for i in a]

def load_data():
    df = pd.read_csv("./data.csv")

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