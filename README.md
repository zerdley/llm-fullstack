# LLM Fullstack

Zach Erdley

## What this project is

This is a project where I implement and serve an llm from scratch. I follow Karpathy's Zero to Hero for the code to train a miniGPT and subsequently containerize an application that streams the output tokens of the miniGPT. My goal with this project is to get into more breadth of both the ML architecture for llms and the infrastructure required to serve llm output at scale. 

## How to run this project

Set up environment:

`cp .env.example .env`

`uv sync`

To run in dev docker setup:

`docker compose -f compose.yaml -f compose.dev.yaml up --watch`

To run in prod docker setup (and detach):

`docker compose up -d`

Run migrations, after database is up from previous step:

`uv run alembic upgrade head`

To run type check, format, lint, and tests:

`uv run pyright`

`uv run ruff format`

`uv run ruff check --fix`

`uv run pytest`

## AI Policy

As I would like to really learn this stuff, I am writing all this code myself. It would be silly to fully ban myself from using AI, as it can be used as a tool for learning, but I think directly copying and pasting code from AI would hinder my learning. You can refer to my `CLAUDE.md` file to see how I use AI in this project to help me learn without "cheating". I believe using AI as a reference for documentation and learning resources is beneficial, so I am doing that in this project.