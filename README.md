# Customer Behaviour and Segmentation Analysis

## Project Overview

This project analyses customer purchasing behaviour using
the UCI Online Retail dataset.

The goal is to understand customer purchasing patterns,
identify valuable customer groups and recommend targeted
marketing strategies.

## Project Objectives

- Clean and prepare retail transaction data.
- Perform Recency, Frequency and Monetary (RFM) analysis.
- Segment customers into meaningful groups.
- Analyse customer distribution and revenue.
- Develop data-driven marketing recommendations.

## Dataset

Source: UCI Machine Learning Repository

Dataset: Online Retail

https://archive.ics.uci.edu/dataset/352/online+retail

The original dataset contains 541,909 transaction records
and 8 columns.

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- VS Code

## Data Cleaning

The analysis involved:

- Removing duplicate records.
- Removing records with missing CustomerIDs.
- Excluding non-positive quantities and unit prices.
- Calculating transaction sales value.

The final cleaned dataset contains 392,692 records
and 4,338 unique customers.

## Customer Segmentation

RFM analysis was used to classify customers into six groups:

1. Champions
2. Loyal Customers
3. Potential Loyalists
4. At-Risk Customers
5. Hibernating Customers
6. Regular Customers

## Key Findings

- 4,338 unique customers were analysed.
- Total positive sales amounted to £8,887,208.89.
- Champions contributed approximately 63.55% of total sales.
- November 2011 recorded the highest monthly revenue.

## Visualisations

Four charts were developed:

1. Customer Distribution by Segment
2. Revenue Contribution by Customer Segment
3. Top 10 Countries by Revenue
4. Monthly Revenue Trend

## Marketing Recommendations

- Retain Champions through loyalty rewards and personalised offers.
- Re-engage At-Risk Customers through targeted campaigns.
- Reactivate Hibernating Customers through win-back campaigns.

## Project Structure

customer-behaviour-segmentation/
- data/
- notebooks/
- reports/
- src/
- requirements.txt
- README.md

## How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

   pip install -r requirements.txt

3. Place the Online Retail dataset in the data folder.
4. Open the customer_analysis.ipynb notebook.
5. Run the notebook cells from top to bottom.

## Limitations

Negative quantities were excluded, so Monetary represents
positive sales rather than net sales after returns.

Customer segments were assigned using rule-based RFM conditions.

## Author

Customer Behaviour and Segmentation Analysis Project.
