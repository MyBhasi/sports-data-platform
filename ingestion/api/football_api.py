from ingestion.api.client import BaseAPIClient


class FootballAPIClient(BaseAPIClient):
    def get_fixtures(self, league_id: int, season: int) -> dict:
        return self.get(f"competitions/{league_id}/matches", {"season": season})

    def get_standings(self, league_id: int, season: int) -> dict:
        return self.get(f"competitions/{league_id}/standings", {"season": season})

    def get_players(self, team_id: int, season: int = None) -> dict:
        return self.get(f"teams/{team_id}")

    def get_teams(self, league_id: int, season: int) -> dict:
        return self.get(f"competitions/{league_id}/teams", {"season": season})
    def get_scorers(self, league_id: int, season: int) -> dict:
        return self.get(f"competitions/{league_id}/scorers", {"season": season})

    def get_match_detail(self, match_id: int) -> dict:
       return self.get(f"matches/{match_id}")

    def get_team_detail(self, team_id: int) -> dict:
       return self.get(f"teams/{team_id}")