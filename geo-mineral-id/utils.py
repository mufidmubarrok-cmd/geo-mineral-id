import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf


def set_theme_fttm():
    st.markdown("""
        <style>
            body { background-color: #f5f9ff; }
            .main { background-color: #ffffff; }
            h1, h2, h3 { color: #003c8f; }
            .stButton>button {
                background-color: #0056c7 !important;
                color: white !important;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)


def animasi_masuk():
    st.markdown("""
        <style>
        @keyframes fadeIn {
            from {opacity: 0; transform: translateY(15px);}
            to {opacity: 1; transform: translateY(0);}
        }
        .anim {
            animation: fadeIn 0.6s ease-out;
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='anim'>", unsafe_allow_html=True)


def viewer_3d_mineral():
    fig = go.Figure(data=[
        go.Surface(
            z=[[1,2,1],[2,3,2],[1,2,1]]
        )
    ])
    fig.update_layout(
        title="3D Mineral Surface",
        autosize=True,
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)


def ambil_harga(komoditas="GC=F"):
    try:
        data = yf.download(komoditas, period="1mo", interval="1d")
        return data
    except:
        return None

