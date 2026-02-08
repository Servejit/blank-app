# streamlit_app.py

import streamlit as st
import yfinance as yf
import pandas as pd

# -----------------------------------
# PAGE CONFIG
st.set_page_config(page_title="Live Stock P2L Tracker", layout="wide")
st.title("📊 Live Stock P2L Tracker")

# -----------------------------------
# FULL STOCK LIST
stocks = {
    "AMBUJACEM.NS": 492.12, "BAJAJFINSV.NS": 1867.22, "BAJAJHLDNG.NS": 10348.00,
    "BANKBARODA.NS": 269.82, "BEL.NS": 423.42, "BOSCHLTD.NS": 35596.13,
    "COALINDIA.NS": 411.97, "DRREDDY.NS": 1161.26, "FEDERALBNK.NS": 274.62,
    "FORTIS.NS": 808.54, "GAIL.NS": 157.01, "GRASIM.NS": 2699.44,
    "HDFCLIFE.NS": 695.06, "HINDALCO.NS": 917.39, "INDUSINDBK.NS": 890.53,
    "IRCTC.NS": 593.02, "IRFC.NS": 110.97, "ITC.NS": 300.49,
    "JINDALSTEL.NS": 1077.29, "JIOFIN.NS": 236.41, "LICI.NS": 784.51,
    "MARICO.NS": 704.76, "MARUTI.NS": 13987.71, "MUTHOOTFIN.NS": 3401.97,
    "NAUKRI.NS": 1113.01, "NHPC.NS": 74.17, "NMDC.NS": 78.03,
    "OBEROIRLTY.NS": 1421.86, "OFSS.NS": 7109.28, "ONGC.NS": 246.98,
    "PIIND.NS": 2995.95, "PNB.NS": 117.56, "POLICYBZR.NS": 1408.77,
    "POWERGRID.NS": 248.75, "SBICARD.NS": 723.34, "SHREECEM.NS": 25979.45,
    "SOLARINDS.NS": 12796.70, "SUZLON.NS": 45.18, "TATAPOWER.NS": 346.66,
    "TATASTEEL.NS": 182.09, "TCS.NS": 2901.42, "TORNTPHARM.NS": 3889.26,
    "TRENT.NS": 3626.78, "ULTRACEMCO.NS": 12130.05, "VBL.NS": 430.04,
    "HDFCBANK.NS": 932.91, "SBILIFE.NS": 1964.43, "BAJAJ-AUTO.NS": 9424.14,
    "TECHM.NS": 1592.00, "TMPV.NS": 359.20, "APOLLOHOSP.NS": 6959.03,
    "CIPLA.NS": 1309.92, "HCLTECH.NS": 1566.23, "NTPC.NS": 359.20,
    "KOTAKBANK.NS": 408.25, "AXISBANK.NS": 1318.08, "JSWSTEEL.NS": 1216.29,
    "LT.NS": 4022.09, "EICHERMOT.NS": 7074.95, "MAXHEALTH.NS": 1002.96,
    "HINDUNILVR.NS": 2325.81, "TATACONSUM.NS": 1140.27, "TITAN.NS": 4044.97,
    "SUNPHARMA.NS": 1681.15, "ADANIPORTS.NS": 1519.37, "M&M.NS": 3512.95,
    "SHRIRAMFIN.NS": 968.04, "NESTLEIND.NS": 1272.31, "BAJFINANCE.NS": 961.27,
    "INDIGO.NS": 4845.65, "RELIANCE.NS": 1426.33, "ICICIBANK.NS": 1387.73,
    "ETERNAL.NS": 280.24, "ASIANPAINT.NS": 2374.17, "INFY.NS": 1472.60,
    "SBIN.NS": 1045.75, "WIPRO.NS": 227.46, "ADANIENT.NS": 2189.40,
    "BHARTIARTL.NS": 1978.56, "ABB.NS": 5697.87, "ADANIENSOL.NS": 996.49,
    "ADANIGREEN.NS": 949.48, "ADANIPOWER.NS": 149.25, "BAJAJHFL.NS": 89.50,
    "BPCL.NS": 379.44, "BRITANNIA.NS": 5775.98, "CANBK.NS": 144.14,
    "CGPOWER.NS": 659.98, "CHOLAFIN.NS": 1693.29, "DIVISLAB.NS": 5909.31,
    "DLF.NS": 646.05, "DMART.NS": 3830.75, "ENRIN.NS": 2578.64,
    "GODREJCP.NS": 1150.22, "HAL.NS": 3965.08, "HAVELLS.NS": 1319.47,
    "HINDZINC.NS": 591.03, "HYUNDAI.NS": 2141.24, "ICICIGI.NS": 1833.79,
    "INDHOTEL.NS": 671.92, "IOC.NS": 172.41, "JSWENERGY.NS": 463.02,
    "LODHA.NS": 1022.26, "LTIM.NS": 5472.50, "MAZDOCK.NS": 2344.22,
    "MOTHERSON.NS": 115.47, "PFC.NS": 403.87, "PIDILITIND.NS": 1463.65,
    "RECLTD.NS": 366.16, "SIEMENS.NS": 3116.34, "TVSMOTOR.NS": 3648.76,
    "UNITDSPR.NS": 1345.24, "VEDL.NS": 637.05, "ZYDUSLIFE.NS": 879.58,
    "MANKIND.NS": 2022.84, "PAYTM.NS": 1164.55, "LUPIN.NS": 2151.29,
    "UPL.NS": 733.27, "TIINDIA.NS": 2258.75, "COFORGE.NS": 1523.54,
    "BSE.NS": 2820.83, "OIL.NS": 488.55, "AUROPHARMA.NS": 1160.17,
    "COLPAL.NS": 2077.56, "HDFCAMC.NS": 2684.31, "DABUR.NS": 496.06,
    "PERSISTENT.NS": 5712.30, "HEROMOTOCO.NS": 5686.92, "CUMMINSIND.NS": 4210.54,
    "MPHASIS.NS": 2564.12, "APLAPOLLO.NS": 2154.18, "BHEL.NS": 261.78,
    "SRF.NS": 2848.69, "PRESTIGE.NS": 1499.86, "POLYCAB.NS": 7486.38,
    "INDUSTOWER.NS": 430.69, "IDFCFIRSTB.NS": 83.73, "HINDPETRO.NS": 457.35,
    "SUPREMEIND.NS": 3625.48, "DIXON.NS": 11116.14, "PAGEIND.NS": 34033.98,
    "MFSL.NS": 1677.77, "BHARATFORG.NS": 1533.69, "GMRAIRPORT.NS": 95.43,
    "YESBANK.NS": 20.96, "AUBANK.NS": 970.92, "JUBLFOOD.NS": 530.34,
    "GODREJPROP.NS": 1635.98, "PHOENIXLTD.NS": 1692.00, "ASHOKLEY.NS": 198.26
}

# -----------------------------------
# STOCKSTAR LIST
stockstar = [
    "TCS.NS", "HDFCLIFE.NS", "BEL.NS", "HINDALCO.NS", "NAUKRI.NS",
    "TORNTPHARM.NS", "BOSCHLTD.NS", "SOLARINDS.NS", "OFSS.NS",
    "PIIND.NS", "INDUSINDBK.NS", "VBL.NS", "POLICYBZR.NS"
]

# -----------------------------------
# FETCH DATA FUNCTION
@st.cache_data(ttl=60)
def fetch_data():
    rows = []
    for sym, ref_low in stocks.items():
        try:
            t = yf.Ticker(sym)
            info = t.info
            price = info.get("regularMarketPrice", 0)
            p2l = ((price - ref_low) / ref_low) * 100
            rows.append({
                "Stock": info.get("shortName", sym.replace(".NS","")),
                "P2L %": round(p2l,2),
                "Price": round(price,2),
                "% Chg": round(info.get("regularMarketChangePercent",0),2),
                "Low Price": round(ref_low,2),
                "Open": round(info.get("open",0),2),
                "High": round(info.get("dayHigh",0),2),
                "Low": round(info.get("dayLow",0),2)
            })
        except:
            pass
    return pd.DataFrame(rows)

# -----------------------------------
# HIGHLIGHT FUNCTION
def highlight_stocks(row):
    p2l = row["P2L %"]
    color = ''
    if p2l < -2:
        color = 'orange'
    elif p2l < -1:
        color = 'hotpink'
    elif p2l < 0:
        color = 'magenta'
    return ['color: ' + color if col == 'Stock' else '' for col in row.index]

# -----------------------------------
# MAIN APP
df = fetch_data()

# Sidebar options
st.sidebar.header("Options")
sort_option = st.sidebar.selectbox("Sort by:", ["Default", "P2L %"])
show_highlight = st.sidebar.checkbox("Show Highlighted Stocks (P2L < -1)")

if sort_option == "P2L %":
    df = df.sort_values("P2L %", ascending=False)

# Display all stocks with 2 decimals
st.subheader("All Stocks")
st.dataframe(
    df.style.format("{:.2f}", subset=["P2L %","Price","% Chg","Low Price","Open","High","Low"])
        .apply(highlight_stocks, axis=1)
)

# Display highlighted stocks
if show_highlight:
    st.subheader("📌 Highlighted Stocks")
    df_highlight = df[df["P2L %"] < -1]
    st.dataframe(
        df_highlight.style.format("{:.2f}", subset=["P2L %","Price","% Chg","Low Price","Open","High","Low"])
            .apply(highlight_stocks, axis=1)
    )
    
