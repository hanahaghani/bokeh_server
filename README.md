# ✈️ Flight Delays Dashboard with Bokeh

An interactive data visualization dashboard built using Bokeh. It analyzes flight delays with three tabs:

- 📊 Histogram of delays by airline  
- 📋 Summary table of delay statistics  
- 🧭 Origin–Destination scatter plot by airline  

---

## 📌 How to Run

1. Install dependencies:
  ```
   pip install bokeh pandas
   ```
2.Start the server:
```
bokeh serve --show main.py
```

📁 Files
main.py – integrates all tabs

hist.py – histogram tab

table.py – summary statistics tab

route.py – route delay visualization

flights.csv – dataset used
