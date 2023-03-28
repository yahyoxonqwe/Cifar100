import tensorflow as tf
from tensorflow import keras
import streamlit as st
import cv2
import numpy as np

st.cache_data()
with st.spinner('Model is being loaded..'):
    model = keras.models.load_model('cifar100.h5')
file = st.file_uploader("Please upload an brain scan file", type=["jpg", "png"])


if file is None:
    st.text("Please upload an image file")
else:
    image_bytes = file.read()
    image_array = np.asarray(bytearray(image_bytes), dtype=np.uint8)
    img = cv2.imdecode(image_array, 1)
    st.image(img, use_column_width=True) 
    img = cv2.resize(img, (32,32))
    img = img.astype('float32')
    img = img/255.0
    img = np.reshape(img, (1, 32, 32, 3))
    encoding = model.predict(img)  
    
    classes = ['apple','aquarium_fish','baby','bear','beaver','bed','bee','beetle','bicycle','bottle','bowl','boy','bridge',\
           'bus','butterfly','camel','can','castle','caterpillar','cattle','chair','chimpanzee','clock','cloud',\
           'cockroach','couch','cra','crocodile','cup','dinosaur','dolphin','elephant','flatfish','forest','fox','girl',\
           'hamster','house','kangaroo','keyboard','lamp','lawn_mower','leopard','lion','lizard','lobster','man',\
           'maple_tree','motorcycle','mountain','mouse','mushroom','oak_tree','orange','orchid','otter','palm_tree',\
           'pear','pickup_truck','pine_tree','plain','plate','poppy','porcupine','possum','rabbit','raccoon','ray','road',\
           'rocket','rose','sea','seal','shark','shrew','skunk','skyscraper','snail','snake','spider','squirrel',\
           'streetcar','sunflower','sweet_pepper','table','tank','telephone','television','tiger','tractor','train',\
           'trout','tulip','turtle','wardrobe','whale','willow_tree','wolf','woman','worm',
    ] 
    
    bashorat = np.argmax(encoding)
    score = encoding[0][bashorat]
    st.write("Predict  : ",classes[bashorat])
    st.write("Score : ",score)
    
    
    
