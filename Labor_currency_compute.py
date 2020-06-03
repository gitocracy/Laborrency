from num2words import num2words                                                 
                                                                                
def laborrencycompute(hourly,children,danger,skills,importance,demand,quality): 
    """This Function calculates wages in the Federation of Cooperatives.        
       There is a Minimum Base wage of $15 Laborrency Coins, and 5              
       Additional Variables which are all multipliers of the hourly Wage        
       This Laborrency seeks to be On Demand - Guaranteed - Living Wage -       
       Meritocratic. """                                                        
                                                                                
    var1_hourly = hourly+(hourly*(children*.5)) # Minimum $15.00                
    var2_danger = hourly*danger # Multiply by 3                                 
    var3_skills = hourly*skills # Multiply by 3                                 
    var4_importance = hourly*importance # Multiply by 6                         
    var5_demand = hourly*demand # Multiply by 2                                 
    var6_quality = hourly*quality # Multiply by 7                               
                                                                                
    tophourly = var1_hourly+var2_danger+var3_skills+var4_importance+\           
                var5_demand+var6_quality                                        
    topweekly = tophourly*40                                                    
    topmonthly = topweekly*4.33                                                 
    topyearly = topmonthly*12                                                   
                                                                                
    print(f"""{chr(10)}                                                         
              Hourly Pay is {num2words(tophourly)} Laborrency{chr(10)}          
              Weekly Pay is {num2words(topweekly)}{chr(10)}                     
              Monthly Pay is {num2words(topmonthly)}{chr(10)}                   
              Yearly Pay is {num2words(topyearly)}                              
              {chr(21328)}""")                                                  
                                                                                
if __name__ == '__main__':                                                      
    laborrencycompute(15,4,0,0,0,0,0)  
