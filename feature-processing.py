def broker_status_to_tensor(value:str):
    broker_status_tensors = {
        'Approved':  torch.tensor(  [1.,0.,0.]),
        'Deactivated': torch.tensor([0.,1.,0.]),
        'Watch List': torch.tensor( [0.,0.,1.])
    }
    return broker_status_tensors[value]

def broker_tier_to_tensor(value:str):
    broker_tier_tensors = {
        'Key Account' : torch.tensor([1,0]),
        'Non Key Account' : torch.tensor([0,1])
    }
    return broker_tier_tensors[value]

def client_risk_rating_to_tensor (value:str):
    client_risk_rating_tensors = {
        '7' :  torch.tensor([1,0,0,0,0,0,0,0,0]),
        '6' :  torch.tensor([0,1,0,0,0,0,0,0,0]),
        '4' :  torch.tensor([0,0,1,0,0,0,0,0,0]),
        '1' :  torch.tensor([0,0,0,1,0,0,0,0,0]),
        '0' :  torch.tensor([0,0,0,0,1,0,0,0,0]),
        '-1' : torch.tensor([0,0,0,0,0,1,0,0,0]),
        '2' : torch.tensor([0,0,0,0,0,0,1,0,0]),
        '3' :  torch.tensor([0,0,0,0,0,0,0,1,0]),
        '5' :  torch.tensor([0,0,0,0,0,0,0,0,1])
    }
    return client_risk_rating_tensors[value]

def employment_status_borrower_2_to_tensor (value:str):
    employment_status_borrower_2_tensors = {
        'Pension'       : torch.tensor([1,0,0,0,0,0,0]),
        'Salary'        : torch.tensor([0,1,0,0,0,0,0]),
        'Self-employed' : torch.tensor([0,0,1,0,0,0,0]),
        'Contract'      : torch.tensor([0,0,0,1,0,0,0]),
        'Commissions'   : torch.tensor([0,0,0,0,1,0,0]),
        'Other'        : torch.tensor([0,0,0,0,0,1,0]),
        'Hourly'        : torch.tensor([0,0,0,0,0,0,1])
    }
    return employment_status_borrower_2_tensors[value]

def employment_status_to_tensor (value:str):
    employment_status_tensors = {
        'Pension'       : torch.tensor([1,0,0,0,0,0,0]),
        'Other'         : torch.tensor([0,1,0,0,0,0,0]),
        'Self-employed' : torch.tensor([0,0,1,0,0,0,0]),
        'Salary'        : torch.tensor([0,0,0,1,0,0,0]),
        'Contract'      : torch.tensor([0,0,0,0,1,0,0]),
        'Commissions'   : torch.tensor([0,0,0,0,0,1,0]),
        'Hourly'        : torch.tensor([0,0,0,0,0,0,1])
    }
    return employment_status_tensors[value]

def mortgage_position_to_tensor (value:str):
    mortgage_position_tensors = {
        '3'       : torch.tensor([1,0,0]),
        '1'       : torch.tensor([0,1,0]),
        '2'       : torch.tensor([0,0,1]) 
    }
    return mortgage_position_tensors[value]

def mortgage_purpose_to_tensor (value:str):
    mortgage_purpose_tensors = {
        'Equity Takeout'                     : torch.tensor([1,0,0,0,0]),
        'Purchase Rent to Own'               : torch.tensor([0,1,0,0,0]),
        'Refinance for Debt Consolidation'   : torch.tensor([0,0,1,0,0]),
        'Refinance'                          : torch.tensor([0,0,0,1,0]),
        'Purchase'                           : torch.tensor([0,0,0,0,1])
    }
    return mortgage_purpose_tensors[value]

def occupancy_type_to_tensor (value:str):
    occupancy_type_tensors = {
        'Rental'       : torch.tensor([1,0,0]),
        'Owner'       : torch.tensor([0,1,0]),
        'Rent To Own' : torch.tensor([0,0,1])        
    }
    return occupancy_type_tensors[value]

def property_type_to_tensor (value:str):
    property_type_tensors = {
        'Row'                   : torch.tensor([1,0,0,0,0]),
        'Semi-detached'         : torch.tensor([0,1,0,0,0]),
        'Apartment High Rise'   : torch.tensor([0,0,1,0,0]),
        'Apartment Low Rise'    : torch.tensor([0,0,0,1,0]),
        'Single'                : torch.tensor([0,0,0,0,1])       
    }
    return property_type_tensors[value]

def self_employed_to_tensor(value:str):
    self_employed_tensors = {
        'False' : torch.tensor([1,0]),
        'True'  : torch.tensor([0,1])
    }
    return self_employed_tensors[value]


def categorical_values_to_tensors (loan_application_hash:str):
    #retrieve categorical values from the loan_application
    broker_status                   =   redis.execute("HGET", loan_application_hash,'Broker_Status')
    broker_tier                     =   redis.execute("HGET", loan_application_hash,'Broker_Tier')
    client_risk_rating              =   redis.execute("HGET", loan_application_hash,'Client_Risk_Rating')
    employment_status_borrower_2    =   redis.execute("HGET", loan_application_hash,'Employment_Status_Borrower_2')
    employment_status               =   redis.execute("HGET", loan_application_hash,'Employment_Status')
    mortgage_position               =   redis.execute("HGET", loan_application_hash,'Mortgage_Position')
    mortgage_purpose                =   redis.execute("HGET", loan_application_hash,'Mortgage_Purpose')
    occupancy_type                  =   redis.execute("HGET", loan_application_hash,'Occupancy_Type')
    property_type                   =   redis.execute("HGET", loan_application_hash,'Property_Type')
    self_employed                   =   redis.execute("HGET", loan_application_hash,'Self_Employed')
    #convert to tensors
    broker_status_t             =  broker_status_to_tensor(str(broker_status))
    broker_tier_t               =  broker_tier_to_tensor(str(broker_tier))
    client_risk_rating_t        =  client_risk_rating_to_tensor(str(client_risk_rating))
    empt_status_borrower_2_t    =  employment_status_borrower_2_to_tensor(str(employment_status_borrower_2))
    employment_status_t         =  employment_status_to_tensor(str(employment_status))
    mortgage_position_t         =  mortgage_position_to_tensor(str(mortgage_position))
    mortgage_purpose_t          =  mortgage_purpose_to_tensor(str(mortgage_purpose))
    occupancy_type_t            =  occupancy_type_to_tensor(str(occupancy_type))
    property_type_t             =  property_type_to_tensor(str(property_type))
    self_employed_t             =  self_employed_to_tensor(str(self_employed))

    #return a single tensor
    result = torch.hstack([
        broker_status_t,broker_tier_t,client_risk_rating_t,empt_status_borrower_2_t,
        employment_status_t,mortgage_position_t,mortgage_purpose_t,occupancy_type_t,
        property_type_t,self_employed_t
    ])
    return torch.reshape(result, (1,46))

def scale(x: torch.Tensor, mean: torch.Tensor, std: torch.Tensor) -> torch.Tensor:
    x_scaled = x - mean
    x_scaled /= (std + 1e-7)
    return x_scaled


def numeric_values_to_tensors (loan_application_hash:str, mean: torch.Tensor, std: torch.Tensor):
    #retrieve numeric values from the loan_application
    amount                   =  float(str(redis.execute("HGET", loan_application_hash,'Amount')))
    credit_score_2           =  float(str(redis.execute("HGET", loan_application_hash,'Credit_Score_2')))
    credit_score             =  float(str(redis.execute("HGET", loan_application_hash,'Credit_Score_1')))
    current_term_months      =  float(str(redis.execute("HGET", loan_application_hash,'Current_Term_Months')))
    global_debt_ratio        =  float(str(redis.execute("HGET", loan_application_hash,'Global_Debt_Ratio')))
    interest_rate            =  float(str(redis.execute("HGET", loan_application_hash,'Interest_Rate')))
    loan_to_value            =  float(str(redis.execute("HGET", loan_application_hash,'Loan_To_Value')))
    total_debt_service_ratio =  float(str(redis.execute("HGET", loan_application_hash,'Total_Debt_Service_Ratio')))

    #a single tensor with all numeric features
    all_numeric_tensor = torch.tensor([
        amount,credit_score_2,credit_score,current_term_months,global_debt_ratio,
        interest_rate,loan_to_value,total_debt_service_ratio
    ])
    #return scaled tensor - values between 0 & 1 using mean/std tensors obtained from training data
    return scale(all_numeric_tensor,mean,std)

def pre_process (loan_application_hash:str, mean: torch.Tensor, std: torch.Tensor):
    scaled_numeric_feature_tensor = numeric_values_to_tensors(loan_application_hash,mean,std)
    categorical_feature_tensor    = categorical_values_to_tensors(loan_application_hash)
    featurized_data = torch.hstack((scaled_numeric_feature_tensor,categorical_feature_tensor))
    return featurized_data


