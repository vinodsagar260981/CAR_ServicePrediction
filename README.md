# Auto Sense — CAR service  Maintenance System

## Overview

Auto Sense is an automotive predictive maintenance and vehicle diagnostics platform built to analyze vehicle telemetry data, detect abnormal operating conditions, and provide engineering-oriented maintenance guidance.

The system uses a **rule-based diagnostic engine**, **PostgreSQL**, **RAG (Retrieval-Augmented Generation)**, **Chroma vector search**, **LLM-based explanation**, and **LangGraph** to create an AI-assisted vehicle maintenance workflow.

The system does **not depend on a machine learning model for vehicle diagnosis**.

Instead, vehicle telemetry is evaluated using explicit engineering rules. The resulting diagnosis is then passed through a RAG and LLM workflow to generate a technical maintenance explanation.

---

# Project Architecture

```text
                    ┌─────────────────────┐
                    │     React / Vite    │
                    │    Dashboard UI     │
                    └──────────┬──────────┘
                               │
                               │ REST API
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │      Backend        │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
      ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
      │ PostgreSQL   │ │ Rule Engine  │ │  RAG System  │
      │              │ │              │ │              │
      │ Telemetry    │ │ Diagnosis    │ │ Chroma       │
      │ Data         │ │              │ │ Vector Store │
      └──────────────┘ └──────┬───────┘ └──────┬───────┘
                              │                │
                              └───────┬────────┘
                                      ▼
                              ┌──────────────┐
                              │  LangGraph   │
                              │    Agent     │
                              └──────┬───────┘
                                     │
                                     ▼
                              ┌──────────────┐
                              │     LLM      │
                              │ Explanation  │
                              └──────────────┘

# Main Components

### 1. Vehicle Telemetry
Collects automotive sensor data such as engine, oil, coolant, battery, vibration, and brake parameters.

### 2. PostgreSQL
Stores vehicle telemetry and historical data.

### 3. Repository Layer
Handles database operations such as reading, inserting, and retrieving vehicle telemetry.

### 4. Analytics
Analyzes telemetry, calculates sensor trends, historical averages, risk points, and vehicle health.

### 5. Rule-Based Diagnosis
Uses predefined engineering rules to detect abnormal conditions such as high temperature, low oil pressure, and high vibration.

### 6. RAG
Retrieves relevant automotive engineering knowledge from the project knowledge base.

### 7. Chroma
Stores document embeddings and performs similarity-based knowledge retrieval.

### 8. LLM
Converts the rule-based diagnosis and retrieved engineering knowledge into a concise maintenance explanation.

### 9. LangGraph
Orchestrates the AI workflow:

`Diagnose → Retrieve → Explain`

### 10. FastAPI
Provides REST APIs for vehicle data, health, diagnosis, telemetry, and AI assessment.

### 11. React Dashboard
Provides vehicle selection, health monitoring, telemetry charts, diagnosis, maintenance actions, and AI assessment.

### 12. End-to-End Flow

`Telemetry → PostgreSQL → Analytics → Rule-Based Diagnosis → RAG → LLM → React Dashboard`

### 13. Key Principle

**Diagnosis = Rules**  
**Knowledge = RAG**  
**Explanation = LLM**

### 14. Technology Stack

**Backend:** Python, FastAPI, Pandas, PostgreSQL  
**AI:** LangChain, LangGraph, RAG, Chroma, Ollama Embeddings, LLM  
**Frontend:** React, Vite, Recharts, React Markdown
