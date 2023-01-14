import joblib,os

def loadHAmodel():
    
    # model & scaler name    
    model_fname  = 'allapps/prediction/heart_attack/files/hert_attack.pkl'
    scaler_fname = 'allapps/prediction/heart_attack/files/scaler.pkl'
    
    # load the scaler from disk
    scaler = joblib.load(open(os.path.abspath(scaler_fname), 'rb'))
    
    # load the model from disk
    model = joblib.load(open(os.path.abspath(model_fname), 'rb'))
    

    return scaler, model


def HApredict(scaler, model,cp,thalachh,exng,oldpeak,age,sex):
    
    input_data  = [[cp,thalachh,exng,oldpeak,age,sex]]
    scaled_data = scaler.transform(input_data)
    
    prid = model.predict(scaled_data)
    conf   = model.predict_proba(scaled_data)
    
    if prid==0:

        result = {"prid":"Low","conf": f'({conf[0][1]:.2%})'}

    elif  prid==1: 
        result = {"prid":"High","conf": f'({conf[0][1]:.2%})'}

    else :
        result = {"prid":"error","conf": "error"}

        
    return result