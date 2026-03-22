# Video Game Sales Analysis-Python
This project performs a comprehensive Exploratory Data Analysis (EDA) on a dataset of **16,598 games** to uncover the drivers of revenue in the gaming industry. By analyzing 30 years of data, this study identifies high-growth genres, dominant publishers, and regional market variances. 
**Key finding:** The industry is heavily "top-heavy," where a small percentage of "Super-Hit" outliers drive the majority of global revenue, creating a massive gap between average (Mean) and typical (Median) sales.


## Business Challenges Addressed
A strategic look at four key pillars of the gaming economy:
1. **Revenue Drivers:** Which genres are the most bankable globally?
2. **Geographic Dominance:** How do sales distributions differ between North America, Europe, and Japan?
3. **Market Concentration:** Which publishers hold the largest market share?
4. **Historical Trends:** How has the industry evolved from the 8-bit era to the peak of physical media?


## Key Insights & Visualizations

### 1. The Revenue Leaders: Genre Analysis
Action and Sports genres emerged as the primary revenue drivers. However, using `adjust_text` for label optimization, we can see how specific genres outperform others relative to the number of games produced
<img width="580" height="526" alt="output_6_1" src="https://github.com/user-attachments/assets/deb2cdec-00a5-400d-8a14-b6049567511b" />

*Figure 1: Global Genre Performance: Number of Games vs. Total Sales.*

### 2. Regional Market Dynamics
* **North America & Europe:** Mirror each other with a heavy preference for **Action** and **Sports**.
* **Japan:** Displays a unique market profile where **Role-Playing Games (RPGs)** are the primary revenue driver, often outperforming Action titles 3-to-1.
<img width="1384" height="784" alt="output_10_0" src="https://github.com/user-attachments/assets/f7d3e187-2220-4f10-a00a-5681b717317d" />
*Figure 2: Regional Favour: How Genre Preferences Shift by Continent.*

### 3. Industry Evolution (1986 - 2016)
The analysis highlights a "Golden Era" of sales peaking in the late 2000s, driven by the seventh generation of consoles (Wii, PS3, Xbox 360). This visualization tracks the industry's growth from a niche hobby to a dominant global entertainment force.
<img width="1009" height="564" alt="output_11_0" src="https://github.com/user-attachments/assets/83630f7c-b557-4e56-b32e-968b967c4700" />
*Figure: Global Video Game Sales Trend (1980-2016)*


## Recommendations
* **Target the "Genre Gap":** Marketing and development for the Japanese market should prioritize RPG mechanics, whereas Western releases should prioritize Action/Shooter elements.
* **Realistic Budgeting:** Stakeholders should not base budget projections on "Mean" sales, as these are inflated by outliers. Using "Median" sales provides a more realistic risk assessment for new IPs.
* **Diversify Portfolio:** While blockbusters drive the most revenue, diversifying across platforms (Wii, PS3, X360) based on historical peak performance mitigates hardware-specific risks.

  
## Technical Toolkit
* **Languages:** Python (v3.x)
* **Libraries:** Pandas (Data Cleaning), NumPy (Numerical Analysis), Matplotlib & Seaborn (Advanced Visualization).
* **Environment:** Jupyter Notebook / Anaconda.
* 
  ## Project Files
* `Game-Dataset.ipynb`: Full analytical workflow and code.
* `gamers.csv`: The cleaned dataset (16,598 records)

  **Author:** Jackline Gatwiri Kaburu, CPA-K
*Passionate about turning complex data into actionable business strategy.*
