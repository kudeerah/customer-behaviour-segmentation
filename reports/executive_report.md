
# CUSTOMER BEHAVIOUR AND SEGMENTATION ANALYSIS

## 1. Executive Summary

This project analyses customer purchasing behaviour using the
UCI Online Retail dataset. The objective was to identify valuable
customer groups, understand purchasing patterns, and develop
data-driven marketing recommendations.

After cleaning, 392,692 transaction records representing
4,338 unique customers were retained. Total positive sales
amounted to £8,887,208.89.

## 2. Methodology

The analysis was conducted using Python, Pandas, NumPy
and Matplotlib.

Data cleaning involved:
- Removing duplicate records.
- Removing records with missing CustomerIDs.
- Excluding non-positive quantities and unit prices.
- Calculating transaction value as Quantity multiplied by UnitPrice.

Customer segmentation was performed using Recency,
Frequency and Monetary (RFM) analysis.

- Recency measures how recently a customer purchased.
- Frequency measures the number of unique invoices.
- Monetary measures total positive sales value.

Customers were scored from 1 to 5 and assigned to six
rule-based segments.

## 3. Key Findings

The analysis identified 4,338 customers across six segments:

- Hibernating Customers: 966
- Champions: 902
- Regular Customers: 830
- At-Risk Customers: 772
- Potential Loyalists: 480
- Loyal Customers: 388

Champions generated £5,648,057.89, approximately
63.55% of total positive sales.

At-Risk Customers generated £929,317.82,
approximately 10.46% of sales.

The highest revenue month was November 2011,
with £1,156,205.61.

The lowest revenue month was February 2011,
with £44,608.92.

## 4. Marketing Recommendations

1. Retain Champions:
Provide loyalty rewards, early access to new products
and personalised offers to protect this valuable customer group.

2. Re-engage At-Risk Customers:
Use targeted email campaigns, relevant product suggestions
and carefully selected incentives to encourage repeat purchases.

3. Reactivate Hibernating Customers:
Run low-cost reactivation campaigns and test limited-time
offers to identify customers who may be willing to return.

## 5. Limitations

Negative quantities were excluded from the analysis.
Consequently, Monetary represents positive sales rather
than net sales after returns.

The customer segments were created using rule-based
RFM conditions. They should be interpreted as analytical
groups rather than definitive customer characteristics.

## 6. Conclusion

The analysis shows that customer value is concentrated
in the Champions segment, while At-Risk and Hibernating
customers represent opportunities for targeted marketing.

The business should prioritise customer retention,
reactivation and personalised marketing strategies.

## 7. Data Source

UCI Machine Learning Repository:
Online Retail Dataset.
https://archive.ics.uci.edu/dataset/352/online+retail
