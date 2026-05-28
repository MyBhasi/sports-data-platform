import pytest
from unittest.mock import MagicMock, patch
from ingestion.api.football_api import FootballAPIClient
from ingestion.loaders.bronze_loader import BronzeLoader


class TestFootballAPIClient:
    @patch("ingestion.api.client.requests.get")
    def test_get_fixtures_calls_correct_endpoint(self, mock_get):
        mock_get.return_value.json.return_value = {"response": []}
        mock_get.return_value.raise_for_status = MagicMock()
        client = FootballAPIClient()
        client.get_fixtures(league_id=39, season=2024)
        mock_get.assert_called_once()
        args, kwargs = mock_get.call_args
        assert "fixtures" in args[0]


class TestBronzeLoader:
    def test_save_creates_file(self, tmp_path):
        loader = BronzeLoader(base_path=str(tmp_path))
        path = loader.save({"data": [1, 2, 3]}, "fixtures")
        assert path.endswith(".json")
