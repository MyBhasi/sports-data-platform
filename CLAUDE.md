# Sports Data Platform

## Project Goal
End-to-end sports data engineering platform using 
football data with Medallion Architecture.

## Architecture
Medallion Architecture (Bronze → Silver → Gold)

## Tech Stack
- Python, PySpark
- PostgreSQL
- Kafka, Cassandra
- Airflow
- Docker
- GenAI (Weekend 7)

## Weekend Plan
- Weekend 1 → Python + API + Bronze layer ✅
- Weekend 2 → PySpark + Silver layer
- Weekend 3 → PostgreSQL + Gold layer
- Weekend 4 → Kafka + Cassandra streaming
- Weekend 5 → Airflow automation
- Weekend 6 → Docker packaging
- Weekend 7 → GenAI integration
- Weekend 8 → Final polish + portfolio ready

## Setup
- Local Linux machine
- IntelliJ IDEA + Python plugin
- Claude Code (local)
- GitHub repo
- Codespaces for running full pipeline

## Workflow
Write code locally with Claude Code → push to 
GitHub → run on Codespaces

## Data Strategy
### Semi-structured JSON (API data)
- Bronze → raw JSON saved as-is
- Silver → PySpark flattens and cleans JSON
- Gold → PySpark aggregates to business metrics
- GenAI → applied on Gold layer only (less tokens)

### Unstructured Text (news, commentary, social media)
- Bronze → raw text saved as-is
- GenAI → applied directly on Bronze text
- Output → structured insights saved back to Silver/Gold

### Why this approach
- Reduces GenAI token usage significantly
- Bronze JSON = ~10,000 tokens
- Gold JSON = ~100 tokens
- Always process to Gold first then apply GenAI

## API Details
- Provider: football-data.org
- Base URL: https://api.football-data.org/v4
- League IDs:
  - Premier League = 2021
  - La Liga = 2014
  - Champions League = 2001
  - Bundesliga = 2002
  - Serie A = 2019

## Data Flow
