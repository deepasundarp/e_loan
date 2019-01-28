# e_loan
Energy Loan package performs the role of a central market for the product of energy loan based flexibility service. It accepts the bids and asks collected from the Buyers and Sellers in the form of '.csv' file in the specified format. After allocations being made, it reports back as a DataFrame, which can be communicated back to stakeholders.

## CSV format for bids

Buyer_ID, Loan_Type (FTL/VTL/NZPL/NZVPL), Service_Start_Time(PTU), Loan_Crediting_Time (PTU count), Credit_Load_capacity (kW), Credit_Ramp_capacity (kW/PTU), Service_Period (PTU count), Loan_Debiting_Time (PTU count), Debit_Load_Capacity (kW), Debit_Ramp_capacity (kW/PTU), Price (Euro/kWPTU2) 

## CSV format for asks

Seller_ID, Loan_Type (FTL/VTL/NZPL/NZVPL), Service_Start_Time(PTU), Loan_Crediting_Time (PTU count), Credit_Load_capacity (kW), Credit_Ramp_capacity (kW/PTU), Service_Period (PTU count), Loan_Debiting_Time (PTU count), Debit_Load_Capacity (kW), Debit_Ramp_capacity (kW/PTU), Price (Euro/kWPTU2) 
