#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" Some graphs on the database """

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#########################################################
# Load data                                             #
#########################################################
TRAIN_DF = pd.read_csv('data/train.csv', header=0)
COLUMNS_WO_TYPE = ['bone_length', 'rotting_flesh', 'hair_length', 'has_soul']
COLUMNS_WITH_TYPE = ['bone_length', 'rotting_flesh', 'hair_length', 'has_soul', 'type']

#########################################################
# General information on columns                        #
#########################################################

def general_info(data_df):
    """ Print general information on the database 
    - type of columns and number of non-null elements
    - basic statistics on numerical columns (global and per monster type)  """
    # Print for each column the type and the number of non-null element
    print "##### Column infos with info #####"
    print data_df.info()
    print
    # Print for each numerical column count, mean, std, min, 25%, 50%, 75%, max
    print "##### Basic statistics on numerical columns with describe #####"
    print data_df.describe()
    print
    # Print stat for each monster type
    list_monsters = data_df['type'].drop_duplicates().values
    print "##### List monsters #####"
    print list_monsters
    for i in range(0, len(list_monsters)):
        print "Monsters: " + list_monsters[i]
        print data_df[data_df['type'] == list_monsters[i]].describe()
    print

# general_info(TRAIN_DF)

#########################################################
# General graphs                                        #
#########################################################

def split_df_according_to_col(data_df, col):
    """ Split the database according to the value of one column """
    list_df = []
    values_col = list(data_df[col].unique())
    for val in values_col:
        list_df.append(data_df[data_df[col] == val])
    return list_df

# LIST_DF_TYPE = split_df_according_to_col(TRAIN_DF, "type")
# for df in LIST_DF_TYPE:
#     print df[COLUMNS_WITH_TYPE].head(5)

def save_several_boxplots(data_df, cols):
    """ Create one boxplot graph per numerical column """
    for col in cols:
        plt.clf()
        sns.boxplot(x="type", y=col, data=data_df)
        sns.swarmplot(x="type", y=col, data=data_df, color=".25")
        plt.savefig("Graphs/boxplot_" + col + ".png")

# save_several_boxplots(TRAIN_DF, COLUMNS_WO_TYPE)

def save_one_bloxplot(data_df, cols):
    """ Create one big boxplot graph with all numerical columns """
    plt.clf()
    data_df_melt = pd.melt(data_df, id_vars="type", value_vars=cols)
    sns.boxplot(x="variable", y="value", hue="type", data=data_df_melt)
    plt.legend(loc='best')
    plt.savefig("Graphs/boxplot_all.png")

# save_one_bloxplot(TRAIN_DF[COLUMNS_WITH_TYPE], COLUMNS_WO_TYPE)

def save_pairplot(data_df, cols):
    """ Create a pairplot with all numerical columns """
    plt.clf()
    sns.pairplot(data_df, vars=cols, kind='scatter', diag_kind='kde', hue="type")
    plt.savefig("Graphs/pairplot.png")

# save_pairplot(TRAIN_DF, COLUMNS_WO_TYPE)

def save_scatter_two_cols(data_df, col1, col2, labels):
    """ Create one scatter graph with col1 and col2 """
    plt.clf()
    for key, val in data_df.groupby(labels):
        plt.plot(val[col1], val[col2], label=key, linestyle="_", marker='.')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.legend(loc='best')
    plt.savefig("Graphs/scatter-" + col1 + "-" + col2 + ".png")

# save_scatter_two_cols(TRAIN_DF, "hair_length", "has_soul", "type")

#########################################################
# Modify string color columns                           #
#########################################################

def add_color_int_col(data_df):
    """ Create a new column into the database where colors are replaced by intergers """
    print "##### List of colors #####"
    print data_df['color'].unique()
    print
    list_colors = list(data_df['color'].unique())
    data_df['color_int'] = data_df['color'].map(list_colors.index)
    return data_df, list_colors

# TRAIN_DF, LIST_COLORS = add_color_int_col(TRAIN_DF)
# print LIST_COLORS
# print TRAIN_DF.head(10)

def save_countplot_color(data_df):
    """ Create a bar graph with color column """
    plt.clf()
    sns.countplot(x="color", hue="type", data=data_df)
    plt.savefig("Graphs/countplot_color.png")

# save_countplot_color(TRAIN_DF)
