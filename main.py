import pandas as pd
import numpy as np
import streamlit as st
import pickle


st.write('  # **Bosten House Predictor MOdel** \n'
        'this Model predicts the price in **BOSTEN**')


st.sidebar.header(' #INPUT PARAMETERS FOR PRICING OF HOUSE')

def input_data():
        UNDER_CONSTRUCTION=st.sidebar.slider('UNDER_CONSTRUCTION',0, 1,0)
        RERA=              st.sidebar.slider('RERA',0,1,0)
        BHK_NO=            st.sidebar.slider('BHK_NO.',1.0,20.0,2.3922)
        SQUARE_FT=         st.sidebar.slider('SQUARE_FT',3.0,2545.5,19802.17)
        READY_TO_MOVE=     st.sidebar.slider('READY_TO_MOVE',0,1,0)
        RESALE=            st.sidebar.slider('RESALE',0,1, 0)
        LONGITUDE=         st.sidebar.slider('LONGITUDE', -37.7130075 ,59.912884 ,21.300255165028354)
        LATITUDE=          st.sidebar.slider('LATITUDE', -121.7612481 ,152.962676, 76.83769524877074)

        features= {'UNDER_CONSTRUCTION':UNDER_CONSTRUCTION,
                   'RERA':RERA,
                   'BHK_NO':BHK_NO,
                   'SQUARE_FT':SQUARE_FT,
                   'READY_TO_MOVE':READY_TO_MOVE,
                   'RESALE':RESALE,
                   'LONGITUDE':LONGITUDE,
                   'LATITUDE':LATITUDE}
        df=pd.DataFrame(features,index=[0])
        return df
data=input_data()

st.subheader(' # Data_Entries')
st.write(data)

model=pickle.load(open('Bosten_Predictor.pkl','rb'))


predictions=model.predict(data)

st.subheader('# Value__PREDICTED ')
st.write(predictions)