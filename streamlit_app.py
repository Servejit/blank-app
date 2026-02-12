# ---------------------------------------------------
# INSTALL (Run once in terminal)
# pip install streamlit yfinance pandas
# ---------------------------------------------------

import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="📊 Live Stock P2L", layout="wide")
st.title("📊 Live Prices with P2L")

# ---------------------------------------------------
# STOCK LIST (Stock : Reference Low Price)

stocks = {
"ABB.NS": 5697.87,
"ADANIENSOL.NS": 996.49,
"ADANIENT.NS": 2160.15,
"ADANIGREEN.NS": 948.28,
"ADANIPORTS.NS": 1517.38,
"ADANIPOWER.NS": 147.06,
"AMBUJACEM.NS": 521.38,
"APLAPOLLO.NS": 2154.18,
"APOLLOHOSP.NS": 6959.03,
"ASHOKLEY.NS": 198.26,
"ASIANPAINT.NS": 2364.42,
"AUBANK.NS": 970.92,
"AUROPHARMA.NS": 1100.47,
"AXISBANK.NS": 1318.08,
"BAJAJ-AUTO.NS": 9424.14,
"BAJAJFINSV.NS": 1973.09,
"BAJAJHFL.NS": 89.35,
"BAJAJHLDNG.NS": 10621.63,
"BAJFINANCE.NS": 956.49,
"BANKBARODA.NS": 283.28,
"BEL.NS": 423.42,
"BHARATFORG.NS": 1533.69,
"BHARTIARTL.NS": 1978.56,
"BHEL.NS": 257.31,
"BOSCHLTD.NS": 35024.0,
"BPCL.NS": 371.68,
"BRITANNIA.NS": 5763.54,
"BSE.NS": 2820.83,
"CANBK.NS": 142.93,
"CGPOWER.NS": 659.98,
"CHOLAFIN.NS": 1690.51,
"CIPLA.NS": 1309.92,
"COALINDIA.NS": 414.07,
"COFORGE.NS": 1405.24,
"COLPAL.NS": 2077.56,
"CUMMINSIND.NS": 4210.54,
"DABUR.NS": 496.06,
"DIVISLAB.NS": 5909.31,
"DIXON.NS": 11116.14,
"DLF.NS": 646.05,
"DMART.NS": 3830.75,
"DRREDDY.NS": 1218.88,
"EICHERMOT.NS": 7028.18,
"ENRIN.NS": 2578.64,
"ETERNAL.NS": 280.24,
"FEDERALBNK.NS": 278.25,
"FORTIS.NS": 839.83,
"GAIL.NS": 158.23,
"GMRAIRPORT.NS": 95.32,
"GODREJCP.NS": 1150.22,
"GODREJPROP.NS": 1635.98,
"GRASIM.NS": 2806.6,
"HAL.NS": 3965.08,
"HAVELLS.NS": 1319.47,
"HCLTECH.NS": 1462.15,
"HDFCAMC.NS": 2684.31,
"HDFCBANK.NS": 913.91,
"HDFCLIFE.NS": 685.46,
"HEROMOTOCO.NS": 5518.27,
"HINDALCO.NS": 917.39,
"HINDPETRO.NS": 446.01,
"HINDUNILVR.NS": 2325.81,
"HINDZINC.NS": 591.03,
"HYUNDAI.NS": 2133.28,
"ICICIBANK.NS": 1381.86,
"ICICIGI.NS": 1833.79,
"IDFCFIRSTB.NS": 80.84,
"INDHOTEL.NS": 671.92,
"INDIGO.NS": 4845.65,
"INDUSINDBK.NS": 890.53,
"INDUSTOWER.NS": 430.69,
"INFY.NS": 1373.6,
"IOC.NS": 172.41,
"IRCTC.NS": 608.94,
"IRFC.NS": 112.03,
"ITC.NS": 306.76,
"JINDALSTEL.NS": 1157.09,
"JIOFIN.NS": 265.17,
"JSWENERGY.NS": 463.02,
"JSWSTEEL.NS": 1216.29,
"JUBLFOOD.NS": 530.34,
"KOTAKBANK.NS": 408.25,
"LICI.NS": 843.21,
"LODHA.NS": 1022.26,
"LT.NS": 4022.09,
"LTIM.NS": 5154.1,
"LUPIN.NS": 2151.29,
"MANKIND.NS": 2022.84,
"MARICO.NS": 736.9,
"MARUTI.NS": 14796.65,
"MAXHEALTH.NS": 1002.56,
"MAZDOCK.NS": 2344.22,
"MFSL.NS": 1677.77,
"MOTHERSON.NS": 115.47,
"MPHASIS.NS": 2445.51,
"MUTHOOTFIN.NS": 3453.05,
"NAUKRI.NS": 1113.01,
"NESTLEIND.NS": 1272.31,
"NHPC.NS": 75.78,
"NMDC.NS": 82.71,
"NTPC.NS": 359.2,
"OBEROIRLTY.NS": 1497.48,
"OFSS.NS": 6697.84,
"OIL.NS": 468.65,
"ONGC.NS": 263.38,
"PAGEIND.NS": 33501.65,
"PAYTM.NS": 1132.31,
"PERSISTENT.NS": 5403.85,
"PFC.NS": 403.47,
"PHOENIXLTD.NS": 1692.0,
"PIDILITIND.NS": 1460.56,
"PIIND.NS": 3074.15,
"PNB.NS": 119.9,
"POLICYBZR.NS": 1452.7,
"POLYCAB.NS": 7486.38,
"POWERGRID.NS": 285.07,
"PRESTIGE.NS": 1499.86,
"RECLTD.NS": 347.5,
"RELIANCE.NS": 1426.33,
"SBICARD.NS": 737.94,
"SBILIFE.NS": 1964.43,
"SBIN.NS": 1045.75,
"SHREECEM.NS": 26148.6,
"SHRIRAMFIN.NS": 968.04,
"SIEMENS.NS": 3021.52,
"SOLARINDS.NS": 12796.7,
"SRF.NS": 2798.44,
"SUNPHARMA.NS": 1681.15,
"SUPREMEIND.NS": 3625.48,
"SUZLON.NS": 46.47,
"TATACONSUM.NS": 1136.59,
"TATAPOWER.NS": 359.2,
"TATASTEEL.NS": 193.4,
"TCS.NS": 2726.3,
"TECHM.NS": 1520.36,
"TIINDIA.NS": 2258.75,
"TITAN.NS": 4044.97,
"TMPV.NS": 359.2,
"TORNTPHARM.NS": 3889.26,
"TRENT.NS": 4024.18,
"TVSMOTOR.NS": 3648.76,
"ULTRACEMCO.NS": 12558.89,
"UNITDSPR.NS": 1345.24,
"UPL.NS": 730.53,
"VBL.NS": 430.04,
"VEDL.NS": 637.05,
"WIPRO.NS": 217.41,
"YESBANK.NS": 20.9,
"ZYDUSLIFE.NS": 877.59,
}

# ---------------------------------------------------
# FETCH DATA (FAST + STABLE)

@st.cache_data(ttl=60)
def fetch_data():
    symbols = list(stocks.keys())

    data = yf.download(
        tickers=symbols,
        period="1d",
        interval="1d",
        group_by="ticker",
        progress=False,
        threads=True
    )

    rows = []

    for sym in symbols:
        try:
            ref_low = stocks[sym]

            price = data[sym]["Close"].iloc[-1]
            open_p = data[sym]["Open"].iloc[-1]
            high = data[sym]["High"].iloc[-1]
            low = data[sym]["Low"].iloc[-1]

            p2l = ((price - ref_low) / ref_low) * 100

            rows.append({
                "Stock": sym.replace(".NS", ""),
                "P2L %": p2l,
                "Price": price,
                "Low Price": ref_low,
                "Open": open_p,
                "High": high,
                "Low": low
            })

        except:
            pass

    return pd.DataFrame(rows)

# ---------------------------------------------------
# BUTTONS

col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Refresh"):
        st.cache_data.clear()
        st.rerun()

with col2:
    sort_clicked = st.button("📈 Sort by P2L")

# ---------------------------------------------------
# LOAD DATA

df = fetch_data()

if df.empty:
    st.error("⚠️ No data received from Yahoo Finance.")
    st.stop()

# Convert numeric safely
numeric_cols = ["P2L %", "Price", "Low Price", "Open", "High", "Low"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Sort if clicked
if sort_clicked:
    df = df.sort_values("P2L %", ascending=False)

# ---------------------------------------------------
# COLOR STYLING

def highlight_p2l(val):
    if pd.isna(val):
        return ""
    elif val > 0:
        return "color: green; font-weight: bold"
    elif val < 0:
        return "color: red; font-weight: bold"
    else:
        return ""

styled_df = (
    df.style
    .format("{:.2f}", subset=numeric_cols)
    .applymap(highlight_p2l, subset=["P2L %"])
)

# ---------------------------------------------------
# DISPLAY

st.dataframe(styled_df, use_container_width=True)
