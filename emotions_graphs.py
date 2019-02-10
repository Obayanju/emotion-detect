# -*- coding: utf-8 -*-
"""
Displaying the emotion profile graphs at two snapshots in time as evaluated by emo_detect.py 
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.image as mpimg

 
emotions = ('Anger', 'Joy', 'Surprise', 'Sorrow')
y_pos = np.arange(len(objects))
performance1 = [4, 0, 0, 2]

fig1 = plt.bar(y_pos, performance1, align='center', alpha=0.5)
plt.xticks(y_pos, emotions)
plt.ylabel('Magtitude')
plt.title('Emotion Profile')
 
plt.show()
plt.savefig('/home/roshnib/Emotions/Emotion_profile1.png', dpi=100)
plt.savefig('/home/roshnib/Emotions/Emotion_profile1.pdf')



performance2 = [0, 4, 3, 1]
fig2 = plt.bar(y_pos, performance2, align='center', alpha=0.5)
plt.xticks(y_pos, emotions)
plt.ylabel('Magtitude')
plt.title('Emotion Profile')
 
plt.show()
plt.savefig('/home/roshnib/Emotions/Emotion_profile2.png', dpi=100)
plt.savefig('/home/roshnib/Emotions/Emotion_profile2.pdf')
