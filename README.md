# Web Scraping NFL QB Data
I used Python to create the web scraper, with the help of GeeksforGeeks and Stack Overflow to guide my work. The data comes from the 2024 NFL season, and I used ESPN to web scrape. After completion, I ran the output through Stata to create confidence intervals and averages. The goals were to predict QB stats for the 2026 season, compare them to a season from 10 years ago, and track outlier performances.

## Requirements
- Python 3.9+
- Install dependencies: `pip install -r requirements.txt`

## Usage
Run everything from the repository root.

### Scrape
1. Run the scraper: `python scraper.py`
2. The script will scrape the example URL (ESPN NFL QB passing stats) and print the table.
3. Data is also saved to `scraped_data.csv`.

### Charts
Each script reads `2024_Season.csv` and `2014_Season.csv` and writes its PNG:

| Script | Output |
| --- | --- |
| `python plot_script.py` | `box_plots_qbr_ydsg.png` — QBR and YDS/G box plots, 2024 vs 2014 |
| `python heatmap_script.py` | `heatmaps_cmp_ydsg_td_int_qbr.png` — correlation heatmaps for CMP%, YDS/G, TD, INT, QBR |
| `python scatterplot_script.py` | `scatterplot_cmp_avg.png` — CMP% vs AVG with a line of best fit per season |

## Files
- `scraper.py` — the ESPN scraper.
- `2024_Season.csv`, `2014_Season.csv` — the top 50 passers for each season, cleaned up for analysis. These are the inputs to the chart scripts.
- `2024 Output with Names Below`, `2014 Output with Names Below` — the same stats with each player's name and team listed underneath the table.
- `Data From Web Scraper` — the Stata session log for the confidence intervals and averages.

## Customization
- Change the `url` variable in `scraper.py` to scrape different ESPN NFL stats pages.
- The script is designed for ESPN's NFL player stats pages.

## Dependencies
- requests: For HTTP requests
- beautifulsoup4: For HTML parsing
- pandas: For data manipulation and table display
- lxml: For faster HTML parsing
- matplotlib, seaborn: For the charts
