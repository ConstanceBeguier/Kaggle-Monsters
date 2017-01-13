import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.pylab as plot

from pdb import set_trace as st

#########################################################
# Load data                                             #
#########################################################
train_df = pd.read_csv('data/train.csv', header=0)

#########################################################
# General information on columns                        #
#########################################################

# Print for each column the type and the number of non-null element
print "##### Column infos with info #####"
print train_df.info()
print

# Print for each numerical column count, mean, std, min, 25%, 50%, 75%, max
print "##### Basic statistics on numerical columns with describe #####"
print train_df.describe()
print

#########################################################
# General statistics per type of monsters               #
#########################################################

LIST_MONSTERS = train_df['type'].drop_duplicates().values
print "##### List monsters #####"
print LIST_MONSTERS

for i in range(0, len(LIST_MONSTERS)):
    print "Monsters: " + LIST_MONSTERS[i]
    print train_df[train_df['type'] == LIST_MONSTERS[i]].describe()

train_df_Ghost = train_df[train_df['type'] == 'Ghost']
train_df_Goblin = train_df[train_df['type'] == 'Goblin']
train_df_Ghoul = train_df[train_df['type'] == 'Ghoul']

# plt.scatter(x=train_df_Ghost.bone_length, y=train_df_Ghost.hair_length, s=train_df_Ghost['rotting_flesh']*200, color='DarkBlue', label='Ghost')
plt.scatter(x=train_df_Ghost['bone_length'], y=train_df_Ghost.hair_length, color='DarkBlue', label='Ghost')
plt.scatter(x=train_df_Goblin.bone_length, y=train_df_Goblin.hair_length, color='DarkGreen', label='Goblin')
plt.scatter(x=train_df_Ghoul.bone_length, y=train_df_Ghoul.hair_length, color='DarkRed', label='Ghoul')
plt.legend()
plt.show()
