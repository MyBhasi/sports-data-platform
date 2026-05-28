SELECT player_name, team_name, total_goals
FROM gold.top_scorers
WHERE season = :season
ORDER BY total_goals DESC
LIMIT 20;
