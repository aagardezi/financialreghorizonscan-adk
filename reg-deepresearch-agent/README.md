# Financial Regulatory Horizon Scanning Agent

## Overview

The Financial Regulatory Horizon Scanning Agent is a powerful tool designed for in-house legal and compliance teams at financial institutions, such as hedge funds. This application leverages the Gemini API to proactively analyze the regulatory landscape, assess the potential impact of new and existing regulations on your business, and enhance your compliance strategies.

By integrating with internal document stores and external regulatory sources like the Financial Conduct Authority (FCA) and the Prudential Regulation Authority (PRA) handbooks, the agent provides comprehensive and context-aware insights. This enables your team to move from a reactive to a proactive compliance posture, saving time and resources while mitigating regulatory risks.

## How it Works

The agent employs a sophisticated, multi-step process to deliver high-quality, cited research reports:

1.  **Interactive Planning:** The user provides a research topic or question. The agent then generates a high-level research plan, which the user can review and refine.
2.  **Parallel Research:** Once the plan is approved, the agent executes the research in parallel across three distinct sources:
    *   **Web Search:** For broad, up-to-date information and news.
    *   **FCA Handbook:** A dedicated search of the FCA's regulatory handbook.
    *   **PRA Handbook:** A dedicated search of the PRA's regulatory handbook.
3.  **Iterative Refinement:** Each research stream is independently evaluated for quality and completeness. If the initial findings are insufficient, the agent performs follow-up searches to fill in the gaps, ensuring the research is thorough and reliable.
4.  **Report Composition:** The agent synthesizes the findings from all sources into a single, coherent report. The report is structured, easy to read, and includes in-line citations, allowing your team to verify the source of each piece of information.

## How to Use

### Prerequisites

1.  **Google Cloud Project:** You need a Google Cloud Platform (GCP) project with the Vertex AI API enabled.
2.  **Vertex AI Search:** You must have two Vertex AI Search data stores configured: one for the FCA Handbook and one for the PRA Handbook.
3.  **Environment Variables:** Set the following environment variables with the names of your Vertex AI Search data stores:
    ```bash
    export FCA_VERTEX_SEARCH_INDEX="your-fca-datastore-name"
    export PRA_VERTEX_SEARCH_INDEX="your-pra-datastore-name"
    ```

### Running the Application

Once the prerequisites are met, you can run the application using the ADK CLI.

## Sample Prompts for a Hedge Fund Legal Team

Here are ten sample prompts to get you started:

1.  "Analyze the FCA's latest guidance on crypto-assets and its potential impact on our investment strategies."
2.  "What are the PRA's current regulations regarding outsourcing and third-party risk management for hedge funds?"
3.  "Provide a summary of the key changes in the upcoming MiFID III regulations and their implications for our trading operations."
4.  "Investigate the regulatory requirements for marketing alternative investment funds (AIFs) to retail investors in the UK."
5.  "What are the FCA's expectations for hedge funds regarding market abuse surveillance and reporting?"
6.  "Compare the regulatory treatment of ESG-focused funds in the UK and the EU."
7.  "Analyze the PRA's rules on capital adequacy for hedge funds and how they apply to our current portfolio."
8.  "What are the latest developments in the UK's regulatory framework for artificial intelligence and machine learning in financial services?"
9.  "Provide a detailed overview of the Senior Managers and Certification Regime (SMCR) and its application to our firm."
10. "Investigate the legal and regulatory implications of using decentralized finance (DeFi) protocols in our investment strategies."
