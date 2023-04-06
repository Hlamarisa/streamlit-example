from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

cars_df = pd.read_csv('cars.csv', sep =';', skiprows=[1])
st_title("Cars Data")
st_table(cars_df)
