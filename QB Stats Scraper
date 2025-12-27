import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_espn_table(url):
    """
    Scrape NFL player stats from an ESPN page and return it as a pandas DataFrame.
    """
    try:
        # Send a request to the URL
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML
        soup = BeautifulSoup(response.content, 'lxml')

        # Look for the stats table container
        table_container = soup.find('div', class_='Table__Scroller')

        if not table_container:
            print("No table container found on the page.")
            return None

        # Find all player rows
        player_rows = table_container.find_all('tr', class_='Table__TR')

        print(f"Found {len(player_rows)} player rows")

        if not player_rows:
            print("No player rows found.")
            return None

        # Extract headers 
        header_row = table_container.find('tr', class_='Table__header')
        if header_row:
            headers = [th.get_text(strip=True) for th in header_row.find_all('th')]
        else:
            # Default headers for passing stats
            headers = ['POS', 'GP', 'CMP', 'ATT', 'CMP%', 'YDS', 'AVG', 'YDS/G', 'LNG', 'TD', 'INT', 'SACK', 'SYL', 'QBR', 'RTG']

        # Extract data
        data = []
        for row in player_rows:
            cells = row.find_all('td')
            if not cells:
                cells = row.find_all('div', class_='Table__TD')
            if cells:
                row_data = [cell.get_text(strip=True) for cell in cells]
                data.append(row_data)

        if not data:
            print("No data found in rows.")
            return None

        # Create DataFrame
        df = pd.DataFrame(data, columns=headers[:len(data[0])])

        return df

    except Exception as e:
        print(f"Error scraping the page: {e}")
        return None

if __name__ == "__main__":
    # Example URL: ESPN NFL QB passing stats
    url = "https://www.espn.com/nfl/stats/player/_/season/2024/seasontype/2"

    df = scrape_espn_table(url)

    if df is not None:
        print("Scraped Table:")
        print(df)
        # Save to color-coded CSV
        df.to_csv('scraped_data.csv', index=False)
        print("Data saved to scraped_data.csv")
    else:
        print("Failed to scrape data.")
