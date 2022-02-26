# Valorant Matches Scraper
Simple data scraper for Valorant data.  
Outputs a `.json` file with the latest 200 games playes.  
Still a bit buggy, bear with me.  

### Installation
```py
git clone
pip install requirements.txt
python scraper.py
```

Requires an open tracker.gg account. 
Data will be stored in `data/priv_data/game_data.json`


### Output

```js
    [
        {
            "id": 1,
            "map": "Ascent",
            "agent": "Reyna",
            "time": "07:35 PM",
            "mode": "Competitive",
            "score_won": 13,
            "score_lost": 11,
            "win": true,
            "placement": 1,
            "kills": 25,
            "deaths": 15,
            "assists": 6,
            "kd_percentage": 1.7,
            "hs_percentage": 21.0,
            "damage_per_round": 195,
            "combat_score_total": 195
        }
    ]
```